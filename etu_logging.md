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
Loading checkpoint shards: 100%|███████████████████████████████████████████| 8/8 [00:00<00:00, 384.51it/s]
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
  0%|                                                                               | 0/7 [00:00<?, ?it/s]
❌ 오류 발생: Inference tensors cannot be saved for backward. To work around you can make a clone to get a normal tensor and use it in autograd.
Traceback (most recent call last):
  File "/data/aiuser3/ETU/run_etu_h200.py", line 408, in run_h200_optimized_etu
    run_etu(
  File "/data/aiuser3/ETU/etu/unlearn.py", line 260, in run_etu
    retain_loss = torch.nn.functional.kl_div(upd_ret, base_ret, reduction='batchmean') * retain_w
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/torch/nn/functional.py", line 3367, in kl_div
    reduced = torch.kl_div(input, target, reduction_enum, log_target=log_target)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
RuntimeError: Inference tensors cannot be saved for backward. To work around you can make a clone to get a normal tensor and use it in autograd.
(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ 
