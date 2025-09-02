import os
import datetime
import numpy as np
import torch
from torch.optim import AdamW
from transformers import get_linear_schedule_with_warmup
import tqdm as tqdm
from typing import List, Dict, Optional, Tuple
from collections import deque
import math
import json
import random

from etu.utils import (
    load_model, get_params, get_data,
    build_forbidden_token_ids, estimate_p_S_over_VS, 
    q_mass_from_lambda, adjust_lambda, create_suppression_report,
    preference_loss_from_batches
)

def compute_lambda(p_S: float, epsilon: float, lambda_max: float = 20.0, allow_negative: bool = False) -> float:
    """
    Compute tilting parameter λ from base mass p_S and target bound ε.
    
    Args:
        p_S: Base probability mass on forbidden set S
        epsilon: Target suppression bound
        lambda_max: Maximum allowed magnitude of λ
        allow_negative: Allow amplification regime (λ<0) when ε>p_S
    
    Returns:
        λ: Tilting parameter for exponential tilting
    """
    if p_S <= epsilon and not allow_negative:
        # Inactive constraint case (suppression mode only)
        return 0.0
    
    # Numerically stable computation using logit difference
    p_S_clip = np.clip(p_S, 1e-8, 1 - 1e-8)
    epsilon_clip = np.clip(epsilon, 1e-8, 1 - 1e-8)
    
    lambda_val = (np.log(p_S_clip) - np.log(1 - p_S_clip)) - (np.log(epsilon_clip) - np.log(1 - epsilon_clip))
    
    # Apply magnitude clipping
    lambda_val = float(np.clip(lambda_val, -lambda_max, lambda_max))
    
    return lambda_val if allow_negative else max(0.0, lambda_val)

