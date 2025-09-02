(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ ./run_paper_experiments.sh
=== ETU Paper Experiments (H200 GPU 최적화) ===
Tue Sep  2 03:51:59 PM KST 2025
GPU Summary:
 - 총 GPU: 8
 - H200 GPU: 8
 - 첫 GPU: NVIDIA H200
🚀 H200 GPU 환경 감지됨 - 최적화된 설정 사용
📊 최적화 설정:
 - strategy: ddp
 - batch_size: 64
 - lora_r: 512
 - lora_alpha: 1024
 - max_num_batches: 500
 - frozen_on_cpu: true

=== Zephyr-7B ETU 실험 시작 ===
=== ETU H200 GPU 최적화 실행 ===
🚀 H200 GPU 환경 설정 중...
GPU 0: NVIDIA H200 (139.8 GB)
✅ H200 GPU 1개 감지됨
🔧 모델 크기 기반 최적 배치 크기: 7
🎯 단일 GPU 모드: GPU 0
🔧 H200 최적화 설정 적용:
   - strategy: ddp
   - batch_size: 7
   - batch_size_per_gpu: 8
   - frozen_on_cpu: True
   - lora_r: 512
   - lora_alpha: 1024
   - max_num_batches: 500
   - mixed_precision: bf16
   - gradient_accumulation_steps: 4
🚀 ETU 실행 시작...
📥 모델 로딩 중...
Loading checkpoint shards: 100%|██████████| 8/8 [00:00<00:00, 370.55it/s]
/data/aiuser3/ETU/etu/unlearn.py:99: FutureWarning: `torch.cuda.amp.GradScaler(args...)` is deprecated. Please use `torch.amp.GradScaler('cuda', args...)` instead.
  scaler = torch.cuda.amp.GradScaler(enabled=(use_cuda and not use_bf16))
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
Data loading complete: 2 forget batches, 587 retain batches
====ETU Config====
gpu_id=0
multi_gpu=False
strategy=ddp
batch_size_per_gpu=8
batch_size=7
max_num_batches=500
frozen_on_cpu=True
use_lora=True
lora_r=512
lora_alpha=1024
epsilon=0.05
lambda_max=30.0
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
output_dir=paper_results/zephyr_7b
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
Building forbidden token set V_S...
V_S size: 258 tokens (0.8% of vocab)
Estimating base probability mass p_S over V_S...
Estimated p_S (π_base over V_S): 0.2761
[info] |V_S|/V = 0.8%, π_base(S)=0.2761, ε=0.0500
V_S preview: ['er', '▁a', 'on', 're', '▁the', '▁w', 'it', 'al', 'ed', 'ing']
Initial λ: 1.9807 → expected qλ(S)≈0.0500
======= Epoch 0 =======
  0%|          | 0/5 [00:00<?, ?it/s]/data/aiuser3/ETU/etu/unlearn.py:220: FutureWarning: `torch.cuda.amp.autocast(args...)` is deprecated. Please use `torch.amp.autocast('cuda', args...)` instead.
  with torch.cuda.amp.autocast(enabled=use_amp,
100%|██████████| 5/5 [00:00<00:00,  6.01it/s, loss=7.33, πθ(S)=0.281, λ=1.98]
[HIGH] πθ(S)=0.3062 [95% normal 0.2251,0.3874 | Wilson↑ 0.3922] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=11.66 | λ=1.981
[HIGH] πθ(S)=0.2040 [95% normal 0.0685,0.3395 | Wilson↑ 0.2735] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=1.892 | λ=1.981
[HIGH] πθ(S)=0.1933 [95% normal 0.0606,0.3260 | Wilson↑ 0.2549] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=1.883 | λ=1.981
[HIGH] πθ(S)=0.1088 [95% normal 0.0331,0.1846 | Wilson↑ 0.1528] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=3.13 | λ=1.981
[HIGH] πθ(S)=0.2814 [95% normal 0.1905,0.3723 | Wilson↑ 0.3306] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=7.33 | λ=1.981
======= Epoch 1 =======
100%|██████████| 5/5 [00:00<00:00,  7.64it/s, loss=7.74, πθ(S)=0.297, λ=1.98]
[HIGH] πθ(S)=0.1638 [95% normal 0.0394,0.2881 | Wilson↑ 0.2040] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=1.679 | λ=1.981
[HIGH] πθ(S)=0.1974 [95% normal 0.0655,0.3293 | Wilson↑ 0.2382] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=2.685 | λ=1.981
[HIGH] πθ(S)=0.5525 [95% normal 0.4377,0.6674 | Wilson↑ 0.5959] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=7.892 | λ=1.981
[HIGH] πθ(S)=0.3378 [95% normal 0.2580,0.4176 | Wilson↑ 0.3757] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=19.98 | λ=1.981
[HIGH] πθ(S)=0.2969 [95% normal 0.1899,0.4040 | Wilson↑ 0.3319] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=7.745 | λ=1.981
======= Epoch 2 =======
100%|██████████| 5/5 [00:00<00:00,  8.19it/s, loss=12.3, πθ(S)=0.290, λ=1.98]
[HIGH] πθ(S)=0.1464 [95% normal 0.0276,0.2652 | Wilson↑ 0.1739] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=1.294 | λ=1.981
[HIGH] πθ(S)=0.1452 [95% normal 0.0268,0.2636 | Wilson↑ 0.1719] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=1.279 | λ=1.981
[HIGH] πθ(S)=0.4185 [95% normal 0.3331,0.5040 | Wilson↑ 0.4512] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=13.9 | λ=1.981
[HIGH] πθ(S)=0.0979 [95% normal 0.0256,0.1701 | Wilson↑ 0.1183] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=2.756 | λ=1.981
[HIGH] πθ(S)=0.2903 [95% normal 0.2104,0.3702 | Wilson↑ 0.3192] | E[qλ(S)]=0.0500 | ε=0.0500 | KL=12.3 | λ=1.981
=== ETU Suppression Report ===
  - Perplexity on retain: 4.95
=== Results ===
  - π_base(S): 0.2509
  - π_θ(S): 0.2509
  - Suppression ratio: 1.00 (updated/base)
  - Target ε: 0.0500
  - Target achieved: ✗
  - 95% upper π_base(S): 0.2810
  - 95% upper π_θ(S): 0.2810
  - Target achieved (95% upper): ✗
Saved suppression report to paper_results/zephyr_7b/suppression_report.json
Merging LoRA weights into base model...
Saved V_S to paper_results/zephyr_7b/V_S.ids.json
Saved ETU model to paper_results/zephyr_7b
Saved args to paper_results/zephyr_7b/args.json
Saved metrics to paper_results/zephyr_7b/metrics.json
✅ ETU 실행 완료!
All experiments completed at: Tue Sep  2 03:53:02 PM KST 2025
Results saved in paper_results/zephyr_7b/ and models/ (모델 아티팩트 저장 위치는 스크립트 구현에 따름)
(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ 
