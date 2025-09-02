(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ python3 run_etu_h200.py   --forget_corpora "./datasets/bio-forget"   --retain_corpora "./datasets/bio-retain"   --batch_size 8   --max_num_batches 50   --num_epochs 3   --layer_id 7   --epsilon 0.05   --lambda_max 30.0   --lambda_update_freq 1   --lambda_eta 0.75   --use_pmi_vs   --pmi_top_k 128   --pmi_min_count 10   --pmi_smoothing 1.0   --retain_weight 0.25   --wilson_max_n 10000   --pinsker_cap 0.10   --use_upper_for_lambda   --verbose
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
Loading checkpoint shards: 100%|████████████████████████████████████████████| 8/8 [00:06<00:00,  1.23it/s]
Loading checkpoint shards: 100%|███████████████████████████████████████████| 8/8 [00:00<00:00, 374.93it/s]
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
lambda_max=30.0
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
pmi_top_k=128
pmi_min_count=10
pmi_smoothing=1.0
pmi_max_batches=500
vs_preview_k=10
span_masking=False
span_ngram_max=3
allow_negative_lambda=False
lambda_eta=0.75
pinsker_cap=0.1
use_upper_for_lambda=True
wilson_max_n=10000
log_every=10
output_dir=
seed=None
retain_weight=0.25
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
[debug] adjust_lambda signature: ('lambda_val', 'current_pS', 'kl_delta', 'epsilon', 'eta', 'lambda_max', 'allow_negative', 'pinsker_cap')
[debug] use_upper_for_lambda=True, pinsker_cap=0.1
[λ-update] EMA πθ(S)=0.0455 (upper=0.0649) → λ=0.051→0.051 | E[qλ(S)]=0.0500 | KL_EMA=0.0248
 14%|█████▏                              | 1/7 [00:01<00:08,  1.46s/it, loss=0.00438, πθ(S)=0.044, λ=0.05][OK] πθ(S)=0.0405 [95% normal 0.0208,0.0603 | Wilson↑ 0.0546] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=0.02252 | λ=0.051
[debug] adjust_lambda signature: ('lambda_val', 'current_pS', 'kl_delta', 'epsilon', 'eta', 'lambda_max', 'allow_negative', 'pinsker_cap')
[debug] use_upper_for_lambda=True, pinsker_cap=0.1
[λ-update] EMA πθ(S)=0.0444 (upper=0.0591) → λ=0.051→0.051 | E[qλ(S)]=0.0500 | KL_EMA=0.0513
 29%|██████████▌                          | 2/7 [00:02<00:07,  1.42s/it, loss=0.0246, πθ(S)=0.041, λ=0.05][NEAR] πθ(S)=0.0564 [95% normal 0.0298,0.0831 | Wilson↑ 0.0704] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=0.01957 | λ=0.051
[debug] adjust_lambda signature: ('lambda_val', 'current_pS', 'kl_delta', 'epsilon', 'eta', 'lambda_max', 'allow_negative', 'pinsker_cap')
[debug] use_upper_for_lambda=True, pinsker_cap=0.1
[λ-update] EMA πθ(S)=0.0467 (upper=0.0597) → λ=0.051→0.051 | E[qλ(S)]=0.0500 | KL_EMA=0.0868
 43%|███████████████▊                     | 3/7 [00:04<00:05,  1.37s/it, loss=0.0241, πθ(S)=0.056, λ=0.05][OK] πθ(S)=0.0470 [95% normal 0.0301,0.0638 | Wilson↑ 0.0575] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=0.04172 | λ=0.051
[debug] adjust_lambda signature: ('lambda_val', 'current_pS', 'kl_delta', 'epsilon', 'eta', 'lambda_max', 'allow_negative', 'pinsker_cap')
[debug] use_upper_for_lambda=True, pinsker_cap=0.1
[λ-update] EMA πθ(S)=0.0467 (upper=0.0572) → λ=0.051→0.051 | E[qλ(S)]=0.0500 | KL_EMA=0.1252
 57%|█████████████████████▏               | 4/7 [00:05<00:04,  1.35s/it, loss=0.0461, πθ(S)=0.047, λ=0.05][OK] πθ(S)=0.0453 [95% normal 0.0268,0.0638 | Wilson↑ 0.0544] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=0.03385 | λ=0.051
[debug] adjust_lambda signature: ('lambda_val', 'current_pS', 'kl_delta', 'epsilon', 'eta', 'lambda_max', 'allow_negative', 'pinsker_cap')
[debug] use_upper_for_lambda=True, pinsker_cap=0.1
[λ-update] EMA πθ(S)=0.0465 (upper=0.0558) → λ=0.051→0.051 | E[qλ(S)]=0.0500 | KL_EMA=0.1603
 71%|██████████████████████████▍          | 5/7 [00:06<00:02,  1.36s/it, loss=0.0426, πθ(S)=0.045, λ=0.05][NEAR] πθ(S)=0.0592 [95% normal 0.0382,0.0801 | Wilson↑ 0.0684] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=0.08256 | λ=0.051
[debug] adjust_lambda signature: ('lambda_val', 'current_pS', 'kl_delta', 'epsilon', 'eta', 'lambda_max', 'allow_negative', 'pinsker_cap')
[debug] use_upper_for_lambda=True, pinsker_cap=0.1
[λ-update] EMA πθ(S)=0.0476 (upper=0.0560) → λ=0.051→0.051 | E[qλ(S)]=0.0500 | KL_EMA=0.1985
 86%|███████████████████████████████▋     | 6/7 [00:08<00:01,  1.38s/it, loss=0.0881, πθ(S)=0.059, λ=0.05][HIGH] πθ(S)=0.0741 [95% normal 0.0442,0.1041 | Wilson↑ 0.0838] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=0.03868 | λ=0.051
[debug] adjust_lambda signature: ('lambda_val', 'current_pS', 'kl_delta', 'epsilon', 'eta', 'lambda_max', 'allow_negative', 'pinsker_cap')
[debug] use_upper_for_lambda=True, pinsker_cap=0.1
[λ-update] EMA πθ(S)=0.0494 (upper=0.0575) → λ=0.051→0.051 | E[qλ(S)]=0.0500 | KL_EMA=0.2269
100%|█████████████████████████████████████| 7/7 [00:09<00:00,  1.36s/it, loss=0.0436, πθ(S)=0.074, λ=0.05]
======= Epoch 1 =======
  0%|                                                                               | 0/7 [00:00<?, ?it/s][OK] πθ(S)=0.0416 [95% normal 0.0258,0.0573 | Wilson↑ 0.0484] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=0.411 | λ=0.051
[debug] adjust_lambda signature: ('lambda_val', 'current_pS', 'kl_delta', 'epsilon', 'eta', 'lambda_max', 'allow_negative', 'pinsker_cap')
[debug] use_upper_for_lambda=True, pinsker_cap=0.1
[λ-update] EMA πθ(S)=0.0487 (upper=0.0560) → λ=0.051→0.051 | E[qλ(S)]=0.0500 | KL_EMA=0.2601
 14%|█████▍                                | 1/7 [00:01<00:07,  1.25s/it, loss=0.414, πθ(S)=0.042, λ=0.05][OK] πθ(S)=0.0404 [95% normal 0.0207,0.0601 | Wilson↑ 0.0468] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=0.1409 | λ=0.051
[debug] adjust_lambda signature: ('lambda_val', 'current_pS', 'kl_delta', 'epsilon', 'eta', 'lambda_max', 'allow_negative', 'pinsker_cap')
[debug] use_upper_for_lambda=True, pinsker_cap=0.1
[λ-update] EMA πθ(S)=0.0481 (upper=0.0550) → λ=0.051→0.051 | E[qλ(S)]=0.0500 | KL_EMA=0.2657
 29%|██████████▊                           | 2/7 [00:02<00:06,  1.32s/it, loss=0.144, πθ(S)=0.040, λ=0.05][NEAR] πθ(S)=0.0566 [95% normal 0.0300,0.0832 | Wilson↑ 0.0638] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=0.385 | λ=0.051
[debug] adjust_lambda signature: ('lambda_val', 'current_pS', 'kl_delta', 'epsilon', 'eta', 'lambda_max', 'allow_negative', 'pinsker_cap')
[debug] use_upper_for_lambda=True, pinsker_cap=0.1
[λ-update] EMA πθ(S)=0.0484 (upper=0.0551) → λ=0.051→0.051 | E[qλ(S)]=0.0500 | KL_EMA=0.2714
 43%|████████████████▎                     | 3/7 [00:03<00:05,  1.29s/it, loss=0.391, πθ(S)=0.057, λ=0.05][OK] πθ(S)=0.0465 [95% normal 0.0297,0.0632 | Wilson↑ 0.0526] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=0.3144 | λ=0.051
[debug] adjust_lambda signature: ('lambda_val', 'current_pS', 'kl_delta', 'epsilon', 'eta', 'lambda_max', 'allow_negative', 'pinsker_cap')
[debug] use_upper_for_lambda=True, pinsker_cap=0.1
[λ-update] EMA πθ(S)=0.0482 (upper=0.0545) → λ=0.051→0.051 | E[qλ(S)]=0.0500 | KL_EMA=0.2564
 57%|██████████████████████▎                | 4/7 [00:05<00:03,  1.30s/it, loss=0.32, πθ(S)=0.046, λ=0.05][OK] πθ(S)=0.0451 [95% normal 0.0266,0.0636 | Wilson↑ 0.0509] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=0.1042 | λ=0.051
[debug] adjust_lambda signature: ('lambda_val', 'current_pS', 'kl_delta', 'epsilon', 'eta', 'lambda_max', 'allow_negative', 'pinsker_cap')
[debug] use_upper_for_lambda=True, pinsker_cap=0.1
[λ-update] EMA πθ(S)=0.0480 (upper=0.0540) → λ=0.051→0.051 | E[qλ(S)]=0.0500 | KL_EMA=0.2269
 71%|███████████████████████████▏          | 5/7 [00:07<00:03,  1.60s/it, loss=0.122, πθ(S)=0.045, λ=0.05][NEAR] πθ(S)=0.0589 [95% normal 0.0380,0.0798 | Wilson↑ 0.0652] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=0.2581 | λ=0.051
[debug] adjust_lambda signature: ('lambda_val', 'current_pS', 'kl_delta', 'epsilon', 'eta', 'lambda_max', 'allow_negative', 'pinsker_cap')
[debug] use_upper_for_lambda=True, pinsker_cap=0.1
[λ-update] EMA πθ(S)=0.0484 (upper=0.0541) → λ=0.051→0.051 | E[qλ(S)]=0.0500 | KL_EMA=0.2127
 86%|█████████████████████████████████▍     | 6/7 [00:08<00:01,  1.52s/it, loss=0.27, πθ(S)=0.059, λ=0.05][HIGH] πθ(S)=0.0734 [95% normal 0.0436,0.1032 | Wilson↑ 0.0801] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=0.07324 | λ=0.051
[debug] adjust_lambda signature: ('lambda_val', 'current_pS', 'kl_delta', 'epsilon', 'eta', 'lambda_max', 'allow_negative', 'pinsker_cap')
[debug] use_upper_for_lambda=True, pinsker_cap=0.1
[λ-update] EMA πθ(S)=0.0492 (upper=0.0548) → λ=0.051→0.051 | E[qλ(S)]=0.0500 | KL_EMA=0.1931
100%|█████████████████████████████████████| 7/7 [00:09<00:00,  1.42s/it, loss=0.0786, πθ(S)=0.073, λ=0.05]
======= Epoch 2 =======
  0%|                                                                               | 0/7 [00:00<?, ?it/s][OK] πθ(S)=0.0418 [95% normal 0.0260,0.0576 | Wilson↑ 0.0468] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=0.2426 | λ=0.051
[debug] adjust_lambda signature: ('lambda_val', 'current_pS', 'kl_delta', 'epsilon', 'eta', 'lambda_max', 'allow_negative', 'pinsker_cap')
[debug] use_upper_for_lambda=True, pinsker_cap=0.1
[λ-update] EMA πθ(S)=0.0489 (upper=0.0542) → λ=0.051→0.051 | E[qλ(S)]=0.0500 | KL_EMA=0.1840
 14%|█████▍                                | 1/7 [00:01<00:07,  1.25s/it, loss=0.245, πθ(S)=0.042, λ=0.05][OK] πθ(S)=0.0403 [95% normal 0.0206,0.0600 | Wilson↑ 0.0450] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=0.09632 | λ=0.051
[debug] adjust_lambda signature: ('lambda_val', 'current_pS', 'kl_delta', 'epsilon', 'eta', 'lambda_max', 'allow_negative', 'pinsker_cap')
[debug] use_upper_for_lambda=True, pinsker_cap=0.1
[λ-update] EMA πθ(S)=0.0485 (upper=0.0537) → λ=0.051→0.051 | E[qλ(S)]=0.0500 | KL_EMA=0.1667
 29%|██████████▌                          | 2/7 [00:02<00:06,  1.31s/it, loss=0.0988, πθ(S)=0.040, λ=0.05][NEAR] πθ(S)=0.0565 [95% normal 0.0299,0.0831 | Wilson↑ 0.0619] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=0.1771 | λ=0.051
[debug] adjust_lambda signature: ('lambda_val', 'current_pS', 'kl_delta', 'epsilon', 'eta', 'lambda_max', 'allow_negative', 'pinsker_cap')
[debug] use_upper_for_lambda=True, pinsker_cap=0.1
[λ-update] EMA πθ(S)=0.0487 (upper=0.0538) → λ=0.051→0.051 | E[qλ(S)]=0.0500 | KL_EMA=0.1588
 43%|████████████████▎                     | 3/7 [00:03<00:05,  1.29s/it, loss=0.182, πθ(S)=0.057, λ=0.05][OK] πθ(S)=0.0466 [95% normal 0.0298,0.0634 | Wilson↑ 0.0514] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=0.162 | λ=0.051
[debug] adjust_lambda signature: ('lambda_val', 'current_pS', 'kl_delta', 'epsilon', 'eta', 'lambda_max', 'allow_negative', 'pinsker_cap')
[debug] use_upper_for_lambda=True, pinsker_cap=0.1
[λ-update] EMA πθ(S)=0.0486 (upper=0.0535) → λ=0.051→0.051 | E[qλ(S)]=0.0500 | KL_EMA=0.1493
 57%|█████████████████████▋                | 4/7 [00:05<00:03,  1.29s/it, loss=0.167, πθ(S)=0.047, λ=0.05][OK] πθ(S)=0.0451 [95% normal 0.0266,0.0635 | Wilson↑ 0.0496] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=0.06092 | λ=0.051
[debug] adjust_lambda signature: ('lambda_val', 'current_pS', 'kl_delta', 'epsilon', 'eta', 'lambda_max', 'allow_negative', 'pinsker_cap')
[debug] use_upper_for_lambda=True, pinsker_cap=0.1
[λ-update] EMA πθ(S)=0.0484 (upper=0.0531) → λ=0.051→0.051 | E[qλ(S)]=0.0500 | KL_EMA=0.1388
 71%|██████████████████████████▍          | 5/7 [00:06<00:02,  1.31s/it, loss=0.0704, πθ(S)=0.045, λ=0.05][NEAR] πθ(S)=0.0591 [95% normal 0.0382,0.0801 | Wilson↑ 0.0642] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=0.1628 | λ=0.051
[debug] adjust_lambda signature: ('lambda_val', 'current_pS', 'kl_delta', 'epsilon', 'eta', 'lambda_max', 'allow_negative', 'pinsker_cap')
[debug] use_upper_for_lambda=True, pinsker_cap=0.1
[λ-update] EMA πθ(S)=0.0487 (upper=0.0533) → λ=0.051→0.051 | E[qλ(S)]=0.0500 | KL_EMA=0.1377
 86%|████████████████████████████████▌     | 6/7 [00:07<00:01,  1.34s/it, loss=0.169, πθ(S)=0.059, λ=0.05][HIGH] πθ(S)=0.0737 [95% normal 0.0438,0.1035 | Wilson↑ 0.0791] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=0.0447 | λ=0.051
[debug] adjust_lambda signature: ('lambda_val', 'current_pS', 'kl_delta', 'epsilon', 'eta', 'lambda_max', 'allow_negative', 'pinsker_cap')
[debug] use_upper_for_lambda=True, pinsker_cap=0.1
[λ-update] EMA πθ(S)=0.0494 (upper=0.0539) → λ=0.051→0.051 | E[qλ(S)]=0.0500 | KL_EMA=0.1286
100%|█████████████████████████████████████| 7/7 [00:09<00:00,  1.30s/it, loss=0.0502, πθ(S)=0.074, λ=0.05]
=== ETU Suppression Report ===
  - Perplexity on retain: 5.14
=== Results ===
  - π_base(S): 0.0525
  - π_θ(S): 0.0519
  - Suppression ratio: 0.99 (updated/base)
  - Target ε: 0.0500
  - Target achieved: ✗
  - 95% upper π_base(S): 0.0608
  - 95% upper π_θ(S): 0.0602
  - Target achieved (95% upper): ✗
Saved suppression report to models/zephyr-7b-beta_etu_epsilon-0.05_lambda-0.0505_2025-09-02-16-56-26/suppression_report.json
Merging LoRA weights into base model...
Saved V_S to models/zephyr-7b-beta_etu_epsilon-0.05_lambda-0.0505_2025-09-02-16-56-26/V_S.ids.json