def run_etu(
    updated_model,
    frozen_model,
    tokenizer,
    forget_data_list,
    retain_data_list,
    args,
):
    """
    Run Exponential-Tilted Unlearning (ETU).
    
    Args:
        updated_model: Model to be updated
        frozen_model: Frozen base model for reference
        tokenizer: Tokenizer
        forget_data_list: List of forget datasets
        retain_data_list: List of retain datasets
        args: Training arguments
    """
    etu_config = vars(args)
    print("====ETU Config====")
    print("\n".join(f"{k}={v}" for k,v in etu_config.items()))
    print("=====")

    # Safety: ensure lambda updates actually trigger
    args.lambda_update_freq = max(1, int(getattr(args, "lambda_update_freq", 1)))

    # Set determinism for reproducibility
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False

    # Initialize models
    updated_model = updated_model.train()
    frozen_model = frozen_model.eval()
    
    # Apply LoRA if requested
    if args.use_lora:
        from etu.utils import apply_lora_to_model
        print("Applying LoRA for efficient parameter updates...")
        updated_model = apply_lora_to_model(args, updated_model, args.layer_ids)
    
    # Get parameters to update
    if args.use_lora:
        params = [p for p in updated_model.parameters() if p.requires_grad]
    else:
        params = get_params(updated_model, args.layer_ids, args.param_ids, 
                           name_keywords=args.name_keywords, module_str=args.module_str)
    optimizer = AdamW(params, lr=args.lr, weight_decay=0.01)
    
    # Setup AMP for mixed precision training (fix bf16 GradScaler issue)
    use_cuda = torch.cuda.is_available()
    use_bf16 = use_cuda and torch.cuda.is_bf16_supported()
    use_amp = use_cuda  # AMP only on CUDA
    scaler = torch.cuda.amp.GradScaler(enabled=(use_cuda and not use_bf16))
    
    # Setup learning rate scheduler with boundary guards
    num_batches = min(
        args.max_num_batches,
        min([len(f) for f in forget_data_list]),
    )
    num_steps = max(1, args.num_epochs * num_batches)
    if num_batches == 0:
        raise RuntimeError("No training batches. Check forget_corpora / filters / batch_size.")
    warmup = min(int(0.03 * num_steps), num_steps - 1)
    scheduler = get_linear_schedule_with_warmup(optimizer, warmup, num_steps)
    
    # 0) Build V_S once, BEFORE training
    print("Building forbidden token set V_S...")
    if args.use_pmi_vs:
        from etu.utils import build_forbidden_token_ids_pmi
        V_S = build_forbidden_token_ids_pmi(
            forget_data_list, retain_data_list, tokenizer,
            top_k=args.pmi_top_k, min_count=args.pmi_min_count, alpha=args.pmi_smoothing,
            max_batches_per_split=args.pmi_max_batches,
            span_masking=getattr(args, "span_masking", False),
            span_ngram_max=getattr(args, "span_ngram_max", 3),
        )
        print(f"V_S (PMI-refined) size: {len(V_S)} tokens")
        
        # PMI token preview for debugging
        if args.verbose:
            try:
                printable = tokenizer.convert_ids_to_tokens(V_S[:args.vs_preview_k])
                print(f"Top PMI tokens preview: {printable}")
            except Exception as e:
                print(f"(debug) token decode skipped: {e}")
    else:
        V_S = build_forbidden_token_ids(forget_data_list, tokenizer, vocab_top_k=args.vocab_top_k,
                                       rate=args.vs_freq_rate, abs_cap=args.vs_abs_cap)
    
    if len(V_S) == 0:
        raise RuntimeError("V_S is empty. Check forget data/tokenization or set a looser filter.")
    
    # Warn if V_S is too large (might make training meaningless)
    if len(V_S) > 0.5 * tokenizer.vocab_size:
        print(f"[warn] V_S size {len(V_S)} is >50% of vocab; consider smaller --vocab_top_k or PMI refinement.")
    
    vocab = getattr(tokenizer, "vocab_size", None) or len(getattr(tokenizer, "get_vocab", lambda: {})())
    print(f"V_S size: {len(V_S)} tokens ({(len(V_S)/max(vocab,1)):.1%} of vocab)")
    
    # 1) Estimate base p_S on π_base over V_S
    print("Estimating base probability mass p_S over V_S...")
    p_S = estimate_p_S_over_VS(frozen_model, tokenizer, forget_data_list, V_S, sample_size=512)  # Increased sample size
    print(f"Estimated p_S (π_base over V_S): {p_S:.4f}")
    
    # Consolidated info line for debugging
    print(f"[info] |V_S|/V = {(len(V_S)/max(vocab,1)):.1%}, π_base(S)={p_S:.4f}, ε={args.epsilon:.4f}")
    
    # V_S preview for debugging (basic mode)
    if args.verbose:
        try:
            print("V_S preview:", tokenizer.convert_ids_to_tokens(V_S[:args.vs_preview_k]))
        except Exception as e:
            print(f"(debug) token decode skipped: {e}")
    
    # 2) Compute initial λ
    lambda_val = compute_lambda(p_S, args.epsilon, args.lambda_max, args.allow_negative_lambda)
    expected_q_S = q_mass_from_lambda(p_S, lambda_val)
    print(f"Initial λ: {lambda_val:.4f} → expected qλ(S)≈{expected_q_S:.4f}")
    
    # Setup EMA for p_S tracking
    pS_hist = deque(maxlen=20)
    
    # Setup EMA for KL tracking
    kl_ema = None
    
    # Setup held-out mini evaluation for unbiased λ control
    forget_eval_mini = [d[:4] for d in forget_data_list]  # 4 batches per split
    
    # Setup fair round-robin cursors for unbiased rotation
    topic_cursors = [0 for _ in range(len(forget_data_list))]
    
    # Setup cumulative n_eff for Wilson upper bound
    n_eff_cum = 0
    
    # Get device safely from model parameters
    device = next(updated_model.parameters()).device
    frozen_device = next(frozen_model.parameters()).device
    
    truncation_side = tokenizer.truncation_side
    tokenizer.truncation_side = "right"

    for epoch in range(args.num_epochs):
        print(f"======= Epoch {epoch} =======")
        with tqdm.tqdm(total=num_batches) as pbar:
            for idx in range(num_batches):
                # Fair round-robin rotation to prevent bias from split length mismatches
                topic_idx = (idx + epoch) % len(forget_data_list)
                max_b = len(forget_data_list[topic_idx])
                if max_b == 0:
                    pbar.update(1)
                    continue  # 비어있는 split은 건너뜀
                batch_idx = topic_cursors[topic_idx]
                topic_cursors[topic_idx] = (topic_cursors[topic_idx] + 1) % max_b
                
                unlearn_batch = forget_data_list[topic_idx][batch_idx]
                
                # Check if retain data is available
                has_retain = (args.retain_weight > 0) and (len(retain_data_list) == len(forget_data_list)) and all(len(s) > 0 for s in retain_data_list)
                retain_batch = None
                if has_retain:
                    retain_batch = retain_data_list[topic_idx][batch_idx]

                # ETU Loss: KL divergence to tilted distribution
                max_length = 512  # Fixed length for reproducibility
                unlearn_inputs = tokenizer(
                    unlearn_batch, return_tensors="pt", padding=True, truncation=True, max_length=max_length
                ).to(device)
                
                # 1) Get logits from both models (frozen: CPU/inference_mode, updated: GPU/AMP)
                # frozen (CPU) - autocast 밖
                with torch.inference_mode():
                    base_inputs = {k: v.to(frozen_device, non_blocking=True) for k, v in unlearn_inputs.items()}
                    base_logits = frozen_model(**base_inputs).logits.float()

                # updated (GPU) - autocast 안
                with torch.cuda.amp.autocast(enabled=use_amp, 
                                           dtype=(torch.bfloat16 if use_bf16 else torch.float16)):
                    updated_outputs = updated_model(**unlearn_inputs)
                    updated_logits = updated_outputs.logits
                
                # Move base logits to updated device efficiently (fix device mismatch)
                with torch.no_grad():
                    base_logits = base_logits.to(updated_logits.device, dtype=updated_logits.dtype, non_blocking=True)
                
                # Build tilted logits on the same device (no grad, then cast to fp32 for stability)
                with torch.no_grad():
                    tilted_logits = base_logits.clone()
                    tilted_logits[..., V_S] -= lambda_val  # Direct slicing, no mask needed
                
                # ETU loss: KL divergence to tilted distribution (fp32 for stability, outside autocast)
                logp_upd = torch.log_softmax(updated_logits.float(), dim=-1)
                p_tilt = torch.softmax(tilted_logits.float(), dim=-1)
                etu_loss = torch.nn.functional.kl_div(logp_upd, p_tilt, reduction='batchmean')

                # 3) Retain loss as KL instead of MSE (with optional weight scheduling)
                retain_loss = 0.0
                if has_retain and retain_batch is not None:
                    retain_inputs_upd = tokenizer(
                        retain_batch, return_tensors="pt", padding=True, truncation=True, max_length=512
                    ).to(device)

                    retain_inputs_ref = {k: v.to(frozen_device, non_blocking=True) for k, v in retain_inputs_upd.items()}
                    with torch.inference_mode():
                        base_ret_logits = frozen_model(**retain_inputs_ref).logits
                        base_ret = torch.softmax(base_ret_logits.float(), dim=-1)

                    upd_ret = torch.log_softmax(updated_model(**retain_inputs_upd).logits.float(), dim=-1)
                    
                    # Optional: retain weight scheduling to prevent early collapse
                    retain_w = args.retain_weight * min(1.0, (idx + 1) / (0.2 * num_steps))
                    retain_loss = torch.nn.functional.kl_div(upd_ret, base_ret, reduction='batchmean') * retain_w
                elif args.retain_weight > 0:
                    print("[warn] retain_weight>0 이지만 retain 데이터가 없어 retain 손실을 건너뜁니다.")

                # 3.5) Optional preference-based refinement (NPO default, DPO optional)
                preference_loss = 0.0
                if args.preference_weight > 0 and has_retain and retain_batch and unlearn_batch \
                   and any(len(t.strip()) for t in retain_batch) and any(len(t.strip()) for t in unlearn_batch) \
                   and ((idx + 1) % max(1, args.pref_every) == 0):
                    # pos: retain_batch, neg: forget_batch (동일 step에서 간단히 대응)
                    m = min(len(retain_batch), len(unlearn_batch))
                    if m > 0:
                        pref_loss = preference_loss_from_batches(
                            updated_model, tokenizer,
                            pos_texts=retain_batch[:m], neg_texts=unlearn_batch[:m],
                            format_=args.pref_format, beta=args.pref_beta,
                            margin=args.pref_margin, max_length=args.pref_max_len,
                            reference_model=(frozen_model if args.pref_format == "dpo" else None)
                        )
                        preference_loss = args.preference_weight * pref_loss

                # Total loss
                total_loss = etu_loss + retain_loss + preference_loss
                
                # Update model with gradient clipping and AMP
                optimizer.zero_grad()
                scaler.scale(total_loss).backward()
                scaler.unscale_(optimizer) # clip_grad_norm_은 scaled grad에 하면 왜곡되므로 unscale 먼저
                torch.nn.utils.clip_grad_norm_(params, 1.0)
                scaler.step(optimizer)
                scheduler.step()
                scaler.update()
                
                # 5) Logging with correct p_S(πθ) over V_S and confidence intervals
                # Always accumulate n_eff for Wilson bounds (regardless of verbose mode)
                n_eff = int(unlearn_inputs["attention_mask"].sum().item())
                n_eff_cum += n_eff
                
                if args.verbose:
                    with torch.no_grad():
                        cur_probs = torch.softmax(updated_logits.float(), dim=-1)  # .float() for numerical stability
                        cur_pS = cur_probs[..., V_S].sum(dim=-1).mean().item()  # mean over B,L
                        
                        # Calculate confidence interval
                        se = math.sqrt(max(cur_pS * (1 - cur_pS) / max(n_eff, 1), 1e-12))
                        ci_lo = max(0.0, cur_pS - 1.96 * se)
                        ci_hi = min(1.0, cur_pS + 1.96 * se)
                        
                        # Wilson upper bound for control (누적 n_eff 사용)
                        from etu.utils import wilson_upper
                        p_upper = wilson_upper(cur_pS, n_eff_cum, max_n=args.wilson_max_n)
                        
                        expected_q_S = q_mass_from_lambda(p_S, lambda_val)
                        
                        # Add intuitive status indicator
                        gap = (cur_pS - args.epsilon)
                        status = "OK" if cur_pS <= args.epsilon else ("NEAR" if gap < 0.01 else "HIGH")
                        
                        print(f"[{status}] πθ(S)={cur_pS:.4f} [95% normal {ci_lo:.4f},{ci_hi:.4f} | Wilson↑ {p_upper:.4f}] "
                              f"| E[qλ(S)]={expected_q_S:.4f} | ε={args.epsilon:.4f} | KL={etu_loss.item():.4g} | λ={lambda_val:.3f}")
                
                # Track p_S for EMA (reuse computed values)
                if args.verbose:
                    pS_hist.append(cur_pS)
                    cur_pS_ema = sum(pS_hist) / len(pS_hist)
                else:
                    # If not verbose, still need to compute for EMA
                    with torch.no_grad():
                        cur_probs = torch.softmax(updated_logits.float(), dim=-1)
                        cur_pS = cur_probs[..., V_S].sum(dim=-1).mean().item()
                        pS_hist.append(cur_pS)
                        cur_pS_ema = sum(pS_hist) / len(pS_hist)
                
                # Calculate status and adaptive learning rate (always needed for λ updates)
                gap = (cur_pS - args.epsilon)
                status = "OK" if cur_pS <= args.epsilon else ("NEAR" if gap < 0.01 else "HIGH")
                eta_eff = min(args.lambda_eta * 1.5, args.lambda_eta + 0.25) if status == "NEAR" else args.lambda_eta
                
                # Track KL for EMA
                if kl_ema is None:
                    kl_ema = etu_loss.detach().item()
                else:
                    kl_ema = 0.9 * kl_ema + 0.1 * etu_loss.detach().item()
                
                # 6) Periodic λ adjustment with explicit δ calculation
                if (idx + 1) % args.lambda_update_freq == 0:
                    old_lambda = lambda_val
                    
                    # Held-out evaluation for unbiased π_θ(S) and δ
                    from etu.utils import evaluate_suppression_effect
                    cur_pS_eval = evaluate_suppression_effect(
                        updated_model, tokenizer, V_S, forget_eval_mini, sample_size=8
                    )
                    cur_pS_ema = 0.5 * cur_pS_ema + 0.5 * cur_pS_eval
                    
                    # Held-out δ calculation (fp32) - multiple batches for better averaging
                    with torch.no_grad():
                        deltas = []
                        taken = 0
                        for ds in forget_eval_mini:
                            for b in ds:
                                if taken >= 8:
                                    break
                                ei = tokenizer(b, return_tensors="pt", padding=True, truncation=True, max_length=512).to(device)
                                base_eval = frozen_model(**ei).logits.float()
                                upd_eval = updated_model(**ei).logits.float()
                                tilt = base_eval.clone()
                                tilt[..., V_S] -= lambda_val
                                d = torch.nn.functional.kl_div(
                                    torch.log_softmax(upd_eval, dim=-1),
                                    torch.softmax(tilt, dim=-1),
                                    reduction='batchmean'
                                ).item()
                                deltas.append(d)
                                taken += 1
                            if taken >= 8:
                                break
                        delta_eval = float(sum(deltas) / len(deltas)) if deltas else (kl_ema or 0.0)
                    
                    # Update KL EMA with held-out δ
                    kl_ema = 0.5 * kl_ema + 0.5 * delta_eval if kl_ema is not None else delta_eval
                    
                    # Wilson upper bound for conservative control (누적 n_eff 사용)
                    from etu.utils import wilson_upper
                    p_upper = wilson_upper(cur_pS_ema, n_eff_cum, max_n=args.wilson_max_n)
                    
                    lambda_val = adjust_lambda(
                        lambda_val, p_upper, kl_ema, args.epsilon,
                        eta=eta_eff, lambda_max=args.lambda_max, 
                        allow_negative=args.allow_negative_lambda
                    )
                    
                    if args.verbose:
                        exp_q = q_mass_from_lambda(p_S, lambda_val)
                        print(f"[λ-update] EMA πθ(S)={cur_pS_ema:.4f} (upper={p_upper:.4f}) → λ={old_lambda:.3f}→{lambda_val:.3f} | E[qλ(S)]={exp_q:.4f} | KL_EMA={kl_ema:.4f}")
                
                # Update TQDM with key metrics
                pref_val = (preference_loss.item() if isinstance(preference_loss, torch.Tensor) else float(preference_loss))
                pbar.set_postfix({
                    'loss': f"{total_loss.item():.3g}",
                    'πθ(S)': f"{cur_pS:.3f}",
                    'λ': f"{lambda_val:.2f}",
                    **({'pref': f"{pref_val:.3g}"} if args.preference_weight > 0 else {})
                })
                
                # 진행 요약(quiet 모드)
                if (not args.verbose) and ((idx + 1) % args.log_every == 0):
                    print(f"[{idx+1}/{num_batches}] πθ(S)={cur_pS:.4f} λ={lambda_val:.3f} loss={total_loss.item():.3g}")

                pbar.update(1)

        # --- epoch-end forced λ update (if not aligned with freq) ---
        if (num_batches % args.lambda_update_freq) != 0:
            old_lambda = lambda_val
            from etu.utils import evaluate_suppression_effect, wilson_upper
            cur_pS_eval = evaluate_suppression_effect(
                updated_model, tokenizer, V_S, forget_eval_mini, sample_size=8
            )
            if len(pS_hist) > 0:
                cur_pS_ema = 0.5 * (sum(pS_hist)/len(pS_hist)) + 0.5 * cur_pS_eval
            else:
                cur_pS_ema = cur_pS_eval
            p_upper = wilson_upper(cur_pS_ema, n_eff_cum, max_n=args.wilson_max_n)
            lambda_val = adjust_lambda(
                lambda_val, p_upper, (kl_ema or 0.0), args.epsilon,
                eta=args.lambda_eta, lambda_max=args.lambda_max,
                allow_negative=args.allow_negative_lambda
            )
            if args.verbose:
                exp_q = q_mass_from_lambda(p_S, lambda_val)
                print(f"[λ-update@epoch-end] EMA πθ(S)={cur_pS_ema:.4f} (upper={p_upper:.4f}) "
                      f"→ λ={old_lambda:.3f}→{lambda_val:.3f} | E[qλ(S)]={exp_q:.4f} | KL_EMA={(kl_ema or 0.0):.4f}")

    tokenizer.truncation_side = truncation_side
    
    # Final evaluation and report
    report = create_suppression_report(
        base_model=frozen_model,
        updated_model=updated_model,
        tokenizer=tokenizer,
        V_S=V_S,
        forget_data_list=forget_data_list,
        retain_data_list=retain_data_list,
        epsilon=args.epsilon,
        wilson_max_n=args.wilson_max_n
    )
    
    # Save suppression report
    if args.output_dir:
        path = args.output_dir
    else:
        date = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        safe_name = os.path.basename(args.model_name_or_path).replace('/', '_')
        # Limit path length to prevent OS restrictions
        safe_name = safe_name[:64] if len(safe_name) > 64 else safe_name
        path = f"models/{safe_name}_etu_epsilon-{args.epsilon}_lambda-{lambda_val:.4f}_{date}"
    
    # Ensure directory exists before saving
    os.makedirs(path, exist_ok=True)
    
    # Save suppression report as JSON
    report_path = os.path.join(path, "suppression_report.json")
    with open(report_path, "w") as f:
        json.dump(report, f, indent=2)
    print(f"Saved suppression report to {report_path}")
    
    # Save model
    if args.output_dir:
        path = args.output_dir
    else:
        date = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        safe_name = os.path.basename(args.model_name_or_path).replace('/', '_')
        # Limit path length to prevent OS restrictions
        safe_name = safe_name[:64] if len(safe_name) > 64 else safe_name
        path = f"models/{safe_name}_etu_epsilon-{args.epsilon}_lambda-{lambda_val:.4f}_{date}"
    
    # Ensure directory exists before saving
    os.makedirs(path, exist_ok=True)
    
    # Merge LoRA weights if used
    if args.use_lora:
        from etu.utils import merge_lora_model
        print("Merging LoRA weights into base model...")
        updated_model = merge_lora_model(updated_model)
    
    # Save V_S for reproducibility
    vs_path = os.path.join(path, "V_S.ids.json")
    with open(vs_path, "w") as f:
        json.dump(list(map(int, V_S)), f)
    print(f"Saved V_S to {vs_path}")
    
    updated_model.save_pretrained(path)
    tokenizer.save_pretrained(path)
    print(f"Saved ETU model to {path}")
    
    # Save args for reproducibility
    cfg_path = os.path.join(path, "args.json")
    with open(cfg_path, "w") as f:
        json.dump(vars(args), f, indent=2)
    print(f"Saved args to {cfg_path}")
    
    # Save metrics snapshot
    metrics = {
        "epsilon": args.epsilon,
        "p_base_S": float(p_S),
        "lambda_final": float(lambda_val),
        "V_S_size": len(V_S),
        "training_success": True,
        "timestamp": datetime.datetime.now().isoformat()
    }
    metrics_path = os.path.join(path, "metrics.json")
    with open(metrics_path, "w") as f:
        json.dump(metrics, f, indent=2)
    print(f"Saved metrics to {metrics_path}")


