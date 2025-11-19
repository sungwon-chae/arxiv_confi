# Qwen3-Next-80B-A3B-Instruct Chatbot

vLLM을 사용한 Qwen3-Next-80B-A3B-Instruct 모델 기반 채팅봇입니다.

## 구성

- **vLLM 서버**: GPU 6,7번에서 실행되는 모델 서버
- **FastAPI 서버**: vLLM과 Streamlit 사이의 중간 API 서버
- **Streamlit 앱**: 웹 기반 채팅 인터페이스

## 사전 요구사항

1. vLLM 서버가 실행 중이어야 합니다:
```bash
CUDA_VISIBLE_DEVICES=6,7 python -m vllm.entrypoints.openai.api_server --model /data/models/Qwen3-Next-80B-A3B-Instruct --host 0.0.0.0 --port 8000
```

2. 필요한 패키지 설치:
```bash
pip install -r requirements.txt
```

## 실행 방법

### 방법 1: 통합 실행 (권장)
```bash
chmod +x run_all.sh
./run_all.sh
```

### 방법 2: 개별 실행

1. FastAPI 서버 시작:
```bash
chmod +x start_chat.sh
./start_chat.sh
```

2. 다른 터미널에서 Streamlit 앱 시작:
```bash
chmod +x start_streamlit.sh
./start_streamlit.sh
```

## 접속

- **Streamlit 앱**: http://localhost:8501
- **FastAPI 서버**: http://localhost:8001
- **vLLM 서버**: http://localhost:8000
