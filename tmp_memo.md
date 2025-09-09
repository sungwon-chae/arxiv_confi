aiuser3@ai-smartlaw:~$ lsof -i -P -n | grep LISTEN
code-fabd 2359204 aiuser3    9u  IPv4 69758669      0t0  TCP 127.0.0.1:41255 (LISTEN)
aiuser3@ai-smartlaw:~$ ps -ef | grep -E "vllm|api_server|openai" | grep -v grep
aiuser1  1739450  405874  0 Sep05 pts/13   00:00:14 /data/aiuser1/my_env/bin/python3.11 /data/aiuser1/my_env/bin/vllm serve /data/models_ckpt/Qwen3-32B --port 8124 --api-key token-abc123 --trust-remote-code --dtype bfloat16 --gpu-memory-utilization 0.9 --enable-auto-tool-choice --tool-call-parser hermes --tensor-parallel-size 2
aiuser1  1739881  405874  0 Sep05 pts/13   00:02:03 /data/aiuser1/my_env/bin/python3.11 /data/aiuser1/my_env/bin/vllm serve /data/models/Qwen3-32B --port 8124 --api-key token-abc123 --trust-remote-code --dtype bfloat16 --gpu-memory-utilization 0.9 --enable-auto-tool-choice --tool-call-parser hermes --tensor-parallel-size 2
aiuser1  1744154 1741765  0 Sep05 pts/17   00:01:57 /data/aiuser1/my_env_py312/bin/python3 /data/aiuser1/my_env_py312/bin/vllm serve google/gemma-3-270m-it --port 8125 --api-key token-abc123 --trust-remote-code --dtype bfloat16 --gpu-memory-utilization 0.9 --tensor-parallel-size 1
aiuser3@ai-smartlaw:~$ tr '\0' ' ' < /proc/1739450/cmdline | sed 's/ /\n/g' | grep -E -- '--port|--host|--model'
--port
aiuser3@ai-smartlaw:~$ ss -ltn | grep 8124
LISTEN 0      2048         0.0.0.0:8124       0.0.0.0:*          
aiuser3@ai-smartlaw:~$ hostname -I | awk '{print $1}'
10.10.190.10
aiuser3@ai-smartlaw:~$ 





C:\Users\sungwon.chae\Desktop\kars-workspace

성원님 혹시 KARS 테케 만든거 LTT 서버에 파일로 올려줄 수 있어요?? 파일 형식은 상관없는데, filter만 실제 weaviate이 받아야 하는 형태로 변환해서요!!! 

아 그리구 저거 테케가 무조건 답이 있는 경우만 봐야하는거라...,...,., 혹시 시간나면 저 쿼리 돌렸을때 무조건 뭐가 나온다는것만 좀 보장 가능할까요ㅠ 

The terminal process failed to launch: Access was denied to the path containing your executable "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe". Manage and change your permissions to get this to work.
