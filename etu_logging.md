(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ python -c "
import sys
sys.path.append('.')
from etu.utils import get_data

print('=== 단계별 데이터 확인 ===')

# 1. 원본 데이터셋 확인
from datasets import load_dataset
cyber_forget = load_dataset('cais/wmdp-corpora', 'cyber-forget-corpus', split='train')
bio_retain = load_dataset('cais/wmdp-corpora', 'bio-retain-corpus', split='train')

print(f'1. 원본 데이터:')
print(f'   Cyber-forget: {len(cyber_forget)} rows')
print(f'   Bio-retain: {len(bio_retain)} rows')

# 2. load_corpus 함수 직접 테스트
from etu.utils import load_corpus
cyber_data = load_corpus('cais/wmdp-corpora:cyber-forget-corpus')
bio_data = load_corpus('cais/wmdp-corpora:bio-retain-corpus')

print(f'\\n2. load_corpus 결과:')
print(f'   Cyber-forget: {len(cyber_data)} items')
print(f'   Bio-retain: {len(bio_data)} items')

# 3. to_batches 함수 직접 테스트
from etu.utils import to_batches
cyber_batches = to_batches(cyber_data)
bio_batches = to_batches(bio_data)

print(f'\\n3. to_batches 결과:')
print(f'   Cyber-forget: {len(cyber_batches)} batches')
for i, batch in enumerate(cyber_batches):
    print(f'     Batch {i}: {len(batch)} items')
print(f'   Bio-retain: {len(bio_batches)} batches')
for i, batch in enumerate(bio_batches):
    print(f'     Batch {i}: {len(batch)} items')
"
=== 단계별 데이터 확인 ===
HF google storage unreachable. Downloading and preparing it from source
Downloading data: 100%|████████████████████████████████████████████████| 222M/222M [00:15<00:00, 14.1MB/s]
Downloading data: 100%|████████████████████████████████████████████████| 220M/220M [00:16<00:00, 13.3MB/s]
Downloading data: 100%|████████████████████████████████████████████████| 222M/222M [00:12<00:00, 17.7MB/s]
Downloading data: 100%|████████████████████████████████████████████████| 221M/221M [00:16<00:00, 13.8MB/s]
Generating train split: 100%|█████████████████████████████| 60887/60887 [00:05<00:00, 10758.13 examples/s]
1. 원본 데이터:
   Cyber-forget: 1000 rows
   Bio-retain: 60887 rows
Traceback (most recent call last):
  File "<string>", line 18, in <module>
ImportError: cannot import name 'load_corpus' from 'etu.utils' (/data/aiuser3/ETU/etu/utils.py)
(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ python -c "
import sys
sys.path.append('.')
from etu.utils import *

# 사용 가능한 함수들 확인
print('=== etu.utils에서 사용 가능한 함수들 ===')
functions = [name for name in dir() if not name.startswith('_')]
for func in functions:
    print(f'  {func}')

# get_data 함수의 내부 구조 확인
print('\\n=== get_data 함수 내부 구조 ===')
import inspect
print(inspect.getsource(get_data))
"
=== etu.utils에서 사용 가능한 함수들 ===
  AutoModelForCausalLM
  AutoTokenizer
  Counter
  Dict
  List
  LoraConfig
  Optional
  PEFT_AVAILABLE
  PeftModel
  Tuple
  adjust_lambda
  apply_lora_to_model
  build_forbidden_token_ids
  build_forbidden_token_ids_pmi
  compute_forbidden_mask
  compute_kl_divergence
  compute_perplexity
  create_preference_pairs
  create_suppression_report
  effective_tokens
  estimate_p_S_over_VS
  estimate_probability_mass
  evaluate_suppression_effect
  extract_layer_activations
  forward_with_cache
  freeze_all_layers
  get_data
  get_params
  get_peft_model
  json
  load_dataset
  load_model
  math
  merge_lora_model
  np
  os
  preference_loss_from_batches
  prepare_model_for_unlearning
  q_mass_from_lambda
  random
  string
  sys
  torch
  unfreeze_all_layers
  wilson_upper

=== get_data 함수 내부 구조 ===
def get_data(forget_corpora, retain_corpora, min_len=50, max_len=2000, batch_size=4):
    """
    Flexible loader for WMDP + WikiText + local files:
    - "bio:forget", "cyber:forget"
    - "bio:retain", "cyber:retain"
    - "wikitext"
    - local file paths
    """
    from datasets import load_dataset
    import os

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

    def load_local_file(file_path):
        """로컬 파일에서 텍스트 로드"""
        data = []
        try:
            if os.path.isfile(file_path):
                with open(file_path, 'r', encoding='utf-8') as f:
                    text = f.read().strip()
                    if min_len < len(text) <= max_len:
                        data.append(text)
                    else:
                        # 긴 텍스트를 청크로 분할
                        words = text.split()
                        current_chunk = []
                        for word in words:
                            current_chunk.append(word)
                            chunk_text = " ".join(current_chunk)
                            if min_len < len(chunk_text) <= max_len:
                                data.append(chunk_text)
                                current_chunk = []
                        # 마지막 청크 처리
                        if current_chunk:
                            chunk_text = " ".join(current_chunk)
                            if min_len < len(chunk_text) <= max_len:
                                data.append(chunk_text)
            return data
        except Exception as e:
            print(f"Warning: Failed to load local file {file_path}: {e}")
            return []

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
        # 로컬 파일 경로 확인
        if os.path.exists(spec):
            return load_local_file(spec)
        
        spec_lower = spec.lower()
        if spec_lower == "wikitext":
            raw = load_dataset("wikitext", "wikitext-2-raw-v1", split="test", cache_dir="./data_cache")
            return [str(x['text']) for x in raw if len(x['text']) > min_len]
        if ":" in spec_lower:
            dom, role = spec_lower.split(":")
            return load_wmdp(dom, role)
        return []

    def to_batches(data):
        return [data[i:i+batch_size] for i in range(0, len(data), batch_size)]

    return (
        [to_batches(load_corpus(c)) for c in forget_corpora],
        [to_batches(load_corpus(c)) for c in retain_corpora],
    )


    def to_batches(data):
        return [data[i:i+batch_size] for i in range(0, len(data), batch_size)]

    return (
        [to_batches(load_corpus(c)) for c in forget_corpora],
        [to_batches(load_corpus(c)) for c in retain_corpora],
    )

(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ 
