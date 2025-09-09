Qwen 접속 정보 드립니다.

- Base URL: http://10.10.190.10:8124
- 인증 Key: token-abc123  (기존과 동일)
- Endpoint: /v1/chat/completions
- Model: Qwen3-32B

간단한 테스트용 예제 코드도 함께 공유드립니다.

### 샘플 코드 (Python)

import requests

API_BASE = "http://10.10.190.10:8124"
API_KEY = "token-abc123"

url = f"{API_BASE}/v1/chat/completions"
headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
data = {
    "model": "Qwen3-32B",
    "messages": [{"role": "user", "content": "Hello Qwen"}],
    "temperature": 0.2,
}

resp = requests.post(url, headers=headers, json=data, timeout=30)
print(resp.status_code)
print(resp.json())

### 샘플 (curl)

curl -X POST "http://10.10.190.10:8124/v1/chat/completions" \
  -H "Authorization: Bearer token-abc123" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "Qwen3-32B",
    "messages": [{"role":"user","content":"Hello Qwen"}],
    "temperature": 0.2
  }'

aiuser3@ai-smartlaw:~$ curl -X POST "http://10.10.190.10:8124/v1/chat/completions" \
  -H "Authorization: Bearer token-abc123" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "Qwen3-32B",
    "messages": [{"role":"user","content":"Hello Qwen"}],
    "temperature": 0.2
  }'
{"object":"error","message":"The model `Qwen3-32B` does not exist.","type":"NotFoundError","param":null,"code":404}aiuser3@ai-smartlaw:~$ 


C:\Users\sungwon.chae\Desktop\kars-workspace

성원님 혹시 KARS 테케 만든거 LTT 서버에 파일로 올려줄 수 있어요?? 파일 형식은 상관없는데, filter만 실제 weaviate이 받아야 하는 형태로 변환해서요!!! 

아 그리구 저거 테케가 무조건 답이 있는 경우만 봐야하는거라...,...,., 혹시 시간나면 저 쿼리 돌렸을때 무조건 뭐가 나온다는것만 좀 보장 가능할까요ㅠ 

The terminal process failed to launch: Access was denied to the path containing your executable "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe". Manage and change your permissions to get this to work.
