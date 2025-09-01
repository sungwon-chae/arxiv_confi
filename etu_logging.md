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
❌ 오류 발생: expected an indented block after 'if' statement on line 465 (utils.py, line 466)
Traceback (most recent call last):
  File "/data/aiuser3/ETU/run_etu_h200.py", line 236, in run_h200_optimized_etu
    from etu.unlearn import run_etu
  File "/data/aiuser3/ETU/etu/unlearn.py", line 14, in <module>
    from etu.utils import (
  File "/data/aiuser3/ETU/etu/utils.py", line 466
    params.append(p)
    ^^^^^^
IndentationError: expected an indented block after 'if' statement on line 465
(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ 
