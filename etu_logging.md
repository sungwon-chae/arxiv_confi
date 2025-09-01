(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ python3 run_etu_h200.py   --forget_corpora "test_data/forget.txt"   --retain_corpora "test_data/retain.txt"   --batch_size 1   --max_num_batches 3   --layer_id 7   --min_len 10   --max_len 500   --verbose
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
   - batch_size: 1
   - frozen_on_cpu: False
   - lora_r: 512
   - lora_alpha: 1024
   - max_num_batches: 3
🚀 ETU 실행 시작...
📥 모델 로딩 중...
Loading checkpoint shards: 100%|███████████████████████████████| 8/8 [00:06<00:00,  1.22it/s]
Loading checkpoint shards: 100%|██████████████████████████████| 8/8 [00:00<00:00, 374.12it/s]
📊 데이터 로딩 중...
🔍 Forget 데이터셋: test_data/forget.txt
🔍 Retain 데이터셋: test_data/retain.txt
Processing corpus spec: 't'
Unknown corpus spec: t
Processing corpus spec: 'e'
Unknown corpus spec: e
Processing corpus spec: 's'
Unknown corpus spec: s
Processing corpus spec: 't'
Unknown corpus spec: t
Processing corpus spec: '_'
Unknown corpus spec: _
Processing corpus spec: 'd'
Unknown corpus spec: d
Processing corpus spec: 'a'
Unknown corpus spec: a
Processing corpus spec: 't'
Unknown corpus spec: t
Processing corpus spec: 'a'
Unknown corpus spec: a
Processing corpus spec: '/'
Loading local file: /
Loaded 0 items from local file
Processing corpus spec: 'f'
Unknown corpus spec: f
Processing corpus spec: 'o'
Unknown corpus spec: o
Processing corpus spec: 'r'
Unknown corpus spec: r
Processing corpus spec: 'g'
Unknown corpus spec: g
Processing corpus spec: 'e'
Unknown corpus spec: e
Processing corpus spec: 't'
Unknown corpus spec: t
Processing corpus spec: '.'
Loading local file: .
Loaded 0 items from local file
Processing corpus spec: 't'
Unknown corpus spec: t
Processing corpus spec: 'x'
Unknown corpus spec: x
Processing corpus spec: 't'
Unknown corpus spec: t
Processing corpus spec: 't'
Unknown corpus spec: t
Processing corpus spec: 'e'
Unknown corpus spec: e
Processing corpus spec: 's'
Unknown corpus spec: s
Processing corpus spec: 't'
Unknown corpus spec: t
Processing corpus spec: '_'
Unknown corpus spec: _
Processing corpus spec: 'd'
Unknown corpus spec: d
Processing corpus spec: 'a'
Unknown corpus spec: a
Processing corpus spec: 't'
Unknown corpus spec: t
Processing corpus spec: 'a'
Unknown corpus spec: a
Processing corpus spec: '/'
Loading local file: /
Loaded 0 items from local file
Processing corpus spec: 'r'
Unknown corpus spec: r
Processing corpus spec: 'e'
Unknown corpus spec: e
Processing corpus spec: 't'
Unknown corpus spec: t
Processing corpus spec: 'a'
Unknown corpus spec: a
Processing corpus spec: 'i'
Unknown corpus spec: i
Processing corpus spec: 'n'
Unknown corpus spec: n
Processing corpus spec: '.'
Loading local file: .
Loaded 0 items from local file
Processing corpus spec: 't'
Unknown corpus spec: t
Processing corpus spec: 'x'
Unknown corpus spec: x
Processing corpus spec: 't'
Unknown corpus spec: t
Data loading complete: 0 forget batches, 0 retain batches
====ETU Config====
gpu_id=0
multi_gpu=False
batch_size=1
max_num_batches=3
frozen_on_cpu=False
use_lora=True
lora_r=512
lora_alpha=1024
epsilon=0.05
lambda_max=12.0
lambda_update_freq=25
forget_corpora=test_data/forget.txt
retain_corpora=test_data/retain.txt
model_name_or_path=HuggingFaceH4/zephyr-7b-beta
deterministic=False
verbose=True
lr=1e-05
num_epochs=1
min_len=10
max_len=500
layer_ids=7
param_ids=
name_keywords=
module_str=
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
Applying LoRA to layers: [7]
trainable params: 13,631,488 || all params: 7,255,363,584 || trainable%: 0.1879
/data/aiuser3/ETU/etu/unlearn.py:99: FutureWarning: `torch.cuda.amp.GradScaler(args...)` is deprecated. Please use `torch.amp.GradScaler('cuda', args...)` instead.
  scaler = torch.cuda.amp.GradScaler(enabled=(use_cuda and not use_bf16))
❌ 오류 발생: min() iterable argument is empty
Traceback (most recent call last):
  File "/data/aiuser3/ETU/run_etu_h200.py", line 263, in run_h200_optimized_etu
    run_etu(
  File "/data/aiuser3/ETU/etu/unlearn.py", line 104, in run_etu
    min([len(f) for f in forget_data_list]),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: min() iterable argument is empty
(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ 
