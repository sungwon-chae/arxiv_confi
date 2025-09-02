import json
import os
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
import random
import numpy as np
import math
import string
from typing import List, Dict, Optional, Tuple
from collections import Counter
random.seed(0)
from datasets import load_dataset

# Add LoRA support
try:
    from peft import LoraConfig, get_peft_model, PeftModel
    PEFT_AVAILABLE = True
except ImportError:
    PEFT_AVAILABLE = False
    print("Warning: PEFT not available. LoRA features will be disabled.")

################################
##### LoRA Integration #####
################################

def apply_lora_to_model(args, model, chosen_layers):
    """
    Apply LoRA to specific layers of the model for efficient unlearning.
    """
    if not PEFT_AVAILABLE:
        raise RuntimeError("PEFT(LoRA) 미설치 상태에서 --use_lora가 지정되었습니다. peft를 설치하거나 --use_lora를 끄세요.")
    
    # Freeze all layers first
    freeze_all_layers(model)
    
    # Convert chosen_layers to list of integers for PEFT compatibility
    if isinstance(chosen_layers, str):
        # Handle "5,6,7" format
        layer_list = [int(x.strip()) for x in chosen_layers.split(",")]
    elif isinstance(chosen_layers, int):
        # Handle single layer ID
        layer_list = [chosen_layers]
    elif isinstance(chosen_layers, list):
        # Already a list
        layer_list = chosen_layers
    else:
        raise ValueError(f"chosen_layers must be string, int, or list, got {type(chosen_layers)}")
    
    print(f"Applying LoRA to layers: {layer_list}")
    
    lora_config = LoraConfig(
        r=getattr(args, 'lora_r', 256),
        lora_alpha=getattr(args, 'lora_alpha', 512),
        target_modules=getattr(args, 'lora_target_modules', ["q_proj", "k_proj", "v_proj", "o_proj"]),
        lora_dropout=getattr(args, 'lora_dropout', 0.1),
        bias="none",
        task_type="CAUSAL_LM",
        layers_to_transform=layer_list,
    )

    model = get_peft_model(model, lora_config)
    model.print_trainable_parameters()
    return model

def freeze_all_layers(model):
    """Freeze all layers of the model."""
    for layer in model.model.layers:
        for p in layer.parameters():
            p.requires_grad = False

def unfreeze_all_layers(model):
    """Unfreeze all layers of the model."""
    for layer in model.model.layers:
        for p in layer.parameters():
            p.requires_grad = True

def prepare_model_for_unlearning(model, chosen_layers):
    """Prepare model for unlearning by freezing/unfreezing specific layers."""
    freeze_all_layers(model)
    for layer_id in chosen_layers:
        for p in model.model.layers[layer_id].parameters():
            p.requires_grad = True

def merge_lora_model(model):
    """Merge LoRA weights into base model for final saving."""
    if not PEFT_AVAILABLE:
        return model
    
    if hasattr(model, 'merge_and_unload'):
        model = model.merge_and_unload()
    
    # Remove LoRA parameters if they exist
    if isinstance(model, PeftModel):
        model = model.base_model
    
    return model

################################
##### Statistical utilities #####
################################

def _span_enrich_vs(vs_ids: List[int], tokenizer, forget_data_list, max_len: int = 512, ngram_max: int = 3, top_cap: int = 4096) -> List[int]:
    """
    간단 스팬(n-gram) 결합 강화:
    - 선택된 V_S 토큰들이 인접 BPE로 자주 붙는 경우, 해당 구성성분 토큰들을 유지/강화.
    - 구현은 경량화: 빈도 높은 인접 쌍/트리플이 등장하는 구성 토큰을 우선 포함.
    """
    from collections import Counter
    vs = set(vs_ids)
    adj = Counter()
    tri = Counter()

    for dataset in forget_data_list:
        for batch in dataset:
            enc = tokenizer(batch, return_tensors="pt", padding=True, truncation=True, max_length=max_len)
            ids = enc["input_ids"].tolist()
            attn = enc["attention_mask"].tolist()
            for row, mask in zip(ids, attn):
                toks = [t for t, m in zip(row, mask) if m]
                # bigram
                for i in range(len(toks)-1):
                    if toks[i] in vs and toks[i+1] in vs:
                        adj[(toks[i], toks[i+1])] += 1
                # trigram
                for i in range(len(toks)-2):
                    if toks[i] in vs and toks[i+1] in vs and toks[i+2] in vs:
                        tri[(toks[i], toks[i+1], toks[i+2])] += 1

    # 상위 스팬에 포함된 구성 토큰은 유지(이미 vs에 있음) + 누락된 구성 토큰이 있으면 보강
    enriched = set(vs)
    for (a,b), _ in adj.most_common(top_cap):
        enriched.add(a); enriched.add(b)
    if ngram_max >= 3:
        for (a,b,c), _ in tri.most_common(top_cap):
            enriched.update([a,b,c])

    return sorted(enriched)

