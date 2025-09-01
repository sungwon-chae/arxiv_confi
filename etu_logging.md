(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ python run_etu_h200.py --forget_corpora "cais/wmdp-corpora:cyber-forget-corpus" --retain_corpora "cais/wmdp-corpora:cyber-retain-corpus" --batch_size 4 --max_num_batches 20 --layer_id 7 --verbose
=== ETU H200 GPU 최적화 실행 ===
🚀 H200 GPU 환경 설정 중...
GPU 0: NVIDIA H200 (139.8 GB)
GPU 1: NVIDIA H200 (139.8 GB)
GPU 2: NVIDIA H200 (139.8 GB)
GPU 3: NVIDIA H200 (139.8 GB)
GPU 4: NVIDIA H200 (139.8 GB)
GPU 5: NVIDIA H200 (139.8 GB)
GPU 6: NVIDIA H200 (139.8 GB)
GPU 7: NVIDIA H200 (139.8 GB)
✅ H200 GPU 8개 감지됨
🎯 단일 GPU 모드: GPU 0
🔧 H200 최적화 설정 적용:
   - batch_size: 4
   - frozen_on_cpu: False
   - lora_r: 512
   - lora_alpha: 1024
   - max_num_batches: 20
🚀 ETU 실행 시작...
📥 모델 로딩 중...
Loading checkpoint shards: 100%|████████████████████████████████████████████| 8/8 [00:07<00:00,  1.08it/s]
Loading checkpoint shards: 100%|███████████████████████████████████████████| 8/8 [00:00<00:00, 366.11it/s]
📊 데이터 로딩 중...
🔍 Forget 데이터셋: ['cais/wmdp-corpora:cyber-forget-corpus']
🔍 Retain 데이터셋: ['cais/wmdp-corpora:cyber-retain-corpus']
Layer 설정: layer_id=7, layer_ids=7
Processing corpus spec: 'cais/wmdp-corpora:cyber-forget-corpus'
Converted 'cais/wmdp-corpora:cyber-forget-corpus' to dataset name: 'cyber-forget-corpus'
Loading dataset: cyber-forget-corpus
HF google storage unreachable. Downloading and preparing it from source
Error loading dataset cyber-forget-corpus: Couldn't find file at https://huggingface.co/datasets/cais/wmdp-corpora/resolve/daf89fa9b618b63a624228061a9cebacca88009c/./data_cache/downloads/11a09952dddc72c6cb31feace763612a199bb022c59ea5d6674c4bc51930c09f
Traceback (most recent call last):
  File "/data/aiuser3/ETU/etu/utils.py", line 551, in get_dataset
    dataset = load_dataset("cais/wmdp-corpora", name, cache_dir="./data_cache", split="train")
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/datasets/load.py", line 2545, in load_dataset
    builder_instance.download_and_prepare(
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/datasets/builder.py", line 1003, in download_and_prepare
    self._download_and_prepare(
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/datasets/builder.py", line 1076, in _download_and_prepare
    split_generators = self._split_generators(dl_manager, **split_generators_kwargs)
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/datasets/packaged_modules/parquet/parquet.py", line 43, in _split_generators
    data_files = dl_manager.download_and_extract(self.config.data_files)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/datasets/download/download_manager.py", line 566, in download_and_extract
    return self.extract(self.download(url_or_urls))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/datasets/download/download_manager.py", line 539, in extract
    extracted_paths = map_nested(
                      ^^^^^^^^^^^
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/datasets/utils/py_utils.py", line 467, in map_nested
    _single_map_nested((function, obj, types, None, True, None))
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/datasets/utils/py_utils.py", line 387, in _single_map_nested
    mapped = [_single_map_nested((function, v, types, None, True, None)) for v in pbar]
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/datasets/utils/py_utils.py", line 370, in _single_map_nested
    return function(data_struct)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/datasets/download/download_manager.py", line 451, in _download
    out = cached_path(url_or_filename, download_config=download_config)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/datasets/utils/file_utils.py", line 188, in cached_path
    output_path = get_from_cache(
                  ^^^^^^^^^^^^^^^
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/datasets/utils/file_utils.py", line 570, in get_from_cache
    raise FileNotFoundError(f"Couldn't find file at {url}")
FileNotFoundError: Couldn't find file at https://huggingface.co/datasets/cais/wmdp-corpora/resolve/daf89fa9b618b63a624228061a9cebacca88009c/./data_cache/downloads/11a09952dddc72c6cb31feace763612a199bb022c59ea5d6674c4bc51930c09f
Processing corpus spec: 'cais/wmdp-corpora:cyber-retain-corpus'
Converted 'cais/wmdp-corpora:cyber-retain-corpus' to dataset name: 'cyber-retain-corpus'
Loading dataset: cyber-retain-corpus
HF google storage unreachable. Downloading and preparing it from source
Error loading dataset cyber-retain-corpus: Couldn't find file at https://huggingface.co/datasets/cais/wmdp-corpora/resolve/daf89fa9b618b63a624228061a9cebacca88009c/./data_cache/downloads/faa200f50bf62bea8ffa6cf284df20e92f1620b41702f3fb275ce629abd98caa
Traceback (most recent call last):
  File "/data/aiuser3/ETU/etu/utils.py", line 565, in get_dataset
    dataset = load_dataset("cais/wmdp-corpora", name, cache_dir="./data_cache", split="train")
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/datasets/load.py", line 2545, in load_dataset
    builder_instance.download_and_prepare(
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/datasets/builder.py", line 1003, in download_and_prepare
    self._download_and_prepare(
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/datasets/builder.py", line 1076, in _download_and_prepare
    split_generators = self._split_generators(dl_manager, **split_generators_kwargs)
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/datasets/packaged_modules/parquet/parquet.py", line 43, in _split_generators
    data_files = dl_manager.download_and_extract(self.config.data_files)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/datasets/download/download_manager.py", line 566, in download_and_extract
    return self.extract(self.download(url_or_urls))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/datasets/download/download_manager.py", line 539, in extract
    extracted_paths = map_nested(
                      ^^^^^^^^^^^
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/datasets/utils/py_utils.py", line 467, in map_nested
    _single_map_nested((function, obj, types, None, True, None))
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/datasets/utils/py_utils.py", line 387, in _single_map_nested
    mapped = [_single_map_nested((function, v, types, None, True, None)) for v in pbar]
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/datasets/utils/py_utils.py", line 370, in _single_map_nested
    return function(data_struct)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/datasets/download/download_manager.py", line 451, in _download
    out = cached_path(url_or_filename, download_config=download_config)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/datasets/utils/file_utils.py", line 188, in cached_path
    output_path = get_from_cache(
                  ^^^^^^^^^^^^^^^
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/datasets/utils/file_utils.py", line 570, in get_from_cache
    raise FileNotFoundError(f"Couldn't find file at {url}")
FileNotFoundError: Couldn't find file at https://huggingface.co/datasets/cais/wmdp-corpora/resolve/daf89fa9b618b63a624228061a9cebacca88009c/./data_cache/downloads/faa200f50bf62bea8ffa6cf284df20e92f1620b41702f3fb275ce629abd98caa
Final result: 0 forget batches, 0 retain batches
====ETU Config====
gpu_id=0
multi_gpu=False
batch_size=4
max_num_batches=20
frozen_on_cpu=False
use_lora=True
lora_r=512
lora_alpha=1024
epsilon=0.05
lambda_max=12.0
lambda_update_freq=25
forget_corpora=cais/wmdp-corpora:cyber-forget-corpus
retain_corpora=cais/wmdp-corpora:cyber-retain-corpus
model_name_or_path=HuggingFaceH4/zephyr-7b-beta
deterministic=False
verbose=True
lr=1e-05
num_epochs=1
min_len=10
max_len=512
layer_id=7
layer_ids=7
param_ids=
name_keywords=q_proj,k_proj,v_proj,o_proj
module_str={model_name}.model.layers[{layer_id}]
use_pmi_vs=False
vocab_top_k=1000
vs_freq_rate=0.1
vs_abs_cap=1000
pmi_top_k=1000
pmi_min_count=10
pmi_smoothing=0.1
pmi_max_batches=100
vs_preview_k=10
allow_negative_lambda=False
lambda_eta=0.1
wilson_max_n=1000
log_every=10
output_dir=
seed=None
retain_weight=0.0
retain_broadcast=False
preference_weight=0.0
pref_every=10
pref_format=dpo
pref_beta=0.1
pref_margin=0.1
pref_max_len=512
=====
Applying LoRA for efficient parameter updates...
trainable params: 13,631,488 || all params: 7,255,363,584 || trainable%: 0.1879
/data/aiuser3/ETU/etu/unlearn.py:99: FutureWarning: `torch.cuda.amp.GradScaler(args...)` is deprecated. Please use `torch.amp.GradScaler('cuda', args...)` instead.
  scaler = torch.cuda.amp.GradScaler(enabled=(use_cuda and not use_bf16))
❌ 오류 발생: min() iterable argument is empty
Traceback (most recent call last):
  File "/data/aiuser3/ETU/run_etu_h200.py", line 273, in run_h200_optimized_etu
    run_etu(
  File "/data/aiuser3/ETU/etu/unlearn.py", line 104, in run_etu
    min([len(f) for f in forget_data_list]),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: min() iterable argument is empty
(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ 
