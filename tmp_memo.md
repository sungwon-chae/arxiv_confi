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

Do you want to continue? [Y/n] y
0% [Waiting for headers]
0% [Waiting for headers]Y
Ign:1 http://mirror.kakao.com/ubuntu noble/universe amd64 python3-lib2to3 all 3.12.3-0ubuntu1
Ign:2 http://mirror.kakao.com/ubuntu noble-updates/universe amd64 2to3 all 3.12.3-0ubuntu2
Ign:3 http://mirror.kakao.com/ubuntu noble/main amd64 tk8.6-blt2.5 amd64 2.5.3+dfsg-7build1
Ign:4 http://mirror.kakao.com/ubuntu noble/main amd64 blt amd64 2.5.3+dfsg-7build1
Ign:5 http://mirror.kakao.com/ubuntu noble/main amd64 fonts-mathjax all 2.7.9+dfsg-1
Ign:6 http://mirror.kakao.com/ubuntu noble/main amd64 python3-tk amd64 3.12.3-0ubuntu1
Ign:7 http://mirror.kakao.com/ubuntu noble/main amd64 libjs-mathjax all 2.7.9+dfsg-1
Ign:8 http://mirror.kakao.com/ubuntu noble-updates/universe amd64 idle-python3.12 all 3.12.3-1ubuntu0.7
Ign:9 http://mirror.kakao.com/ubuntu noble-updates/universe amd64 idle all 3.12.3-0ubuntu2
Ign:10 http://mirror.kakao.com/ubuntu noble-updates/universe amd64 libpython3.12-testsuite all 3.12.3-1ubuntu0.7
Ign:11 http://mirror.kakao.com/ubuntu noble-updates/main amd64 python3.12-doc all 3.12.3-1ubuntu0.7
Ign:12 http://mirror.kakao.com/ubuntu noble-updates/main amd64 python3-doc all 3.12.3-0ubuntu2
Ign:13 http://mirror.kakao.com/ubuntu noble-updates/main amd64 python3.12-examples all 3.12.3-1ubuntu0.7
Ign:14 http://mirror.kakao.com/ubuntu noble-updates/main amd64 python3-examples all 3.12.3-0ubuntu2
Ign:15 http://mirror.kakao.com/ubuntu noble-updates/universe amd64 python3.12-full amd64 3.12.3-1ubuntu0.7
Ign:16 http://mirror.kakao.com/ubuntu noble-updates/universe amd64 python3-full amd64 3.12.3-0ubuntu2
Ign:1 http://mirror.kakao.com/ubuntu noble/universe amd64 python3-lib2to3 all 3.12.3-0ubuntu1
Ign:2 http://mirror.kakao.com/ubuntu noble-updates/universe amd64 2to3 all 3.12.3-0ubuntu2
Ign:3 http://mirror.kakao.com/ubuntu noble/main amd64 tk8.6-blt2.5 amd64 2.5.3+dfsg-7build1
Ign:4 http://mirror.kakao.com/ubuntu noble/main amd64 blt amd64 2.5.3+dfsg-7build1
Ign:5 http://mirror.kakao.com/ubuntu noble/main amd64 fonts-mathjax all 2.7.9+dfsg-1
Ign:6 http://mirror.kakao.com/ubuntu noble/main amd64 python3-tk amd64 3.12.3-0ubuntu1
Ign:7 http://mirror.kakao.com/ubuntu noble/main amd64 libjs-mathjax all 2.7.9+dfsg-1
Ign:8 http://mirror.kakao.com/ubuntu noble-updates/universe amd64 idle-python3.12 all 3.12.3-1ubuntu0.7
Ign:9 http://mirror.kakao.com/ubuntu noble-updates/universe amd64 idle all 3.12.3-0ubuntu2
Ign:10 http://mirror.kakao.com/ubuntu noble-updates/universe amd64 libpython3.12-testsuite all 3.12.3-1ubuntu0.7
Ign:11 http://mirror.kakao.com/ubuntu noble-updates/main amd64 python3.12-doc all 3.12.3-1ubuntu0.7
Ign:12 http://mirror.kakao.com/ubuntu noble-updates/main amd64 python3-doc all 3.12.3-0ubuntu2
Ign:13 http://mirror.kakao.com/ubuntu noble-updates/main amd64 python3.12-examples all 3.12.3-1ubuntu0.7
Ign:14 http://mirror.kakao.com/ubuntu noble-updates/main amd64 python3-examples all 3.12.3-0ubuntu2
Ign:15 http://mirror.kakao.com/ubuntu noble-updates/universe amd64 python3.12-full amd64 3.12.3-1ubuntu0.7
Ign:16 http://mirror.kakao.com/ubuntu noble-updates/universe amd64 python3-full amd64 3.12.3-0ubuntu2
Ign:1 http://mirror.kakao.com/ubuntu noble/universe amd64 python3-lib2to3 all 3.12.3-0ubuntu1
Ign:2 http://mirror.kakao.com/ubuntu noble-updates/universe amd64 2to3 all 3.12.3-0ubuntu2
Ign:3 http://mirror.kakao.com/ubuntu noble/main amd64 tk8.6-blt2.5 amd64 2.5.3+dfsg-7build1
Ign:4 http://mirror.kakao.com/ubuntu noble/main amd64 blt amd64 2.5.3+dfsg-7build1
Ign:5 http://mirror.kakao.com/ubuntu noble/main amd64 fonts-mathjax all 2.7.9+dfsg-1
Ign:6 http://mirror.kakao.com/ubuntu noble/main amd64 python3-tk amd64 3.12.3-0ubuntu1
Ign:7 http://mirror.kakao.com/ubuntu noble/main amd64 libjs-mathjax all 2.7.9+dfsg-1
Ign:8 http://mirror.kakao.com/ubuntu noble-updates/universe amd64 idle-python3.12 all 3.12.3-1ubuntu0.7
Ign:9 http://mirror.kakao.com/ubuntu noble-updates/universe amd64 idle all 3.12.3-0ubuntu2
Ign:10 http://mirror.kakao.com/ubuntu noble-updates/universe amd64 libpython3.12-testsuite all 3.12.3-1ubuntu0.7
Ign:11 http://mirror.kakao.com/ubuntu noble-updates/main amd64 python3.12-doc all 3.12.3-1ubuntu0.7
Ign:12 http://mirror.kakao.com/ubuntu noble-updates/main amd64 python3-doc all 3.12.3-0ubuntu2
Ign:13 http://mirror.kakao.com/ubuntu noble-updates/main amd64 python3.12-examples all 3.12.3-1ubuntu0.7
Ign:14 http://mirror.kakao.com/ubuntu noble-updates/main amd64 python3-examples all 3.12.3-0ubuntu2
Ign:15 http://mirror.kakao.com/ubuntu noble-updates/universe amd64 python3.12-full amd64 3.12.3-1ubuntu0.7
Ign:16 http://mirror.kakao.com/ubuntu noble-updates/universe amd64 python3-full amd64 3.12.3-0ubuntu2
Err:1 http://mirror.kakao.com/ubuntu noble/universe amd64 python3-lib2to3 all 3.12.3-0ubuntu1
  Connection failed [IP: 113.29.189.165 80]
