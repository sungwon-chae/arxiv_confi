(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ export CUDA_VISIBLE_DEVICES=1,2,3,4,5,6,7
(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ python3 run_etu_h200.py   --multi_gpu   --strategy ddp   --forget_corpora "./datasets/cyber-forget"   --retain_corpora "./datasets/bio-retain"   --batch_size 32   --max_num_batches 50   --layer_id 7   --epsilon 0.05   --lambda_max 12.0   --verbose
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
Loading checkpoint shards: 100%|███████████████████████████████████████████| 8/8 [00:00<00:00, 368.89it/s]
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
num_epochs=3
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
pmi_max_batches=500
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
  8%|███▏                                  | 1/12 [00:00<00:03,  3.64it/s, loss=11.7, πθ(S)=0.306, λ=1.98][HIGH] πθ(S)=0.2036 [95% normal 0.0683,0.3390 | Wilson↑ 0.2731] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=1.903 | λ=1.981
 17%|██████▌                                | 2/12 [00:00<00:02,  4.98it/s, loss=1.9, πθ(S)=0.204, λ=1.98][HIGH] πθ(S)=0.2813 [95% normal 0.1904,0.3722 | Wilson↑ 0.3398] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=7.452 | λ=1.981
 25%|█████████▌                            | 3/12 [00:00<00:01,  5.69it/s, loss=7.45, πθ(S)=0.281, λ=1.98][HIGH] πθ(S)=0.1959 [95% normal 0.0644,0.3274 | Wilson↑ 0.2458] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=2.651 | λ=1.981
 33%|████████████▋                         | 4/12 [00:00<00:01,  6.38it/s, loss=2.65, πθ(S)=0.196, λ=1.98][HIGH] πθ(S)=0.3383 [95% normal 0.2585,0.4181 | Wilson↑ 0.3847] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=19.89 | λ=1.981
 42%|███████████████▊                      | 5/12 [00:00<00:01,  6.50it/s, loss=19.9, πθ(S)=0.338, λ=1.98][HIGH] πθ(S)=0.1777 [95% normal 0.0492,0.3062 | Wilson↑ 0.2154] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=1.841 | λ=1.981
 50%|███████████████████                   | 6/12 [00:00<00:00,  7.09it/s, loss=1.84, πθ(S)=0.178, λ=1.98][HIGH] πθ(S)=0.4188 [95% normal 0.3334,0.5043 | Wilson↑ 0.4592] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=13.8 | λ=1.981
 58%|██████████████████████▏               | 7/12 [00:01<00:00,  7.05it/s, loss=13.8, πθ(S)=0.419, λ=1.98][HIGH] πθ(S)=0.1633 [95% normal 0.0391,0.2876 | Wilson↑ 0.1945] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=1.693 | λ=1.981
 67%|█████████████████████████▎            | 8/12 [00:01<00:00,  7.50it/s, loss=1.69, πθ(S)=0.163, λ=1.98][HIGH] πθ(S)=0.1081 [95% normal 0.0326,0.1836 | Wilson↑ 0.1336] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=3.099 | λ=1.981
 75%|█████████████████████████████▎         | 9/12 [00:01<00:00,  7.34it/s, loss=3.1, πθ(S)=0.108, λ=1.98][HIGH] πθ(S)=0.1493 [95% normal 0.0295,0.2690 | Wilson↑ 0.1772] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=1.352 | λ=1.981
 83%|██████████████████████████████▊      | 10/12 [00:01<00:00,  7.74it/s, loss=1.35, πθ(S)=0.149, λ=1.98][HIGH] πθ(S)=0.5510 [95% normal 0.4361,0.6659 | Wilson↑ 0.5854] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=7.913 | λ=1.981
 92%|█████████████████████████████████▉   | 11/12 [00:01<00:00,  7.70it/s, loss=7.91, πθ(S)=0.551, λ=1.98][HIGH] πθ(S)=0.2968 [95% normal 0.1898,0.4038 | Wilson↑ 0.3282] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=8.011 | λ=1.981
100%|█████████████████████████████████████| 12/12 [00:01<00:00,  6.90it/s, loss=8.01, πθ(S)=0.297, λ=1.98]
======= Epoch 1 =======
  0%|                                                                              | 0/12 [00:00<?, ?it/s][HIGH] πθ(S)=0.2947 [95% normal 0.2145,0.3750 | Wilson↑ 0.3240] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=12.23 | λ=1.981
  8%|███▏                                  | 1/12 [00:00<00:01,  8.32it/s, loss=12.2, πθ(S)=0.295, λ=1.98][HIGH] πθ(S)=0.1388 [95% normal 0.0226,0.2550 | Wilson↑ 0.1616] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=1.129 | λ=1.981
 17%|██████▎                               | 2/12 [00:00<00:01,  8.51it/s, loss=1.13, πθ(S)=0.139, λ=1.98][HIGH] πθ(S)=0.2600 [95% normal 0.1713,0.3487 | Wilson↑ 0.2881] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=7.624 | λ=1.981
 25%|█████████▌                            | 3/12 [00:00<00:01,  8.38it/s, loss=7.62, πθ(S)=0.260, λ=1.98][HIGH] πθ(S)=0.1834 [95% normal 0.0552,0.3116 | Wilson↑ 0.2086] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=2.691 | λ=1.981
 33%|████████████▋                         | 4/12 [00:00<00:00,  8.50it/s, loss=2.69, πθ(S)=0.183, λ=1.98][HIGH] πθ(S)=0.3224 [95% normal 0.2435,0.4012 | Wilson↑ 0.3520] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=19.33 | λ=1.981
 42%|███████████████▊                      | 5/12 [00:00<00:00,  8.34it/s, loss=19.3, πθ(S)=0.322, λ=1.98][HIGH] πθ(S)=0.1321 [95% normal 0.0183,0.2459 | Wilson↑ 0.1545] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=0.9771 | λ=1.981
 50%|██████████████████▌                  | 6/12 [00:00<00:00,  8.46it/s, loss=0.977, πθ(S)=0.132, λ=1.98][HIGH] πθ(S)=0.3970 [95% normal 0.3123,0.4818 | Wilson↑ 0.4277] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=12.91 | λ=1.981
 58%|██████████████████████▏               | 7/12 [00:00<00:00,  8.40it/s, loss=12.9, πθ(S)=0.397, λ=1.98][HIGH] πθ(S)=0.1292 [95% normal 0.0165,0.2420 | Wilson↑ 0.1515] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=0.9224 | λ=1.981
 67%|████████████████████████▋            | 8/12 [00:00<00:00,  8.49it/s, loss=0.922, πθ(S)=0.129, λ=1.98][HIGH] πθ(S)=0.0983 [95% normal 0.0259,0.1706 | Wilson↑ 0.1183] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=2.777 | λ=1.981
 75%|████████████████████████████▌         | 9/12 [00:01<00:00,  8.54it/s, loss=2.78, πθ(S)=0.098, λ=1.98][HIGH] πθ(S)=0.1271 [95% normal 0.0151,0.2391 | Wilson↑ 0.1492] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=0.8778 | λ=1.981
 83%|██████████████████████████████      | 10/12 [00:01<00:00,  8.56it/s, loss=0.878, πθ(S)=0.127, λ=1.98][HIGH] πθ(S)=0.5369 [95% normal 0.4218,0.6521 | Wilson↑ 0.5676] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=7.827 | λ=1.981
 92%|█████████████████████████████████▉   | 11/12 [00:01<00:00,  8.58it/s, loss=7.83, πθ(S)=0.537, λ=1.98][HIGH] πθ(S)=0.2856 [95% normal 0.1798,0.3915 | Wilson↑ 0.3144] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=7.923 | λ=1.981
100%|█████████████████████████████████████| 12/12 [00:01<00:00,  8.51it/s, loss=7.92, πθ(S)=0.286, λ=1.98]
======= Epoch 2 =======
  0%|                                                                              | 0/12 [00:00<?, ?it/s][HIGH] πθ(S)=0.2876 [95% normal 0.2080,0.3673 | Wilson↑ 0.3165] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=12.07 | λ=1.981
  8%|███▏                                  | 1/12 [00:00<00:01,  8.28it/s, loss=12.1, πθ(S)=0.288, λ=1.98][HIGH] πθ(S)=0.1234 [95% normal 0.0128,0.2339 | Wilson↑ 0.1452] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=0.8093 | λ=1.981
 17%|██████▏                              | 2/12 [00:00<00:01,  8.41it/s, loss=0.809, πθ(S)=0.123, λ=1.98][HIGH] πθ(S)=0.2492 [95% normal 0.1617,0.3366 | Wilson↑ 0.2769] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=7.394 | λ=1.981
 25%|█████████▌                            | 3/12 [00:00<00:01,  8.44it/s, loss=7.39, πθ(S)=0.249, λ=1.98][HIGH] πθ(S)=0.1725 [95% normal 0.0473,0.2977 | Wilson↑ 0.1972] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=2.842 | λ=1.981
 33%|████████████▋                         | 4/12 [00:00<00:00,  8.53it/s, loss=2.84, πθ(S)=0.173, λ=1.98][HIGH] πθ(S)=0.3120 [95% normal 0.2338,0.3902 | Wilson↑ 0.3414] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=18.82 | λ=1.981
 42%|███████████████▊                      | 5/12 [00:00<00:00,  8.36it/s, loss=18.8, πθ(S)=0.312, λ=1.98][HIGH] πθ(S)=0.1209 [95% normal 0.0113,0.2304 | Wilson↑ 0.1425] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=0.7515 | λ=1.981
 50%|██████████████████▌                  | 6/12 [00:00<00:00,  8.43it/s, loss=0.751, πθ(S)=0.121, λ=1.98][HIGH] πθ(S)=0.3863 [95% normal 0.3020,0.4707 | Wilson↑ 0.4169] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=12.71 | λ=1.981
 58%|██████████████████████▏               | 7/12 [00:00<00:00,  8.38it/s, loss=12.7, πθ(S)=0.386, λ=1.98][HIGH] πθ(S)=0.1202 [95% normal 0.0109,0.2295 | Wilson↑ 0.1418] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=0.7382 | λ=1.981
 67%|████████████████████████▋            | 8/12 [00:00<00:00,  8.47it/s, loss=0.738, πθ(S)=0.120, λ=1.98][HIGH] πθ(S)=0.0937 [95% normal 0.0228,0.1645 | Wilson↑ 0.1133] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=2.605 | λ=1.981
 75%|████████████████████████████▌         | 9/12 [00:01<00:00,  8.51it/s, loss=2.61, πθ(S)=0.094, λ=1.98][HIGH] πθ(S)=0.1197 [95% normal 0.0106,0.2288 | Wilson↑ 0.1413] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=0.731 | λ=1.981
 83%|██████████████████████████████      | 10/12 [00:01<00:00,  8.57it/s, loss=0.731, πθ(S)=0.120, λ=1.98][HIGH] πθ(S)=0.5312 [95% normal 0.4160,0.6465 | Wilson↑ 0.5620] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=8.019 | λ=1.981
 92%|█████████████████████████████████▉   | 11/12 [00:01<00:00,  8.58it/s, loss=8.02, πθ(S)=0.531, λ=1.98][HIGH] πθ(S)=0.2796 [95% normal 0.1744,0.3847 | Wilson↑ 0.3082] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=7.898 | λ=1.981
100%|██████████████████████████████████████| 12/12 [00:01<00:00,  8.50it/s, loss=7.9, πθ(S)=0.280, λ=1.98]
=== ETU Suppression Report ===
  - Perplexity on retain: 4.93
=== Results ===
  - π_base(S): 0.2313
  - π_θ(S): 0.2313
  - Suppression ratio: 1.00 (updated/base)
  - Target ε: 0.0500
  - Target achieved: ✗
  - 95% upper π_base(S): 0.2607
  - 95% upper π_θ(S): 0.2607
  - Target achieved (95% upper): ✗
Saved suppression report to models/zephyr-7b-beta_etu_epsilon-0.05_lambda-1.9807_2025-09-02-15-38-32/suppression_report.json
Merging LoRA weights into base model...
Saved V_S to models/zephyr-7b-beta_etu_epsilon-0.05_lambda-1.9807_2025-09-02-15-38-32/V_S.ids.json
Saved ETU model to models/zephyr-7b-beta_etu_epsilon-0.05_lambda-1.9807_2025-09-02-15-38-32
Saved args to models/zephyr-7b-beta_etu_epsilon-0.05_lambda-1.9807_2025-09-02-15-38-32/args.json
Saved metrics to models/zephyr-7b-beta_etu_epsilon-0.05_lambda-1.9807_2025-09-02-15-38-32/metrics.json
✅ ETU 실행 완료!
(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ 
