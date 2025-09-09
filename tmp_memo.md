aiuser3@ai-smartlaw:~$ nvidia-smi
Tue Sep  9 13:08:12 2025       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 570.158.01             Driver Version: 570.158.01     CUDA Version: 12.8     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA H200                    Off |   00000000:0A:00.0 Off |                    0 |
| N/A   30C    P0            121W /  700W |  130429MiB / 143771MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   1  NVIDIA H200                    Off |   00000000:18:00.0 Off |                    0 |
| N/A   28C    P0            121W /  700W |  130429MiB / 143771MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   2  NVIDIA H200                    Off |   00000000:3B:00.0 Off |                    0 |
| N/A   24C    P0             74W /  700W |       4MiB / 143771MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   3  NVIDIA H200                    Off |   00000000:44:00.0 Off |                    0 |
| N/A   31C    P0            118W /  700W |  130003MiB / 143771MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   4  NVIDIA H200                    Off |   00000000:87:00.0 Off |                    0 |
| N/A   27C    P0             77W /  700W |       4MiB / 143771MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   5  NVIDIA H200                    Off |   00000000:90:00.0 Off |                    0 |
| N/A   26C    P0             78W /  700W |       4MiB / 143771MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   6  NVIDIA H200                    Off |   00000000:B9:00.0 Off |                    0 |
| N/A   25C    P0             76W /  700W |       4MiB / 143771MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   7  NVIDIA H200                    Off |   00000000:C2:00.0 Off |                    0 |
| N/A   27C    P0             76W /  700W |       4MiB / 143771MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
                                                                                         
+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|    0   N/A  N/A         1740209      C   ...aiuser1/my_env/bin/python3.11      13042... |
|    1   N/A  N/A         1740210      C   ...aiuser1/my_env/bin/python3.11      13042... |
|    3   N/A  N/A         1744542      C   VLLM::EngineCore                      12999... |
+-----------------------------------------------------------------------------------------+
aiuser3@ai-smartlaw:~$ lsof -i -P -n | grep LISTEN
code-fabd 2359204 aiuser3    9u  IPv4 69758669      0t0  TCP 127.0.0.1:41255 (LISTEN)
aiuser3@ai-smartlaw:~$ 


C:\Users\sungwon.chae\Desktop\kars-workspace

성원님 혹시 KARS 테케 만든거 LTT 서버에 파일로 올려줄 수 있어요?? 파일 형식은 상관없는데, filter만 실제 weaviate이 받아야 하는 형태로 변환해서요!!! 

아 그리구 저거 테케가 무조건 답이 있는 경우만 봐야하는거라...,...,., 혹시 시간나면 저 쿼리 돌렸을때 무조건 뭐가 나온다는것만 좀 보장 가능할까요ㅠ 

The terminal process failed to launch: Access was denied to the path containing your executable "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe". Manage and change your permissions to get this to work.