Err:2 http://mirror.kakao.com/ubuntu noble-updates/universe amd64 2to3 all 3.12.3-0ubuntu2
  Connection failed [IP: 113.29.189.165 80]
Err:3 http://mirror.kakao.com/ubuntu noble/main amd64 tk8.6-blt2.5 amd64 2.5.3+dfsg-7build1
  Connection failed [IP: 113.29.189.165 80]
Err:4 http://mirror.kakao.com/ubuntu noble/main amd64 blt amd64 2.5.3+dfsg-7build1
  Connection failed [IP: 113.29.189.165 80]
Err:5 http://mirror.kakao.com/ubuntu noble/main amd64 fonts-mathjax all 2.7.9+dfsg-1
  Connection failed [IP: 113.29.189.165 80]
Err:6 http://mirror.kakao.com/ubuntu noble/main amd64 python3-tk amd64 3.12.3-0ubuntu1
  Connection failed [IP: 113.29.189.165 80]
Err:7 http://mirror.kakao.com/ubuntu noble/main amd64 libjs-mathjax all 2.7.9+dfsg-1
  Connection failed [IP: 113.29.189.165 80]
Ign:8 http://mirror.kakao.com/ubuntu noble-updates/universe amd64 idle-python3.12 all 3.12.3-1ubuntu0.7
Err:9 http://mirror.kakao.com/ubuntu noble-updates/universe amd64 idle all 3.12.3-0ubuntu2
  Connection failed [IP: 113.29.189.165 80]
