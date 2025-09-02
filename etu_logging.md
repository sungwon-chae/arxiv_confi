(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ python3 run_etu_h200.py   --forget_corpora "./datasets/bio-forget/data"   --retain_corpora "./datasets/bio-retain/bio-retain-corpus"   --batch_size 8   --max_num_batches 50   --num_epochs 3   --layer_id 7   --epsilon 0.05   --lambda_max 30.0   --lambda_update_freq 1   --lambda_eta 0.75   --use_pmi_vs   --pmi_min_count 3   --pmi_top_k 256   --pmi_smoothing 1.0   --retain_weight 0.25   --wilson_max_n 10000   --pinsker_cap 0.10   --use_upper_for_lambda   --verbose
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
🔧 사용자 지정 배치 크기 사용: 8 (heuristic=55)
🎯 단일 GPU 모드: GPU 0
🔧 H200 최적화 설정 적용:
   - strategy: single
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
Loading checkpoint shards: 100%|███████████████████████████████████████████| 8/8 [00:00<00:00, 371.44it/s]
🔧 Frozen 모델을 GPU에 로드
📊 데이터 로딩 중...
🔍 Forget 데이터셋: ['./datasets/bio-forget/data']
🔍 Retain 데이터셋: ['./datasets/bio-retain/bio-retain-corpus']
🔧 Layer 설정: layer_id=7, layer_ids=7
Processing corpus spec: './datasets/bio-forget/data'
Loading local dataset folder: ./datasets/bio-forget/data
Loading from actual path: ./datasets/bio-forget/data
Loaded 56 items from local dataset folder
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
/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/torch/backends/__init__.py:46: UserWarning: Please use the new API settings to control TF32 behavior, such as torch.backends.cudnn.conv.fp32_precision = 'tf32' or torch.backends.cuda.matmul.fp32_precision = 'ieee'. Old settings, e.g, torch.backends.cuda.matmul.allow_tf32 = True, torch.backends.cudnn.allow_tf32 = True, allowTF32CuDNN() and allowTF32CuBLAS() will be deprecated after Pytorch 2.9. Please see https://pytorch.org/docs/main/notes/cuda.html#tensorfloat-32-tf32-on-ampere-and-later-devices (Triggered internally at /pytorch/aten/src/ATen/Context.cpp:80.)
  self.setter(val)
Applying LoRA for efficient parameter updates...
Applying LoRA to layers: [7]
trainable params: 13,631,488 || all params: 7,255,363,584 || trainable%: 0.1879
Building forbidden token set V_S...
[PMI] counting capped at 500 batches per split
[PMI] split 0: used 7 batches (cap=500)
[PMI] split 0: used 500 batches (cap=500)
[V_S] token filter kept 192/216 (88.9%) after _filter_vs_tokens
V_S (PMI-refined) size: 192 tokens
Top PMI tokens preview: ['in', 'er', '▁a', 'en', 'at', '▁the', 'al', 'ed', 'ing', '▁in']
V_S size: 192 tokens (0.6% of vocab)
Estimating base probability mass p_S over V_S...
Estimated p_S (π_base over V_S): 0.1325
[info] |V_S|/V = 0.6%, π_base(S)=0.1325, ε=0.0500
V_S preview: ['in', 'er', '▁a', 'en', 'at', '▁the', 'al', 'ed', 'ing', '▁in']
Initial λ: 1.0651 → expected qλ(S)≈0.0500
======= Epoch 0 =======
  0%|                                                                               | 0/7 [00:00<?, ?it/s][HIGH] πθ(S)=0.1652 [95% normal 0.1359,0.1946 | Wilson↑ 0.1967] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=0.04128 | λ=1.065
[λ-update] EMA πθ(S)=0.1483 (controller=0.1785) → λ=1.065→1.815 | E[qλ(S)]=0.0243 | KL_EMA=1.0540
 14%|█████▎                               | 1/7 [00:01<00:08,  1.37s/it, loss=0.0413, πθ(S)=0.165, λ=1.82][HIGH] πθ(S)=0.1035 [95% normal 0.0697,0.1372 | Wilson↑ 0.1247] | E[qλ(S)]=0.0243 | ε=0.0500 | KL=0.1021 | λ=1.815
[λ-update] EMA πθ(S)=0.1328 (controller=0.1562) → λ=1.815→2.565 | E[qλ(S)]=0.0116 | KL_EMA=3.1324
 29%|██████████▊                           | 2/7 [00:02<00:06,  1.39s/it, loss=0.102, πθ(S)=0.103, λ=2.57][HIGH] πθ(S)=0.1499 [95% normal 0.1112,0.1885 | Wilson↑ 0.1707] | E[qλ(S)]=0.0116 | ε=0.0500 | KL=0.1414 | λ=2.565
[λ-update] EMA πθ(S)=0.1354 (controller=0.1554) → λ=2.565→3.315 | E[qλ(S)]=0.0055 | KL_EMA=6.0529
 43%|████████████████▎                     | 3/7 [00:04<00:05,  1.36s/it, loss=0.141, πθ(S)=0.150, λ=3.32][HIGH] πθ(S)=0.1065 [95% normal 0.0801,0.1329 | Wilson↑ 0.1217] | E[qλ(S)]=0.0055 | ε=0.0500 | KL=0.2006 | λ=3.315
[λ-update] EMA πθ(S)=0.1306 (controller=0.1470) → λ=3.315→3.315 | E[qλ(S)]=0.0055 | KL_EMA=9.2954
 57%|█████████████████████▋                | 4/7 [00:05<00:04,  1.37s/it, loss=0.201, πθ(S)=0.106, λ=3.32][HIGH] πθ(S)=0.1322 [95% normal 0.1006,0.1638 | Wilson↑ 0.1469] | E[qλ(S)]=0.0055 | ε=0.0500 | KL=0.2426 | λ=3.315
[λ-update] EMA πθ(S)=0.1307 (controller=0.1453) → λ=3.315→3.315 | E[qλ(S)]=0.0055 | KL_EMA=10.7567
 71%|███████████████████████████▏          | 5/7 [00:06<00:02,  1.36s/it, loss=0.251, πθ(S)=0.132, λ=3.32][HIGH] πθ(S)=0.1190 [95% normal 0.0920,0.1461 | Wilson↑ 0.1316] | E[qλ(S)]=0.0055 | ε=0.0500 | KL=0.2728 | λ=3.315
[λ-update] EMA πθ(S)=0.1296 (controller=0.1427) → λ=3.315→3.315 | E[qλ(S)]=0.0055 | KL_EMA=11.4158
 86%|█████████████████████████████████▍     | 6/7 [00:08<00:01,  1.40s/it, loss=0.28, πθ(S)=0.119, λ=3.32][HIGH] πθ(S)=0.1511 [95% normal 0.1158,0.1864 | Wilson↑ 0.1640] | E[qλ(S)]=0.0055 | ε=0.0500 | KL=0.3117 | λ=3.315
[λ-update] EMA πθ(S)=0.1310 (controller=0.1432) → λ=3.315→3.315 | E[qλ(S)]=0.0055 | KL_EMA=11.6594
100%|██████████████████████████████████████| 7/7 [00:09<00:00,  1.37s/it, loss=0.317, πθ(S)=0.151, λ=3.32]
======= Epoch 1 =======
  0%|                                                                               | 0/7 [00:00<?, ?it/s][HIGH] πθ(S)=0.1645 [95% normal 0.1352,0.1938 | Wilson↑ 0.1767] | E[qλ(S)]=0.0055 | ε=0.0500 | KL=0.2982 | λ=3.315
[λ-update] EMA πθ(S)=0.1330 (controller=0.1442) → λ=3.315→3.315 | E[qλ(S)]=0.0055 | KL_EMA=11.7684
 14%|█████▍                                | 1/7 [00:01<00:07,  1.27s/it, loss=0.318, πθ(S)=0.165, λ=3.32][HIGH] πθ(S)=0.1022 [95% normal 0.0686,0.1357 | Wilson↑ 0.1118] | E[qλ(S)]=0.0055 | ε=0.0500 | KL=0.2292 | λ=3.315
[λ-update] EMA πθ(S)=0.1311 (controller=0.1417) → λ=3.315→3.315 | E[qλ(S)]=0.0055 | KL_EMA=11.8140
 29%|██████████▊                           | 2/7 [00:02<00:06,  1.33s/it, loss=0.238, πθ(S)=0.102, λ=3.32][HIGH] πθ(S)=0.1471 [95% normal 0.1087,0.1855 | Wilson↑ 0.1579] | E[qλ(S)]=0.0055 | ε=0.0500 | KL=0.188 | λ=3.315
[λ-update] EMA πθ(S)=0.1318 (controller=0.1421) → λ=3.315→3.315 | E[qλ(S)]=0.0055 | KL_EMA=11.8324
 43%|████████████████▎                     | 3/7 [00:03<00:05,  1.31s/it, loss=0.196, πθ(S)=0.147, λ=3.32][HIGH] πθ(S)=0.1044 [95% normal 0.0782,0.1306 | Wilson↑ 0.1132] | E[qλ(S)]=0.0055 | ε=0.0500 | KL=0.1886 | λ=3.315
[λ-update] EMA πθ(S)=0.1303 (controller=0.1400) → λ=3.315→3.315 | E[qλ(S)]=0.0055 | KL_EMA=11.8166
 57%|█████████████████████▋                | 4/7 [00:06<00:04,  1.62s/it, loss=0.196, πθ(S)=0.104, λ=3.32][HIGH] πθ(S)=0.1316 [95% normal 0.1000,0.1631 | Wilson↑ 0.1409] | E[qλ(S)]=0.0055 | ε=0.0500 | KL=0.2365 | λ=3.315
[λ-update] EMA πθ(S)=0.1303 (controller=0.1396) → λ=3.315→3.315 | E[qλ(S)]=0.0055 | KL_EMA=11.8119
 71%|███████████████████████████▏          | 5/7 [00:07<00:03,  1.50s/it, loss=0.255, πθ(S)=0.132, λ=3.32][HIGH] πθ(S)=0.1187 [95% normal 0.0917,0.1457 | Wilson↑ 0.1272] | E[qλ(S)]=0.0055 | ε=0.0500 | KL=0.2704 | λ=3.315
[λ-update] EMA πθ(S)=0.1299 (controller=0.1386) → λ=3.315→3.315 | E[qλ(S)]=0.0055 | KL_EMA=11.8115
 86%|████████████████████████████████▌     | 6/7 [00:08<00:01,  1.48s/it, loss=0.287, πθ(S)=0.119, λ=3.32][HIGH] πθ(S)=0.1503 [95% normal 0.1151,0.1855 | Wilson↑ 0.1593] | E[qλ(S)]=0.0055 | ε=0.0500 | KL=0.3059 | λ=3.315
[λ-update] EMA πθ(S)=0.1305 (controller=0.1390) → λ=3.315→3.315 | E[qλ(S)]=0.0055 | KL_EMA=11.7867
100%|███████████████████████████████████████| 7/7 [00:10<00:00,  1.43s/it, loss=0.32, πθ(S)=0.150, λ=3.32]
======= Epoch 2 =======
  0%|                                                                               | 0/7 [00:00<?, ?it/s][HIGH] πθ(S)=0.1643 [95% normal 0.1350,0.1936 | Wilson↑ 0.1732] | E[qλ(S)]=0.0055 | ε=0.0500 | KL=0.2964 | λ=3.315
[λ-update] EMA πθ(S)=0.1315 (controller=0.1397) → λ=3.315→3.315 | E[qλ(S)]=0.0055 | KL_EMA=11.7750
 14%|█████▍                                | 1/7 [00:01<00:07,  1.27s/it, loss=0.305, πθ(S)=0.164, λ=3.32][HIGH] πθ(S)=0.1018 [95% normal 0.0683,0.1353 | Wilson↑ 0.1089] | E[qλ(S)]=0.0055 | ε=0.0500 | KL=0.2269 | λ=3.315
[λ-update] EMA πθ(S)=0.1305 (controller=0.1385) → λ=3.315→3.315 | E[qλ(S)]=0.0055 | KL_EMA=11.7663
 29%|██████████▊                           | 2/7 [00:02<00:06,  1.32s/it, loss=0.232, πθ(S)=0.102, λ=3.32][HIGH] πθ(S)=0.1465 [95% normal 0.1082,0.1848 | Wilson↑ 0.1546] | E[qλ(S)]=0.0055 | ε=0.0500 | KL=0.186 | λ=3.315
[λ-update] EMA πθ(S)=0.1310 (controller=0.1387) → λ=3.315→3.315 | E[qλ(S)]=0.0055 | KL_EMA=11.7603
 43%|████████████████▎                     | 3/7 [00:03<00:05,  1.30s/it, loss=0.192, πθ(S)=0.147, λ=3.32][HIGH] πθ(S)=0.1038 [95% normal 0.0777,0.1299 | Wilson↑ 0.1107] | E[qλ(S)]=0.0055 | ε=0.0500 | KL=0.1869 | λ=3.315
[λ-update] EMA πθ(S)=0.1301 (controller=0.1376) → λ=3.315→3.315 | E[qλ(S)]=0.0055 | KL_EMA=11.7511
 57%|█████████████████████▋                | 4/7 [00:05<00:03,  1.30s/it, loss=0.191, πθ(S)=0.104, λ=3.32][HIGH] πθ(S)=0.1314 [95% normal 0.0999,0.1630 | Wilson↑ 0.1388] | E[qλ(S)]=0.0055 | ε=0.0500 | KL=0.2351 | λ=3.315
[λ-update] EMA πθ(S)=0.1301 (controller=0.1374) → λ=3.315→3.315 | E[qλ(S)]=0.0055 | KL_EMA=11.7494
 71%|███████████████████████████▏          | 5/7 [00:06<00:02,  1.30s/it, loss=0.244, πθ(S)=0.131, λ=3.32][HIGH] πθ(S)=0.1185 [95% normal 0.0915,0.1455 | Wilson↑ 0.1253] | E[qλ(S)]=0.0055 | ε=0.0500 | KL=0.269 | λ=3.315
[λ-update] EMA πθ(S)=0.1298 (controller=0.1369) → λ=3.315→3.315 | E[qλ(S)]=0.0055 | KL_EMA=11.7503
 86%|████████████████████████████████▌     | 6/7 [00:07<00:01,  1.35s/it, loss=0.275, πθ(S)=0.119, λ=3.32][HIGH] πθ(S)=0.1500 [95% normal 0.1148,0.1851 | Wilson↑ 0.1573] | E[qλ(S)]=0.0055 | ε=0.0500 | KL=0.3035 | λ=3.315
[λ-update] EMA πθ(S)=0.1294 (controller=0.1363) → λ=3.315→3.315 | E[qλ(S)]=0.0055 | KL_EMA=11.7440
100%|███████████████████████████████████████| 7/7 [00:09<00:00,  1.42s/it, loss=0.31, πθ(S)=0.150, λ=3.32]
=== ETU Suppression Report ===
  - Perplexity on retain: 5.15
=== Results ===
  - π_base(S): 0.1325
  - π_θ(S): 0.1308
  - Suppression ratio: 0.99 (updated/base)
  - Target ε: 0.0500
  - Target achieved: ✗
  - 95% upper π_base(S): 0.1447
  - 95% upper π_θ(S): 0.1430
  - Target achieved (95% upper): ✗
Saved suppression report to models/zephyr-7b-beta_etu_epsilon-0.05_lambda-3.3151_2025-09-02-18-09-49/suppression_report.json
Merging LoRA weights into base model...
Saved V_S to models/zephyr-7b-beta_etu_epsilon-0.05_lambda-3.3151_2025-09-02-18-09-49/V_S.ids.json
Saved ETU model to models/zephyr-7b-beta_etu_epsilon-0.05_lambda-3.3151_2025-09-02-18-09-49
Saved args to models/zephyr-7b-beta_etu_epsilon-0.05_lambda-3.3151_2025-09-02-18-09-49/args.json
Saved metrics to models/zephyr-7b-beta_etu_epsilon-0.05_lambda-3.3151_2025-09-02-18-09-49/metrics.json
✅ ETU 실행 완료!
(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ 
