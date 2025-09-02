(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ python3 run_etu_h200.py
--forget_corpora "bio:forget"
--retain_corpora "bio:retain"
--batch_size 64
--max_num_batches 500
--num_epochs 2
--layer_ids "4,5,6,7,8"
--lora_target_modules "q_proj,k_proj,v_proj,o_proj,gate_proj,up_proj,down_proj"
--lora_r 256
--epsilon 0.10
--lambda_max 20.0
--lambda_update_freq 10
--lambda_eta 0.25
--use_pmi_vs
--pmi_min_count 3
--pmi_top_k 1024
--pmi_smoothing 1.0
--pmi_max_batches 2000
--span_masking
--span_ngram_max 4
--retain_weight 0.1
--wilson_max_n 10000
--pinsker_cap 0.10
--mixed_precision bf16
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
   - lora_r: 512
   - lora_alpha: 1024
   - max_num_batches: 500
   - mixed_precision: bf16
   - gradient_accumulation_steps: 4
🚀 ETU 실행 시작...
📥 모델 로딩 중...
Loading checkpoint shards: 100%|████████████████████████████████████████████| 8/8 [00:06<00:00,  1.23it/s]
Loading checkpoint shards: 100%|███████████████████████████████████████████| 8/8 [00:00<00:00, 380.00it/s]
🔧 Frozen 모델을 GPU에 로드
📊 데이터 로딩 중...
🔍 Forget 데이터셋: ['./datasets/cyber-forget']
🔍 Retain 데이터셋: ['./datasets/bio-retain']
🔧 Layer 설정: layer_id=7, layer_ids=7
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
use_lora=True
lora_r=512
lora_alpha=1024
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
layer_id=7
layer_ids=7
param_ids=
name_keywords=q_proj,k_proj,v_proj,o_proj
module_str={model_name}.model.layers[{layer_id}]
use_pmi_vs=True
vocab_top_k=1000
vs_freq_rate=0.1
vs_abs_cap=1000
pmi_top_k=1000
pmi_min_count=10
pmi_smoothing=0.1
pmi_max_batches=500
vs_preview_k=10
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
Applying LoRA to layers: [7]
trainable params: 13,631,488 || all params: 7,255,363,584 || trainable%: 0.1879
Building forbidden token set V_S...
[PMI] counting capped at 500 batches per split
[PMI] split 0: used 1 batches (cap=500)
[PMI] split 0: used 75 batches (cap=500)
[V_S] token filter kept 1/10 (10.0%) after _filter_vs_tokens
V_S (PMI-refined) size: 1 tokens
[warn] PMI V_S too small → fallback to freq-based augmentation
V_S after fallback: 258 tokens
V_S fallback preview: ['er', '▁a', 'on', 're', '▁the', '▁w', 'it', 'al', 'ed', 'ing']
Top PMI tokens preview: ['er', '▁a', 'on', 're', '▁the', '▁w', 'it', 'al', 'ed', 'ing']
V_S size: 258 tokens (0.8% of vocab)
Estimating base probability mass p_S over V_S...
Estimated p_S (π_base over V_S): 0.1826
[info] |V_S|/V = 0.8%, π_base(S)=0.1826, ε=0.0500
V_S preview: ['er', '▁a', 'on', 're', '▁the', '▁w', 'it', 'al', 'ed', 'ing']
Initial λ: 1.4457 → expected qλ(S)≈0.0500
======= Epoch 0 =======
  0%|                                                                               | 0/1 [00:00<?, ?it/s][HIGH] πθ(S)=0.1823 [95% normal 0.1564,0.2081 | Wilson↑ 0.2095] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=0.05351 | λ=1.446
[λ-update] EMA πθ(S)=0.1809 (controller=0.2080) → λ=1.446→1.546 | E[qλ(S)]=0.0455 | KL_EMA=2.2733
100%|█████████████████████████████████████| 1/1 [00:00<00:00,  1.39it/s, loss=0.0535, πθ(S)=0.182, λ=1.55]
======= Epoch 1 =======
  0%|                                                                               | 0/1 [00:00<?, ?it/s][HIGH] πθ(S)=0.1796 [95% normal 0.1540,0.2053 | Wilson↑ 0.2046] | E[qλ(S)]=0.0455 | ε=0.0500 | KL=0.05521 | λ=1.546
[λ-update] EMA πθ(S)=0.1795 (controller=0.2045) → λ=1.546→1.646 | E[qλ(S)]=0.0413 | KL_EMA=3.4532
100%|█████████████████████████████████████| 1/1 [00:00<00:00,  1.79it/s, loss=0.0552, πθ(S)=0.180, λ=1.65]
======= Epoch 2 =======
  0%|                                                                               | 0/1 [00:00<?, ?it/s][HIGH] πθ(S)=0.1780 [95% normal 0.1524,0.2036 | Wilson↑ 0.2029] | E[qλ(S)]=0.0413 | ε=0.0500 | KL=0.05723 | λ=1.646
[λ-update] EMA πθ(S)=0.1786 (controller=0.2036) → λ=1.646→1.746 | E[qλ(S)]=0.0375 | KL_EMA=4.2083
100%|█████████████████████████████████████| 1/1 [00:00<00:00,  1.76it/s, loss=0.0572, πθ(S)=0.178, λ=1.75]
=== ETU Suppression Report ===
  - Perplexity on retain: 5.09
=== Results ===
  - π_base(S): 0.1826
  - π_θ(S): 0.1768
  - Suppression ratio: 0.97 (updated/base)
  - Target ε: 0.0500
  - Target achieved: ✗
  - 95% upper π_base(S): 0.2098
  - 95% upper π_θ(S): 0.2037
  - Target achieved (95% upper): ✗
Saved suppression report to models/zephyr-7b-beta_etu_epsilon-0.05_lambda-1.7457_2025-09-02-19-52-06/suppression_report.json
Merging LoRA weights into base model...
Saved V_S to models/zephyr-7b-beta_etu_epsilon-0.05_lambda-1.7457_2025-09-02-19-52-06/V_S.ids.json
Saved ETU model to models/zephyr-7b-beta_etu_epsilon-0.05_lambda-1.7457_2025-09-02-19-52-06
Saved args to models/zephyr-7b-beta_etu_epsilon-0.05_lambda-1.7457_2025-09-02-19-52-06/args.json
Saved metrics to models/zephyr-7b-beta_etu_epsilon-0.05_lambda-1.7457_2025-09-02-19-52-06/metrics.json
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

--verbose: command not found
(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ 