def get_dataset_mapping():
    """데이터셋 별칭을 실제 경로로 매핑"""
    return {
        # HuggingFace 경로
        "bio:forget": "cais/wmdp-bio-forget-corpus",
        "bio:retain": "cais/wmdp-corpora:bio-retain-corpus", 
        "cyber:forget": "cais/wmdp-corpora:cyber-forget-corpus",
        "cyber:retain": "cais/wmdp-corpora:cyber-retain-corpus",
        "wikitext": "wikitext",
        
        # 로컬 경로
        "local:cyber-forget": "./datasets/cyber-forget",
        "local:cyber-retain": "./datasets/cyber-retain",
        "local:bio-forget": "./datasets/bio-forget",
        "local:bio-retain": "./datasets/bio-retain",
        "local:wikitext": "./datasets/wikitext",
    }

def resolve_dataset_paths(forget_corpora, retain_corpora):
    """데이터셋 별칭을 실제 경로로 변환"""
    mapping = get_dataset_mapping()
    
    def resolve_corpus(corpus):
        if corpus in mapping:
            return mapping[corpus]
        return corpus
    
    # 쉼표로 구분된 여러 데이터셋 처리
    forget_paths = [resolve_corpus(c.strip()) for c in forget_corpora.split(",")]
    retain_paths = [resolve_corpus(c.strip()) for c in retain_corpora.split(",")]
    
    return ",".join(forget_paths), ",".join(retain_paths)

