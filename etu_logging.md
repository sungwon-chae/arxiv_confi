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
🚀 모델 로딩 중...
config.json: 100%|███████████████████████████████████████████████████████| 638/638 [00:00<00:00, 2.68MB/s]
model.safetensors.index.json: 23.9kB [00:00, 106MB/s]
model-00008-of-00008.safetensors: 100%|████████████████████████████████| 816M/816M [03:41<00:00, 3.69MB/s]
model-00004-of-00008.safetensors: 100%|██████████████████████████████| 1.95G/1.95G [03:59<00:00, 8.13MB/s]
model-00002-of-00008.safetensors: 100%|██████████████████████████████| 1.95G/1.95G [04:04<00:00, 7.97MB/s]
model-00003-of-00008.safetensors: 100%|██████████████████████████████| 1.98G/1.98G [04:11<00:00, 7.86MB/s]
model-00007-of-00008.safetensors: 100%|██████████████████████████████| 1.98G/1.98G [04:52<00:00, 6.76MB/s]
model-00001-of-00008.safetensors: 100%|██████████████████████████████| 1.89G/1.89G [04:55<00:00, 6.39MB/s]
model-00006-of-00008.safetensors: 100%|██████████████████████████████| 1.95G/1.95G [04:55<00:00, 6.58MB/s]
model-00005-of-00008.safetensors: 100%|██████████████████████████████| 1.98G/1.98G [04:56<00:00, 6.68MB/s]
Fetching 8 files: 100%|█████████████████████████████████████████████████████| 8/8 [04:56<00:00, 37.12s/it]
Loading checkpoint shards: 100%|████████████████████████████████████████████| 8/8 [00:07<00:00,  1.09it/s]
generation_config.json: 100%|█████████████████████████████████████████████| 111/111 [00:00<00:00, 620kB/s]
tokenizer_config.json: 1.43kB [00:00, 3.33MB/s]████████████████████▉ | 1.82G/1.89G [04:51<00:02, 33.3MB/s]
tokenizer.model: 100%|██████████████████████████████████████████████████| 493k/493k [00:01<00:00, 374kB/s]
added_tokens.json: 100%|████████████████████████████████████████████████| 42.0/42.0 [00:00<00:00, 258kB/s]
special_tokens_map.json: 100%|████████████████████████████████████████████| 168/168 [00:00<00:00, 765kB/s]
tokenizer.json: 1.80MB [00:00, 13.9MB/s]
Loading checkpoint shards: 100%|███████████████████████████████████████████| 8/8 [00:00<00:00, 372.57it/s]
🚀 데이터 로딩 중...
Downloading readme: 3.77kB [00:00, 7.64MB/s]
Downloading readme: 3.77kB [00:00, 14.9MB/s]
❌ 오류 발생: name 'run_etu' is not defined
Traceback (most recent call last):
  File "/data/aiuser3/ETU/run_etu_h200.py", line 149, in run_h200_optimized_etu
    run_etu(
    ^^^^^^^
NameError: name 'run_etu' is not defined
(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ ^C
(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ ^C
(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ ^C
(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ ^C
