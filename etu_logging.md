(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ python3 run_etu_h200.py --forget_corpora "./datasets/cyber-forget" --retain_corpora "./datasets/bio-retain" --batch_size 1 --max_num_batches 3 --layer_id 7  --ve
rbose
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
Loading checkpoint shards: 100%|████████████████████████████████████████████| 8/8 [00:06<00:00,  1.24it/s]
Loading checkpoint shards: 100%|███████████████████████████████████████████| 8/8 [00:00<00:00, 377.85it/s]
📊 데이터 로딩 중...
🔍 Forget 데이터셋: ['./datasets/cyber-forget']
🔍 Retain 데이터셋: ['./datasets/bio-retain']
🔧 Layer 설정: layer_id=7, layer_ids=7
Processing corpus spec: './datasets/cyber-forget'
Loading local dataset folder: ./datasets/cyber-forget
Loading from actual path: ./datasets/cyber-forget/cyber-forget-corpus
HF google storage unreachable. Downloading and preparing it from source
Generating train split: 1000 examples [00:00, 9035.67 examples/s]
Loaded 12 items from local dataset folder
Processing corpus spec: './datasets/bio-retain'
Loading local dataset folder: ./datasets/bio-retain
Loading from actual path: ./datasets/bio-retain/bio-retain-corpus
HF google storage unreachable. Downloading and preparing it from source
Generating train split: 60887 examples [00:05, 10359.22 examples/s]
Loaded 4106 items from local dataset folder
Data loading complete: 12 forget batches, 4106 retain batches
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
forget_corpora=./datasets/cyber-forget
retain_corpora=./datasets/bio-retain
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
Applying LoRA to layers: [7]
trainable params: 13,631,488 || all params: 7,255,363,584 || trainable%: 0.1879
/data/aiuser3/ETU/etu/unlearn.py:99: FutureWarning: `torch.cuda.amp.GradScaler(args...)` is deprecated. Please use `torch.amp.GradScaler('cuda', args...)` instead.
  scaler = torch.cuda.amp.GradScaler(enabled=(use_cuda and not use_bf16))
Building forbidden token set V_S...
V_S size: 258 tokens (0.8% of vocab)
Estimating base probability mass p_S over V_S...
Estimated p_S (π_base over V_S): 0.2761
[info] |V_S|/V = 0.8%, π_base(S)=0.2761, ε=0.0500
V_S preview: ['er', '▁a', 'on', 're', '▁the', '▁w', 'it', 'al', 'ed', 'ing']
Initial λ: 1.9807 → expected qλ(S)≈0.0500
======= Epoch 0 =======
  0%|                                                                               | 0/1 [00:00<?, ?it/s]/data/aiuser3/ETU/etu/unlearn.py:220: FutureWarning: `torch.cuda.amp.autocast(args...)` is deprecated. Please use `torch.amp.autocast('cuda', args...)` instead.
  with torch.cuda.amp.autocast(enabled=use_amp,
[HIGH] πθ(S)=0.3062 [95% normal 0.2251,0.3874 | Wilson↑ 0.3922] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=11.66 | λ=1.981
100%|███████████████████████████████████████| 1/1 [00:00<00:00,  2.28it/s, loss=11.7, πθ(S)=0.306, λ=1.98]
=== ETU Suppression Report ===
  - Perplexity on retain: 4.95
=== Results ===
  - π_base(S): 0.2761
  - π_θ(S): 0.2753
  - Suppression ratio: 1.00 (updated/base)
  - Target ε: 0.0500
  - Target achieved: ✗
  - 95% upper π_base(S): 0.3070
  - 95% upper π_θ(S): 0.3061
  - Target achieved (95% upper): ✗
Saved suppression report to models/zephyr-7b-beta_etu_epsilon-0.05_lambda-1.9807_2025-09-02-13-14-40/suppression_report.json
Merging LoRA weights into base model...
Saved V_S to models/zephyr-7b-beta_etu_epsilon-0.05_lambda-1.9807_2025-09-02-13-14-40/V_S.ids.json
Saved ETU model to models/zephyr-7b-beta_etu_epsilon-0.05_lambda-1.9807_2025-09-02-13-14-40
Saved args to models/zephyr-7b-beta_etu_epsilon-0.05_lambda-1.9807_2025-09-02-13-14-40/args.json
Saved metrics to models/zephyr-7b-beta_etu_epsilon-0.05_lambda-1.9807_2025-09-02-13-14-40/metrics.json
✅ ETU 실행 완료!
(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ 