def get_args():
    import argparse

    parser = argparse.ArgumentParser()
    ### Model arguments # default: HuggingFaceH4/zephyr-7b-beta
    parser.add_argument(
        "--model_name_or_path", type=str, default="HuggingFaceH4/zephyr-7b-beta"
    )
    parser.add_argument(
        "--output_dir", type=str, default=None
    )
    ### Data arguments # default: ./datasets/bio-retain, ./datasets/cyber-forget
    parser.add_argument(
        "--retain_corpora",
        type=str,
        default="./datasets/bio-retain",
        help="comma-separated list of corpora to retain (aliases: bio:retain, cyber:retain, wikitext, or actual paths)",
    )
    parser.add_argument(
        "--forget_corpora",
        type=str,
        default="./datasets/cyber-forget",
        help="comma-separated list of corpora to forget (aliases: bio:forget, cyber:forget, or actual paths)",
    )
    ### ETU hyperparameters
    parser.add_argument("--epsilon", type=float, default=0.05, help="Target suppression bound ε")
    parser.add_argument("--lambda_max", type=float, default=12.0, help="Maximum magnitude of λ (reduced for stability)")
    parser.add_argument("--allow_negative_lambda", action="store_true", help="Allow amplification regime (λ<0) when ε>p_S")
    parser.add_argument("--vocab_top_k", type=int, default=None, help="Top K tokens for V_S (None for all)")
    parser.add_argument("--vs_freq_rate", type=float, default=0.01, help="V_S 빈도 컷 비율")
    parser.add_argument("--vs_abs_cap", type=int, default=20000, help="V_S 빈도 절대 상한")
    parser.add_argument("--span_masking", action="store_true", help="BPE 연속 조각 스팬 단위 V_S 확장(실험적)")
    parser.add_argument("--span_ngram_max", type=int, default=3, help="Maximum n-gram size for span masking")
    parser.add_argument("--use_pmi_vs", action=argparse.BooleanOptionalAction, default=True, help="Use PMI-based V_S refinement (use --no-use-pmi-vs to disable)")
    parser.add_argument("--frozen_on_cpu", action="store_true", help="Keep frozen reference model on CPU to save VRAM")
    parser.add_argument("--log_every", type=int, default=50, help="Non-verbose mode: print every N steps")
    parser.add_argument("--deterministic", action="store_true", help="Enable deterministic algorithms (may impact performance)")
    parser.add_argument("--pmi_top_k", type=int, default=2000, help="Top-K tokens by PMI to keep in V_S")
    parser.add_argument("--pmi_min_count", type=int, default=20, help="Min freq in forget to compute PMI")
    parser.add_argument("--pmi_smoothing", type=float, default=1.0, help="Additive smoothing for PMI")
    parser.add_argument("--pmi_max_batches", type=int, default=None, help="Max batches per split for PMI counting")
    parser.add_argument("--vs_preview_k", type=int, default=30, help="How many tokens to preview for V_S")
    parser.add_argument("--retain_weight", type=float, default=1.0, help="Weight for retain loss")
    parser.add_argument("--preference_weight", type=float, default=0.0, help="Weight for preference loss")
    # Preference options
    parser.add_argument("--pref_format", type=str, default="npo", choices=["npo","dpo"],
                        help="Preference loss format: npo (default) or dpo")
    parser.add_argument("--pref_beta", type=float, default=0.1,
                        help="Inverse temperature for DPO-style logistic term")
    parser.add_argument("--pref_margin", type=float, default=0.0,
                        help="Hinge margin for NPO (0=none)")
    parser.add_argument("--pref_max_len", type=int, default=256,
                        help="Max length when building preference inputs")
    parser.add_argument("--pref_every", type=int, default=1,
                        help="Apply preference loss every N steps (for speed)")
    
    # Retain data management
    parser.add_argument("--retain_broadcast", action="store_true",
                        help="retain_corpora가 1개일 때 모든 forget split에 재사용")
    parser.add_argument("--lambda_update_freq", type=int, default=25, help="Frequency of λ updates (increased for stability)")
    parser.add_argument("--lambda_eta", type=float, default=0.25, help="Learning rate for λ adjustment")
    parser.add_argument("--wilson_max_n", type=int, default=2048, help="Wilson upper bound에서 사용할 n_eff 상한")
    parser.add_argument("--lr", type=float, default=5e-5, help="learning rate")
    parser.add_argument("--min_len", type=int, default=0)
    parser.add_argument("--max_len", type=int, default=2000)
    parser.add_argument("--batch_size", type=int, default=4)
    parser.add_argument("--max_num_batches", type=int, default=80)
    parser.add_argument("--num_epochs", type=int, default=1, help="Number of training epochs")
    parser.add_argument("--layer_id", type=int, default=7, help="layer to unlearn")
    parser.add_argument("--layer_ids", type=str, default="5,6,7", help="update layers")
    parser.add_argument("--param_ids", type=int, nargs="+", default=None, help="Parameter indices to update")
    parser.add_argument("--name_keywords", type=str, nargs="+", default=["q_proj", "k_proj", "v_proj", "o_proj"], 
                       help="Parameter name keywords for selection (default: attention projections)")
    parser.add_argument("--module_str", type=str, default="{model_name}.model.layers[{layer_id}]", 
                       help="Module path template for parameter selection")
    
    # LoRA options
    parser.add_argument("--use_lora", action="store_true", help="Use LoRA for efficient parameter updates")
    parser.add_argument("--lora_r", type=int, default=256, help="LoRA rank")
    parser.add_argument("--lora_alpha", type=int, default=512, help="LoRA scaling factor")
    parser.add_argument("--lora_dropout", type=float, default=0.1, help="LoRA dropout rate")
    parser.add_argument("--lora_target_modules", type=str, nargs="+", 
                       default=["q_proj", "k_proj", "v_proj", "o_proj"], 
                       help="Target modules for LoRA")
    
    parser.add_argument("--seed", type=int, default=42, help="Seed")
    parser.add_argument("--verbose", action="store_true", help="Detailed logging including V_S preview, λ updates, and training metrics")
    parser.add_argument("--analyze_activations", action="store_true", help="Enable activation analysis for debugging (ERASER-inspired, optional)")

    args = parser.parse_args()
    
    # 데이터셋 별칭 해결
    args.forget_corpora, args.retain_corpora = resolve_dataset_paths(
        args.forget_corpora, args.retain_corpora
    )
    
    args.retain_corpora = [s for s in args.retain_corpora.split(",") if s.strip()]  # 빈 항목 제거
    args.forget_corpora = [s for s in args.forget_corpora.split(",") if s.strip()]
    
    # layer_id가 설정되어 있으면 layer_ids를 덮어쓰기
    if hasattr(args, 'layer_id') and args.layer_id is not None:
        args.layer_ids = str(args.layer_id)
    
    args.layer_ids = [int(layer_id) for layer_id in args.layer_ids.split(",")]
    
    # param_ids: nargs="+" 이므로 이미 List[int] 또는 None
    if args.param_ids is not None and len(args.param_ids) == 0:
        args.param_ids = None
    
    return args