def wilson_upper(p_hat: float, n_eff: int, conf: float = 0.95, max_n: int = 2048) -> float:
    """
    Wilson upper bound for binomial proportion with configurable n_eff clamping.
    """
    import math
    
    n = max(1, min(n_eff, max_n))  # Clamp n_eff to max_n
    # conf는 0.95만 지원(간단화); 필요시 케이스 분기
    z = 1.959963984540054  # 95% 양측
    
    # Wilson interval
    denom = 1 + z * z / n
    center = p_hat + z * z / (2 * n)
    margin = z * math.sqrt((p_hat * (1 - p_hat) + z * z / (4 * n)) / n)
    return min(1.0, (center + margin) / denom)

################################
##### Activation functions (ERASER-inspired, optional) #####
################################

def forward_with_cache(model, inputs, module, no_grad=True):
    """
    Extract activations from a specific module during forward pass.
    Based on ERASER's implementation for activation-based analysis.
    
    Note: This is primarily for analysis/debugging purposes in ETU.
    ETU's core mechanism relies on probability mass estimation over V_S,
    not activation-based unlearning like ERASER.
    
    Use cases:
    - Layer selection validation: Check if target layers show activation changes
    - Stability monitoring: Detect activation blow-up during strong suppression
    - LoRA debugging: Verify only adapter paths change when LoRA is enabled
    - Ablation studies: Correlate layer activation drift with πθ(S) reduction
    
    Performance: Only use when needed - hooks add overhead and memory usage.
    """
    cache = []
    def hook(module, input, output):
        if isinstance(output, tuple):
            cache.append(output[0])
        else:
            cache.append(output)
        return None 
    
    hook_handle = module.register_forward_hook(hook)
    
    if no_grad:
        with torch.no_grad():
            _ = model(**inputs)
    else:
        _ = model(**inputs)
        
    hook_handle.remove()
    return cache[0]

def extract_layer_activations(model, tokenizer, data_list, layer_id, device, 
                            sample_size=100, max_length=512):
    """
    Extract activations from a specific layer for analysis.
    Useful for understanding model behavior and computing statistics.
    
    Note: This is primarily for analysis/debugging purposes in ETU.
    ETU's core mechanism relies on probability mass estimation over V_S,
    not activation-based unlearning like ERASER.
    
    Recommended usage:
    - Use with --analyze_activations flag only when needed
    - Call at epoch end or λ update timing for summary statistics
    - Use no_grad() + eval() mode to minimize overhead
    - Limit sample_size for performance (e.g., 4-8 batches)
    """
    activations = []
    model.eval()
    
    with torch.no_grad():
        for dataset in data_list:
            for i, batch in enumerate(dataset):
                if i >= sample_size:
                    break
                    
                inputs = tokenizer(batch, return_tensors="pt", 
                                 padding=True, truncation=True, 
                                 max_length=max_length).to(device)
                
                # Get the target layer
                target_layer = model.model.layers[layer_id]
                activation = forward_with_cache(model, inputs, target_layer, no_grad=True)
                
                # Average over sequence length if 3D
                if activation.dim() == 3:
                    activation = activation.mean(dim=1)
                
                activations.append(activation)
    
    return torch.cat(activations, dim=0) if activations else None

#######################################
##### PMI-based V_S refinement #####
#######################################

def _token_counts(data_list: List[List[List[str]]], tokenizer, max_len: int = 512, max_batches_per_split: int = None) -> Tuple[Counter, int]:
    """
    Count token frequencies over batched text lists.
    Returns (Counter, total_token_positions)
    """
    cnt = Counter()
    total = 0
    for dataset in data_list:
        for bi, batch in enumerate(dataset):
            if max_batches_per_split and bi >= max_batches_per_split:
                break
            enc = tokenizer(batch, return_tensors="pt", padding=True, truncation=True, max_length=max_len)
            ids = enc["input_ids"].tolist()
            attn = enc["attention_mask"].tolist()
            for row, mask in zip(ids, attn):
                # count only attended positions
                for tid, m in zip(row, mask):
                    if m:
                        cnt[tid] += 1
                        total += 1
    return cnt, total

