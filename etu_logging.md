(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ python3 run_etu_h200.py   --forget_corpora "./datasets/bio-forget/data"   --retain_corpora "./datasets/bio-retain/bio-retain-corpus"   --batch_size 55   --max_num_batches 500   --num_epochs 2   --layer_ids "4,5,6,7,8"   --lora_target_modules "q_proj,k_proj,v_proj,o_proj,gate_proj,up_proj,down_proj"   --lora_r 256   --epsilon 0.10   --lambda_max 20.0   --lambda_update_freq 10   --lambda_eta 0.25   --use_pmi_vs   --pmi_min_count 3   --pmi_top_k 1024   --pmi_smoothing 1.0   --pmi_max_batches 2000   --span_masking   --span_ngram_max 4   --retain_weight 0.1   --wilson_max_n 10000   --pinsker_cap 0.10   --mixed_precision bf16   --verbose
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
❌ 오류 발생: argument --use_lora/--no-use_lora: conflicting option string: --use_lora
Traceback (most recent call last):
  File "/data/aiuser3/ETU/run_etu_h200.py", line 345, in run_h200_optimized_etu
    args = get_h200_optimized_args()
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/aiuser3/ETU/run_etu_h200.py", line 255, in get_h200_optimized_args
    parser.add_argument("--use_lora", action=argparse.BooleanOptionalAction, default=True,
  File "/usr/lib/python3.12/argparse.py", line 1507, in add_argument
    return self._add_action(action)
           ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/argparse.py", line 1889, in _add_action
    self._optionals._add_action(action)
  File "/usr/lib/python3.12/argparse.py", line 1709, in _add_action
    action = super(_ArgumentGroup, self)._add_action(action)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/argparse.py", line 1521, in _add_action
    self._check_conflict(action)
  File "/usr/lib/python3.12/argparse.py", line 1658, in _check_conflict
    conflict_handler(action, confl_optionals)
  File "/usr/lib/python3.12/argparse.py", line 1667, in _handle_conflict_error
    raise ArgumentError(action, message % conflict_string)
argparse.ArgumentError: argument --use_lora/--no-use_lora: conflicting option string: --use_lora
(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ 
