(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ nvidia-smi
Tue Sep  2 15:14:35 2025       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 570.158.01             Driver Version: 570.158.01     CUDA Version: 12.8     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA H200                    Off |   00000000:0A:00.0 Off |                    0 |
| N/A   30C    P0            122W /  700W |  130215MiB / 143771MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   1  NVIDIA H200                    Off |   00000000:18:00.0 Off |                    0 |
| N/A   26C    P0             78W /  700W |       0MiB / 143771MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   2  NVIDIA H200                    Off |   00000000:3B:00.0 Off |                    0 |
| N/A   25C    P0             74W /  700W |       0MiB / 143771MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   3  NVIDIA H200                    Off |   00000000:44:00.0 Off |                    0 |
| N/A   28C    P0             77W /  700W |       0MiB / 143771MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   4  NVIDIA H200                    Off |   00000000:87:00.0 Off |                    0 |
| N/A   28C    P0             77W /  700W |       0MiB / 143771MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   5  NVIDIA H200                    Off |   00000000:90:00.0 Off |                    0 |
| N/A   26C    P0             79W /  700W |       0MiB / 143771MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   6  NVIDIA H200                    Off |   00000000:B9:00.0 Off |                    0 |
| N/A   25C    P0             76W /  700W |       0MiB / 143771MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   7  NVIDIA H200                    Off |   00000000:C2:00.0 Off |                    0 |
| N/A   28C    P0             76W /  700W |       0MiB / 143771MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
                                                                                         
+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|    0   N/A  N/A         1117159      C   VLLM::EngineCore                      13020... |
+-----------------------------------------------------------------------------------------+
(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ sudo fuser -v /dev/nvidia*
[sudo] password for aiuser3: 
                     USER        PID ACCESS COMMAND
/dev/nvidia0:        aiuser1   1116621 F.... vllm
                     aiuser1   1117159 F...m VLLM::EngineCor
/dev/nvidia1:        aiuser1   1116621 F.... vllm
                     aiuser1   1117159 F.... VLLM::EngineCor
/dev/nvidia2:        aiuser1   1116621 F.... vllm
                     aiuser1   1117159 F.... VLLM::EngineCor
/dev/nvidia3:        aiuser1   1116621 F.... vllm
                     aiuser1   1117159 F.... VLLM::EngineCor
/dev/nvidia4:        aiuser1   1116621 F.... vllm
                     aiuser1   1117159 F.... VLLM::EngineCor
/dev/nvidia5:        aiuser1   1116621 F.... vllm
                     aiuser1   1117159 F.... VLLM::EngineCor
/dev/nvidia6:        aiuser1   1116621 F.... vllm
                     aiuser1   1117159 F.... VLLM::EngineCor
/dev/nvidia7:        aiuser1   1116621 F.... vllm
                     aiuser1   1117159 F.... VLLM::EngineCor
/dev/nvidiactl:      aiuser1   1116621 F.... vllm
                     aiuser1   1117159 F...m VLLM::EngineCor
/dev/nvidia-nvlink:  root       4334 F.... nv-fabricmanage
/dev/nvidia-nvswitch0:
                     root       4334 F.... nv-fabricmanage
/dev/nvidia-nvswitch1:
                     root       4334 F.... nv-fabricmanage
/dev/nvidia-nvswitch2:
                     root       4334 F.... nv-fabricmanage
/dev/nvidia-nvswitch3:
                     root       4334 F.... nv-fabricmanage
/dev/nvidia-uvm:     aiuser1   1116621 F.... vllm
                     aiuser1   1117159 F...m VLLM::EngineCor
(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ nvidia-smi
Tue Sep  2 15:15:08 2025       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 570.158.01             Driver Version: 570.158.01     CUDA Version: 12.8     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA H200                    Off |   00000000:0A:00.0 Off |                    0 |
| N/A   30C    P0            122W /  700W |  130215MiB / 143771MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   1  NVIDIA H200                    Off |   00000000:18:00.0 Off |                    0 |
| N/A   26C    P0             78W /  700W |       0MiB / 143771MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   2  NVIDIA H200                    Off |   00000000:3B:00.0 Off |                    0 |
| N/A   24C    P0             74W /  700W |       0MiB / 143771MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   3  NVIDIA H200                    Off |   00000000:44:00.0 Off |                    0 |
| N/A   27C    P0             77W /  700W |       0MiB / 143771MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   4  NVIDIA H200                    Off |   00000000:87:00.0 Off |                    0 |
| N/A   28C    P0             77W /  700W |       0MiB / 143771MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   5  NVIDIA H200                    Off |   00000000:90:00.0 Off |                    0 |
| N/A   26C    P0             79W /  700W |       0MiB / 143771MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   6  NVIDIA H200                    Off |   00000000:B9:00.0 Off |                    0 |
| N/A   25C    P0             76W /  700W |       0MiB / 143771MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   7  NVIDIA H200                    Off |   00000000:C2:00.0 Off |                    0 |
| N/A   28C    P0             76W /  700W |       0MiB / 143771MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
                                                                                         
+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|    0   N/A  N/A         1117159      C   VLLM::EngineCore                      13020... |
+-----------------------------------------------------------------------------------------+
(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ 