def build_forbidden_token_ids_pmi(
    forget_data_list: List[List[List[str]]],
    retain_data_list: List[List[List[str]]],
    tokenizer,
    top_k: int = 2000,
    min_count: int = 20,
    alpha: float = 1.0,
    max_batches_per_split: int = None,
    span_masking: bool = False,
    span_ngram_max: int = 3,
) -> List[int]:
    """
    PMI-like refinement for V_S: select tokens strongly enriched in forget vs retain.
    Score ≈ log-odds with additive smoothing. (forget vs retain)
    span_masking: 선택된 V_S 토큰들의 인접 n-gram 결합을 약하게 보강(토큰 레벨).
    """
    cf, Nf = _token_counts(forget_data_list, tokenizer, max_len=512, max_batches_per_split=max_batches_per_split)
    cr, Nr = _token_counts(retain_data_list, tokenizer, max_len=512, max_batches_per_split=max_batches_per_split)

    specials = set(tokenizer.all_special_ids or [])
    for s in specials:
        cf.pop(s, None); cr.pop(s, None)

    V = max(tokenizer.vocab_size or 50000, len(set(list(cf.keys()) + list(cr.keys()))))
    scores = []
    for tid, c_f in cf.items():
        if c_f < min_count:
            continue
        c_r = cr.get(tid, 0)
        pf = (c_f + alpha) / (Nf + alpha * V)
        pr = (c_r + alpha) / (Nr + alpha * V)
        score = float(np.log(max(pf, 1e-12)) - np.log(max(pr, 1e-12)))
        scores.append((score, tid))

    scores.sort(reverse=True)
    vs = [tid for _, tid in (scores[:top_k] if top_k else scores)]
    if not vs:
        raise RuntimeError("PMI refinement produced empty V_S. Lower --pmi_min_count or increase data.")

    vs = sorted(set(vs))
    vs = _filter_vs_tokens(tokenizer, vs)

    # --- span-aware enrichment (optional) ---
    if span_masking and vs:
        vs = _span_enrich_vs(vs, tokenizer, forget_data_list, ngram_max=span_ngram_max)

    return vs

#######################################
##### ETU-specific utilities #####
#######################################

# 중복 정의 제거 - 아래 build_forbidden_token_ids() 함수 사용

def estimate_p_S_over_VS(frozen_model, tokenizer, forget_data_list, V_S, sample_size: int = 100):
    """
    Estimate base probability mass p_S = π_base(S) over forbidden token set V_S.
    """
    frozen_model.eval()
    device = next(frozen_model.parameters()).device
    total = 0.0
    n = 0
    
    with torch.no_grad():
        for forget_data in forget_data_list:
            for i, batch in enumerate(forget_data):
                if n >= sample_size: 
                    break
                    
                enc = tokenizer(batch, return_tensors="pt", padding=True, truncation=True, max_length=512).to(device)
                logits = frozen_model(**enc).logits  # [B, L, V]
                probs = torch.softmax(logits, dim=-1)
                mass_S = probs[..., V_S].sum(dim=-1)  # [B, L] → mass on S per position
                # average over positions then over batch
                pS_batch = mass_S.mean()
                total += pS_batch.item()
                n += 1
            if n >= sample_size: 
                break
    
    return (total / max(n, 1)) if n > 0 else 0.1

def q_mass_from_lambda(pS, lam):
    """
    Compute q_λ(S) = e^{-λ}·pS / (e^{-λ}·pS + 1 - pS)
    """
    num = math.exp(-lam) * pS
    den = num + (1 - pS)
    return num / den

def adjust_lambda(lambda_val, current_pS, kl_delta, epsilon, eta=0.5, lambda_max=20.0, allow_negative=False):
    """
    Simple proportional controller with Pinsker margin.
    Symmetric control for both suppression (λ>0) and amplification (λ<0) modes.
    """
    import math
    margin = epsilon + math.sqrt(max(kl_delta, 0.0) / 2.0)
    upper_threshold = margin + 0.005
    lower_threshold = max(epsilon - 0.005, 0.0)
    
    if current_pS > upper_threshold:   # 더 줄여야 함 → λ 증가(더 양수/덜 음수)
        lambda_val = min(lambda_val + eta, lambda_max)
    elif current_pS < lower_threshold: # 더 늘려야 함 → λ 감소(덜 양수/더 음수)
        step = -0.25 * eta
        lambda_val = lambda_val + step
    
    # 클램프 시 allow_negative 반영
    lo = (-lambda_max if allow_negative else 0.0)
    hi = lambda_max
    return float(max(lo, min(hi, lambda_val)))

def compute_forbidden_mask(logits: torch.Tensor, 
                          forbidden_tokens: Optional[List[int]] = None,
                          threshold: float = 0.1) -> torch.Tensor:
    """
    Compute forbidden mask for ETU.
    Only use explicit forbidden_tokens (V_S). Probability thresholding is disabled to avoid mis-specifying S.
    """
    if forbidden_tokens is None:
        raise ValueError("ETU requires an explicit forbidden token set V_S. Provide `forbidden_tokens`.")
    
    mask = torch.zeros_like(logits, dtype=torch.bool)
    mask[..., forbidden_tokens] = True
    return mask

