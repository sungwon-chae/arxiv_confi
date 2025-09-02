(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ python3 run_etu_h200.py \
  --forget_corpora "./datasets/bio-forget/data" \
  --retain_corpora "./datasets/bio-retain/bio-retain-corpus" \
  --batch_size 8 \
  --max_num_batches 50 \
  --num_epochs 3 \
  --layer_id 7 \
  --epsilon 0.10 \
  --lambda_max 30.0 \
  --lambda_update_freq 1 \
  --lambda_eta 0.5 \
  --use_pmi_vs \
  --pmi_min_count 30 \
  --pmi_top_k 256 \
  --pmi_smoothing 1.0 \
  --vs_abs_cap 200 \
  --retain_weight 0.25 \
  --wilson_max_n 10000 \
  --pinsker_cap 0.10 \
  --use_upper_for_lambda \
  --mixed_precision bf16 \
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
Loading checkpoint shards: 100%|████████████████████████████████████████████| 8/8 [00:08<00:00,  1.11s/it]
Loading checkpoint shards: 100%|███████████████████████████████████████████| 8/8 [00:00<00:00, 379.73it/s]
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
epsilon=0.1
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
vs_abs_cap=200
pmi_top_k=256
pmi_min_count=30
pmi_smoothing=1.0
pmi_max_batches=500
vs_preview_k=10
span_masking=False
span_ngram_max=3
allow_negative_lambda=False
lambda_eta=0.5
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
[V_S] token filter kept 3/16 (18.8%) after _filter_vs_tokens
V_S (PMI-refined) size: 3 tokens
[warn] PMI V_S too small → fallback to freq-based augmentation
V_S after fallback: 928 tokens
V_S fallback preview: ['in', 'er', '▁a', 're', 'en', 'at', 'or', '▁the', 'es', 'an']
Top PMI tokens preview: ['in', 'er', '▁a', 're', 'en', 'at', 'or', '▁the', 'es', 'an']
V_S size: 928 tokens (2.9% of vocab)
Estimating base probability mass p_S over V_S...
Estimated p_S (π_base over V_S): 0.2140
[info] |V_S|/V = 2.9%, π_base(S)=0.2140, ε=0.1000
V_S preview: ['in', 'er', '▁a', 're', 'en', 'at', 'or', '▁the', 'es', 'an']
Initial λ: 0.8963 → expected qλ(S)≈0.1000
======= Epoch 0 =======
  0%|                                                                               | 0/7 [00:00<?, ?it/s][HIGH] πθ(S)=0.2375 [95% normal 0.2039,0.2711 | Wilson↑ 0.2727] | E[qλ(S)]=0.1000 | ε=0.1000 | KL=0.03382 | λ=0.896
[λ-update] EMA πθ(S)=0.2271 (controller=0.2618) → λ=0.896→1.396 | E[qλ(S)]=0.0631 | KL_EMA=0.9992
 14%|█████▎                               | 1/7 [00:01<00:08,  1.48s/it, loss=0.0338, πθ(S)=0.238, λ=1.40][HIGH] πθ(S)=0.1707 [95% normal 0.1290,0.2124 | Wilson↑ 0.1962] | E[qλ(S)]=0.0631 | ε=0.1000 | KL=0.08245 | λ=1.396
[λ-update] EMA πθ(S)=0.2104 (controller=0.2378) → λ=1.396→1.896 | E[qλ(S)]=0.0393 | KL_EMA=2.7294
 29%|██████████▌                          | 2/7 [00:02<00:07,  1.44s/it, loss=0.0824, πθ(S)=0.171, λ=1.90][HIGH] πθ(S)=0.2621 [95% normal 0.2145,0.3098 | Wilson↑ 0.2872] | E[qλ(S)]=0.0393 | ε=0.1000 | KL=0.1316 | λ=1.896
[λ-update] EMA πθ(S)=0.2201 (controller=0.2438) → λ=1.896→2.396 | E[qλ(S)]=0.0242 | KL_EMA=5.2191
 43%|████████████████▎                     | 3/7 [00:04<00:05,  1.38s/it, loss=0.132, πθ(S)=0.262, λ=2.40][HIGH] πθ(S)=0.1964 [95% normal 0.1624,0.2304 | Wilson↑ 0.2155] | E[qλ(S)]=0.0242 | ε=0.1000 | KL=0.1901 | λ=2.396
[λ-update] EMA πθ(S)=0.2160 (controller=0.2357) → λ=2.396→2.896 | E[qλ(S)]=0.0148 | KL_EMA=8.2099
 57%|██████████████████████▎                | 4/7 [00:05<00:04,  1.41s/it, loss=0.19, πθ(S)=0.196, λ=2.90][HIGH] πθ(S)=0.2111 [95% normal 0.1730,0.2492 | Wilson↑ 0.2286] | E[qλ(S)]=0.0148 | ε=0.1000 | KL=0.2747 | λ=2.896
[λ-update] EMA πθ(S)=0.2155 (controller=0.2330) → λ=2.896→3.396 | E[qλ(S)]=0.0090 | KL_EMA=11.7883
 71%|███████████████████████████▏          | 5/7 [00:06<00:02,  1.38s/it, loss=0.283, πθ(S)=0.211, λ=3.40][HIGH] πθ(S)=0.1854 [95% normal 0.1530,0.2179 | Wilson↑ 0.2003] | E[qλ(S)]=0.0090 | ε=0.1000 | KL=0.4087 | λ=3.396
[λ-update] EMA πθ(S)=0.2129 (controller=0.2286) → λ=3.396→3.896 | E[qλ(S)]=0.0055 | KL_EMA=15.8087
 86%|████████████████████████████████▌     | 6/7 [00:08<00:01,  1.41s/it, loss=0.415, πθ(S)=0.185, λ=3.90][HIGH] πθ(S)=0.2346 [95% normal 0.1928,0.2763 | Wilson↑ 0.2496] | E[qλ(S)]=0.0055 | ε=0.1000 | KL=0.5881 | λ=3.896
[λ-update] EMA πθ(S)=0.2144 (controller=0.2290) → λ=3.896→4.396 | E[qλ(S)]=0.0033 | KL_EMA=20.0769
100%|██████████████████████████████████████| 7/7 [00:09<00:00,  1.40s/it, loss=0.594, πθ(S)=0.235, λ=4.40]
======= Epoch 1 =======
  0%|                                                                               | 0/7 [00:00<?, ?it/s][HIGH] πθ(S)=0.2369 [95% normal 0.2033,0.2705 | Wilson↑ 0.2507] | E[qλ(S)]=0.0033 | ε=0.1000 | KL=0.6415 | λ=4.396
[λ-update] EMA πθ(S)=0.2158 (controller=0.2292) → λ=4.396→4.896 | E[qλ(S)]=0.0020 | KL_EMA=24.6025
 14%|█████▍                                | 1/7 [00:01<00:07,  1.26s/it, loss=0.659, πθ(S)=0.237, λ=4.90][HIGH] πθ(S)=0.1690 [95% normal 0.1275,0.2106 | Wilson↑ 0.1808] | E[qλ(S)]=0.0020 | ε=0.1000 | KL=0.629 | λ=4.896
[λ-update] EMA πθ(S)=0.2132 (controller=0.2260) → λ=4.896→5.396 | E[qλ(S)]=0.0012 | KL_EMA=29.2887
 29%|██████████▊                           | 2/7 [00:02<00:06,  1.32s/it, loss=0.637, πθ(S)=0.169, λ=5.40][HIGH] πθ(S)=0.2591 [95% normal 0.2116,0.3066 | Wilson↑ 0.2722] | E[qλ(S)]=0.0012 | ε=0.1000 | KL=0.645 | λ=5.396
[λ-update] EMA πθ(S)=0.2156 (controller=0.2279) → λ=5.396→5.896 | E[qλ(S)]=0.0007 | KL_EMA=34.0632
 43%|████████████████▎                     | 3/7 [00:03<00:05,  1.31s/it, loss=0.652, πθ(S)=0.259, λ=5.90][HIGH] πθ(S)=0.1945 [95% normal 0.1606,0.2283 | Wilson↑ 0.2057] | E[qλ(S)]=0.0007 | ε=0.1000 | KL=0.7799 | λ=5.896
[λ-update] EMA πθ(S)=0.2144 (controller=0.2260) → λ=5.896→6.396 | E[qλ(S)]=0.0005 | KL_EMA=38.7266
 57%|█████████████████████▋                | 4/7 [00:05<00:04,  1.61s/it, loss=0.787, πθ(S)=0.194, λ=6.40][HIGH] πθ(S)=0.2104 [95% normal 0.1724,0.2485 | Wilson↑ 0.2215] | E[qλ(S)]=0.0005 | ε=0.1000 | KL=0.9651 | λ=6.396
[λ-update] EMA πθ(S)=0.2142 (controller=0.2254) → λ=6.396→6.896 | E[qλ(S)]=0.0003 | KL_EMA=43.4361
 71%|███████████████████████████▏          | 5/7 [00:07<00:02,  1.49s/it, loss=0.985, πθ(S)=0.210, λ=6.90][HIGH] πθ(S)=0.1848 [95% normal 0.1524,0.2172 | Wilson↑ 0.1949] | E[qλ(S)]=0.0003 | ε=0.1000 | KL=0.9192 | λ=6.896
[λ-update] EMA πθ(S)=0.2131 (controller=0.2237) → λ=6.896→7.396 | E[qλ(S)]=0.0002 | KL_EMA=48.1044
 86%|████████████████████████████████▌     | 6/7 [00:08<00:01,  1.47s/it, loss=0.935, πθ(S)=0.185, λ=7.40][HIGH] πθ(S)=0.2336 [95% normal 0.1919,0.2753 | Wilson↑ 0.2442] | E[qλ(S)]=0.0002 | ε=0.1000 | KL=1.299 | λ=7.396
[λ-update] EMA πθ(S)=0.2138 (controller=0.2240) → λ=7.396→7.896 | E[qλ(S)]=0.0001 | KL_EMA=52.6554
100%|███████████████████████████████████████| 7/7 [00:09<00:00,  1.42s/it, loss=1.31, πθ(S)=0.234, λ=7.90]
======= Epoch 2 =======
  0%|                                                                               | 0/7 [00:00<?, ?it/s][HIGH] πθ(S)=0.2364 [95% normal 0.2028,0.2700 | Wilson↑ 0.2465] | E[qλ(S)]=0.0001 | ε=0.1000 | KL=1.295 | λ=7.896
[λ-update] EMA πθ(S)=0.2146 (controller=0.2244) → λ=7.896→8.396 | E[qλ(S)]=0.0001 | KL_EMA=57.1242
 14%|█████▋                                  | 1/7 [00:01<00:07,  1.27s/it, loss=1.3, πθ(S)=0.236, λ=8.40][HIGH] πθ(S)=0.1686 [95% normal 0.1271,0.2101 | Wilson↑ 0.1774] | E[qλ(S)]=0.0001 | ε=0.1000 | KL=1.087 | λ=8.396
[λ-update] EMA πθ(S)=0.2131 (controller=0.2227) → λ=8.396→8.896 | E[qλ(S)]=0.0000 | KL_EMA=61.4606
 29%|███████████▏                           | 2/7 [00:02<00:06,  1.32s/it, loss=1.09, πθ(S)=0.169, λ=8.90][HIGH] πθ(S)=0.2584 [95% normal 0.2110,0.3059 | Wilson↑ 0.2684] | E[qλ(S)]=0.0000 | ε=0.1000 | KL=1.34 | λ=8.896
[λ-update] EMA πθ(S)=0.2145 (controller=0.2238) → λ=8.896→9.396 | E[qλ(S)]=0.0000 | KL_EMA=65.6482
 43%|████████████████▋                      | 3/7 [00:03<00:05,  1.30s/it, loss=1.35, πθ(S)=0.258, λ=9.40][HIGH] πθ(S)=0.1938 [95% normal 0.1600,0.2276 | Wilson↑ 0.2025] | E[qλ(S)]=0.0000 | ε=0.1000 | KL=1.513 | λ=9.396
[λ-update] EMA πθ(S)=0.2138 (controller=0.2229) → λ=9.396→9.896 | E[qλ(S)]=0.0000 | KL_EMA=69.4714
 57%|██████████████████████▎                | 4/7 [00:05<00:03,  1.29s/it, loss=1.52, πθ(S)=0.194, λ=9.90][HIGH] πθ(S)=0.2100 [95% normal 0.1720,0.2480 | Wilson↑ 0.2188] | E[qλ(S)]=0.0000 | ε=0.1000 | KL=1.523 | λ=9.896
[λ-update] EMA πθ(S)=0.2137 (controller=0.2225) → λ=9.896→10.396 | E[qλ(S)]=0.0000 | KL_EMA=73.0726
 71%|███████████████████████████▏          | 5/7 [00:06<00:02,  1.30s/it, loss=1.53, πθ(S)=0.210, λ=10.40][HIGH] πθ(S)=0.1843 [95% normal 0.1520,0.2167 | Wilson↑ 0.1924] | E[qλ(S)]=0.0000 | ε=0.1000 | KL=1.23 | λ=10.396
[λ-update] EMA πθ(S)=0.2130 (controller=0.2215) → λ=10.396→10.896 | E[qλ(S)]=0.0000 | KL_EMA=76.3381
 86%|████████████████████████████████▌     | 6/7 [00:07<00:01,  1.34s/it, loss=1.24, πθ(S)=0.184, λ=10.90][HIGH] πθ(S)=0.2329 [95% normal 0.1913,0.2745 | Wilson↑ 0.2415] | E[qλ(S)]=0.0000 | ε=0.1000 | KL=1.783 | λ=10.896
[λ-update] EMA πθ(S)=0.2129 (controller=0.2212) → λ=10.896→11.396 | E[qλ(S)]=0.0000 | KL_EMA=79.2171
100%|██████████████████████████████████████| 7/7 [00:09<00:00,  1.41s/it, loss=1.79, πθ(S)=0.233, λ=11.40]
=== ETU Suppression Report ===
  - Perplexity on retain: 5.15
=== Results ===
  - π_base(S): 0.2140
  - π_θ(S): 0.2119
  - Suppression ratio: 0.99 (updated/base)
  - Target ε: 0.1000
  - Target achieved: ✗
  - 95% upper π_base(S): 0.2286
  - 95% upper π_θ(S): 0.2265
  - Target achieved (95% upper): ✗
Saved suppression report to models/zephyr-7b-beta_etu_epsilon-0.1_lambda-11.3963_2025-09-02-19-43-59/suppression_report.json
Merging LoRA weights into base model...
Saved V_S to models/zephyr-7b-beta_etu_epsilon-0.1_lambda-11.3963_2025-09-02-19-43-59/V_S.ids.json
Saved ETU model to models/zephyr-7b-beta_etu_epsilon-0.1_lambda-11.3963_2025-09-02-19-43-59
Saved args to models/zephyr-7b-beta_etu_epsilon-0.1_lambda-11.3963_2025-09-02-19-43-59/args.json
Saved metrics to models/zephyr-7b-beta_etu_epsilon-0.1_lambda-11.3963_2025-09-02-19-43-59/metrics.json
✅ ETU 실행 완료!
(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ 
