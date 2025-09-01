"""
ETU (Exponential-Tilted Unlearning) Utilities
Original clean implementation based on conversation analysis

This module provides:
- Data loading for local files, HuggingFace datasets, and WMDP corpora
- Model loading and LoRA integration
- Parameter selection and management
- Utility functions for ETU algorithm
"""

import os
import json
import math
import random
import numpy as np
import torch
from typing import List, Dict, Optional, Tuple
from collections import Counter, deque
from transformers import AutoModelForCausalLM, AutoTokenizer
from dataclasses import dataclass

# PEFT/LoRA availability check
try:
    from peft import LoraConfig, get_peft_model, PeftModel
    PEFT_AVAILABLE = True
except ImportError:
    PEFT_AVAILABLE = False

#######################################
##### Data Loading Functions #####
#######################################

def get_data(forget_corpora, retain_corpora, min_len=50, max_len=2000, batch_size=4):
    """
    Flexible data loader supporting:
    - Local files
    - HuggingFace datasets (when accessible)
    - WMDP corpora
    - WikiText
    
    Args:
        forget_corpora: List of forget corpus paths/specs
        retain_corpora: List of retain corpus paths/specs
        min_len: Minimum text length filter
        max_len: Maximum text length filter
        batch_size: Batch size for training
    
    Returns:
        Tuple of (forget_batches, retain_batches)
    """
    from datasets import load_dataset
    
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
    
    def load_huggingface_dataset(name):
        """Load HuggingFace dataset with fallback handling"""
        try:
            if name == "wikitext":
                dataset = load_dataset("wikitext", "wikitext-2-raw-v1", split="test", cache_dir="./data_cache")
                return [str(x['text']) for x in dataset if min_len < len(x['text']) <= max_len]
            
            elif name in ["cyber-forget-corpus", "bio-forget-corpus", "cyber-retain-corpus", "bio-retain-corpus"]:
                dataset = load_dataset("cais/wmdp-corpora", name, split="train", cache_dir="./data_cache")
                return [str(x['text']) for x in dataset if min_len < len(x['text']) <= max_len]
            
            else:
                print(f"Unknown dataset: {name}")
                return []
                
        except Exception as e:
            print(f"Warning: Failed to load HuggingFace dataset {name}: {e}")
            print("This might be due to network restrictions in closed network environment")
            return []
    
    def load_corpus(spec):
        """Load corpus from various sources"""
        spec = spec.strip()
        
        # Local file check
        if os.path.exists(spec):
            return load_local_file(spec)
        
        # HuggingFace dataset specs
        if ":" in spec:
            parts = spec.split(":")
            if len(parts) == 2:
                dataset_name = parts[1]
                return load_huggingface_dataset(dataset_name)
        
        # Direct dataset names
        if spec in ["wikitext", "cyber-forget-corpus", "bio-forget-corpus", "cyber-retain-corpus", "bio-retain-corpus"]:
            return load_huggingface_dataset(spec)
        
        print(f"Unknown corpus spec: {spec}")
        return []
    
    def create_batches(data):
        """Create batches from data list"""
        return [data[i:i + batch_size] for i in range(0, len(data), batch_size)]
    
    # Process forget and retain corpora
    forget_batches = []
    retain_batches = []
    
    for corpus in forget_corpora:
        data = load_corpus(corpus)
        if data:
            batches = create_batches(data)
            forget_batches.extend(batches)
    
    for corpus in retain_corpora:
        data = load_corpus(corpus)
        if data:
            batches = create_batches(data)
            retain_batches.extend(batches)
    
    print(f"Data loading complete: {len(forget_batches)} forget batches, {len(retain_batches)} retain batches")
    
    return forget_batches, retain_batches

#######################################
##### Model Loading Functions #####
#######################################