def estimate_probability_mass(model, tokenizer, data_list: List, 
                            forbidden_tokens: Optional[List[int]] = None,
                            sample_size: int = 100) -> float:
    """
    Estimate π(S): average probability mass on forbidden set V_S across positions and batch.
    """
    if not forbidden_tokens:
        raise ValueError("`forbidden_tokens`(V_S) must be provided to estimate π(S).")
    
    model.eval()
    device = next(model.parameters()).device
    total = 0.0
    n = 0
    
    with torch.no_grad():
        for data in data_list:
            for batch in data:
                if n >= sample_size:
                    break
                    
                enc = tokenizer(batch, return_tensors="pt", padding=True,
                               truncation=True, max_length=512).to(device)
                logits = model(**enc).logits          # [B, L, V]
                probs = torch.softmax(logits, dim=-1) # [B, L, V]
                # mass on S per position: sum over V_S
                mass_S = probs[..., forbidden_tokens].sum(dim=-1)  # [B, L]
                # average over positions, then over batch
                pS_batch = mass_S.mean()
                total += pS_batch.item()
                n += 1
            if n >= sample_size:
                break
    
    return (total / n) if n > 0 else 0.1

def create_preference_pairs(retain_data: List, forget_data: List, 
                          num_pairs: int = 100) -> List[Tuple[str, str, str]]:
    """
    Create preference pairs for ETU preference-based refinement.
    
    Args:
        retain_data: Retain dataset
        forget_data: Forget dataset
        num_pairs: Number of preference pairs to create
    
    Returns:
        List of (x, y+, y-) tuples
    """
    pairs = []
    
    for _ in range(num_pairs):
        # Sample from retain and forget data
        retain_sample = random.choice(retain_data[0]) if retain_data else "Sample retain text"
        forget_sample = random.choice(forget_data[0]) if forget_data else "Sample forget text"
        
        # Create a simple prompt
        prompt = "Generate a response:"
        
        pairs.append((prompt, retain_sample, forget_sample))
    
    return pairs

def compute_kl_divergence(p: torch.Tensor, q: torch.Tensor, dim: int = -1, reduction: str = "batchmean") -> torch.Tensor:
    """
    Compute KL(p||q) with proper reduction.
    p, q: probabilities along `dim`
    """
    p = torch.clamp(p, min=1e-8)
    q = torch.clamp(q, min=1e-8)
    kl_per_elem = p * (torch.log(p) - torch.log(q))
    
    if reduction == "none":
        return kl_per_elem.sum(dim=dim)
    elif reduction == "mean":
        return kl_per_elem.sum(dim=dim).mean()
    elif reduction == "batchmean":
        # assume batch is dimension 0
        return kl_per_elem.sum(dim=dim).mean(dim=0).mean()
    else:
        return kl_per_elem.sum()

#######################################
##### Model and data loading code #####
#######################################

def _resolve_module(model, module_str, layer_id):
    """
    Resolve module path like "model.model.layers[7]" to actual module.
    """
    s = module_str.format(model_name="model", layer_id=layer_id)
    mod = model
    for part in s.split('.'):
        if part.endswith(']'):  # layers[7] 형태
            name, idx = part[:-1].split('[')
            mod = getattr(mod, name)[int(idx)]
        else:
            mod = getattr(mod, part)
    return mod

def get_params(model, layer_ids, param_ids=None, name_keywords=None, module_str="{model_name}.model.layers[{layer_id}]"):
    """
    Select trainable parameters by layer index and/or name keywords.
    Generalized to work with different architectures via module_str.
    """
    params = []
    for layer_id in layer_ids:
        layer = _resolve_module(model, module_str, layer_id)
        named = list(layer.named_parameters())
        if param_ids is not None:
            # index 기반 선택 with safety check
            for i in param_ids:
                if not (0 <= i < len(named)):
                    raise IndexError(f"param_ids[{i}] out of range for layer {layer_id} (len={len(named)})")
                params.append(named[i][1])
            continue  # 이름 키워드 선택과 중복 방지
        else:
            # 이름 키워드 기반 (없으면 전체)
            for name, p in named:
                if (name_keywords is None) or any(kw in name for kw in name_keywords):
                    params.append(p)
    return params

