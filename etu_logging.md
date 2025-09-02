(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ python3 run_etu_h200.py \
  --multi_gpu \
  --strategy ddp \
  --forget_corpora "./datasets/cyber-forget" \
  --retain_corpora "./datasets/bio-retain" \
  --batch_size 32 \
  --max_num_batches 50 \
  --layer_id 7 \
  --epsilon 0.05 \
  --lambda_max 12.0 \
  --verbose
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
🔄 멀티 GPU 모드: GPU [0, 1, 2, 3, 4, 5, 6, 7]
🔧 멀티 GPU 환경 설정: ddp
✅ DDP 환경 설정 완료
🔧 H200 최적화 설정 적용:
   - strategy: ddp
   - batch_size: 32
   - batch_size_per_gpu: 8
   - frozen_on_cpu: True
   - lora_r: 512
   - lora_alpha: 1024
   - max_num_batches: 50
   - mixed_precision: bf16
   - gradient_accumulation_steps: 4
🚀 ETU 실행 시작...
📥 모델 로딩 중...
Loading checkpoint shards: 100%|███████████████████████████████████████████| 8/8 [00:00<00:00, 369.62it/s]
❌ 오류 발생: CUDA out of memory. Tried to allocate 112.00 MiB. GPU 0 has a total capacity of 139.81 GiB of which 24.12 MiB is free. Process 1117159 has 127.15 GiB memory in use. Including non-PyTorch memory, this process has 12.62 GiB memory in use. Of the allocated memory 12.10 GiB is allocated by PyTorch, and 7.55 MiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True to avoid fragmentation.  See documentation for Memory Management  (https://pytorch.org/docs/stable/notes/cuda.html#environment-variables)
Traceback (most recent call last):
  File "/data/aiuser3/ETU/run_etu_h200.py", line 367, in run_h200_optimized_etu
    base_model, tokenizer = load_model(args.model_name_or_path, train=True)
                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/aiuser3/ETU/etu/utils.py", line 512, in load_model
    model.to("cuda")
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/transformers/modeling_utils.py", line 4333, in to
    return super().to(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1371, in to
    return self._apply(convert)
           ^^^^^^^^^^^^^^^^^^^^
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/torch/nn/modules/module.py", line 930, in _apply
    module._apply(fn)
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/torch/nn/modules/module.py", line 930, in _apply
    module._apply(fn)
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/torch/nn/modules/module.py", line 930, in _apply
    module._apply(fn)
  [Previous line repeated 2 more times]
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/torch/nn/modules/module.py", line 957, in _apply
    param_applied = fn(param)
                    ^^^^^^^^^
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1357, in convert
    return t.to(
           ^^^^^
torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 112.00 MiB. GPU 0 has a total capacity of 139.81 GiB of which 24.12 MiB is free. Process 1117159 has 127.15 GiB memory in use. Including non-PyTorch memory, this process has 12.62 GiB memory in use. Of the allocated memory 12.10 GiB is allocated by PyTorch, and 7.55 MiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True to avoid fragmentation.  See documentation for Memory Management  (https://pytorch.org/docs/stable/notes/cuda.html#environment-variables)
