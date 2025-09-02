(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ python3 run_etu_h200.py \
  --forget_corpora "./datasets/bio-forget/data" \
  --retain_corpora "./datasets/bio-retain/bio-retain-corpus" \
  --batch_size 8 \
  --max_num_batches 50 \
  --num_epochs 3 \
  --layer_id 7 \
  --epsilon 0.05 \
  --lambda_max 30.0 \
  --lambda_update_freq 1 \
  --lambda_eta 0.75 \
  --use_pmi_vs \
  --pmi_min_count 3 \
  --pmi_top_k 256 \
  --pmi_smoothing 1.0 \
  --retain_weight 0.25 \
  --wilson_max_n 10000 \
  --pinsker_cap 0.10 \
  --use_upper_for_lambda \
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
Loading checkpoint shards: 100%|███████████████████████████████████████████| 8/8 [00:00<00:00, 381.19it/s]
🔧 Frozen 모델을 GPU에 로드
📊 데이터 로딩 중...
🔍 Forget 데이터셋: ['./datasets/bio-forget/data']
🔍 Retain 데이터셋: ['./datasets/bio-retain/bio-retain-corpus']
🔧 Layer 설정: layer_id=7, layer_ids=7
Processing corpus spec: './datasets/bio-forget/data'
Loading local dataset folder: ./datasets/bio-forget/data
Loading from actual path: ./datasets/bio-forget/data
Loaded 54 items from local dataset folder
Processing corpus spec: './datasets/bio-retain/bio-retain-corpus'
Loading local dataset folder: ./datasets/bio-retain/bio-retain-corpus
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
forget_corpora=./datasets/bio-forget/data
retain_corpora=./datasets/bio-retain/bio-retain-corpus
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
pmi_top_k=256
pmi_min_count=3
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
V_S (PMI-refined) size: 189 tokens
Top PMI tokens preview: ['in', 'er', '▁a', 'en', 'at', '▁the', 'al', 'ed', 'ing', '▁in']
V_S size: 189 tokens (0.6% of vocab)
Estimating base probability mass p_S over V_S...
Estimated p_S (π_base over V_S): 0.1422
[info] |V_S|/V = 0.6%, π_base(S)=0.1422, ε=0.0500
V_S preview: ['in', 'er', '▁a', 'en', 'at', '▁the', 'al', 'ed', 'ing', '▁in']
Initial λ: 1.1470 → expected qλ(S)≈0.0500
======= Epoch 0 =======
  0%|                                                                               | 0/7 [00:00<?, ?it/s][HIGH] πθ(S)=0.1652 [95% normal 0.1359,0.1946 | Wilson↑ 0.1967] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=3.504 | λ=1.147
[debug] adjust_lambda signature: ('lambda_val', 'current_pS', 'kl_delta', 'epsilon', 'eta', 'lambda_max', 'allow_negative', 'pinsker_cap')
[debug] use_upper_for_lambda=True, pinsker_cap=0.1
[λ-update] EMA πθ(S)=0.1550 (upper=0.1857) → λ=1.147→1.897 | E[qλ(S)]=0.0243 | KL_EMA=2.9748
 14%|█████▋                                  | 1/7 [00:01<00:08,  1.46s/it, loss=3.5, πθ(S)=0.165, λ=1.90][HIGH] πθ(S)=0.1234 [95% normal 0.0904,0.1563 | Wilson↑ 0.1452] | E[qλ(S)]=0.0243 | ε=0.0500 | KL=5.093 | λ=1.897
[debug] adjust_lambda signature: ('lambda_val', 'current_pS', 'kl_delta', 'epsilon', 'eta', 'lambda_max', 'allow_negative', 'pinsker_cap')
[debug] use_upper_for_lambda=True, pinsker_cap=0.1
[λ-update] EMA πθ(S)=0.1442 (upper=0.1673) → λ=1.897→2.647 | E[qλ(S)]=0.0116 | KL_EMA=4.5019
 29%|███████████▍                            | 2/7 [00:02<00:07,  1.42s/it, loss=5.1, πθ(S)=0.123, λ=2.65][HIGH] πθ(S)=0.1643 [95% normal 0.1216,0.2070 | Wilson↑ 0.1855] | E[qλ(S)]=0.0116 | ε=0.0500 | KL=5.022 | λ=2.647
[debug] adjust_lambda signature: ('lambda_val', 'current_pS', 'kl_delta', 'epsilon', 'eta', 'lambda_max', 'allow_negative', 'pinsker_cap')
[debug] use_upper_for_lambda=True, pinsker_cap=0.1
[λ-update] EMA πθ(S)=0.1470 (upper=0.1674) → λ=2.647→3.397 | E[qλ(S)]=0.0055 | KL_EMA=7.2051
 43%|████████████████▋                      | 3/7 [00:04<00:05,  1.36s/it, loss=5.03, πθ(S)=0.164, λ=3.40][HIGH] πθ(S)=0.1279 [95% normal 0.1013,0.1545 | Wilson↑ 0.1437] | E[qλ(S)]=0.0055 | ε=0.0500 | KL=16.95 | λ=3.397
[debug] adjust_lambda signature: ('lambda_val', 'current_pS', 'kl_delta', 'epsilon', 'eta', 'lambda_max', 'allow_negative', 'pinsker_cap')
[debug] use_upper_for_lambda=True, pinsker_cap=0.1
[λ-update] EMA πθ(S)=0.1438 (upper=0.1604) → λ=3.397→4.147 | E[qλ(S)]=0.0026 | KL_EMA=11.1459
 57%|███████████████████████▍                 | 4/7 [00:05<00:04,  1.34s/it, loss=17, πθ(S)=0.128, λ=4.15][HIGH] πθ(S)=0.1041 [95% normal 0.0769,0.1312 | Wilson↑ 0.1170] | E[qλ(S)]=0.0026 | ε=0.0500 | KL=19.11 | λ=4.147
[debug] adjust_lambda signature: ('lambda_val', 'current_pS', 'kl_delta', 'epsilon', 'eta', 'lambda_max', 'allow_negative', 'pinsker_cap')
[debug] use_upper_for_lambda=True, pinsker_cap=0.1
[λ-update] EMA πθ(S)=0.1395 (upper=0.1540) → λ=4.147→4.147 | E[qλ(S)]=0.0026 | KL_EMA=15.2041
 71%|███████████████████████████▊           | 5/7 [00:06<00:02,  1.35s/it, loss=19.1, πθ(S)=0.104, λ=4.15][HIGH] πθ(S)=0.1619 [95% normal 0.1292,0.1946 | Wilson↑ 0.1758] | E[qλ(S)]=0.0026 | ε=0.0500 | KL=23.61 | λ=4.147
[debug] adjust_lambda signature: ('lambda_val', 'current_pS', 'kl_delta', 'epsilon', 'eta', 'lambda_max', 'allow_negative', 'pinsker_cap')
[debug] use_upper_for_lambda=True, pinsker_cap=0.1
[λ-update] EMA πθ(S)=0.1414 (upper=0.1546) → λ=4.147→4.147 | E[qλ(S)]=0.0026 | KL_EMA=17.1952
 86%|█████████████████████████████████▍     | 6/7 [00:08<00:01,  1.37s/it, loss=23.6, πθ(S)=0.162, λ=4.15][HIGH] πθ(S)=0.1469 [95% normal 0.1064,0.1873 | Wilson↑ 0.1596] | E[qλ(S)]=0.0026 | ε=0.0500 | KL=20.52 | λ=4.147
[debug] adjust_lambda signature: ('lambda_val', 'current_pS', 'kl_delta', 'epsilon', 'eta', 'lambda_max', 'allow_negative', 'pinsker_cap')
[debug] use_upper_for_lambda=True, pinsker_cap=0.1
[λ-update] EMA πθ(S)=0.1416 (upper=0.1542) → λ=4.147→4.147 | E[qλ(S)]=0.0026 | KL_EMA=17.8995
100%|███████████████████████████████████████| 7/7 [00:09<00:00,  1.36s/it, loss=20.5, πθ(S)=0.147, λ=4.15]
======= Epoch 1 =======
  0%|                                                                               | 0/7 [00:00<?, ?it/s][HIGH] πθ(S)=0.1599 [95% normal 0.1309,0.1889 | Wilson↑ 0.1720] | E[qλ(S)]=0.0026 | ε=0.0500 | KL=29.44 | λ=4.147
[debug] adjust_lambda signature: ('lambda_val', 'current_pS', 'kl_delta', 'epsilon', 'eta', 'lambda_max', 'allow_negative', 'pinsker_cap')
[debug] use_upper_for_lambda=True, pinsker_cap=0.1
[λ-update] EMA πθ(S)=0.1426 (upper=0.1541) → λ=4.147→4.147 | E[qλ(S)]=0.0026 | KL_EMA=18.6099
 14%|█████▌                                 | 1/7 [00:01<00:07,  1.25s/it, loss=29.4, πθ(S)=0.160, λ=4.15][HIGH] πθ(S)=0.1182 [95% normal 0.0859,0.1505 | Wilson↑ 0.1284] | E[qλ(S)]=0.0026 | ε=0.0500 | KL=13.21 | λ=4.147
[debug] adjust_lambda signature: ('lambda_val', 'current_pS', 'kl_delta', 'epsilon', 'eta', 'lambda_max', 'allow_negative', 'pinsker_cap')
[debug] use_upper_for_lambda=True, pinsker_cap=0.1
[λ-update] EMA πθ(S)=0.1411 (upper=0.1520) → λ=4.147→4.147 | E[qλ(S)]=0.0026 | KL_EMA=18.0836
 29%|███████████▏                           | 2/7 [00:02<00:06,  1.31s/it, loss=13.2, πθ(S)=0.118, λ=4.15][HIGH] πθ(S)=0.1607 [95% normal 0.1184,0.2031 | Wilson↑ 0.1718] | E[qλ(S)]=0.0026 | ε=0.0500 | KL=8.425 | λ=4.147
[debug] adjust_lambda signature: ('lambda_val', 'current_pS', 'kl_delta', 'epsilon', 'eta', 'lambda_max', 'allow_negative', 'pinsker_cap')
[debug] use_upper_for_lambda=True, pinsker_cap=0.1
[λ-update] EMA πθ(S)=0.1418 (upper=0.1524) → λ=4.147→4.147 | E[qλ(S)]=0.0026 | KL_EMA=17.5526
 43%|████████████████▋                      | 3/7 [00:03<00:05,  1.28s/it, loss=8.44, πθ(S)=0.161, λ=4.15][HIGH] πθ(S)=0.1251 [95% normal 0.0987,0.1514 | Wilson↑ 0.1345] | E[qλ(S)]=0.0026 | ε=0.0500 | KL=21.22 | λ=4.147
[debug] adjust_lambda signature: ('lambda_val', 'current_pS', 'kl_delta', 'epsilon', 'eta', 'lambda_max', 'allow_negative', 'pinsker_cap')
[debug] use_upper_for_lambda=True, pinsker_cap=0.1
[λ-update] EMA πθ(S)=0.1409 (upper=0.1508) → λ=4.147→4.147 | E[qλ(S)]=0.0026 | KL_EMA=17.9097
 57%|██████████████████████▎                | 4/7 [00:05<00:03,  1.29s/it, loss=21.2, πθ(S)=0.125, λ=4.15][HIGH] πθ(S)=0.1026 [95% normal 0.0756,0.1296 | Wilson↑ 0.1109] | E[qλ(S)]=0.0026 | ε=0.0500 | KL=18.18 | λ=4.147
[debug] adjust_lambda signature: ('lambda_val', 'current_pS', 'kl_delta', 'epsilon', 'eta', 'lambda_max', 'allow_negative', 'pinsker_cap')
[debug] use_upper_for_lambda=True, pinsker_cap=0.1
[λ-update] EMA πθ(S)=0.1392 (upper=0.1485) → λ=4.147→4.147 | E[qλ(S)]=0.0026 | KL_EMA=17.8784
 71%|███████████████████████████▊           | 5/7 [00:07<00:03,  1.58s/it, loss=18.2, πθ(S)=0.103, λ=4.15][HIGH] πθ(S)=0.1592 [95% normal 0.1267,0.1917 | Wilson↑ 0.1686] | E[qλ(S)]=0.0026 | ε=0.0500 | KL=22.7 | λ=4.147
[debug] adjust_lambda signature: ('lambda_val', 'current_pS', 'kl_delta', 'epsilon', 'eta', 'lambda_max', 'allow_negative', 'pinsker_cap')
[debug] use_upper_for_lambda=True, pinsker_cap=0.1
[λ-update] EMA πθ(S)=0.1399 (upper=0.1489) → λ=4.147→4.147 | E[qλ(S)]=0.0026 | KL_EMA=18.0620
 86%|█████████████████████████████████▍     | 6/7 [00:08<00:01,  1.51s/it, loss=22.7, πθ(S)=0.159, λ=4.15][HIGH] πθ(S)=0.1447 [95% normal 0.1045,0.1849 | Wilson↑ 0.1536] | E[qλ(S)]=0.0026 | ε=0.0500 | KL=19.61 | λ=4.147
[debug] adjust_lambda signature: ('lambda_val', 'current_pS', 'kl_delta', 'epsilon', 'eta', 'lambda_max', 'allow_negative', 'pinsker_cap')
[debug] use_upper_for_lambda=True, pinsker_cap=0.1
[λ-update] EMA πθ(S)=0.1400 (upper=0.1488) → λ=4.147→4.147 | E[qλ(S)]=0.0026 | KL_EMA=17.9883
100%|███████████████████████████████████████| 7/7 [00:09<00:00,  1.40s/it, loss=19.6, πθ(S)=0.145, λ=4.15]
======= Epoch 2 =======
  0%|                                                                               | 0/7 [00:00<?, ?it/s][HIGH] πθ(S)=0.1582 [95% normal 0.1294,0.1870 | Wilson↑ 0.1670] | E[qλ(S)]=0.0026 | ε=0.0500 | KL=28.51 | λ=4.147
[debug] adjust_lambda signature: ('lambda_val', 'current_pS', 'kl_delta', 'epsilon', 'eta', 'lambda_max', 'allow_negative', 'pinsker_cap')
[debug] use_upper_for_lambda=True, pinsker_cap=0.1
[λ-update] EMA πθ(S)=0.1405 (upper=0.1489) → λ=4.147→4.147 | E[qλ(S)]=0.0026 | KL_EMA=18.3684
 14%|█████▌                                 | 1/7 [00:01<00:07,  1.24s/it, loss=28.5, πθ(S)=0.158, λ=4.15][HIGH] πθ(S)=0.1167 [95% normal 0.0845,0.1488 | Wilson↑ 0.1242] | E[qλ(S)]=0.0026 | ε=0.0500 | KL=12.86 | λ=4.147
[debug] adjust_lambda signature: ('lambda_val', 'current_pS', 'kl_delta', 'epsilon', 'eta', 'lambda_max', 'allow_negative', 'pinsker_cap')
[debug] use_upper_for_lambda=True, pinsker_cap=0.1
[λ-update] EMA πθ(S)=0.1397 (upper=0.1479) → λ=4.147→4.147 | E[qλ(S)]=0.0026 | KL_EMA=17.7261
 29%|███████████▏                           | 2/7 [00:02<00:06,  1.30s/it, loss=12.9, πθ(S)=0.117, λ=4.15][HIGH] πθ(S)=0.1595 [95% normal 0.1173,0.2017 | Wilson↑ 0.1679] | E[qλ(S)]=0.0026 | ε=0.0500 | KL=8.206 | λ=4.147
[debug] adjust_lambda signature: ('lambda_val', 'current_pS', 'kl_delta', 'epsilon', 'eta', 'lambda_max', 'allow_negative', 'pinsker_cap')
[debug] use_upper_for_lambda=True, pinsker_cap=0.1
[λ-update] EMA πθ(S)=0.1402 (upper=0.1482) → λ=4.147→4.147 | E[qλ(S)]=0.0026 | KL_EMA=17.1981
 43%|████████████████▋                      | 3/7 [00:03<00:05,  1.28s/it, loss=8.22, πθ(S)=0.159, λ=4.15][HIGH] πθ(S)=0.1242 [95% normal 0.0980,0.1505 | Wilson↑ 0.1315] | E[qλ(S)]=0.0026 | ε=0.0500 | KL=20.72 | λ=4.147
[debug] adjust_lambda signature: ('lambda_val', 'current_pS', 'kl_delta', 'epsilon', 'eta', 'lambda_max', 'allow_negative', 'pinsker_cap')
[debug] use_upper_for_lambda=True, pinsker_cap=0.1
[λ-update] EMA πθ(S)=0.1397 (upper=0.1474) → λ=4.147→4.147 | E[qλ(S)]=0.0026 | KL_EMA=17.5597
 57%|██████████████████████▎                | 4/7 [00:05<00:03,  1.28s/it, loss=20.7, πθ(S)=0.124, λ=4.15][HIGH] πθ(S)=0.1018 [95% normal 0.0749,0.1287 | Wilson↑ 0.1084] | E[qλ(S)]=0.0026 | ε=0.0500 | KL=17.76 | λ=4.147
[debug] adjust_lambda signature: ('lambda_val', 'current_pS', 'kl_delta', 'epsilon', 'eta', 'lambda_max', 'allow_negative', 'pinsker_cap')
[debug] use_upper_for_lambda=True, pinsker_cap=0.1
[λ-update] EMA πθ(S)=0.1387 (upper=0.1461) → λ=4.147→4.147 | E[qλ(S)]=0.0026 | KL_EMA=17.5713
 71%|███████████████████████████▊           | 5/7 [00:06<00:02,  1.30s/it, loss=17.8, πθ(S)=0.102, λ=4.15][HIGH] πθ(S)=0.1581 [95% normal 0.1257,0.1905 | Wilson↑ 0.1657] | E[qλ(S)]=0.0026 | ε=0.0500 | KL=22.33 | λ=4.147
[debug] adjust_lambda signature: ('lambda_val', 'current_pS', 'kl_delta', 'epsilon', 'eta', 'lambda_max', 'allow_negative', 'pinsker_cap')
[debug] use_upper_for_lambda=True, pinsker_cap=0.1
[λ-update] EMA πθ(S)=0.1392 (upper=0.1464) → λ=4.147→4.147 | E[qλ(S)]=0.0026 | KL_EMA=17.8012
 86%|█████████████████████████████████▍     | 6/7 [00:07<00:01,  1.32s/it, loss=22.3, πθ(S)=0.158, λ=4.15][HIGH] πθ(S)=0.1438 [95% normal 0.1037,0.1839 | Wilson↑ 0.1510] | E[qλ(S)]=0.0026 | ε=0.0500 | KL=19.26 | λ=4.147
[debug] adjust_lambda signature: ('lambda_val', 'current_pS', 'kl_delta', 'epsilon', 'eta', 'lambda_max', 'allow_negative', 'pinsker_cap')
[debug] use_upper_for_lambda=True, pinsker_cap=0.1
[λ-update] EMA πθ(S)=0.1386 (upper=0.1457) → λ=4.147→4.147 | E[qλ(S)]=0.0026 | KL_EMA=17.7431
100%|███████████████████████████████████████| 7/7 [00:09<00:00,  1.29s/it, loss=19.3, πθ(S)=0.144, λ=4.15]
=== ETU Suppression Report ===
  - Perplexity on retain: 5.15
=== Results ===
  - π_base(S): 0.1422
  - π_θ(S): 0.1371
  - Suppression ratio: 0.96 (updated/base)
  - Target ε: 0.0500
  - Target achieved: ✗
  - 95% upper π_base(S): 0.1548
  - 95% upper π_θ(S): 0.1496
  - Target achieved (95% upper): ✗
Saved suppression report to models/zephyr-7b-beta_etu_epsilon-0.05_lambda-4.1470_2025-09-02-17-03-52/suppression_report.json
Merging LoRA weights into base model...
Saved V_S to models/zephyr-7b-beta_etu_epsilon-0.05_lambda-4.1470_2025-09-02-17-03-52/V_S.ids.json
Saved ETU model to models/zephyr-7b-beta_etu_epsilon-0.05_lambda-4.1470_2025-09-02-17-03-52
Saved args to models/zephyr-7b-beta_etu_epsilon-0.05_lambda-4.1470_2025-09-02-17-03-52/args.json
Saved metrics to models/zephyr-7b-beta_etu_epsilon-0.05_lambda-4.1470_2025-09-02-17-03-52/metrics.json
✅ ETU 실행 완료!
(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ 
