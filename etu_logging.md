(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ python run_etu_h200.py --verbose
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
❌ 오류 발생: run_etu() missing 5 required positional arguments: 'frozen_model', 'tokenizer', 'forget_data_list', 'retain_data_list', and 'args'
Traceback (most recent call last):
  File "/data/aiuser3/ETU/run_etu_h200.py", line 132, in run_h200_optimized_etu
    run_etu(args)
TypeError: run_etu() missing 5 required positional arguments: 'frozen_model', 'tokenizer', 'forget_data_list', 'retain_data_list', and 'args'
(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ 