def load_model(model_name_or_path, train: bool = False, infer_on_cpu: bool = False):
    """
    Load model with appropriate device mapping for training vs inference.
    Enhanced for offline/closed network environments.
    """
    use_cuda = torch.cuda.is_available()
    
    if use_cuda and torch.cuda.is_bf16_supported():
        torch_dtype = torch.bfloat16
    elif use_cuda:
        torch_dtype = torch.float16
    else:
        torch_dtype = torch.float32  # CPU에서 fp16 금지
    
    # Device mapping strategy
    if train and use_cuda:
        device_map = None
    else:
        device_map = "cpu" if (infer_on_cpu or not use_cuda) else "auto"
    
    # Enhanced error handling for offline environments
    try:
        model = AutoModelForCausalLM.from_pretrained(
            model_name_or_path,
            torch_dtype=torch_dtype,
            trust_remote_code=True,
            device_map=device_map,
            local_files_only=False,  # Allow online fallback
        )
    except Exception as e:
        print(f"Warning: Online loading failed, trying local files only: {e}")
        model = AutoModelForCausalLM.from_pretrained(
            model_name_or_path,
            torch_dtype=torch_dtype,
            trust_remote_code=True,
            device_map=device_map,
            local_files_only=True,  # Force local only
        )
    
    # Move to CUDA if training and not using device_map
    if train and use_cuda and device_map is None:
        model.to("cuda")
    
    # Enhanced tokenizer loading with fallback
    try:
        tokenizer = AutoTokenizer.from_pretrained(
            model_name_or_path,
            trust_remote_code=True,
            use_fast=False,
            local_files_only=False,
        )
    except Exception as e:
        print(f"Warning: Online tokenizer loading failed, trying local files only: {e}")
        tokenizer = AutoTokenizer.from_pretrained(
            model_name_or_path,
            trust_remote_code=True,
            use_fast=False,
            local_files_only=True,
        )
    
    # Safe tokenizer configuration
    if not hasattr(tokenizer, 'pad_token_id') or tokenizer.pad_token_id is None:
        tokenizer.pad_token_id = tokenizer.eos_token_id
    tokenizer.padding_side = "left"
    
    return model, tokenizer

def get_data(forget_corpora, retain_corpora, min_len=50, max_len=2000, batch_size=4):
    """
    Flexible data loader supporting:
    - Local files
    - HuggingFace datasets (when accessible)
    - WMDP corpora
    - WikiText
    """
    from datasets import load_dataset
    import os

    def load_local_file(file_path):
        """Load text from local file with chunking support"""
        data = []
        try:
            if os.path.isfile(file_path):
                with open(file_path, 'r', encoding='utf-8') as f:
                    text = f.read().strip()
                    
                    if min_len < len(text) <= max_len:
                        data.append(text)
                    else:
                        # Split long text into chunks
                        words = text.split()
                        current_chunk = []
                        
                        for word in words:
                            current_chunk.append(word)
                            chunk_text = " ".join(current_chunk)
                            
                            if min_len < len(chunk_text) <= max_len:
                                data.append(chunk_text)
                                current_chunk = []
                        
                        # Handle last chunk
                        if current_chunk:
                            chunk_text = " ".join(current_chunk)
                            if min_len < len(chunk_text) <= max_len:
                                data.append(chunk_text)
                                
            return data
        except Exception as e:
            print(f"Warning: Failed to load local file {file_path}: {e}")
            return []

    def normalize_text(rec):
        if 'text' in rec and isinstance(rec['text'], str):
            return rec['text']
        parts = []
        for k in ['question', 'prompt', 'instruction']:
            if k in rec and isinstance(rec[k], str):
                parts.append(rec[k])
        if 'choices' in rec and isinstance(rec['choices'], (list, tuple)):
            parts.append("Choices: " + " | ".join(map(str, rec['choices'])))
        for k in ['context', 'passage', 'body', 'response', 'completion']:
            if k in rec and isinstance(rec[k], str):
                parts.append(rec[k])
        return " ".join(parts) if parts else str(rec)

    def load_wmdp(domain, role):
        data = []
        # 1) 전용 데이터셋 시도 (예: cais/wmdp-bio-forget-corpus)
        try:
            ds = load_dataset(f"cais/wmdp-{domain}-{role}-corpus", split="train", cache_dir="./data_cache")
            for rec in ds:
                txt = normalize_text(rec)
                if min_len < len(txt) <= max_len:
                    data.append(txt)
            return data
        except Exception:
            pass
        # 2) 통합 데이터셋 시도 (cais/wmdp-corpora config=bio/cyber)
        try:
            ds = load_dataset("cais/wmdp-corpora", domain, split="train", cache_dir="./data_cache")
            role_key = None
            for k in ['role', 'split', 'subset', 'category', 'part']:
                if k in ds.features:
                    role_key = k; break
            if role_key:
                ds = ds.filter(lambda x: str(x.get(role_key, "")).lower() == role)
            for rec in ds:
                txt = normalize_text(rec)
                if min_len < len(txt) <= max_len:
                    data.append(txt)
            return data
        except Exception:
            return []

    def load_corpus(spec):
        spec = spec.strip()
        print(f"Processing corpus spec: '{spec}'")
        
        # Handle local dataset folders first (./datasets/ 경로)
        if spec.startswith("./datasets/"):
            print(f"Loading local dataset folder: {spec}")
            try:
                # Map folder paths to actual data locations
                if spec == "./datasets/bio-forget":
                    actual_path = "./datasets/bio-forget/data"
                elif spec == "./datasets/bio-retain":
                    actual_path = "./datasets/bio-retain/bio-retain-corpus"
                elif spec == "./datasets/cyber-forget":
                    actual_path = "./datasets/cyber-forget/cyber-forget-corpus"
                elif spec == "./datasets/cyber-retain":
                    actual_path = "./datasets/cyber-retain/cyber-retain-corpus"
                elif spec == "./datasets/wikitext":
                    actual_path = "./datasets/wikitext/wikitext-2-raw-v1"
                else:
                    actual_path = spec
                
                print(f"Loading from actual path: {actual_path}")
                ds = load_dataset(actual_path, split="train", cache_dir="./data_cache")
                data = []
                for rec in ds:
                    txt = normalize_text(rec)
                    if min_len < len(txt) <= max_len:
                        data.append(txt)
                print(f"Loaded {len(data)} items from local dataset folder")
                return data
            except Exception as e:
                print(f"Failed to load local dataset folder: {e}")
                return []
        
        # Handle local files (파일인 경우만)
        if os.path.isfile(spec):
            print(f"Loading local file: {spec}")
            data = load_local_file(spec)
            print(f"Loaded {len(data)} items from local file")
            return data
        
        # Handle dataset specs
        spec_lower = spec.lower()
        if spec_lower == "wikitext":
            raw = load_dataset("wikitext", "wikitext-2-raw-v1", split="test", cache_dir="./data_cache")
            return [str(x['text']) for x in raw if min_len < len(x['text']) <= max_len]
        if ":" in spec_lower:
            dom, role = spec_lower.split(":")
            return load_wmdp(dom, role)
        
        print(f"Unknown corpus spec: {spec}")
        return []

    def to_batches(data):
        if not data:
            return []
        return [data[i:i+batch_size] for i in range(0, len(data), batch_size)]

    # Process forget and retain corpora
    forget_batches = []
    retain_batches = []
    
    for corpus in forget_corpora:
        data = load_corpus(corpus)
        if data:
            batches = to_batches(data)
            # 스플릿 단위로 보존 (리스트의 리스트)
            forget_batches.append(batches)
    
    for corpus in retain_corpora:
        data = load_corpus(corpus)
        if data:
            batches = to_batches(data)
            retain_batches.append(batches)
    
    total_forget = sum(len(s) for s in forget_batches)
    total_retain = sum(len(s) for s in retain_batches)
    print(f"Data loading complete: {len(forget_batches)} forget splits ({total_forget} batches), "
          f"{len(retain_batches)} retain splits ({total_retain} batches)")
    
    return forget_batches, retain_batches