if __name__ == "__main__":
    args = get_args()

    # Set seed for reproducibility
    if args.seed is not None:
        torch.manual_seed(args.seed)
        np.random.seed(args.seed)
        random.seed(args.seed)
        if torch.cuda.is_available():
            torch.cuda.manual_seed_all(args.seed)
    
    # Enable deterministic algorithms if requested
    if args.deterministic:
        torch.use_deterministic_algorithms(True)
        print("[info] Deterministic algorithms enabled (may impact performance)")

    frozen_model, tokenizer = load_model(args.model_name_or_path, train=False, infer_on_cpu=args.frozen_on_cpu)
    updated_model, tokenizer = load_model(args.model_name_or_path, train=True)
    forget_data_list, retain_data_list = get_data(
        args.forget_corpora,
        args.retain_corpora,
        args.min_len,
        args.max_len,
        args.batch_size,
    )
    
    # Retain broadcast: single retain corpus to all forget splits
    if args.retain_broadcast and len(retain_data_list) == 1 and len(forget_data_list) > 1:
        retain_data_list = [retain_data_list[0] for _ in range(len(forget_data_list))]
        print(f"Broadcasting single retain corpus to {len(forget_data_list)} forget splits")
    run_etu(
        updated_model,
        frozen_model,
        tokenizer,
        forget_data_list,
        retain_data_list,
        args,
    )
