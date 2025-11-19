#!/bin/bash

echo "=== Qwen3-Next-80B-A3B-Instruct Chatbot 시작 ==="
echo ""

if [ -f ".env" ]; then
    echo ".env 파일에서 환경변수 로드 중..."
    export $(grep -v '^#' .env | xargs)
else
    echo "⚠️  .env 파일이 없습니다. 기본값을 사용합니다."
fi

echo "환경변수 설정 완료:"
echo "- vLLM 서버: $LLM_API_BASE"
echo "- 모델: $LLM_MODEL"
echo "- FastAPI 서버: $BACKEND_URL"
echo "- Swagger UI: $BACKEND_URL/docs"
echo "- Streamlit: http://localhost:8501"
echo ""

# vLLM 서버 상태 확인
echo "vLLM 서버 상태 확인 중..."
if curl -s "$LLM_API_BASE/health" > /dev/null; then
    echo "✅ vLLM 서버가 실행 중입니다."
else
    echo "❌ vLLM 서버가 실행되지 않았습니다."
    echo "다음 명령어로 vLLM 서버를 먼저 시작하세요:"
    echo "CUDA_VISIBLE_DEVICES=6,7 python -m vllm.entrypoints.openai.api_server --model /data/models/Qwen3-Next-80B-A3B-Instruct --host 0.0.0.0 --port 8000 --tensor-parallel-size 2"
    exit 1
fi

echo ""
echo "기존 FastAPI 서버 확인 중..."
EXISTING_PID=$(lsof -ti:8001 2>/dev/null)
if [ ! -z "$EXISTING_PID" ]; then
    echo "기존 서버(PID: $EXISTING_PID) 종료 중..."
    kill $EXISTING_PID 2>/dev/null
    sleep 2
fi

echo "FastAPI 서버 시작 중... (백그라운드)"
cd /data/aiuser3/LegalAI-DataPipeline/buyer_seller/chat
source ../../.venv/bin/activate
nohup uvicorn server_langgraph:app --host 0.0.0.0 --port 8001 --reload --log-level warning > fastapi.log 2>&1 &
FASTAPI_PID=$!

# FastAPI 서버 시작 대기
echo "FastAPI 서버 시작 대기 중..."
sleep 5

if curl -s "$BACKEND_URL/health" > /dev/null; then
    echo "✅ FastAPI 서버가 시작되었습니다."
else
    echo "❌ FastAPI 서버 시작 실패. 로그를 확인하세요: cat fastapi.log"
    exit 1
fi

echo ""
echo "Streamlit 앱 시작 중..."
echo "브라우저에서 http://localhost:8501 에 접속하세요."
echo ""
echo "종료하려면 Ctrl+C를 누르세요."

# Streamlit 실행
cd /data/aiuser3/LegalAI-DataPipeline/buyer_seller/chat
source ../../.venv/bin/activate
streamlit run streamlit_app.py --server.port 8501 --server.address 0.0.0.0

# 정리
echo "FastAPI 서버 종료 중..."
kill $FASTAPI_PID 2>/dev/null
