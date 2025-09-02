./run_paper_experiments.sh
./run_hyperparameter_sweep.sh
./run_large_model_experiments.sh

(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ nvidia-smi
Tue Sep  2 15:37:15 2025       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 570.158.01             Driver Version: 570.158.01     CUDA Version: 12.8     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA H200                    Off |   00000000:0A:00.0 Off |                    0 |
| N/A   30C    P0            122W /  700W |  130215MiB / 143771MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   1  NVIDIA H200                    Off |   00000000:18:00.0 Off |                    0 |
| N/A   26C    P0             78W /  700W |       0MiB / 143771MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   2  NVIDIA H200                    Off |   00000000:3B:00.0 Off |                    0 |
| N/A   24C    P0             74W /  700W |       0MiB / 143771MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   3  NVIDIA H200                    Off |   00000000:44:00.0 Off |                    0 |
| N/A   27C    P0             77W /  700W |       0MiB / 143771MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   4  NVIDIA H200                    Off |   00000000:87:00.0 Off |                    0 |
| N/A   28C    P0             77W /  700W |       0MiB / 143771MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   5  NVIDIA H200                    Off |   00000000:90:00.0 Off |                    0 |
| N/A   26C    P0             79W /  700W |       0MiB / 143771MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   6  NVIDIA H200                    Off |   00000000:B9:00.0 Off |                    0 |
| N/A   25C    P0             76W /  700W |       0MiB / 143771MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   7  NVIDIA H200                    Off |   00000000:C2:00.0 Off |                    0 |
| N/A   28C    P0             76W /  700W |       0MiB / 143771MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
                                                                                         
+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|    0   N/A  N/A         1117159      C   VLLM::EngineCore                      13020... |
+-----------------------------------------------------------------------------------------+
(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ ./run_paper_experiments.sh
=== ETU Paper Experiments (H200 GPU 최적화) ===
Tue Sep  2 03:37:21 PM KST 2025
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
W0902 15:37:22.739000 1133389 torch/distributed/run.py:803] 
W0902 15:37:22.739000 1133389 torch/distributed/run.py:803] *****************************************
W0902 15:37:22.739000 1133389 torch/distributed/run.py:803] Setting OMP_NUM_THREADS environment variable for each process to be 1 in default, to avoid your system being overloaded, please further tune the variable for optimal performance in your application as needed. 
W0902 15:37:22.739000 1133389 torch/distributed/run.py:803] *****************************************
=== ETU H200 GPU 최적화 실행 ===
🚀 H200 GPU 환경 설정 중...
=== ETU H200 GPU 최적화 실행 ===
🚀 H200 GPU 환경 설정 중...
=== ETU H200 GPU 최적화 실행 ===
🚀 H200 GPU 환경 설정 중...
=== ETU H200 GPU 최적화 실행 ===
🚀 H200 GPU 환경 설정 중...
=== ETU H200 GPU 최적화 실행 ===
🚀 H200 GPU 환경 설정 중...
=== ETU H200 GPU 최적화 실행 ===
🚀 H200 GPU 환경 설정 중...
=== ETU H200 GPU 최적화 실행 ===
🚀 H200 GPU 환경 설정 중...
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
usage: run_etu_h200.py [-h] [--gpu_id GPU_ID] [--multi_gpu]
                       [--strategy {ddp,fsdp,tensor_parallel}]
                       [--batch_size_per_gpu BATCH_SIZE_PER_GPU]
                       [--batch_size BATCH_SIZE]
                       [--max_num_batches MAX_NUM_BATCHES] [--frozen_on_cpu]
                       [--use_lora] [--lora_r LORA_R]
                       [--lora_alpha LORA_ALPHA] [--epsilon EPSILON]
                       [--lambda_max LAMBDA_MAX]
                       [--lambda_update_freq LAMBDA_UPDATE_FREQ]
                       [--forget_corpora FORGET_CORPORA]
                       [--retain_corpora RETAIN_CORPORA]
                       [--model_name_or_path MODEL_NAME_OR_PATH]
                       [--deterministic] [--verbose]
                       [--gradient_accumulation_steps GRADIENT_ACCUMULATION_STEPS]
                       [--mixed_precision {fp16,bf16,fp32}]
                       [--trust_remote_code] [--lr LR]
                       [--num_epochs NUM_EPOCHS] [--min_len MIN_LEN]
                       [--max_len MAX_LEN] [--layer_id LAYER_ID]
                       [--layer_ids LAYER_IDS] [--param_ids PARAM_IDS]
                       [--name_keywords NAME_KEYWORDS]
                       [--module_str MODULE_STR] [--use_pmi_vs]
                       [--vocab_top_k VOCAB_TOP_K]
                       [--vs_freq_rate VS_FREQ_RATE] [--vs_abs_cap VS_ABS_CAP]
                       [--pmi_top_k PMI_TOP_K] [--pmi_min_count PMI_MIN_COUNT]
                       [--pmi_smoothing PMI_SMOOTHING]
                       [--pmi_max_batches PMI_MAX_BATCHES]
                       [--vs_preview_k VS_PREVIEW_K] [--allow_negative_lambda]
                       [--lambda_eta LAMBDA_ETA] [--wilson_max_n WILSON_MAX_N]
                       [--log_every LOG_EVERY] [--output_dir OUTPUT_DIR]
                       [--seed SEED] [--retain_weight RETAIN_WEIGHT]
                       [--retain_broadcast]
                       [--preference_weight PREFERENCE_WEIGHT]
                       [--pref_every PREF_EVERY] [--pref_format PREF_FORMAT]
                       [--pref_beta PREF_BETA] [--pref_margin PREF_MARGIN]
                       [--pref_max_len PREF_MAX_LEN]
