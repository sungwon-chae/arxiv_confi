(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ python3 run_etu_h200.py --forget_corpora "./datasets/cyber-forget" --retain_corpora "./datasets/bio-retain" --batch_size 1 --max_num_batches 3 --layer_id 7 --min_len 10 --max_len 500 --verbose
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
Loading checkpoint shards: 100%|████████████████████████████████████████████| 8/8 [00:06<00:00,  1.23it/s]
Loading checkpoint shards: 100%|███████████████████████████████████████████| 8/8 [00:00<00:00, 372.19it/s]
📊 데이터 로딩 중...
🔍 Forget 데이터셋: ['./datasets/cyber-forget']
🔍 Retain 데이터셋: ['./datasets/bio-retain']
🔧 Layer 설정: layer_id=7, layer_ids=7
Processing corpus spec: './datasets/cyber-forget'
Loading local file: ./datasets/cyber-forget
Loaded 0 items from local file
Processing corpus spec: './datasets/bio-retain'
Loading local file: ./datasets/bio-retain
Loaded 0 items from local file
Data loading complete: 0 forget batches, 0 retain batches
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
forget_corpora=./datasets/cyber-forget
retain_corpora=./datasets/bio-retain
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
❌ 오류 발생: min() iterable argument is empty
Traceback (most recent call last):
  File "/data/aiuser3/ETU/run_etu_h200.py", line 299, in run_h200_optimized_etu
    run_etu(
  File "/data/aiuser3/ETU/etu/unlearn.py", line 104, in run_etu
    min([len(f) for f in forget_data_list]),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: min() iterable argument is empty
(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ nvidia-smi
Tue Sep  2 13:09:37 2025       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 570.158.01             Driver Version: 570.158.01     CUDA Version: 12.8     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA H200                    Off |   00000000:0A:00.0 Off |                    0 |
| N/A   32C    P0            120W /  700W |       0MiB / 143771MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   1  NVIDIA H200                    Off |   00000000:18:00.0 Off |                    0 |
| N/A   29C    P0            122W /  700W |       0MiB / 143771MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   2  NVIDIA H200                    Off |   00000000:3B:00.0 Off |                    0 |
| N/A   27C    P0            113W /  700W |       0MiB / 143771MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   3  NVIDIA H200                    Off |   00000000:44:00.0 Off |                    0 |
| N/A   32C    P0            120W /  700W |       0MiB / 143771MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   4  NVIDIA H200                    Off |   00000000:87:00.0 Off |                    0 |
| N/A   32C    P0            118W /  700W |       0MiB / 143771MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   5  NVIDIA H200                    Off |   00000000:90:00.0 Off |                    0 |
| N/A   29C    P0            121W /  700W |       0MiB / 143771MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   6  NVIDIA H200                    Off |   00000000:B9:00.0 Off |                    0 |
| N/A   28C    P0            119W /  700W |       0MiB / 143771MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   7  NVIDIA H200                    Off |   00000000:C2:00.0 Off |                    0 |
| N/A   32C    P0            118W /  700W |       0MiB / 143771MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
                                                                                         
+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|  No running processes found                                                             |
+-----------------------------------------------------------------------------------------+
^A(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ 