def build_forbidden_token_ids(forget_data_list, tokenizer, vocab_top_k: Optional[int] = None,
                             rate: float = 0.01, abs_cap: int = 20000):
    """
    Build forbidden token set V_S from forget data with frequency filtering.
    
    Mode: Frequency-based filtering (vs PMI-based refinement in build_forbidden_token_ids_pmi)
    - Filters out high-frequency tokens (likely stop words)
    - Applies V_S token filtering (numbers, whitespace, pure punctuation)
    - Use this for basic V_S construction
    """
    from collections import Counter
    
    cnt = Counter()
    for forget_data in forget_data_list:
        for batch in forget_data:
            # assume batch is a list[str] or list of texts
            enc = tokenizer(batch, return_tensors="pt", padding=True, truncation=True, max_length=512)
            ids = enc["input_ids"]  # [B, L]
            for row in ids.tolist():
                cnt.update(row)
    
    # remove padding/specials
    special = set(tokenizer.all_special_ids or [])
    for sid in list(special):
        if sid in cnt:
            del cnt[sid]
    
    # frequency filtering
    total_positions = sum(cnt.values())
    if total_positions > 0:
        freq_cut = max(1, min(int(rate * total_positions), abs_cap))
        cnt = Counter({k: v for k, v in cnt.items() if v <= freq_cut})  # KEEP Counter
    
    if vocab_top_k:
        vs = [tid for tid, _ in cnt.most_common(vocab_top_k)]
    else:
        vs = list(cnt.keys())
    
    vs = sorted(set(vs))
    return _filter_vs_tokens(tokenizer, vs)

