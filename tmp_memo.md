aiuser1@ai-smartlaw:/data/models$ nvidia-smi
Mon Sep  1 14:11:47 2025       
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
| N/A   28C    P0            117W /  700W |       0MiB / 143771MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   7  NVIDIA H200                    Off |   00000000:C2:00.0 Off |                    0 |
| N/A   33C    P0            120W /  700W |       0MiB / 143771MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
                                                                                         
+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|  No running processes found                                                             |
+-----------------------------------------------------------------------------------------+
aiuser1@ai-smartlaw:/data/models$ 


(etu_env) aiuser1@ai-smartlaw:~/workspace/ETU$ deactivate
aiuser1@ai-smartlaw:~/workspace/ETU$ source ~/my_env/bin/activate
(my_env) aiuser1@ai-smartlaw:~/workspace/ETU$ python --version
Python 3.11.13
(my_env) aiuser1@ai-smartlaw:~/workspace/ETU$ pip list | head 10
head: cannot open '10' for reading: No such file or directory
ERROR: Pipe to stdout was broken
Exception ignored in: <_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>
BrokenPipeError: [Errno 32] Broken pipe
(my_env) aiuser1@ai-smartlaw:~/workspace/ETU$ pip list | head -10
Package                                  Version
---------------------------------------- -------------
accelerate                               1.6.0
aiohappyeyeballs                         2.6.1
aiohttp                                  3.11.18
aiosignal                                1.3.2
airportsdata                             20250224
annotated-types                          0.7.0
anyio                                    4.9.0
astor                                    0.8.1
ERROR: Pipe to stdout was broken
Exception ignored in: <_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>
BrokenPipeError: [Errno 32] Broken pipe
(my_env) aiuser1@ai-smartlaw:~/workspace/ETU$ python -c "
import sys
print('=== my_env 환경 패키지 확인 ===')
packages = ['torch', 'transformers', 'numpy', 'datasets', 'accelerate', 'peft']
for pkg in packages:
    try:
        module = __import__(pkg)
        version = getattr(module, '__version__', 'unknown')
        print(f'✅ {pkg} {version}')
    except ImportError:
        print(f'❌ {pkg} 없음')
"
=== my_env 환경 패키지 확인 ===
✅ torch 2.6.0+cu124
✅ transformers 4.51.3
✅ numpy 2.2.5
❌ datasets 없음
✅ accelerate 1.6.0
❌ peft 없음
(my_env) aiuser1@ai-smartlaw:~/workspace/ETU$ python -c "
import torch
print(f'✅ PyTorch {torch.__version__}')
print(f'CUDA available: {torch.cuda.is_available()}')
print(f'GPU count: {torch.cuda.device_count()}')
if torch.cuda.is_available():
    for i in range(torch.cuda.device_count()):
        print(f'GPU {i}: {torch.cuda.get_device_name(i)}')
"
✅ PyTorch 2.6.0+cu124
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
(my_env) aiuser1@ai-smartlaw:~/workspace/ETU$ cd ~/workspace/ETU
python -c "
from etu.unlearn import get_args
from etu.utils import load_model
print('✅ ETU 모듈 모두 정상 import됨')
> 
> ^C
(my_env) aiuser1@ai-smartlaw:~/workspace/ETU$ cd ~/workspace/ETU
(my_env) aiuser1@ai-smartlaw:~/workspace/ETU$ python -c "
from etu.unlearn import get_args
from etu.utils import load_model
print('✅ ETU 모듈 모두 정상 import됨')

# 기본 인자 확인
args = get_args()
print(f'기본 epsilon: {args.epsilon}')
print(f'기본 lambda_max: {args.lambda_max}')
"
Traceback (most recent call last):
  File "<string>", line 2, in <module>
  File "/data/aiuser1/workspace/ETU/etu/unlearn.py", line 14, in <module>
    from etu.utils import (
  File "/data/aiuser1/workspace/ETU/etu/utils.py", line 12, in <module>
    from datasets import load_dataset
ModuleNotFoundError: No module named 'datasets'
(my_env) aiuser1@ai-smartlaw:~/workspace/ETU$ ^C
