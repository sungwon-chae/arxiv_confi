(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ python3 run_etu_h200.py   --forget_corpora "test_data/forget.txt"   --retain_corpora "test_data/retain.txt"   --batch_size 1   --max_num_batches 3   --layer_id 7   --min_len 10   --max_len 500   --verbose
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
Loading checkpoint shards: 100%|███████████████████████████████| 8/8 [00:06<00:00,  1.23it/s]
Loading checkpoint shards: 100%|██████████████████████████████| 8/8 [00:00<00:00, 373.79it/s]
📊 데이터 로딩 중...
🔍 Forget 데이터셋: ['test_data/forget.txt']
🔍 Retain 데이터셋: ['test_data/retain.txt']
🔧 Layer 설정: layer_id=7, layer_ids=7
Processing corpus spec: 'test_data/forget.txt'
Loading local file: test_data/forget.txt
Loaded 36 items from local file
Processing corpus spec: 'test_data/retain.txt'
Loading local file: test_data/retain.txt
Loaded 1 items from local file
Data loading complete: 36 forget batches, 1 retain batches
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
forget_corpora=test_data/forget.txt
retain_corpora=test_data/retain.txt
model_name_or_path=HuggingFaceH4/zephyr-7b-beta
deterministic=False
verbose=True
lr=1e-05
num_epochs=1
min_len=10
max_len=500
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
V_S size: 68 tokens (0.2% of vocab)
Estimating base probability mass p_S over V_S...
Estimated p_S (π_base over V_S): 0.1416
[info] |V_S|/V = 0.2%, π_base(S)=0.1416, ε=0.0500
V_S preview: ['▁a', '▁the', 'ed', '▁to', '▁and', '▁A', '▁be', '▁is', '▁that', '▁R']
Initial λ: 1.1423 → expected qλ(S)≈0.0500
======= Epoch 0 =======
  0%|                                                                  | 0/1 [00:00<?, ?it/s]/data/aiuser3/ETU/etu/unlearn.py:220: FutureWarning: `torch.cuda.amp.autocast(args...)` is deprecated. Please use `torch.amp.autocast('cuda', args...)` instead.
  with torch.cuda.amp.autocast(enabled=use_amp,
[HIGH] πθ(S)=0.1969 [95% normal 0.0000,0.5455 | Wilson↑ 0.6220] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=0.2682 | λ=1.142
100%|█████████████████████████| 1/1 [00:00<00:00,  2.45it/s, loss=0.268, πθ(S)=0.197, λ=1.14]
=== ETU Suppression Report ===
  - Perplexity on retain: 8.77
=== Results ===
  - π_base(S): 0.1416
  - π_θ(S): 0.1414
  - Suppression ratio: 1.00 (updated/base)
  - Target ε: 0.0500
  - Target achieved: ✗
  - 95% upper π_base(S): 0.2087
  - 95% upper π_θ(S): 0.2084
  - Target achieved (95% upper): ✗
Saved suppression report to models/zephyr-7b-beta_etu_epsilon-0.05_lambda-1.1423_2025-09-02-00-09-15/suppression_report.json
Merging LoRA weights into base model...
Saved V_S to models/zephyr-7b-beta_etu_epsilon-0.05_lambda-1.1423_2025-09-02-00-09-15/V_S.ids.json
Saved ETU model to models/zephyr-7b-beta_etu_epsilon-0.05_lambda-1.1423_2025-09-02-00-09-15
Saved args to models/zephyr-7b-beta_etu_epsilon-0.05_lambda-1.1423_2025-09-02-00-09-15/args.json
Saved metrics to models/zephyr-7b-beta_etu_epsilon-0.05_lambda-1.1423_2025-09-02-00-09-15/metrics.json
✅ ETU 실행 완료!
(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ 