def load_model(model_name_or_path, train: bool = False, infer_on_cpu: bool = False):
    """
    Load model with appropriate device mapping and error handling
    
    Args:
        model_name_or_path: Model identifier or path
        train: Whether model will be used for training
        infer_on_cpu: Force CPU inference
    
    Returns:
        Loaded model
    """
    use_cuda = torch.cuda.is_available()
    
    # Determine dtype
    if use_cuda and torch.cuda.is_bf16_supported():
        torch_dtype = torch.bfloat16
    elif use_cuda:
        torch_dtype = torch.float16
    else:
        torch_dtype = torch.float32
    
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
            local_files_only=False,
        )
    except Exception as e:
        print(f"Warning: Online loading failed, trying local files only: {e}")
        model = AutoModelForCausalLM.from_pretrained(
            model_name_or_path,
            torch_dtype=torch_dtype,
            trust_remote_code=True,
            device_map=device_map,
            local_files_only=True,
        )
    
    return model

def load_tokenizer(model_name_or_path):
    """Load tokenizer with fallback handling"""
    try:
        tokenizer = AutoTokenizer.from_pretrained(
            model_name_or_path,
            trust_remote_code=True,
            local_files_only=False,
        )
    except Exception as e:
        print(f"Warning: Online loading failed, trying local files only: {e}")
        tokenizer = AutoTokenizer.from_pretrained(
            model_name_or_path,
            trust_remote_code=True,
            local_files_only=True,
        )
    
    # Set padding token
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    
    return tokenizer

#######################################
##### LoRA Integration #####
#######################################

def apply_lora_to_model(args, model, chosen_layers):
    """
    Apply LoRA to specific layers of the model for efficient unlearning
    
    Args:
        args: Training arguments
        model: Base model
        chosen_layers: Layer IDs to apply LoRA to
    
    Returns:
        Model with LoRA applied
    """
    if not PEFT_AVAILABLE:
        raise RuntimeError("PEFT(LoRA) not available. Install peft or disable --use_lora")
    
    # Freeze all layers first
    freeze_all_layers(model)
    
    # Convert chosen_layers to list of integers
    if isinstance(chosen_layers, str):
        chosen_layers = [int(x.strip()) for x in chosen_layers.split(",")]
    elif isinstance(chosen_layers, int):
        chosen_layers = [chosen_layers]
    
    # Create LoRA configuration
    lora_config = LoraConfig(
        r=getattr(args, 'lora_r', 256),
        lora_alpha=getattr(args, 'lora_alpha', 512),
        target_modules=getattr(args, 'lora_target_modules', ["q_proj", "k_proj", "v_proj", "o_proj"]),
        lora_dropout=getattr(args, 'lora_dropout', 0.1),
        bias="none",
        task_type="CAUSAL_LM",
        layers_to_transform=chosen_layers,
    )
    
    model = get_peft_model(model, lora_config)
    model.print_trainable_parameters()
    
    return model

def freeze_all_layers(model):
    """Freeze all parameters in the model"""
    for param in model.parameters():
        param.requires_grad = False

def unfreeze_all_layers(model):
    """Unfreeze all parameters in the model"""
    for param in model.parameters():
        param.requires_grad = True

#######################################
##### Parameter Selection #####
#######################################

def get_params(model, layer_ids, param_ids=None, name_keywords=None, module_str="{model_name}.model.layers[{layer_id}]"):
    """
    Select trainable parameters by layer index and/or name keywords
    
    Args:
        model: Model to extract parameters from
        layer_ids: List of layer IDs to select
        param_ids: List of parameter indices to select
        name_keywords: Keywords to match in parameter names
        module_str: Module path template
    
    Returns:
        List of selected parameters
    """
    params = []
    
    for layer_id in layer_ids:
        layer = _resolve_module(model, module_str, layer_id)
        named = list(layer.named_parameters())
        
        if param_ids is not None:
            # Index-based selection with safety check
            for i in param_ids:
                if not (0 <= i < len(named)):
                    raise IndexError(f"param_ids[{i}] out of range for layer {layer_id} (len={len(named)})")
                params.append(named[i][1])
            continue
        
        # Name keyword-based selection
        for name, p in named:
            if (name_keywords is None) or any(kw in name for kw in name_keywords):
                params.append(p)
    
    return params