def compute_perplexity(model, tokenizer, data_list, max_samples=100):
    """
    Compute perplexity on retain data to measure utility preservation.
    Fix: ignore padding tokens with ignore_index=-100
    """
    model.eval()
    device = next(model.parameters()).device
    total_loss = 0.0
    total_tokens = 0
    n_samples = 0
    
    with torch.no_grad():
        for data in data_list:
            for batch in data:
                if n_samples >= max_samples:
                    break
                    
                inputs = tokenizer(batch, return_tensors="pt", padding=True, truncation=True, max_length=512).to(device)
                
                # Fix: mask padding tokens with -100
                labels = inputs["input_ids"].clone()
                labels[inputs["attention_mask"] == 0] = -100
                
                outputs = model(**inputs)
                logits = outputs.logits
                
                # Shift for next token prediction
                shift_logits = logits[..., :-1, :].contiguous()
                shift_labels = labels[..., 1:].contiguous()
                
                # Compute loss with ignore_index=-100
                loss_fct = torch.nn.CrossEntropyLoss(ignore_index=-100, reduction='sum')
                loss = loss_fct(shift_logits.view(-1, shift_logits.size(-1)), shift_labels.view(-1))
                
                # Count only non-padding tokens
                valid_tokens = (shift_labels != -100).sum().item()
                
                total_loss += loss.item()
                total_tokens += valid_tokens
                n_samples += 1
    
    avg_loss = total_loss / total_tokens if total_tokens > 0 else float('inf')
    perplexity = torch.exp(torch.tensor(avg_loss)).item()
    return perplexity

def evaluate_suppression_effect(model, tokenizer, V_S, forget_eval_mini, sample_size=8):
    """
    Evaluate π_θ(S) on held-out forget data for unbiased λ control.
    """
    model.eval()
    device = next(model.parameters()).device
    total = 0.0
    n = 0
    
    with torch.no_grad():
        for dataset in forget_eval_mini:
            for batch in dataset:
                if n >= sample_size:
                    break
                enc = tokenizer(batch, return_tensors="pt", padding=True, truncation=True, max_length=512).to(device)
                logits = model(**enc).logits.float()
                probs = torch.softmax(logits, dim=-1)
                mass_S = probs[..., V_S].sum(dim=-1)
                pS_batch = mass_S.mean()
                total += pS_batch.item()
                n += 1
                if n >= sample_size:
                    break
            if n >= sample_size:
                break
    
    return (total / max(n, 1)) if n > 0 else 0.1

def effective_tokens(tokenizer, data_list, max_batches=64):
    """
    Calculate effective token count based on actual data for more accurate confidence intervals.
    """
    n = 0
    for k, data in enumerate(data_list):
        for b, batch in enumerate(data):
            if k * len(data) + b >= max_batches:
                break
            enc = tokenizer(batch, return_tensors="pt", padding=True, truncation=True, max_length=512)
            n += int(enc["attention_mask"].sum().item())
    return n

def create_suppression_report(base_model, updated_model, tokenizer, V_S, forget_data_list, retain_data_list, epsilon, wilson_max_n=2048):
    """
    Create a comprehensive suppression report.
    """
    print("=== ETU Suppression Report ===")
    
    # Calculate π_θ(S) on both models
    base_p_S = estimate_probability_mass(base_model, tokenizer, forget_data_list, V_S, sample_size=100)
    updated_p_S = estimate_probability_mass(updated_model, tokenizer, forget_data_list, V_S, sample_size=100)
    
    # Calculate perplexity on retain data (if available)
    base_perplexity = updated_perplexity = None
    if retain_data_list and any(len(s) > 0 for s in retain_data_list):
        base_perplexity = compute_perplexity(base_model, tokenizer, retain_data_list)
        updated_perplexity = compute_perplexity(updated_model, tokenizer, retain_data_list)
        print(f"  - Perplexity on retain: {updated_perplexity:.2f}")
    
    # Calculate suppression and utility ratios
    suppression_ratio = updated_p_S / max(base_p_S, 1e-8)  # 작을수록 억제 효과
    
    print(f"=== Results ===")
    print(f"  - π_base(S): {base_p_S:.4f}")
    print(f"  - π_θ(S): {updated_p_S:.4f}")
    print(f"  - Suppression ratio: {suppression_ratio:.2f} (updated/base)")
    print(f"  - Target ε: {epsilon:.4f}")
    print(f"  - Target achieved: {'✓' if updated_p_S <= epsilon else '✗'}")
    
    # Calculate Wilson upper bounds with actual token count
    n_eff = max(1, min(effective_tokens(tokenizer, forget_data_list), 100_000))
    upper_base = wilson_upper(base_p_S, n_eff=n_eff, max_n=wilson_max_n)
    upper_upd = wilson_upper(updated_p_S, n_eff=n_eff, max_n=wilson_max_n)
    print(f"  - 95% upper π_base(S): {upper_base:.4f}")
    print(f"  - 95% upper π_θ(S): {upper_upd:.4f}")
    print(f"  - Target achieved (95% upper): {'✓' if upper_upd <= epsilon else '✗'}")
    
    result = {
        'base_p_S': base_p_S,
        'updated_p_S': updated_p_S,
        'upper_base': upper_base,
        'upper_upd': upper_upd,
        'suppression_ratio': suppression_ratio,
        'target_achieved_point': updated_p_S <= epsilon,
        'target_achieved_upper': upper_upd <= epsilon,
        'target': {'epsilon': epsilon, 'achieved_point': updated_p_S <= epsilon, 'achieved_upper': upper_upd <= epsilon},
        'ci': {'method': 'wilson', 'n_eff': n_eff, 'upper_base': upper_base, 'upper_updated': upper_upd},
    }
    
    if base_perplexity is not None and updated_perplexity is not None:
        perplexity_ratio = updated_perplexity / max(base_perplexity, 1e-8)
        result.update({
            'base_perplexity': base_perplexity,
            'updated_perplexity': updated_perplexity,
            'perplexity_ratio': perplexity_ratio,
        })
    
    return result

