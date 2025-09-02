(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ python3 run_etu_h200.py \
  --forget_corpora "./datasets/bio-forget" \
  --retain_corpora "./datasets/bio-retain" \
  --batch_size 8 \
  --max_num_batches 50 \
  --num_epochs 3 \
  --layer_id 7 \
  --epsilon 0.05 \
  --lambda_max 30.0 \
  --lambda_update_freq 1 \
  --lambda_eta 0.5 \
  --use_pmi_vs \
  --pmi_top_k 256 \
  --pmi_min_count 3 \
  --pmi_smoothing 1.0 \
  --retain_weight 0.25 \
  --wilson_max_n 10000 \
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
Loading checkpoint shards: 100%|███████████████████████████████████████████| 8/8 [00:00<00:00, 380.00it/s]
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
pmi_top_k=256
pmi_min_count=3
pmi_smoothing=1.0
pmi_max_batches=500
vs_preview_k=10
span_masking=False
span_ngram_max=3
allow_negative_lambda=False
lambda_eta=0.5
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
[λ-update] EMA πθ(S)=0.1550 (upper=0.1857) → λ=1.147→1.147 | E[qλ(S)]=0.0500 | KL_EMA=2.9773
 14%|█████▋                                  | 1/7 [00:01<00:08,  1.45s/it, loss=3.5, πθ(S)=0.165, λ=1.15][HIGH] πθ(S)=0.1233 [95% normal 0.0904,0.1563 | Wilson↑ 0.1452] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=2.16 | λ=1.147
[λ-update] EMA πθ(S)=0.1441 (upper=0.1673) → λ=1.147→1.147 | E[qλ(S)]=0.0500 | KL_EMA=2.6434
 29%|███████████▏                           | 2/7 [00:02<00:07,  1.41s/it, loss=2.16, πθ(S)=0.123, λ=1.15][HIGH] πθ(S)=0.1643 [95% normal 0.1216,0.2070 | Wilson↑ 0.1855] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=1.362 | λ=1.147
[λ-update] EMA πθ(S)=0.1471 (upper=0.1675) → λ=1.147→1.147 | E[qλ(S)]=0.0500 | KL_EMA=2.4414
 43%|████████████████▋                      | 3/7 [00:04<00:05,  1.36s/it, loss=1.37, πθ(S)=0.164, λ=1.15][HIGH] πθ(S)=0.1280 [95% normal 0.1014,0.1546 | Wilson↑ 0.1438] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=2.708 | λ=1.147
[λ-update] EMA πθ(S)=0.1438 (upper=0.1604) → λ=1.147→1.147 | E[qλ(S)]=0.0500 | KL_EMA=2.4050
 57%|██████████████████████▎                | 4/7 [00:05<00:04,  1.34s/it, loss=2.71, πθ(S)=0.128, λ=1.15][HIGH] πθ(S)=0.1040 [95% normal 0.0769,0.1312 | Wilson↑ 0.1170] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=2.462 | λ=1.147
[λ-update] EMA πθ(S)=0.1395 (upper=0.1540) → λ=1.147→1.147 | E[qλ(S)]=0.0500 | KL_EMA=2.3737
 71%|███████████████████████████▊           | 5/7 [00:06<00:02,  1.35s/it, loss=2.48, πθ(S)=0.104, λ=1.15][HIGH] πθ(S)=0.1622 [95% normal 0.1294,0.1949 | Wilson↑ 0.1761] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=2.827 | λ=1.147
[λ-update] EMA πθ(S)=0.1414 (upper=0.1547) → λ=1.147→1.147 | E[qλ(S)]=0.0500 | KL_EMA=2.3831
 86%|█████████████████████████████████▍     | 6/7 [00:08<00:01,  1.37s/it, loss=2.84, πθ(S)=0.162, λ=1.15][HIGH] πθ(S)=0.1470 [95% normal 0.1065,0.1875 | Wilson↑ 0.1598] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=2.531 | λ=1.147
[λ-update] EMA πθ(S)=0.1417 (upper=0.1543) → λ=1.147→1.147 | E[qλ(S)]=0.0500 | KL_EMA=2.3716
100%|███████████████████████████████████████| 7/7 [00:09<00:00,  1.36s/it, loss=2.54, πθ(S)=0.147, λ=1.15]
======= Epoch 1 =======
  0%|                                                                               | 0/7 [00:00<?, ?it/s][HIGH] πθ(S)=0.1602 [95% normal 0.1312,0.1892 | Wilson↑ 0.1723] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=3.207 | λ=1.147
[λ-update] EMA πθ(S)=0.1428 (upper=0.1544) → λ=1.147→1.147 | E[qλ(S)]=0.0500 | KL_EMA=2.4002
 14%|█████▌                                 | 1/7 [00:01<00:07,  1.25s/it, loss=3.21, πθ(S)=0.160, λ=1.15][HIGH] πθ(S)=0.1187 [95% normal 0.0863,0.1511 | Wilson↑ 0.1289] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=1.93 | λ=1.147
[λ-update] EMA πθ(S)=0.1413 (upper=0.1522) → λ=1.147→1.147 | E[qλ(S)]=0.0500 | KL_EMA=2.3424
 29%|███████████▏                           | 2/7 [00:02<00:06,  1.31s/it, loss=1.93, πθ(S)=0.119, λ=1.15][HIGH] πθ(S)=0.1608 [95% normal 0.1184,0.2031 | Wilson↑ 0.1719] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=1.445 | λ=1.147
[λ-update] EMA πθ(S)=0.1422 (upper=0.1528) → λ=1.147→1.147 | E[qλ(S)]=0.0500 | KL_EMA=2.2838
 43%|████████████████▋                      | 3/7 [00:03<00:05,  1.28s/it, loss=1.45, πθ(S)=0.161, λ=1.15][HIGH] πθ(S)=0.1251 [95% normal 0.0987,0.1514 | Wilson↑ 0.1345] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=2.639 | λ=1.147
[λ-update] EMA πθ(S)=0.1413 (upper=0.1512) → λ=1.147→1.147 | E[qλ(S)]=0.0500 | KL_EMA=2.2967
 57%|██████████████████████▎                | 4/7 [00:05<00:03,  1.29s/it, loss=2.65, πθ(S)=0.125, λ=1.15][HIGH] πθ(S)=0.1026 [95% normal 0.0756,0.1296 | Wilson↑ 0.1109] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=2.284 | λ=1.147
[λ-update] EMA πθ(S)=0.1397 (upper=0.1491) → λ=1.147→1.147 | E[qλ(S)]=0.0500 | KL_EMA=2.2750
 71%|████████████████████████████▌           | 5/7 [00:07<00:03,  1.59s/it, loss=2.3, πθ(S)=0.103, λ=1.15][HIGH] πθ(S)=0.1604 [95% normal 0.1278,0.1930 | Wilson↑ 0.1699] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=2.683 | λ=1.147
[λ-update] EMA πθ(S)=0.1405 (upper=0.1496) → λ=1.147→1.147 | E[qλ(S)]=0.0500 | KL_EMA=2.2767
 86%|█████████████████████████████████▍     | 6/7 [00:08<00:01,  1.51s/it, loss=2.69, πθ(S)=0.160, λ=1.15][HIGH] πθ(S)=0.1451 [95% normal 0.1048,0.1853 | Wilson↑ 0.1540] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=2.31 | λ=1.147
[λ-update] EMA πθ(S)=0.1407 (upper=0.1495) → λ=1.147→1.147 | E[qλ(S)]=0.0500 | KL_EMA=2.2545
100%|███████████████████████████████████████| 7/7 [00:09<00:00,  1.41s/it, loss=2.32, πθ(S)=0.145, λ=1.15]
======= Epoch 2 =======
  0%|                                                                               | 0/7 [00:00<?, ?it/s][HIGH] πθ(S)=0.1599 [95% normal 0.1310,0.1889 | Wilson↑ 0.1687] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=2.987 | λ=1.147
[λ-update] EMA πθ(S)=0.1413 (upper=0.1497) → λ=1.147→1.147 | E[qλ(S)]=0.0500 | KL_EMA=2.2682
 14%|█████▌                                 | 1/7 [00:01<00:07,  1.25s/it, loss=2.99, πθ(S)=0.160, λ=1.15][HIGH] πθ(S)=0.1179 [95% normal 0.0856,0.1502 | Wilson↑ 0.1255] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=1.82 | λ=1.147
[λ-update] EMA πθ(S)=0.1406 (upper=0.1487) → λ=1.147→1.147 | E[qλ(S)]=0.0500 | KL_EMA=2.2149
 29%|███████████▏                           | 2/7 [00:02<00:06,  1.30s/it, loss=1.82, πθ(S)=0.118, λ=1.15][HIGH] πθ(S)=0.1601 [95% normal 0.1179,0.2024 | Wilson↑ 0.1686] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=1.347 | λ=1.147
[λ-update] EMA πθ(S)=0.1411 (upper=0.1491) → λ=1.147→1.147 | E[qλ(S)]=0.0500 | KL_EMA=2.1609
 43%|████████████████▋                      | 3/7 [00:03<00:05,  1.28s/it, loss=1.35, πθ(S)=0.160, λ=1.15][HIGH] πθ(S)=0.1249 [95% normal 0.0986,0.1513 | Wilson↑ 0.1323] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=2.42 | λ=1.147
[λ-update] EMA πθ(S)=0.1406 (upper=0.1483) → λ=1.147→1.147 | E[qλ(S)]=0.0500 | KL_EMA=2.1835
 57%|██████████████████████▎                | 4/7 [00:05<00:03,  1.28s/it, loss=2.43, πθ(S)=0.125, λ=1.15][HIGH] πθ(S)=0.1022 [95% normal 0.0752,0.1291 | Wilson↑ 0.1087] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=2.218 | λ=1.147
[λ-update] EMA πθ(S)=0.1396 (upper=0.1470) → λ=1.147→1.147 | E[qλ(S)]=0.0500 | KL_EMA=2.1797
 71%|███████████████████████████▊           | 5/7 [00:06<00:02,  1.30s/it, loss=2.23, πθ(S)=0.102, λ=1.15][HIGH] πθ(S)=0.1595 [95% normal 0.1270,0.1920 | Wilson↑ 0.1672] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=2.584 | λ=1.147
[λ-update] EMA πθ(S)=0.1401 (upper=0.1474) → λ=1.147→1.147 | E[qλ(S)]=0.0500 | KL_EMA=2.1946
 86%|█████████████████████████████████▍     | 6/7 [00:07<00:01,  1.33s/it, loss=2.59, πθ(S)=0.160, λ=1.15][HIGH] πθ(S)=0.1444 [95% normal 0.1042,0.1846 | Wilson↑ 0.1517] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=2.252 | λ=1.147
[λ-update] EMA πθ(S)=0.1396 (upper=0.1467) → λ=1.147→1.147 | E[qλ(S)]=0.0500 | KL_EMA=2.1850
100%|███████████████████████████████████████| 7/7 [00:09<00:00,  1.30s/it, loss=2.26, πθ(S)=0.144, λ=1.15]
=== ETU Suppression Report ===
  - Perplexity on retain: 5.14
=== Results ===
  - π_base(S): 0.1422
  - π_θ(S): 0.1385
  - Suppression ratio: 0.97 (updated/base)
  - Target ε: 0.0500
  - Target achieved: ✗
  - 95% upper π_base(S): 0.1548
  - 95% upper π_θ(S): 0.1510
  - Target achieved (95% upper): ✗
Saved suppression report to models/zephyr-7b-beta_etu_epsilon-0.05_lambda-1.1470_2025-09-02-16-24-22/suppression_report.json
Merging LoRA weights into base model...
Saved V_S to models/zephyr-7b-beta_etu_epsilon-0.05_lambda-1.1470_2025-09-02-16-24-22/V_S.ids.json
Saved ETU model to models/zephyr-7b-beta_etu_epsilon-0.05_lambda-1.1470_2025-09-02-16-24-22
Saved args to models/zephyr-7b-beta_etu_epsilon-0.05_lambda-1.1470_2025-09-02-16-24-22/args.json
Saved metrics to models/zephyr-7b-beta_etu_epsilon-0.05_lambda-1.1470_2025-09-02-16-24-22/metrics.json
✅ ETU 실행 완료!
(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ 