Err:8 http://security.ubuntu.com/ubuntu noble-updates/universe amd64 idle-python3.12 all 3.12.3-1ubuntu0.7
  Connection failed [IP: 113.29.189.165 80]
Ign:10 http://mirror.kakao.com/ubuntu noble-updates/universe amd64 libpython3.12-testsuite all 3.12.3-1ubuntu0.7
Ign:11 http://mirror.kakao.com/ubuntu noble-updates/main amd64 python3.12-doc all 3.12.3-1ubuntu0.7      
Err:10 http://security.ubuntu.com/ubuntu noble-updates/universe amd64 libpython3.12-testsuite all 3.12.3-1ubuntu0.7
  Connection failed [IP: 113.29.189.165 80]
Err:11 http://security.ubuntu.com/ubuntu noble-updates/main amd64 python3.12-doc all 3.12.3-1ubuntu0.7
  Connection failed [IP: 113.29.189.165 80]
Err:12 http://mirror.kakao.com/ubuntu noble-updates/main amd64 python3-doc all 3.12.3-0ubuntu2
  Connection failed [IP: 113.29.189.165 80]
Ign:13 http://mirror.kakao.com/ubuntu noble-updates/main amd64 python3.12-examples all 3.12.3-1ubuntu0.7
Err:13 http://security.ubuntu.com/ubuntu noble-updates/main amd64 python3.12-examples all 3.12.3-1ubuntu0.7
  Connection failed [IP: 113.29.189.165 80]
Err:14 http://mirror.kakao.com/ubuntu noble-updates/main amd64 python3-examples all 3.12.3-0ubuntu2
  Connection failed [IP: 113.29.189.165 80]
Ign:15 http://mirror.kakao.com/ubuntu noble-updates/universe amd64 python3.12-full amd64 3.12.3-1ubuntu0.7
Err:15 http://security.ubuntu.com/ubuntu noble-updates/universe amd64 python3.12-full amd64 3.12.3-1ubuntu0.7
  Connection failed [IP: 113.29.189.165 80]
Err:16 http://mirror.kakao.com/ubuntu noble-updates/universe amd64 python3-full amd64 3.12.3-0ubuntu2
  Connection failed [IP: 113.29.189.165 80]
