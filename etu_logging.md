(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~$ source ~/LLM_EvalPipeline_test/.venv/bin/activate
(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~$ cd ETU
(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ python run_etu_h200.py --verbose
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
   - batch_size: 8
   - frozen_on_cpu: False
   - lora_r: 512
   - lora_alpha: 1024
   - max_num_batches: 100
🚀 ETU 실행 시작...
📥 모델 로딩 중...
Loading checkpoint shards: 100%|████████████████████████████████████████████| 8/8 [00:07<00:00,  1.07it/s]
Loading checkpoint shards: 100%|███████████████████████████████████████████| 8/8 [00:00<00:00, 380.79it/s]
📊 데이터 로딩 중...
🔍 Forget 데이터셋: cais/wmdp-corpora:cyber-forget-corpus
🔍 Retain 데이터셋: cais/wmdp-corpora:bio-retain-corpus
====ETU Config====
gpu_id=0
multi_gpu=False
batch_size=8
max_num_batches=100
frozen_on_cpu=False
use_lora=True
lora_r=512
lora_alpha=1024
epsilon=0.05
lambda_max=12.0
lambda_update_freq=25
forget_corpora=cais/wmdp-corpora:cyber-forget-corpus
retain_corpora=cais/wmdp-corpora:bio-retain-corpus
model_name_or_path=HuggingFaceH4/zephyr-7b-beta
deterministic=False
verbose=True
lr=1e-05
num_epochs=1
min_len=10
max_len=512
layer_ids=
param_ids=
name_keywords=
module_str=
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
❌ 오류 발생: 'in <string>' requires string as left operand, not int
Traceback (most recent call last):
  File "/data/aiuser3/ETU/run_etu_h200.py", line 263, in run_h200_optimized_etu
    run_etu(
  File "/data/aiuser3/ETU/etu/unlearn.py", line 85, in run_etu
    updated_model = apply_lora_to_model(args, updated_model, args.layer_ids)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/aiuser3/ETU/etu/utils.py", line 46, in apply_lora_to_model
    model = get_peft_model(model, lora_config)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/peft/mapping_func.py", line 125, in get_peft_model
    return MODEL_TYPE_TO_PEFT_MODEL_MAPPING[peft_config.task_type](
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/peft/peft_model.py", line 1815, in __init__
    super().__init__(model, peft_config, adapter_name, **kwargs)
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/peft/peft_model.py", line 130, in __init__
    self.base_model = cls(model, {adapter_name: peft_config}, adapter_name)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/peft/tuners/tuners_utils.py", line 209, in __init__
    self.inject_adapter(self.model, adapter_name, low_cpu_mem_usage=low_cpu_mem_usage, state_dict=state_dict)
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/peft/tuners/tuners_utils.py", line 567, in inject_adapter
    result = self._check_target_module_exists(peft_config, key)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/peft/tuners/lora/model.py", line 159, in _check_target_module_exists
    return check_target_module_exists(lora_config, key)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/peft/tuners/tuners_utils.py", line 1255, in check_target_module_exists
    target_module_found = layer_index in layer_indexes
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'in <string>' requires string as left operand, not int
(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ ^C