def _resolve_module(model, module_str, layer_id):
    """Resolve module path like 'model.model.layers[7]' to actual module"""
    s = module_str.format(model_name="model", layer_id=layer_id)
    mod = model
    
    for part in s.split('.'):
        if part.endswith(']'):  # layers[7] format
            name, idx = part[:-1].split('[')
            mod = getattr(mod, name)[int(idx)]
        else:
            mod = getattr(mod, part)
    
    return mod

#######################################
##### V_S Construction #####
#######################################

def build_forbidden_token_ids(forget_data_list, tokenizer, vocab_top_k: Optional[int] = None,
                             rate: float = 0.01, abs_cap: int = 20000):
    """
    Build forbidden token set V_S from forget data with frequency filtering
    
    Args:
        forget_data_list: List of forget datasets
        tokenizer: Tokenizer for tokenization
        vocab_top_k: Top-k tokens to select
        rate: Fraction of vocabulary to select
        abs_cap: Absolute maximum number of tokens
    
    Returns:
        List of forbidden token IDs
    """
    cnt = Counter()
    
    for forget_data in forget_data_list:
        for batch in forget_data:
            # Tokenize batch
            enc = tokenizer(batch, return_tensors="pt", padding=True, truncation=True, max_length=512)
            ids = enc["input_ids"].tolist()
            attn = enc["attention_mask"].tolist()
            
            # Count tokens (only attended positions)
            for row, mask in zip(ids, attn):
                for tid, m in zip(row, mask):
                    if m:
                        cnt[tid] += 1
    
    # Filter special tokens
    specials = set(tokenizer.all_special_ids or [])
    for s in specials:
        cnt.pop(s, None)
    
    # Select top tokens
    if vocab_top_k:
        top_tokens = [tid for tid, _ in cnt.most_common(vocab_top_k)]
    else:
        vocab_size = tokenizer.vocab_size or 50000
        target_size = min(int(vocab_size * rate), abs_cap)
        top_tokens = [tid for tid, _ in cnt.most_common(target_size)]
    
    return sorted(top_tokens)

#######################################
##### Probability Estimation #####
#######################################

