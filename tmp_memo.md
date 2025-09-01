aiuser3@ai-smartlaw:~$ ls -la ~/LLM_EvalPipeline_test/.venv/
total 36
drwxrwxr-x 6 aiuser3 aiuser3 4096 Aug 14 10:16 .
drwxrwxr-x 9 aiuser3 aiuser3 4096 Aug 21 08:51 ..
drwxrwxr-x 2 aiuser3 aiuser3 4096 Aug 14 10:16 bin
-rw-rw-r-- 1 aiuser3 aiuser3   43 Aug 13 14:40 CACHEDIR.TAG
-rw-rw-r-- 1 aiuser3 aiuser3    1 Aug 13 14:40 .gitignore
drwxrwxr-x 3 aiuser3 aiuser3 4096 Aug 14 10:16 include
drwxrwxr-x 3 aiuser3 aiuser3 4096 Aug 13 14:40 lib
lrwxrwxrwx 1 aiuser3 aiuser3    3 Aug 13 14:40 lib64 -> lib
-rwxrwxrwx 1 aiuser3 aiuser3    0 Aug 13 14:40 .lock
-rw-rw-r-- 1 aiuser3 aiuser3  154 Aug 13 14:40 pyvenv.cfg
drwxrwxr-x 3 aiuser3 aiuser3 4096 Aug 13 14:41 share
aiuser3@ai-smartlaw:~$ source ~/LLM_EvalPipeline_test/.venv/bin/activate
(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~$ python --version
Python 3.12.3
(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~$ pip list | head -10
Package                            Version
---------------------------------- ------------------------
absl-py                            2.3.1
accelerate                         1.10.0
aiohappyeyeballs                   2.6.1
aiohttp                            3.12.15
aiosignal                          1.4.0
annotated-types                    0.7.0
anyio                              4.10.0
astor                              0.8.1
ERROR: Pipe to stdout was broken
Exception ignored in: <_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>
BrokenPipeError: [Errno 32] Broken pipe
(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~$ python -c "
import sys
print('=== venv 환경 패키지 확인 ===')
packages = ['torch', 'transformers', 'datasets', 'peft', 'numpy', 'yaml']
for pkg in packages:
    try:
        module = __import__(pkg)
        version = getattr(module, '__version__', 'unknown')
        print(f'✅ {pkg} {version}')
    except ImportError:
        print(f'❌ {pkg} 없음')
"
=== venv 환경 패키지 확인 ===
✅ torch 2.9.0.dev20250804+cu128
✅ transformers 4.55.0
✅ datasets 2.16.0
✅ peft 0.17.0
✅ numpy 2.2.6
✅ yaml 6.0.2
(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~$ python -c "
import torch
print(f'✅ PyTorch {torch.__version__}')
print(f'CUDA available: {torch.cuda.is_available()}')
print(f'GPU count: {torch.cuda.device_count()}')
if torch.cuda.is_available():
    for i in range(torch.cuda.device_count()):
        print(f'GPU {i}: {torch.cuda.get_device_name(i)}')
"
✅ PyTorch 2.9.0.dev20250804+cu128
CUDA available: True
GPU count: 8
GPU 0: NVIDIA H200
GPU 1: NVIDIA H200
GPU 2: NVIDIA H200
GPU 3: NVIDIA H200
GPU 4: NVIDIA H200
GPU 5: NVIDIA H200
GPU 6: NVIDIA H200
GPU 7: NVIDIA H200
(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~$ nvidia -smi
WARNING:root:could not open file '/etc/apt/sources.list.d/sdcss.list': [Errno 13] Permission denied: '/etc/apt/sources.list.d/sdcss.list'

nvidia: command not found
(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~$ nvidia-smi
Mon Sep  1 19:00:39 2025       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 570.158.01             Driver Version: 570.158.01     CUDA Version: 12.8     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA H200                    Off |   00000000:0A:00.0 Off |                    0 |
| N/A   31C    P0            120W /  700W |       0MiB / 143771MiB |      0%      Default |
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
| N/A   28C    P0            117W /  700W |       0MiB / 143771MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   7  NVIDIA H200                    Off |   00000000:C2:00.0 Off |                    0 |
| N/A   32C    P0            120W /  700W |       0MiB / 143771MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
                                                                                         
+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|  No running processes found                                                             |
+-----------------------------------------------------------------------------------------+
(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~$ cd ETU
(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ python benchmark_8gpu.py
=== ETU 8대 H200 GPU 성능 벤치마크 ===
🚀 8대 H200 GPU 벤치마크 시작
============================================================
GPU 0: NVIDIA H200 (139.8 GB)
GPU 1: NVIDIA H200 (139.8 GB)
GPU 2: NVIDIA H200 (139.8 GB)
GPU 3: NVIDIA H200 (139.8 GB)
GPU 4: NVIDIA H200 (139.8 GB)
GPU 5: NVIDIA H200 (139.8 GB)
GPU 6: NVIDIA H200 (139.8 GB)
GPU 7: NVIDIA H200 (139.8 GB)
💾 총 GPU 메모리: 1118.5 GB
============================================================
🚀 전체 벤치마크 시작...

📊 메모리 대역폭 벤치마크 시작...
GPU 0 메모리 대역폭: 1999.65 GB/s
GPU 1 메모리 대역폭: 2532.67 GB/s
GPU 2 메모리 대역폭: 2533.27 GB/s
GPU 3 메모리 대역폭: 2532.78 GB/s
GPU 4 메모리 대역폭: 2533.37 GB/s
GPU 5 메모리 대역폭: 2533.49 GB/s
GPU 6 메모리 대역폭: 2536.84 GB/s
GPU 7 메모리 대역폭: 2534.68 GB/s

🔢 연산 성능 벤치마크 시작...
GPU 0 연산 성능: 51206.64 GFLOPS
GPU 1 연산 성능: 51177.54 GFLOPS
GPU 2 연산 성능: 51184.68 GFLOPS
GPU 3 연산 성능: 51187.45 GFLOPS
GPU 4 연산 성능: 51180.68 GFLOPS
GPU 5 연산 성능: 51184.31 GFLOPS
GPU 6 연산 성능: 51206.73 GFLOPS
GPU 7 연산 성능: 50964.30 GFLOPS

🔄 멀티 GPU 스케일링 벤치마크 시작...
  1대 GPU 테스트...
    1대 GPU 효율성: 281.517
  2대 GPU 테스트...
    2대 GPU 효율성: 12.207
  3대 GPU 테스트...
    3대 GPU 효율성: 6.429
  4대 GPU 테스트...
    4대 GPU 효율성: 3.832
  5대 GPU 테스트...
    5대 GPU 효율성: 2.621
  6대 GPU 테스트...
    6대 GPU 효율성: 1.967
  7대 GPU 테스트...
    7대 GPU 효율성: 1.502
  8대 GPU 테스트...
    8대 GPU 효율성: 1.192

💾 메모리 사용량 벤치마크 시작...
GPU 0 최대 메모리: 18.39 GB
GPU 1 최대 메모리: 18.39 GB
GPU 2 최대 메모리: 18.39 GB
GPU 3 최대 메모리: 18.39 GB
GPU 4 최대 메모리: 18.39 GB
GPU 5 최대 메모리: 18.39 GB
GPU 6 최대 메모리: 18.39 GB
GPU 7 최대 메모리: 18.39 GB

============================================================
📊 벤치마크 결과 요약
============================================================
평균 메모리 대역폭: 2467.09 GB/s
평균 연산 성능: 51161.54 GFLOPS
평균 멀티 GPU 효율성: 38.908
============================================================
📝 벤치마크 결과 저장됨: h200_benchmark_20250901_190127.json
(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ ^C