################################
##### V_S Token Filtering #####
################################

def _filter_vs_tokens(tokenizer, ids):
    """
    Filter V_S tokens to remove numbers, whitespace, and pure punctuation.
    """
    keep = []
    for t in ids:
        if t in set(tokenizer.all_special_ids or []): 
            continue
        try:
            s = tokenizer.decode([t], skip_special_tokens=True)
        except Exception:
            continue
        st = s.strip()
        if not st:
            continue
        if st.isdigit():
            continue
        if all(ch in string.punctuation for ch in st):
            continue
        keep.append(t)
    return keep

################################
##### Preference Loss Functions #####
################################

def _sequence_logprob_from_logits(logits: torch.Tensor, input_ids: torch.Tensor, attention_mask: torch.Tensor) -> torch.Tensor:
    """
    평균 토큰 logprob (next-token 방식). padding은 무시.
    logits: [B, L, V], input_ids: [B, L], attention_mask: [B, L]
    """
    # shift for next-token prediction
    shift_logits = logits[..., :-1, :].contiguous().float()
    shift_labels = input_ids[..., 1:].contiguous()
    shift_mask   = attention_mask[..., 1:].contiguous()
    logp = torch.log_softmax(shift_logits, dim=-1)
    # gather token logp
    token_logp = logp.gather(dim=-1, index=shift_labels.unsqueeze(-1)).squeeze(-1)
    # mask padding
    token_logp = token_logp * shift_mask
    # 평균(유효토큰만)
    denom = torch.clamp(shift_mask.sum(dim=-1), min=1)
    return (token_logp.sum(dim=-1) / denom)  # [B]

def preference_loss_from_batches(
    model,
    tokenizer,
    pos_texts: List[str],
    neg_texts: List[str],
    format_: str = "npo",
    beta: float = 0.1,
    margin: float = 0.0,
    max_length: int = 256,
    reference_model=None,  # NEW: reference model for DPO
) -> torch.Tensor:
    """
    pos=retain 쪽, neg=forget 쪽.
    - NPO: max(0, margin + logp_neg - logp_pos) 의 평균 (hinge 없으면 logistic도 가능)
    - DPO: -log σ( β (logp_pos - logp_neg) ) or with reference model
    """
    device = next(model.parameters()).device
    enc_pos = tokenizer(pos_texts, return_tensors="pt", padding=True, truncation=True, max_length=max_length).to(device)
    enc_neg = tokenizer(neg_texts, return_tensors="pt", padding=True, truncation=True, max_length=max_length).to(device)
    
    # current model (grad ON)
    logits_pos = model(**enc_pos).logits
    logits_neg = model(**enc_neg).logits
    logp_pos = _sequence_logprob_from_logits(logits_pos, enc_pos["input_ids"], enc_pos["attention_mask"])  # [B]
    logp_neg = _sequence_logprob_from_logits(logits_neg, enc_neg["input_ids"], enc_neg["attention_mask"])  # [B]

    if format_.lower() == "dpo" and reference_model is not None:
        # reference (no grad)
        reference_model.eval()
        ref_device = next(reference_model.parameters()).device
        with torch.no_grad():
            r_logits_pos = reference_model(**{k: v.to(ref_device) for k, v in enc_pos.items()}).logits
            r_logp_pos = _sequence_logprob_from_logits(r_logits_pos, enc_pos["input_ids"].to(ref_device), enc_pos["attention_mask"].to(ref_device))
            r_logits_neg = reference_model(**{k: v.to(ref_device) for k, v in enc_neg.items()}).logits
            r_logp_neg = _sequence_logprob_from_logits(r_logits_neg, enc_neg["input_ids"].to(ref_device), enc_neg["attention_mask"].to(ref_device))
        diff = (logp_pos - r_logp_pos.to(logp_pos.device)) - (logp_neg - r_logp_neg.to(logp_pos.device))
        loss = torch.nn.functional.softplus(-beta * diff).mean()
        return loss

    if format_.lower() == "dpo":
        # self-DPO fallback
        diff = logp_pos - logp_neg
        return torch.nn.functional.softplus(-beta * diff).mean()

    # NPO
    diff = logp_pos - logp_neg
    if margin > 0:
        return torch.relu(margin - diff).mean()
    else:
        return torch.relu(-diff).mean()
