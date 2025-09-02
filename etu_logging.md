(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ export CUDA_VISIBLE_DEVICES=1,2,3,4,5,6,7
(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ python3 run_etu_h200.py   --forget_corpora "./datasets/bio-forget"   --retain_corpora "./datasets/bio-retain"   --batch_size 8   --max_num_batches 50   --num_epochs 3   --layer_id 7   --epsilon 0.05   --lambda_max 12.0   --lambda_update_freq 1   --lambda_eta 0.25   --use_pmi_vs   --pmi_top_k 2000   --pmi_min_count 10   --pmi_smoothing 1.0   --span_masking   --span_ngram_max 3   --retain_weight 0.5   --verbose
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
🎯 단일 GPU 모드: GPU 0
🔧 H200 최적화 설정 적용:
   - strategy: ddp
   - batch_size: 8
   - batch_size_per_gpu: 8
   - frozen_on_cpu: False
   - lora_r: 512
   - lora_alpha: 1024
   - max_num_batches: 50
   - mixed_precision: bf16
   - gradient_accumulation_steps: 4
🚀 ETU 실행 시작...
📥 모델 로딩 중...
Loading checkpoint shards: 100%|████████████████████████████████████████████| 8/8 [00:06<00:00,  1.22it/s]
Loading checkpoint shards: 100%|███████████████████████████████████████████| 8/8 [00:00<00:00, 373.66it/s]
🔧 Frozen 모델을 GPU에 로드
📊 데이터 로딩 중...
🔍 Forget 데이터셋: ['./datasets/bio-forget']
🔍 Retain 데이터셋: ['./datasets/bio-retain']
🔧 Layer 설정: layer_id=7, layer_ids=7
Processing corpus spec: './datasets/bio-forget'
Loading local dataset folder: ./datasets/bio-forget
Loading from actual path: ./datasets/bio-forget/data
Loaded 54 items from local dataset folder
Processing corpus spec: './datasets/bio-retain'
Loading local dataset folder: ./datasets/bio-retain
Loading from actual path: ./datasets/bio-retain/bio-retain-corpus
Loaded 4106 items from local dataset folder
Data loading complete: 1 forget splits (7 batches), 1 retain splits (514 batches)
====ETU Config====
gpu_id=0
multi_gpu=False
strategy=ddp
batch_size_per_gpu=8
batch_size=8
max_num_batches=50
frozen_on_cpu=False
use_lora=True
lora_r=512
lora_alpha=1024
epsilon=0.05
lambda_max=12.0
lambda_update_freq=1
forget_corpora=./datasets/bio-forget
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
pmi_top_k=2000
pmi_min_count=10
pmi_smoothing=1.0
pmi_max_batches=500
vs_preview_k=10
span_masking=True
span_ngram_max=3
allow_negative_lambda=False
lambda_eta=0.25
wilson_max_n=1000
log_every=10
output_dir=
seed=None
retain_weight=0.5
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
Building forbidden token set V_S...
V_S (PMI-refined) size: 19 tokens
Top PMI tokens preview: ['▁a', '▁the', '▁in', '▁to', '▁of', '▁and', '▁is', '▁for', '▁H', '▁L']
V_S size: 19 tokens (0.1% of vocab)
Estimating base probability mass p_S over V_S...
Estimated p_S (π_base over V_S): 0.0525
[info] |V_S|/V = 0.1%, π_base(S)=0.0525, ε=0.0500
V_S preview: ['▁a', '▁the', '▁in', '▁to', '▁of', '▁and', '▁is', '▁for', '▁H', '▁L']
Initial λ: 0.0505 → expected qλ(S)≈0.0500
======= Epoch 0 =======
  0%|                                                                               | 0/7 [00:00<?, ?it/s][OK] πθ(S)=0.0442 [95% normal 0.0279,0.0604 | Wilson↑ 0.0634] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=0.004382 | λ=0.051
[λ-update] EMA πθ(S)=0.0454 (upper=0.0649) → λ=0.051→0.051 | E[qλ(S)]=0.0500 | KL_EMA=0.0254
 14%|█████▏                              | 1/7 [00:01<00:08,  1.46s/it, loss=0.00438, πθ(S)=0.044, λ=0.05][OK] πθ(S)=0.0406 [95% normal 0.0208,0.0603 | Wilson↑ 0.0547] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=0.02349 | λ=0.051
[λ-update] EMA πθ(S)=0.0444 (upper=0.0591) → λ=0.051→0.051 | E[qλ(S)]=0.0500 | KL_EMA=0.0546
 29%|██████████▊                           | 2/7 [00:02<00:07,  1.42s/it, loss=0.027, πθ(S)=0.041, λ=0.05][NEAR] πθ(S)=0.0565 [95% normal 0.0299,0.0831 | Wilson↑ 0.0726] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=0.02017 | λ=0.051
[λ-update] EMA πθ(S)=0.0467 (upper=0.0617) → λ=0.051→0.051 | E[qλ(S)]=0.0500 | KL_EMA=0.0895
 43%|███████████████▊                     | 3/7 [00:04<00:05,  1.36s/it, loss=0.0292, πθ(S)=0.056, λ=0.05][OK] πθ(S)=0.0470 [95% normal 0.0301,0.0639 | Wilson↑ 0.0620] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=0.04042 | λ=0.051
[λ-update] EMA πθ(S)=0.0467 (upper=0.0616) → λ=0.051→0.051 | E[qλ(S)]=0.0500 | KL_EMA=0.1288
 57%|█████████████████████▏               | 4/7 [00:05<00:04,  1.34s/it, loss=0.0492, πθ(S)=0.047, λ=0.05][OK] πθ(S)=0.0452 [95% normal 0.0267,0.0637 | Wilson↑ 0.0599] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=0.03071 | λ=0.051
[λ-update] EMA πθ(S)=0.0465 (upper=0.0614) → λ=0.051→0.051 | E[qλ(S)]=0.0500 | KL_EMA=0.1671
 71%|██████████████████████████▍          | 5/7 [00:06<00:02,  1.36s/it, loss=0.0458, πθ(S)=0.045, λ=0.05][NEAR] πθ(S)=0.0591 [95% normal 0.0382,0.0801 | Wilson↑ 0.0755] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=0.06604 | λ=0.051
[λ-update] EMA πθ(S)=0.0475 (upper=0.0625) → λ=0.051→0.051 | E[qλ(S)]=0.0500 | KL_EMA=0.2050
 86%|███████████████████████████████▋     | 6/7 [00:08<00:01,  1.38s/it, loss=0.0759, πθ(S)=0.059, λ=0.05][HIGH] πθ(S)=0.0738 [95% normal 0.0440,0.1037 | Wilson↑ 0.0917] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=0.035 | λ=0.051
[λ-update] EMA πθ(S)=0.0493 (upper=0.0645) → λ=0.051→0.051 | E[qλ(S)]=0.0500 | KL_EMA=0.2320
100%|█████████████████████████████████████| 7/7 [00:09<00:00,  1.36s/it, loss=0.0455, πθ(S)=0.074, λ=0.05]
======= Epoch 1 =======
  0%|                                                                               | 0/7 [00:00<?, ?it/s][OK] πθ(S)=0.0415 [95% normal 0.0258,0.0573 | Wilson↑ 0.0557] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=0.4195 | λ=0.051
[λ-update] EMA πθ(S)=0.0486 (upper=0.0638) → λ=0.051→0.051 | E[qλ(S)]=0.0500 | KL_EMA=0.2660
 14%|█████▍                                | 1/7 [00:01<00:07,  1.25s/it, loss=0.422, πθ(S)=0.042, λ=0.05][OK] πθ(S)=0.0403 [95% normal 0.0206,0.0600 | Wilson↑ 0.0543] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=0.1753 | λ=0.051
[λ-update] EMA πθ(S)=0.0480 (upper=0.0631) → λ=0.051→0.051 | E[qλ(S)]=0.0500 | KL_EMA=0.2712
 29%|███████████▏                           | 2/7 [00:02<00:06,  1.32s/it, loss=0.18, πθ(S)=0.040, λ=0.05][NEAR] πθ(S)=0.0565 [95% normal 0.0299,0.0831 | Wilson↑ 0.0726] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=0.3298 | λ=0.051
[λ-update] EMA πθ(S)=0.0484 (upper=0.0635) → λ=0.051→0.051 | E[qλ(S)]=0.0500 | KL_EMA=0.2692
 43%|████████████████▎                     | 3/7 [00:03<00:05,  1.31s/it, loss=0.341, πθ(S)=0.057, λ=0.05][OK] πθ(S)=0.0465 [95% normal 0.0297,0.0633 | Wilson↑ 0.0614] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=0.339 | λ=0.051
[λ-update] EMA πθ(S)=0.0482 (upper=0.0633) → λ=0.051→0.051 | E[qλ(S)]=0.0500 | KL_EMA=0.2559
 57%|█████████████████████▋                | 4/7 [00:05<00:03,  1.32s/it, loss=0.349, πθ(S)=0.046, λ=0.05][OK] πθ(S)=0.0453 [95% normal 0.0268,0.0638 | Wilson↑ 0.0600] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=0.101 | λ=0.051
[λ-update] EMA πθ(S)=0.0480 (upper=0.0631) → λ=0.051→0.051 | E[qλ(S)]=0.0500 | KL_EMA=0.2224
 71%|███████████████████████████▏          | 5/7 [00:07<00:03,  1.66s/it, loss=0.126, πθ(S)=0.045, λ=0.05][NEAR] πθ(S)=0.0590 [95% normal 0.0381,0.0799 | Wilson↑ 0.0754] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=0.2585 | λ=0.051
[λ-update] EMA πθ(S)=0.0484 (upper=0.0635) → λ=0.051→0.051 | E[qλ(S)]=0.0500 | KL_EMA=0.2073
 86%|████████████████████████████████▌     | 6/7 [00:08<00:01,  1.57s/it, loss=0.271, πθ(S)=0.059, λ=0.05][HIGH] πθ(S)=0.0738 [95% normal 0.0439,0.1037 | Wilson↑ 0.0917] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=0.05641 | λ=0.051
[λ-update] EMA πθ(S)=0.0492 (upper=0.0644) → λ=0.051→0.051 | E[qλ(S)]=0.0500 | KL_EMA=0.1838
100%|█████████████████████████████████████| 7/7 [00:10<00:00,  1.45s/it, loss=0.0693, πθ(S)=0.074, λ=0.05]
======= Epoch 2 =======
  0%|                                                                               | 0/7 [00:00<?, ?it/s][OK] πθ(S)=0.0418 [95% normal 0.0260,0.0576 | Wilson↑ 0.0560] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=0.2499 | λ=0.051
[λ-update] EMA πθ(S)=0.0488 (upper=0.0640) → λ=0.051→0.051 | E[qλ(S)]=0.0500 | KL_EMA=0.1774
 14%|█████▍                                | 1/7 [00:01<00:07,  1.28s/it, loss=0.253, πθ(S)=0.042, λ=0.05][OK] πθ(S)=0.0402 [95% normal 0.0205,0.0598 | Wilson↑ 0.0542] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=0.09256 | λ=0.051
[λ-update] EMA πθ(S)=0.0485 (upper=0.0636) → λ=0.051→0.051 | E[qλ(S)]=0.0500 | KL_EMA=0.1635
 29%|██████████▌                          | 2/7 [00:02<00:06,  1.34s/it, loss=0.0976, πθ(S)=0.040, λ=0.05][NEAR] πθ(S)=0.0565 [95% normal 0.0298,0.0831 | Wilson↑ 0.0725] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=0.1518 | λ=0.051
[λ-update] EMA πθ(S)=0.0487 (upper=0.0638) → λ=0.051→0.051 | E[qλ(S)]=0.0500 | KL_EMA=0.1552
 43%|████████████████▎                     | 3/7 [00:03<00:05,  1.31s/it, loss=0.163, πθ(S)=0.056, λ=0.05][OK] πθ(S)=0.0466 [95% normal 0.0298,0.0634 | Wilson↑ 0.0615] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=0.176 | λ=0.051
[λ-update] EMA πθ(S)=0.0486 (upper=0.0637) → λ=0.051→0.051 | E[qλ(S)]=0.0500 | KL_EMA=0.1490
 57%|█████████████████████▋                | 4/7 [00:05<00:03,  1.32s/it, loss=0.185, πθ(S)=0.047, λ=0.05][OK] πθ(S)=0.0452 [95% normal 0.0267,0.0637 | Wilson↑ 0.0599] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=0.05904 | λ=0.051
[λ-update] EMA πθ(S)=0.0484 (upper=0.0635) → λ=0.051→0.051 | E[qλ(S)]=0.0500 | KL_EMA=0.1356
 71%|██████████████████████████▍          | 5/7 [00:06<00:02,  1.33s/it, loss=0.0817, πθ(S)=0.045, λ=0.05][NEAR] πθ(S)=0.0590 [95% normal 0.0381,0.0799 | Wilson↑ 0.0753] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=0.1557 | λ=0.051
[λ-update] EMA πθ(S)=0.0486 (upper=0.0638) → λ=0.051→0.051 | E[qλ(S)]=0.0500 | KL_EMA=0.1334
 86%|████████████████████████████████▌     | 6/7 [00:08<00:01,  1.36s/it, loss=0.168, πθ(S)=0.059, λ=0.05][HIGH] πθ(S)=0.0738 [95% normal 0.0439,0.1037 | Wilson↑ 0.0917] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=0.03705 | λ=0.051
[λ-update] EMA πθ(S)=0.0494 (upper=0.0646) → λ=0.051→0.051 | E[qλ(S)]=0.0500 | KL_EMA=0.1245
100%|█████████████████████████████████████| 7/7 [00:09<00:00,  1.33s/it, loss=0.0471, πθ(S)=0.074, λ=0.05]
=== ETU Suppression Report ===
  - Perplexity on retain: 5.14
=== Results ===
  - π_base(S): 0.0525
  - π_θ(S): 0.0519
  - Suppression ratio: 0.99 (updated/base)
  - Target ε: 0.0500
  - Target achieved: ✗
  - 95% upper π_base(S): 0.0681
  - 95% upper π_θ(S): 0.0674
  - Target achieved (95% upper): ✗
Saved suppression report to models/zephyr-7b-beta_etu_epsilon-0.05_lambda-0.0505_2025-09-02-16-20-33/suppression_report.json
Merging LoRA weights into base model...
Saved V_S to models/zephyr-7b-beta_etu_epsilon-0.05_lambda-0.0505_2025-09-02-16-20-33/V_S.ids.json
Saved ETU model to models/zephyr-7b-beta_etu_epsilon-0.05_lambda-0.0505_2025-09-02-16-20-33
Saved args to models/zephyr-7b-beta_etu_epsilon-0.05_lambda-0.0505_2025-09-02-16-20-33/args.json
Saved metrics to models/zephyr-7b-beta_etu_epsilon-0.05_lambda-0.0505_2025-09-02-16-20-33/metrics.json
✅ ETU 실행 완료!
(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ 