run_etu_h200.py: error: unrecognized arguments: true
GPU 0: NVIDIA H200 (139.8 GB)
GPU 1: NVIDIA H200 (139.8 GB)
GPU 2: NVIDIA H200 (139.8 GB)
GPU 3: NVIDIA H200 (139.8 GB)
GPU 4: NVIDIA H200 (139.8 GB)
GPU 5: NVIDIA H200 (139.8 GB)
GPU 6: NVIDIA H200 (139.8 GB)
✅ H200 GPU 7개 감지됨
usage: run_etu_h200.py [-h] [--gpu_id GPU_ID] [--multi_gpu]
                       [--strategy {ddp,fsdp,tensor_parallel}]
                       [--batch_size_per_gpu BATCH_SIZE_PER_GPU]
                       [--batch_size BATCH_SIZE]
                       [--max_num_batches MAX_NUM_BATCHES] [--frozen_on_cpu]
                       [--use_lora] [--lora_r LORA_R]
                       [--lora_alpha LORA_ALPHA] [--epsilon EPSILON]
                       [--lambda_max LAMBDA_MAX]
                       [--lambda_update_freq LAMBDA_UPDATE_FREQ]
                       [--forget_corpora FORGET_CORPORA]
                       [--retain_corpora RETAIN_CORPORA]
                       [--model_name_or_path MODEL_NAME_OR_PATH]
                       [--deterministic] [--verbose]
                       [--gradient_accumulation_steps GRADIENT_ACCUMULATION_STEPS]
                       [--mixed_precision {fp16,bf16,fp32}]
                       [--trust_remote_code] [--lr LR]
                       [--num_epochs NUM_EPOCHS] [--min_len MIN_LEN]
                       [--max_len MAX_LEN] [--layer_id LAYER_ID]
                       [--layer_ids LAYER_IDS] [--param_ids PARAM_IDS]
                       [--name_keywords NAME_KEYWORDS]
                       [--module_str MODULE_STR] [--use_pmi_vs]
                       [--vocab_top_k VOCAB_TOP_K]
                       [--vs_freq_rate VS_FREQ_RATE] [--vs_abs_cap VS_ABS_CAP]
                       [--pmi_top_k PMI_TOP_K] [--pmi_min_count PMI_MIN_COUNT]
                       [--pmi_smoothing PMI_SMOOTHING]
                       [--pmi_max_batches PMI_MAX_BATCHES]
                       [--vs_preview_k VS_PREVIEW_K] [--allow_negative_lambda]
                       [--lambda_eta LAMBDA_ETA] [--wilson_max_n WILSON_MAX_N]
                       [--log_every LOG_EVERY] [--output_dir OUTPUT_DIR]
                       [--seed SEED] [--retain_weight RETAIN_WEIGHT]
                       [--retain_broadcast]
                       [--preference_weight PREFERENCE_WEIGHT]
                       [--pref_every PREF_EVERY] [--pref_format PREF_FORMAT]
                       [--pref_beta PREF_BETA] [--pref_margin PREF_MARGIN]
                       [--pref_max_len PREF_MAX_LEN]
run_etu_h200.py: error: unrecognized arguments: true
W0902 15:37:28.769000 1133389 torch/distributed/elastic/multiprocessing/api.py:906] Sending process 1133525 closing signal SIGTERM
W0902 15:37:28.771000 1133389 torch/distributed/elastic/multiprocessing/api.py:906] Sending process 1133527 closing signal SIGTERM
W0902 15:37:28.772000 1133389 torch/distributed/elastic/multiprocessing/api.py:906] Sending process 1133528 closing signal SIGTERM
W0902 15:37:28.772000 1133389 torch/distributed/elastic/multiprocessing/api.py:906] Sending process 1133529 closing signal SIGTERM
W0902 15:37:28.772000 1133389 torch/distributed/elastic/multiprocessing/api.py:906] Sending process 1133530 closing signal SIGTERM
W0902 15:37:28.773000 1133389 torch/distributed/elastic/multiprocessing/api.py:906] Sending process 1133531 closing signal SIGTERM
E0902 15:37:28.952000 1133389 torch/distributed/elastic/multiprocessing/api.py:880] failed (exitcode: 2) local_rank: 0 (pid: 1133524) of binary: /data/aiuser3/LLM_EvalPipeline_test/.venv/bin/python3
Traceback (most recent call last):
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/bin/torchrun", line 10, in <module>
    sys.exit(main())
             ^^^^^^
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/torch/distributed/elastic/multiprocessing/errors/__init__.py", line 357, in wrapper
    return f(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/torch/distributed/run.py", line 936, in main
    run(args)
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/torch/distributed/run.py", line 927, in run
    elastic_launch(
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/torch/distributed/launcher/api.py", line 151, in __call__
    return launch_agent(self._config, self._entrypoint, list(args))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/torch/distributed/launcher/api.py", line 288, in launch_agent
    raise ChildFailedError(
torch.distributed.elastic.multiprocessing.errors.ChildFailedError: 
============================================================
run_etu_h200.py FAILED
------------------------------------------------------------
Failures:
[1]:
  time      : 2025-09-02_15:37:28
  host      : ai-smartlaw
  rank      : 2 (local_rank: 2)
  exitcode  : 2 (pid: 1133526)
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
------------------------------------------------------------
Root Cause (first observed failure):
[0]:
  time      : 2025-09-02_15:37:28
  host      : ai-smartlaw
  rank      : 0 (local_rank: 0)
  exitcode  : 2 (pid: 1133524)
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
============================================================
(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ 
