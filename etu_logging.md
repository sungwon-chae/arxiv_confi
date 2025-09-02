(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ python3 run_etu_h200.py \
  --forget_corpora "./datasets/bio-forget/data" \
  --retain_corpora "./datasets/bio-retain/bio-retain-corpus" \
  --batch_size 32 \
  --max_num_batches 500 \
  --num_epochs 2 \
  --layer_ids "6,7,8" \
  --lora_target_modules "q_proj,k_proj,v_proj,o_proj" \
  --lora_r 128 \
  --epsilon 0.10 \
  --lambda_max 40.0 \
  --lambda_update_freq 1 \
  --lambda_eta 0.5 \
  --use_pmi_vs \
  --pmi_min_count 3 \
  --pmi_top_k 1024 \
  --pmi_smoothing 1.0 \
  --pmi_max_batches 2000 \
  --span_masking \
  --span_ngram_max 4 \
  --retain_weight 0.1 \
  --wilson_max_n 10000 \
  --pinsker_cap 0.10 \
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
🔧 사용자 지정 배치 크기 사용: 32 (heuristic=55)
🎯 단일 GPU 모드: GPU 0
🔧 H200 최적화 설정 적용:
   - strategy: single
   - batch_size: 32
   - batch_size_per_gpu: 8
   - frozen_on_cpu: False
   - lora_r: 128
   - lora_alpha: 512
   - max_num_batches: 500
   - mixed_precision: bf16
   - gradient_accumulation_steps: 4
🚀 ETU 실행 시작...
📥 모델 로딩 중...
Loading checkpoint shards: 100%|████████████████████████████████████████████| 8/8 [00:06<00:00,  1.24it/s]
Loading checkpoint shards: 100%|███████████████████████████████████████████| 8/8 [00:00<00:00, 377.12it/s]
🔧 Frozen 모델을 GPU에 로드
📊 데이터 로딩 중...
🔍 Forget 데이터셋: ['./datasets/bio-forget/data']
🔍 Retain 데이터셋: ['./datasets/bio-retain/bio-retain-corpus']
🔧 Final layer_ids: [6, 7, 8]
🔧 Final lora_target_modules: ['q_proj', 'k_proj', 'v_proj', 'o_proj']
Processing corpus spec: './datasets/bio-forget/data'
Loading local dataset folder: ./datasets/bio-forget/data
Loading from actual path: ./datasets/bio-forget/data
Loaded 56 items from local dataset folder
Processing corpus spec: './datasets/bio-retain/bio-retain-corpus'
Loading local dataset folder: ./datasets/bio-retain/bio-retain-corpus
Loading from actual path: ./datasets/bio-retain/bio-retain-corpus
Loaded 4106 items from local dataset folder
Data loading complete: 1 forget splits (2 batches), 1 retain splits (129 batches)
====ETU Config====
gpu_id=0
multi_gpu=False
strategy=ddp
batch_size_per_gpu=8
batch_size=32
max_num_batches=500
frozen_on_cpu=False
epsilon=0.1
lambda_max=40.0
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
num_epochs=2
min_len=10
max_len=512
layer_id=None
layer_ids=[6, 7, 8]
param_ids=None
name_keywords=q_proj,k_proj,v_proj,o_proj
module_str={model_name}.model.layers[{layer_id}]
use_lora=True
lora_r=128
lora_alpha=512
lora_dropout=0.1
lora_target_modules=['q_proj', 'k_proj', 'v_proj', 'o_proj']
use_pmi_vs=True
vocab_top_k=1000
vs_freq_rate=0.1
vs_abs_cap=1000
pmi_top_k=1024
pmi_min_count=3
pmi_smoothing=1.0
pmi_max_batches=2000
vs_preview_k=10
span_masking=True
span_ngram_max=4
allow_negative_lambda=False
lambda_eta=0.5
pinsker_cap=0.1
use_upper_for_lambda=True
wilson_max_n=10000
log_every=10
output_dir=
seed=None
retain_weight=0.1
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
Applying LoRA to layers: [6, 7, 8]
trainable params: 10,223,616 || all params: 7,251,955,712 || trainable%: 0.1410
Building forbidden token set V_S...
[PMI] counting capped at 2000 batches per split
[PMI] split 0: used 2 batches (cap=2000)
[PMI] split 0: used 129 batches (cap=2000)
[V_S] token filter kept 192/216 (88.9%) after _filter_vs_tokens
V_S (PMI-refined) size: 192 tokens
Top PMI tokens preview: ['in', 'er', '▁a', 'en', 'at', '▁the', 'al', 'ed', 'ing', '▁in']
V_S size: 192 tokens (0.6% of vocab)
Estimating base probability mass p_S over V_S...
Estimated p_S (π_base over V_S): 0.1060
[info] |V_S|/V = 0.6%, π_base(S)=0.1060, ε=0.1000
V_S preview: ['in', 'er', '▁a', 'en', 'at', '▁the', 'al', 'ed', 'ing', '▁in']
Initial λ: 0.0645 → expected qλ(S)≈0.1000
======= Epoch 0 =======
  0%|                                                                               | 0/2 [00:00<?, ?it/s][NEAR] πθ(S)=0.1015 [95% normal 0.0874,0.1155 | Wilson↑ 0.1164] | E[qλ(S)]=0.1000 | ε=0.1000 | KL=0.0002052 | λ=0.065
[λ-update] EMA πθ(S)=0.1037 (controller=0.1187) → λ=0.065→0.065 | E[qλ(S)]=0.1000 | KL_EMA=0.0047
 50%|█████████████████▌                 | 1/2 [00:03<00:03,  3.12s/it, loss=0.000206, πθ(S)=0.101, λ=0.06][HIGH] πθ(S)=0.1104 [95% normal 0.0939,0.1269 | Wilson↑ 0.1218] | E[qλ(S)]=0.1000 | ε=0.1000 | KL=0.0002289 | λ=0.065
[λ-update] EMA πθ(S)=0.1053 (controller=0.1165) → λ=0.065→0.065 | E[qλ(S)]=0.1000 | KL_EMA=0.0535
100%|███████████████████████████████████| 2/2 [00:06<00:00,  3.29s/it, loss=0.000229, πθ(S)=0.110, λ=0.06]
======= Epoch 1 =======
  0%|                                                                               | 0/2 [00:00<?, ?it/s][NEAR] πθ(S)=0.1004 [95% normal 0.0864,0.1143 | Wilson↑ 0.1091] | E[qλ(S)]=0.1000 | ε=0.1000 | KL=0.00153 | λ=0.065
[λ-update] EMA πθ(S)=0.1044 (controller=0.1132) → λ=0.065→0.065 | E[qλ(S)]=0.1000 | KL_EMA=0.0756
 50%|██████████████████                  | 1/2 [00:02<00:02,  2.81s/it, loss=0.00404, πθ(S)=0.100, λ=0.06][NEAR] πθ(S)=0.1090 [95% normal 0.0926,0.1254 | Wilson↑ 0.1169] | E[qλ(S)]=0.1000 | ε=0.1000 | KL=0.002062 | λ=0.065
[λ-update] EMA πθ(S)=0.1050 (controller=0.1128) → λ=0.065→0.065 | E[qλ(S)]=0.1000 | KL_EMA=0.0706
100%|████████████████████████████████████| 2/2 [00:05<00:00,  2.95s/it, loss=0.00635, πθ(S)=0.109, λ=0.06]
=== ETU Suppression Report ===
  - Perplexity on retain: 5.04
=== Results ===
  - π_base(S): 0.1060
  - π_θ(S): 0.1047
  - Suppression ratio: 0.99 (updated/base)
  - Target ε: 0.1000
  - Target achieved: ✗
  - 95% upper π_base(S): 0.1172
  - 95% upper π_θ(S): 0.1159
  - Target achieved (95% upper): ✗
Saved suppression report to models/zephyr-7b-beta_etu_epsilon-0.1_lambda-0.0645_2025-09-02-20-16-27/suppression_report.json
Merging LoRA weights into base model...
Saved V_S to models/zephyr-7b-beta_etu_epsilon-0.1_lambda-0.0645_2025-09-02-20-16-27/V_S.ids.json
Saved ETU model to models/zephyr-7b-beta_etu_epsilon-0.1_lambda-0.0645_2025-09-02-20-16-27
Saved args to models/zephyr-7b-beta_etu_epsilon-0.1_lambda-0.0645_2025-09-02-20-16-27/args.json
Saved metrics to models/zephyr-7b-beta_etu_epsilon-0.1_lambda-0.0645_2025-09-02-20-16-27/metrics.json
✅ ETU 실행 완료!
(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ 