E: Failed to fetch http://mirror.kakao.com/ubuntu/pool/universe/p/python3-stdlib-extensions/python3-lib2to3_3.12.3-0ubuntu1_all.deb  Connection failed [IP: 113.29.189.165 80]
E: Failed to fetch http://mirror.kakao.com/ubuntu/pool/universe/p/python3-defaults/2to3_3.12.3-0ubuntu2_all.deb  Connection failed [IP: 113.29.189.165 80]
E: Failed to fetch http://mirror.kakao.com/ubuntu/pool/main/b/blt/tk8.6-blt2.5_2.5.3%2bdfsg-7build1_amd64.deb  Connection failed [IP: 113.29.189.165 80]
E: Failed to fetch http://mirror.kakao.com/ubuntu/pool/main/b/blt/blt_2.5.3%2bdfsg-7build1_amd64.deb  Connection failed [IP: 113.29.189.165 80]
E: Failed to fetch http://mirror.kakao.com/ubuntu/pool/main/m/mathjax/fonts-mathjax_2.7.9%2bdfsg-1_all.deb  Connection failed [IP: 113.29.189.165 80]
E: Failed to fetch http://mirror.kakao.com/ubuntu/pool/main/p/python3-stdlib-extensions/python3-tk_3.12.3-0ubuntu1_amd64.deb  Connection failed [IP: 113.29.189.165 80]
E: Failed to fetch http://mirror.kakao.com/ubuntu/pool/main/m/mathjax/libjs-mathjax_2.7.9%2bdfsg-1_all.deb  Connection failed [IP: 113.29.189.165 80]
E: Failed to fetch http://security.ubuntu.com/ubuntu/pool/universe/p/python3.12/idle-python3.12_3.12.3-1ubuntu0.7_all.deb  Connection failed [IP: 113.29.189.165 80]
E: Failed to fetch http://mirror.kakao.com/ubuntu/pool/universe/p/python3-defaults/idle_3.12.3-0ubuntu2_all.deb  Connection failed [IP: 113.29.189.165 80]
E: Failed to fetch http://security.ubuntu.com/ubuntu/pool/universe/p/python3.12/libpython3.12-testsuite_3.12.3-1ubuntu0.7_all.deb  Connection failed [IP: 113.29.189.165 80]
E: Failed to fetch http://security.ubuntu.com/ubuntu/pool/main/p/python3.12/python3.12-doc_3.12.3-1ubuntu0.7_all.deb  Connection failed [IP: 113.29.189.165 80]
E: Failed to fetch http://mirror.kakao.com/ubuntu/pool/main/p/python3-defaults/python3-doc_3.12.3-0ubuntu2_all.deb  Connection failed [IP: 113.29.189.165 80]
E: Failed to fetch http://security.ubuntu.com/ubuntu/pool/main/p/python3.12/python3.12-examples_3.12.3-1ubuntu0.7_all.deb  Connection failed [IP: 113.29.189.165 80]
E: Failed to fetch http://mirror.kakao.com/ubuntu/pool/main/p/python3-defaults/python3-examples_3.12.3-0ubuntu2_all.deb  Connection failed [IP: 113.29.189.165 80]
E: Failed to fetch http://security.ubuntu.com/ubuntu/pool/universe/p/python3.12/python3.12-full_3.12.3-1ubuntu0.7_amd64.deb  Connection failed [IP: 113.29.189.165 80]
E: Failed to fetch http://mirror.kakao.com/ubuntu/pool/universe/p/python3-defaults/python3-full_3.12.3-0ubuntu2_amd64.deb  Connection failed [IP: 113.29.189.165 80]
E: Unable to fetch some archives, maybe run apt-get update or try with --fix-missing?
aiuser1@ai-smartlaw:~/workspace/ETU$ nvidia -smi
WARNING:root:could not open file '/etc/apt/sources.list.d/sdcss.list': [Errno 13] Permission denied: '/etc/apt/sources.list.d/sdcss.list'

nvidia: command not found
aiuser1@ai-smartlaw:~/workspace/ETU$ nvidia-smi
Mon Sep  1 16:36:14 2025       
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
| N/A   30C    P0            123W /  700W |       0MiB / 143771MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   2  NVIDIA H200                    Off |   00000000:3B:00.0 Off |                    0 |
| N/A   28C    P0            113W /  700W |       0MiB / 143771MiB |      0%      Default |
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
| N/A   30C    P0            121W /  700W |       0MiB / 143771MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   6  NVIDIA H200                    Off |   00000000:B9:00.0 Off |                    0 |
| N/A   29C    P0            116W /  700W |       0MiB / 143771MiB |      0%      Default |
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
aiuser1@ai-smartlaw:~/workspace/ETU$ ps aux | grep apt
aiuser1   739694  0.0  0.0   6544  1536 pts/18   S+   16:36   0:00 grep apt
aiuser1@ai-smartlaw:~/workspace/ETU$ ps aux | grep dpkg
aiuser1   739750  0.0  0.0   6544  1536 pts/18   S+   16:36   0:00 grep dpkg