def estimate_p_S_over_VS(frozen_model, tokenizer, forget_data_list, V_S, sample_size: int = 100):
    """
    Estimate base probability mass p_S = π_base(S) over forbidden token set V_S
    
    Args:
        frozen_model: Frozen base model for reference
        tokenizer: Tokenizer
        forget_data_list: List of forget datasets
        V_S: Forbidden token set
        sample_size: Number of samples to use for estimation
    
    Returns:
        Estimated probability mass p_S
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
                logits = frozen_model(**enc).logits
                probs = torch.softmax(logits, dim=-1)
                
                # Calculate mass on V_S
                mass_S = probs[..., V_S].sum(dim=-1)
                pS_batch = mass_S.mean()
                
                total += pS_batch.item()
                n += 1
                
            if n >= sample_size:
                break
    
    return (total / max(n, 1)) if n > 0 else 0.1

def q_mass_from_lambda(pS, lam):
    """
    Compute q_λ(S) = e^{-λ}·pS / (e^{-λ}·pS + 1 - pS)
    
    Args:
        pS: Base probability mass
        lam: Lambda parameter
    
    Returns:
        Tilted probability mass q_λ(S)
    """
    if lam == 0:
        return pS
    
    exp_neg_lam = math.exp(-lam)
    numerator = exp_neg_lam * pS
    denominator = numerator + (1 - pS)
    
    return numerator / denominator

#######################################
##### Utility Functions #####
#######################################

def compute_perplexity(model, tokenizer, data_list, max_length: int = 512):
    """Compute perplexity on given data"""
    model.eval()
    device = next(model.parameters()).device
    total_loss = 0.0
    total_tokens = 0
    
    with torch.no_grad():
        for dataset in data_list:
            for batch in dataset:
                enc = tokenizer(batch, return_tensors="pt", padding=True, truncation=True, max_length=max_length).to(device)
                labels = enc["input_ids"].clone()
                
                outputs = model(**enc, labels=labels)
                loss = outputs.loss
                
                # Count non-padding tokens
                num_tokens = (labels != tokenizer.pad_token_id).sum().item()
                
                total_loss += loss.item() * num_tokens
                total_tokens += num_tokens
    
    if total_tokens == 0:
        return float('inf')
    
    avg_loss = total_loss / total_tokens
    return math.exp(avg_loss)

def create_suppression_report(args, metrics, output_dir):
    """Create and save suppression report"""
    report = {
        "timestamp": str(torch.datetime.now()),
        "args": vars(args),
        "metrics": metrics,
        "summary": {
            "suppression_achieved": metrics.get("final_pi_theta", 0) <= args.epsilon,
            "final_suppression": metrics.get("final_pi_theta", 0),
            "target_epsilon": args.epsilon,
            "suppression_ratio": metrics.get("suppression_ratio", 0)
        }
    }
    
    os.makedirs(output_dir, exist_ok=True)
    report_path = os.path.join(output_dir, "suppression_report.json")
    
    with open(report_path, 'w') as f:
        json.dump(report, f, indent=2)
    
    return report_path

def save_model_and_metrics(model, tokenizer, args, metrics, output_dir):
    """Save model, tokenizer, and metrics"""
    os.makedirs(output_dir, exist_ok=True)
    
    # Save model
    if hasattr(model, 'save_pretrained'):
        model.save_pretrained(output_dir)
    
    # Save tokenizer
    tokenizer.save_pretrained(output_dir)
    
    # Save args
    with open(os.path.join(output_dir, "args.json"), 'w') as f:
        json.dump(vars(args), f, indent=2)
    
    # Save metrics
    with open(os.path.join(output_dir, "metrics.json"), 'w') as f:
        json.dump(metrics, f, indent=2)
    
    print(f"Model and metrics saved to {output_dir}")

#######################################
##### Wilson Confidence Interval #####
#######################################

def wilson_upper_bound(successes: int, total: int, confidence: float = 0.95) -> float:
    """
    Compute Wilson upper confidence bound
    
    Args:
        successes: Number of successful trials
        total: Total number of trials
        confidence: Confidence level (default: 0.95)
    
    Returns:
        Upper confidence bound
    """
    if total == 0:
        return 0.0
    
    p_hat = successes / total
    
    # z-score for given confidence level
    if confidence == 0.95:
        z = 1.959963984540054
    else:
        # For other confidence levels, you'd need to compute z
        z = 1.959963984540054  # Default to 95%
    
    # Wilson interval
    denom = 1 + z * z / total
    center = p_hat + z * z / (2 * total)
    margin = z * math.sqrt((p_hat * (1 - p_hat) + z * z / (4 * total)) / total)
    
    return min(1.0, (center + margin) / denom)

#######################################
##### Main Functions #####
#######################################

def main():
    """Test function for utilities"""
    print("ETU Utilities loaded successfully!")
    print(f"PEFT available: {PEFT_AVAILABLE}")
    
    # Test data loading
    test_forget = ["test_data/forget.txt"]
    test_retain = ["test_data/retain.txt"]
    
    try:
        forget_batches, retain_batches = get_data(test_forget, test_retain, min_len=1, max_len=1000, batch_size=2)
        print(f"Test data loading: {len(forget_batches)} forget, {len(retain_batches)} retain batches")
    except Exception as e:
        print(f"Data loading test failed: {e}")

if __name__ == "__main__":
    main() 
