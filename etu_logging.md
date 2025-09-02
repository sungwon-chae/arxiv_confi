(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ export CUDA_VISIBLE_DEVICES=1,2,3,4,5,6,7

python3 run_etu_h200.py \
  --multi_gpu \
  --strategy ddp \
  --forget_corpora "./datasets/cyber-forget" \
  --retain_corpora "./datasets/bio-retain" \
  --batch_size 32 \
  --max_num_batches 50 \
  --layer_id 7 \
  --epsilon 0.05 \
  --lambda_max 12.0 \
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
🔄 멀티 GPU 모드: GPU [0, 1, 2, 3, 4, 5, 6]
🔧 멀티 GPU 환경 설정: ddp
✅ DDP 환경 설정 완료
🔧 H200 최적화 설정 적용:
   - strategy: ddp
   - batch_size: 32
   - batch_size_per_gpu: 8
   - frozen_on_cpu: True
   - lora_r: 512
   - lora_alpha: 1024
   - max_num_batches: 50
   - mixed_precision: bf16
   - gradient_accumulation_steps: 4
🚀 ETU 실행 시작...
📥 모델 로딩 중...
Loading checkpoint shards: 100%|███████████████████████████████████████████| 8/8 [00:00<00:00, 377.50it/s]
🔧 Frozen 모델을 CPU에 유지 (메모리 절약)
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
Data loading complete: 1 forget batches, 129 retain batches
====ETU Config====
gpu_id=0
multi_gpu=True
strategy=ddp
batch_size_per_gpu=8
batch_size=32
max_num_batches=50
frozen_on_cpu=True
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
gradient_accumulation_steps=4
mixed_precision=bf16
trust_remote_code=False
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
  0%|                                                                              | 0/12 [00:00<?, ?it/s]/data/aiuser3/ETU/etu/unlearn.py:220: FutureWarning: `torch.cuda.amp.autocast(args...)` is deprecated. Please use `torch.amp.autocast('cuda', args...)` instead.
  with torch.cuda.amp.autocast(enabled=use_amp,
[HIGH] πθ(S)=0.3062 [95% normal 0.2251,0.3874 | Wilson↑ 0.3922] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=11.66 | λ=1.981
  8%|███▏                                  | 1/12 [00:00<00:04,  2.50it/s, loss=11.7, πθ(S)=0.306, λ=1.98][HIGH] πθ(S)=0.2037 [95% normal 0.0683,0.3390 | Wilson↑ 0.2731] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=2.007 | λ=1.981
 17%|██████▎                               | 2/12 [00:00<00:02,  3.94it/s, loss=2.01, πθ(S)=0.204, λ=1.98][HIGH] πθ(S)=0.2818 [95% normal 0.1908,0.3727 | Wilson↑ 0.3402] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=7.462 | λ=1.981
 25%|█████████▌                            | 3/12 [00:00<00:01,  4.90it/s, loss=7.46, πθ(S)=0.282, λ=1.98][HIGH] πθ(S)=0.1965 [95% normal 0.0649,0.3282 | Wilson↑ 0.2464] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=2.692 | λ=1.981
 33%|████████████▋                         | 4/12 [00:00<00:01,  5.76it/s, loss=2.69, πθ(S)=0.197, λ=1.98][HIGH] πθ(S)=0.3376 [95% normal 0.2578,0.4174 | Wilson↑ 0.3840] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=19.78 | λ=1.981
 42%|███████████████▊                      | 5/12 [00:00<00:01,  6.09it/s, loss=19.8, πθ(S)=0.338, λ=1.98][HIGH] πθ(S)=0.1812 [95% normal 0.0517,0.3107 | Wilson↑ 0.2192] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=1.889 | λ=1.981
 50%|███████████████████                   | 6/12 [00:01<00:00,  6.77it/s, loss=1.89, πθ(S)=0.181, λ=1.98][HIGH] πθ(S)=0.4188 [95% normal 0.3333,0.5043 | Wilson↑ 0.4592] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=13.94 | λ=1.981
 58%|██████████████████████▏               | 7/12 [00:01<00:00,  6.86it/s, loss=13.9, πθ(S)=0.419, λ=1.98][HIGH] πθ(S)=0.1731 [95% normal 0.0460,0.3003 | Wilson↑ 0.2050] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=1.905 | λ=1.981
 67%|██████████████████████████             | 8/12 [00:01<00:00,  7.36it/s, loss=1.9, πθ(S)=0.173, λ=1.98][HIGH] πθ(S)=0.1081 [95% normal 0.0326,0.1835 | Wilson↑ 0.1336] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=3.046 | λ=1.981
 75%|████████████████████████████▌         | 9/12 [00:01<00:00,  7.26it/s, loss=3.05, πθ(S)=0.108, λ=1.98][HIGH] πθ(S)=0.1638 [95% normal 0.0394,0.2882 | Wilson↑ 0.1926] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=1.676 | λ=1.981
 83%|██████████████████████████████▊      | 10/12 [00:01<00:00,  7.68it/s, loss=1.68, πθ(S)=0.164, λ=1.98][HIGH] πθ(S)=0.5516 [95% normal 0.4367,0.6664 | Wilson↑ 0.5859] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=7.851 | λ=1.981
 92%|█████████████████████████████████▉   | 11/12 [00:01<00:00,  7.68it/s, loss=7.85, πθ(S)=0.552, λ=1.98][HIGH] πθ(S)=0.2970 [95% normal 0.1900,0.4041 | Wilson↑ 0.3284] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=8.031 | λ=1.981
100%|█████████████████████████████████████| 12/12 [00:01<00:00,  6.44it/s, loss=8.03, πθ(S)=0.297, λ=1.98]
=== ETU Suppression Report ===
  - Perplexity on retain: 4.94
=== Results ===
  - π_base(S): 0.2570
  - π_θ(S): 0.2570
  - Suppression ratio: 1.00 (updated/base)
  - Target ε: 0.0500
  - Target achieved: ✗
  - 95% upper π_base(S): 0.2872
  - 95% upper π_θ(S): 0.2872
  - Target achieved (95% upper): ✗
Saved suppression report to models/zephyr-7b-beta_etu_epsilon-0.05_lambda-1.9807_2025-09-02-15-17-52/suppression_report.json
Merging LoRA weights into base model...
Saved V_S to models/zephyr-7b-beta_etu_epsilon-0.05_lambda-1.9807_2025-09-02-15-17-52/V_S.ids.json
Saved ETU model to models/zephyr-7b-beta_etu_epsilon-0.05_lambda-1.9807_2025-09-02-15-17-52
Saved args to models/zephyr-7b-beta_etu_epsilon-0.05_lambda-1.9807_2025-09-02-15-17-52/args.json
Saved metrics to models/zephyr-7b-beta_etu_epsilon-0.05_lambda-1.9807_2025-09-02-15-17-52/metrics.json
✅ ETU 실행 완료!
(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ 
