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


(my_env) aiuser1@ai-smartlaw:~/workspace/ETU$ pip install datasets peft
WARNING: Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1016)'))': /simple/datasets/
WARNING: Retrying (Retry(total=3, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1016)'))': /simple/datasets/
WARNING: Retrying (Retry(total=2, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1016)'))': /simple/datasets/
WARNING: Retrying (Retry(total=1, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1016)'))': /simple/datasets/
WARNING: Retrying (Retry(total=0, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1016)'))': /simple/datasets/
Could not fetch URL https://pypi.org/simple/datasets/: There was a problem confirming the ssl certificate: HTTPSConnectionPool(host='pypi.org', port=443): Max retries exceeded with url: /simple/datasets/ (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1016)'))) - skipping
ERROR: Could not find a version that satisfies the requirement datasets (from versions: none)
Could not fetch URL https://pypi.org/simple/pip/: There was a problem confirming the ssl certificate: HTTPSConnectionPool(host='pypi.org', port=443): Max retries exceeded with url: /simple/pip/ (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1016)'))) - skipping
ERROR: No matching distribution found for datasets
(my_env) aiuser1@ai-smartlaw:~/workspace/ETU$ python benchmark_8gpu.py
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
GPU 0 메모리 대역폭: 2154.76 GB/s
GPU 1 메모리 대역폭: 2548.47 GB/s
GPU 2 메모리 대역폭: 2547.81 GB/s
GPU 3 메모리 대역폭: 2545.10 GB/s
GPU 4 메모리 대역폭: 2549.66 GB/s
GPU 5 메모리 대역폭: 2549.09 GB/s
GPU 6 메모리 대역폭: 2550.14 GB/s
GPU 7 메모리 대역폭: 2550.67 GB/s

🔢 연산 성능 벤치마크 시작...
GPU 0 연산 성능: 51164.32 GFLOPS
GPU 1 연산 성능: 51261.41 GFLOPS
GPU 2 연산 성능: 51312.34 GFLOPS
GPU 3 연산 성능: 51287.32 GFLOPS
GPU 4 연산 성능: 51307.18 GFLOPS
GPU 5 연산 성능: 51306.95 GFLOPS
GPU 6 연산 성능: 51319.28 GFLOPS
GPU 7 연산 성능: 51302.34 GFLOPS

🔄 멀티 GPU 스케일링 벤치마크 시작...
  1대 GPU 테스트...
    1대 GPU 효율성: 279.752
  2대 GPU 테스트...
    2대 GPU 효율성: 7.729
  3대 GPU 테스트...
    3대 GPU 효율성: 3.971
  4대 GPU 테스트...
    4대 GPU 효율성: 2.406
  5대 GPU 테스트...
    5대 GPU 효율성: 1.616
  6대 GPU 테스트...
    6대 GPU 효율성: 1.167
  7대 GPU 테스트...
    7대 GPU 효율성: 0.897
  8대 GPU 테스트...
    8대 GPU 효율성: 0.692

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
평균 메모리 대역폭: 2499.46 GB/s
평균 연산 성능: 51282.64 GFLOPS
평균 멀티 GPU 효율성: 37.279
============================================================
📝 벤치마크 결과 저장됨: h200_benchmark_20250901_165154.json






aiuser3@ai-smartlaw:~/LLM_EvalPipeline_test$ cd
aiuser3@ai-smartlaw:~$ whoami
aiuser3
aiuser3@ai-smartlaw:~$ pwd
/data/aiuser3
aiuser3@ai-smartlaw:~$ ls -la
total 1112
drwxr-x--- 13 aiuser3 aiuser3   4096 Sep  1 18:50 .
drwxr-xr-x 11 root    root      4096 Aug 19 13:45 ..
-rw-------  1 aiuser3 aiuser3  13270 Aug 25 12:54 .bash_history
-rw-r--r--  1 aiuser3 aiuser3    220 Jul 29 16:51 .bash_logout
-rw-r--r--  1 aiuser3 aiuser3   3771 Jul 29 16:51 .bashrc
drwx------  8 aiuser3 aiuser3   4096 Aug 13 14:56 .cache
drwxrwxr-x  4 aiuser3 aiuser3   4096 Aug 13 14:53 .config
drwxrwxr-x  5 aiuser3 aiuser3   4096 Sep  1 17:23 .cursor-server
drwxrwxr-x  3 aiuser3 aiuser3   4096 Aug 13 14:21 .dotnet
-rw-rw-r--  1 aiuser3 aiuser3 998146 Sep  1 18:50 ETU-h200-complete.tar.gz
drwxrwxr-x  9 aiuser3 aiuser3   4096 Aug 21 08:51 LLM_EvalPipeline_test
drwxrwxr-x  4 aiuser3 aiuser3   4096 Aug 13 14:38 .local
drwxrwxr-x  3 aiuser3 aiuser3   4096 Aug 13 17:18 nltk_data
drwx------  3 aiuser3 aiuser3   4096 Aug 13 14:53 .nv
-rw-r--r--  1 aiuser3 aiuser3    807 Jul 29 16:51 .profile
-rw-------  1 aiuser3 aiuser3    619 Aug 19 13:45 .python_history
drwx------  2 aiuser3 aiuser3   4096 Aug 19 11:35 .ssh
-rw-r--r--  1 aiuser3 aiuser3      0 Jul 29 17:40 .sudo_as_admin_successful
drwxrwxr-x  3 aiuser3 aiuser3   4096 Aug 13 14:53 .triton
drwxr-x---  5 aiuser3 aiuser3   4096 Sep  1 18:49 .vscode-server
-rw-rw-r--  1 aiuser3 aiuser3  50552 Aug 14 09:43 .zcompdump
aiuser3@ai-smartlaw:~$ python3 --version
Python 3.12.3
aiuser3@ai-smartlaw:~$ which python3
/usr/bin/python3
aiuser3@ai-smartlaw:~$ tar -xzf ETU-h200-complete.tar.gz
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
aiuser3@ai-smartlaw:~$ cd ETU
aiuser3@ai-smartlaw:~/ETU$ ls -la
total 50
drwxr-xr-x  7 aiuser3 aiuser3   4096 Sep  1 14:23 .
drwxr-x--- 14 aiuser3 aiuser3   4096 Sep  1 18:55 ..
-rwxr-xr-x  1 aiuser3 aiuser3    163 Sep  1 14:22 ._benchmark_8gpu.py
-rwxr-xr-x  1 aiuser3 aiuser3   9477 Sep  1 14:22 benchmark_8gpu.py
-rw-r--r--  1 aiuser3 aiuser3    163 Sep  1 14:23 ._config_8gpu.yaml
-rw-r--r--  1 aiuser3 aiuser3   1868 Sep  1 14:23 config_8gpu.yaml
-rwxr-xr-x  1 aiuser3 aiuser3    163 Aug 14 09:10 ._data
drwxr-xr-x  2 aiuser3 aiuser3   4096 Sep  1 18:55 data
-rwxr-xr-x  1 aiuser3 aiuser3    163 Sep  1 13:27 ._etu
drwxr-xr-x  3 aiuser3 aiuser3   4096 Sep  1 18:55 etu
-rwxr-xr-x  1 aiuser3 aiuser3    163 Sep  1 14:23 ._.git
drwxr-xr-x  7 aiuser3 aiuser3   4096 Sep  1 18:55 .git
-rw-r--r--  1 aiuser3 aiuser3    163 Sep  1 13:46 ._.gitignore
-rw-r--r--  1 aiuser3 aiuser3   1974 Sep  1 13:46 .gitignore
-rwxr-xr-x  1 aiuser3 aiuser3    163 Aug 14 09:10 ._images
drwxr-xr-x  2 aiuser3 aiuser3   4096 Sep  1 18:55 images
-rw-r--r--  1 aiuser3 aiuser3    163 Aug 14 09:10 ._LICENSE
-rw-r--r--  1 aiuser3 aiuser3   1074 Aug 14 09:10 LICENSE
-rwxr-xr-x  1 aiuser3 aiuser3    163 Sep  1 14:16 ._monitor_h200.py
-rwxr-xr-x  1 aiuser3 aiuser3   6514 Sep  1 14:16 monitor_h200.py
-rwxr-xr-x  1 aiuser3 aiuser3    163 Sep  1 13:31 .___pycache__
drwxr-xr-x  2 aiuser3 aiuser3   4096 Sep  1 18:55 __pycache__
-rw-r--r--  1 aiuser3 aiuser3    163 Sep  1 14:16 ._README.md
-rw-r--r--  1 aiuser3 aiuser3  21290 Sep  1 14:16 README.md
-rw-r--r--  1 aiuser3 aiuser3    163 Sep  1 10:43 ._requirements.txt
-rw-r--r--  1 aiuser3 aiuser3    103 Sep  1 10:43 requirements.txt
-rwxr-xr-x  1 aiuser3 aiuser3    163 Sep  1 14:14 ._run_etu_h200.py
-rwxr-xr-x  1 aiuser3 aiuser3   5309 Sep  1 14:14 run_etu_h200.py
-rw-r--r--  1 aiuser3 aiuser3    163 Sep  1 10:44 ._run_etu_lora.py
-rw-r--r--  1 aiuser3 aiuser3   2617 Sep  1 10:44 run_etu_lora.py
-rw-r--r--  1 aiuser3 aiuser3    163 Aug 14 09:10 ._run_etu_mixtral.ipynb
-rw-r--r--  1 aiuser3 aiuser3 121830 Aug 14 09:10 run_etu_mixtral.ipynb
-rwxr-xr-x  1 aiuser3 aiuser3    163 Sep  1 14:21 ._run_etu_multi_h200.py
-rwxr-xr-x  1 aiuser3 aiuser3   8616 Sep  1 14:21 run_etu_multi_h200.py
-rw-r--r--  1 aiuser3 aiuser3    163 Sep  1 14:14 ._run_etu.py
-rw-r--r--  1 aiuser3 aiuser3   2572 Sep  1 14:14 run_etu.py
-rw-r--r--  1 aiuser3 aiuser3    163 Aug 14 09:10 ._run_etu_yi.ipynb
-rw-r--r--  1 aiuser3 aiuser3 185053 Aug 14 09:10 run_etu_yi.ipynb
-rw-r--r--  1 aiuser3 aiuser3    163 Aug 14 09:10 ._run_etu_zephyr.ipynb
-rw-r--r--  1 aiuser3 aiuser3 114184 Aug 14 09:10 run_etu_zephyr.ipynb
-rwxr-xr-x  1 aiuser3 aiuser3    163 Sep  1 14:15 ._run_hyperparameter_sweep.sh
-rwxr-xr-x  1 aiuser3 aiuser3   3153 Sep  1 14:15 run_hyperparameter_sweep.sh
-rwxr-xr-x  1 aiuser3 aiuser3    163 Sep  1 14:22 ._run_large_model_experiments.sh
-rwxr-xr-x  1 aiuser3 aiuser3   2575 Sep  1 14:22 run_large_model_experiments.sh
-rwxr-xr-x  1 aiuser3 aiuser3    163 Sep  1 14:15 ._run_paper_experiments.sh
-rwxr-xr-x  1 aiuser3 aiuser3   2419 Sep  1 14:15 run_paper_experiments.sh
-rw-r--r--  1 aiuser3 aiuser3    163 Sep  1 14:04 ._safeguards.txt
-rw-r--r--  1 aiuser3 aiuser3   4330 Sep  1 14:04 safeguards.txt
-rw-r--r--  1 aiuser3 aiuser3    163 Sep  1 13:26 ._test_math.py
-rw-r--r--  1 aiuser3 aiuser3   2281 Sep  1 13:26 test_math.py
aiuser3@ai-smartlaw:~/ETU$ cd
aiuser3@ai-smartlaw:~$ find ~ -name "*venv*" -type d 2>\dev\null
/data/aiuser3/LLM_EvalPipeline_test/.venv
/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/mypy/typeshed/stdlib/venv
aiuser3@ai-smartlaw:~$ 
