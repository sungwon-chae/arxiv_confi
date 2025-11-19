#!/bin/bash

# vLLM 서버 설정
export LLM_API_BASE="http://10.10.190.10:8124"
export LLM_API_KEY="token-abc123"
export LLM_MODEL="/data/models/Qwen3-Next-80B-A3B-Instruct"

# FastAPI 서버 설정
export BACKEND_URL="http://localhost:8001"

# CORS 설정
export ALLOWED_ORIGINS="http://localhost:8501"

echo "환경변수 설정 완료:"
echo "LLM_API_BASE: $LLM_API_BASE"
echo "LLM_MODEL: $LLM_MODEL"
echo "BACKEND_URL: $BACKEND_URL"

# FastAPI 서버 시작
echo "FastAPI 서버 시작 중..."
uvicorn server:app --host 0.0.0.0 --port 8001 --reload
