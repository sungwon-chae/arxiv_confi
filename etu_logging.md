(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ python3 run_etu_h200.py
--forget_corpora "./datasets/bio-forget/data"
--retain_corpora "./datasets/bio-retain/bio-retain-corpus"
--batch_size 16
--max_num_batches 500
--num_epochs 2
--layer_ids "6,7,8"
--lora_target_modules "q_proj,k_proj,v_proj,o_proj"
--lora_r 128
--epsilon 0.03
--lambda_max 40.0
--lambda_update_freq 1
--lambda_eta 0.5
--use_pmi_vs
--pmi_min_count 3
--pmi_top_k 128
--pmi_smoothing 1.0
--pmi_max_batches 2000
--vocab_top_k 300
--vs_abs_cap 128
--vs_freq_rate 0.0
--span_masking
--span_ngram_max 4
--retain_weight 0.1
--wilson_max_n 10000
--pinsker_cap 0.10
--mixed_precision bf16
--vs_debug
--vs_debug_topk 200
--verbose
=== ETU H200 GPU 최적화 실행 ===
🚀 H200 GPU 환경 설정 중...
GPU 0: NVIDIA H200 (139.8 GB)
GPU 1: NVIDIA H200 (139.8 GB)
GPU 2: NVIDIA H200 (139.8 GB)
GPU 3: NVIDIA H200 (139.8 GB)
GPU 4: NVIDIA H200 (139.8 GB)
GPU 5: NVIDIA H200 (139.8 GB)
GPU 6: NVIDIA H200 (139.8 GB)
✅ H200 GPU 7개 감지됨
[batch heuristic] optimal=128, mem_clamp=55, final=55
🔧 모델 크기 기반 최적 배치 크기: 55
🎯 단일 GPU 모드: GPU 0
🔧 H200 최적화 설정 적용:
   - strategy: single
   - batch_size: 55
   - batch_size_per_gpu: 8
   - frozen_on_cpu: False
   - lora_r: 256
   - lora_alpha: 512
   - max_num_batches: 500
   - mixed_precision: bf16
   - gradient_accumulation_steps: 4
🚀 ETU 실행 시작...
📥 모델 로딩 중...
Loading checkpoint shards: 100%|████████████████████████████████████████████| 8/8 [00:06<00:00,  1.21it/s]
Loading checkpoint shards: 100%|███████████████████████████████████████████| 8/8 [00:00<00:00, 380.95it/s]
🔧 Frozen 모델을 GPU에 로드
📊 데이터 로딩 중...
🔍 Forget 데이터셋: ['./datasets/cyber-forget']
🔍 Retain 데이터셋: ['./datasets/bio-retain']
🔧 Final layer_ids: [5, 6, 7]
🔧 Final lora_target_modules: ['q_proj', 'k_proj', 'v_proj', 'o_proj']
Processing corpus spec: './datasets/cyber-forget'
Loading local dataset folder: ./datasets/cyber-forget
Loading from actual path: ./datasets/cyber-forget/cyber-forget-corpus
Loaded 12 items from local dataset folder
Processing corpus spec: './datasets/bio-retain'
Loading local dataset folder: ./datasets/bio-retain
Loading from actual path: ./datasets/bio-retain/bio-retain-corpus
Loaded 4106 items from local dataset folder
Data loading complete: 1 forget splits (1 batches), 1 retain splits (75 batches)
====ETU Config====
gpu_id=0
multi_gpu=False
strategy=ddp
batch_size_per_gpu=8
batch_size=55
max_num_batches=500
frozen_on_cpu=False
epsilon=0.05
lambda_max=30.0
lambda_update_freq=1
forget_corpora=./datasets/cyber-forget
retain_corpora=./datasets/bio-retain
model_name_or_path=HuggingFaceH4/zephyr-7b-beta
deterministic=False
verbose=True
gradient_accumulation_steps=4
mixed_precision=bf16
trust_remote_code=False
lr=1e-05
num_epochs=3
min_len=10
max_len=512
layer_id=None
layer_ids=[5, 6, 7]
param_ids=None
name_keywords=q_proj,k_proj,v_proj,o_proj
module_str={model_name}.model.layers[{layer_id}]
use_lora=True
lora_r=256
lora_alpha=512
lora_dropout=0.1
lora_target_modules=['q_proj', 'k_proj', 'v_proj', 'o_proj']
use_pmi_vs=True
vocab_top_k=1000
vs_freq_rate=0.1
vs_abs_cap=1000
pmi_top_k=1000
pmi_min_count=10
pmi_smoothing=0.1
pmi_max_batches=500
vs_preview_k=10
vs_debug=False
vs_debug_topk=200
span_masking=False
span_ngram_max=3
allow_negative_lambda=False
lambda_eta=0.1
pinsker_cap=0.1
use_upper_for_lambda=True
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
/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/torch/backends/__init__.py:46: UserWarning: Please use the new API settings to control TF32 behavior, such as torch.backends.cudnn.conv.fp32_precision = 'tf32' or torch.backends.cuda.matmul.fp32_precision = 'ieee'. Old settings, e.g, torch.backends.cuda.matmul.allow_tf32 = True, torch.backends.cudnn.allow_tf32 = True, allowTF32CuDNN() and allowTF32CuBLAS() will be deprecated after Pytorch 2.9. Please see https://pytorch.org/docs/main/notes/cuda.html#tensorfloat-32-tf32-on-ampere-and-later-devices (Triggered internally at /pytorch/aten/src/ATen/Context.cpp:80.)
  self.setter(val)
Applying LoRA for efficient parameter updates...
Applying LoRA to layers: [5, 6, 7]
trainable params: 20,447,232 || all params: 7,262,179,328 || trainable%: 0.2816
Building forbidden token set V_S...
[PMI] counting capped at 500 batches per split
[PMI] split 0: used 1 batches (cap=500)
[PMI] split 0: used 75 batches (cap=500)
[V_S] 스톱리스트로 9개 토큰 제거됨
[V_S] PMI ≤ 0으로 1개 토큰 제거됨
[V_S] token filter kept 0/10 (0.0%) after _filter_vs_tokens
V_S (PMI-refined) size: 0 tokens
[warn] PMI V_S too small → fallback to freq-based augmentation
[V_S] 스톱리스트로 78개 토큰 제거됨
V_S after fallback: 230 tokens
V_S fallback preview: ['<0x0A>', 'on', 're', 'it', 'ed', 'st', 'am', 'im', 'ut', 'ay']
Top PMI tokens preview: ['<0x0A>', 'on', 're', 'it', 'ed', 'st', 'am', 'im', 'ut', 'ay']
V_S size: 230 tokens (0.7% of vocab)
Estimating base probability mass p_S over V_S...
Estimated p_S (π_base over V_S): 0.2197
[info] |V_S|/V = 0.7%, π_base(S)=0.2197, ε=0.0500
V_S preview: ['<0x0A>', 'on', 're', 'it', 'ed', 'st', 'am', 'im', 'ut', 'ay']
Initial λ: 1.6772 → expected qλ(S)≈0.0500
======= Epoch 0 =======
  0%|                                                                               | 0/1 [00:00<?, ?it/s][HIGH] πθ(S)=0.2200 [95% normal 0.1923,0.2477 | Wilson↑ 0.2489] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=0.07697 | λ=1.677
[λ-update] EMA πθ(S)=0.2174 (controller=0.2462) → λ=1.677→1.777 | E[qλ(S)]=0.0455 | KL_EMA=3.8616
100%|██████████████████████████████████████| 1/1 [00:00<00:00,  1.33it/s, loss=0.077, πθ(S)=0.220, λ=1.78]
======= Epoch 1 =======
  0%|                                                                               | 0/1 [00:00<?, ?it/s][HIGH] πθ(S)=0.2147 [95% normal 0.1873,0.2422 | Wilson↑ 0.2413] | E[qλ(S)]=0.0455 | ε=0.0500 | KL=0.07611 | λ=1.777
[λ-update] EMA πθ(S)=0.2154 (controller=0.2419) → λ=1.777→1.877 | E[qλ(S)]=0.0413 | KL_EMA=5.7352
100%|█████████████████████████████████████| 1/1 [00:00<00:00,  1.70it/s, loss=0.0761, πθ(S)=0.215, λ=1.88]
======= Epoch 2 =======
  0%|                                                                               | 0/1 [00:00<?, ?it/s][HIGH] πθ(S)=0.2134 [95% normal 0.1860,0.2408 | Wilson↑ 0.2399] | E[qλ(S)]=0.0413 | ε=0.0500 | KL=0.08031 | λ=1.877
[λ-update] EMA πθ(S)=0.2144 (controller=0.2409) → λ=1.877→1.977 | E[qλ(S)]=0.0375 | KL_EMA=6.8492
100%|█████████████████████████████████████| 1/1 [00:00<00:00,  1.70it/s, loss=0.0803, πθ(S)=0.213, λ=1.98]
=== ETU Suppression Report ===
  - Perplexity on retain: 5.08
=== Results ===
  - π_base(S): 0.2197
  - π_θ(S): 0.2129
  - Suppression ratio: 0.97 (updated/base)
  - Target ε: 0.0500
  - Target achieved: ✗
  - 95% upper π_base(S): 0.2486
  - 95% upper π_θ(S): 0.2415
  - Target achieved (95% upper): ✗
Saved suppression report to models/zephyr-7b-beta_etu_epsilon-0.05_lambda-1.9772_2025-09-02-21-19-32/suppression_report.json
Merging LoRA weights into base model...
Saved V_S to models/zephyr-7b-beta_etu_epsilon-0.05_lambda-1.9772_2025-09-02-21-19-32/V_S.ids.json
Saved ETU model to models/zephyr-7b-beta_etu_epsilon-0.05_lambda-1.9772_2025-09-02-21-19-32
Saved args to models/zephyr-7b-beta_etu_epsilon-0.05_lambda-1.9772_2025-09-02-21-19-32/args.json
Saved metrics to models/zephyr-7b-beta_etu_epsilon-0.05_lambda-1.9772_2025-09-02-21-19-32/metrics.json
✅ ETU 실행 완료!
WARNING:root:could not open file '/etc/apt/sources.list.d/sdcss.list': [Errno 13] Permission denied: '/etc/apt/sources.list.d/sdcss.list'

--forget_corpora: command not found
WARNING:root:could not open file '/etc/apt/sources.list.d/sdcss.list': [Errno 13] Permission denied: '/etc/apt/sources.list.d/sdcss.list'

--retain_corpora: command not found
WARNING:root:could not open file '/etc/apt/sources.list.d/sdcss.list': [Errno 13] Permission denied: '/etc/apt/sources.list.d/sdcss.list'

--batch_size: command not found
WARNING:root:could not open file '/etc/apt/sources.list.d/sdcss.list': [Errno 13] Permission denied: '/etc/apt/sources.list.d/sdcss.list'

--max_num_batches: command not found
WARNING:root:could not open file '/etc/apt/sources.list.d/sdcss.list': [Errno 13] Permission denied: '/etc/apt/sources.list.d/sdcss.list'

--num_epochs: command not found
WARNING:root:could not open file '/etc/apt/sources.list.d/sdcss.list': [Errno 13] Permission denied: '/etc/apt/sources.list.d/sdcss.list'

--layer_ids: command not found
WARNING:root:could not open file '/etc/apt/sources.list.d/sdcss.list': [Errno 13] Permission denied: '/etc/apt/sources.list.d/sdcss.list'

--lora_target_modules: command not found
WARNING:root:could not open file '/etc/apt/sources.list.d/sdcss.list': [Errno 13] Permission denied: '/etc/apt/sources.list.d/sdcss.list'

--lora_r: command not found
WARNING:root:could not open file '/etc/apt/sources.list.d/sdcss.list': [Errno 13] Permission denied: '/etc/apt/sources.list.d/sdcss.list'

--epsilon: command not found
WARNING:root:could not open file '/etc/apt/sources.list.d/sdcss.list': [Errno 13] Permission denied: '/etc/apt/sources.list.d/sdcss.list'

--lambda_max: command not found
WARNING:root:could not open file '/etc/apt/sources.list.d/sdcss.list': [Errno 13] Permission denied: '/etc/apt/sources.list.d/sdcss.list'

--lambda_update_freq: command not found
WARNING:root:could not open file '/etc/apt/sources.list.d/sdcss.list': [Errno 13] Permission denied: '/etc/apt/sources.list.d/sdcss.list'

--lambda_eta: command not found
WARNING:root:could not open file '/etc/apt/sources.list.d/sdcss.list': [Errno 13] Permission denied: '/etc/apt/sources.list.d/sdcss.list'

--use_pmi_vs: command not found
WARNING:root:could not open file '/etc/apt/sources.list.d/sdcss.list': [Errno 13] Permission denied: '/etc/apt/sources.list.d/sdcss.list'

--pmi_min_count: command not found
WARNING:root:could not open file '/etc/apt/sources.list.d/sdcss.list': [Errno 13] Permission denied: '/etc/apt/sources.list.d/sdcss.list'

--pmi_top_k: command not found
WARNING:root:could not open file '/etc/apt/sources.list.d/sdcss.list': [Errno 13] Permission denied: '/etc/apt/sources.list.d/sdcss.list'

--pmi_smoothing: command not found
WARNING:root:could not open file '/etc/apt/sources.list.d/sdcss.list': [Errno 13] Permission denied: '/etc/apt/sources.list.d/sdcss.list'

--pmi_max_batches: command not found
WARNING:root:could not open file '/etc/apt/sources.list.d/sdcss.list': [Errno 13] Permission denied: '/etc/apt/sources.list.d/sdcss.list'

--vocab_top_k: command not found
WARNING:root:could not open file '/etc/apt/sources.list.d/sdcss.list': [Errno 13] Permission denied: '/etc/apt/sources.list.d/sdcss.list'

--vs_abs_cap: command not found
WARNING:root:could not open file '/etc/apt/sources.list.d/sdcss.list': [Errno 13] Permission denied: '/etc/apt/sources.list.d/sdcss.list'

--vs_freq_rate: command not found
WARNING:root:could not open file '/etc/apt/sources.list.d/sdcss.list': [Errno 13] Permission denied: '/etc/apt/sources.list.d/sdcss.list'

--span_masking: command not found
WARNING:root:could not open file '/etc/apt/sources.list.d/sdcss.list': [Errno 13] Permission denied: '/etc/apt/sources.list.d/sdcss.list'

--span_ngram_max: command not found
WARNING:root:could not open file '/etc/apt/sources.list.d/sdcss.list': [Errno 13] Permission denied: '/etc/apt/sources.list.d/sdcss.list'

--retain_weight: command not found
WARNING:root:could not open file '/etc/apt/sources.list.d/sdcss.list': [Errno 13] Permission denied: '/etc/apt/sources.list.d/sdcss.list'

--wilson_max_n: command not found
WARNING:root:could not open file '/etc/apt/sources.list.d/sdcss.list': [Errno 13] Permission denied: '/etc/apt/sources.list.d/sdcss.list'

--pinsker_cap: command not found
WARNING:root:could not open file '/etc/apt/sources.list.d/sdcss.list': [Errno 13] Permission denied: '/etc/apt/sources.list.d/sdcss.list'

--mixed_precision: command not found
WARNING:root:could not open file '/etc/apt/sources.list.d/sdcss.list': [Errno 13] Permission denied: '/etc/apt/sources.list.d/sdcss.list'

--vs_debug: command not found
WARNING:root:could not open file '/etc/apt/sources.list.d/sdcss.list': [Errno 13] Permission denied: '/etc/apt/sources.list.d/sdcss.list'

--vs_debug_topk: command not found
WARNING:root:could not open file '/etc/apt/sources.list.d/sdcss.list': [Errno 13] Permission denied: '/etc/apt/sources.list.d/sdcss.list'

--verbose: command not found
(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ 
