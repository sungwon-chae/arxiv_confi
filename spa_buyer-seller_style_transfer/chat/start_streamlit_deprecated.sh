#!/bin/bash

# 환경변수 설정
export BACKEND_URL="http://localhost:8001"

echo "Streamlit 앱 시작 중..."
echo "Backend URL: $BACKEND_URL"
echo "브라우저에서 http://localhost:8501 에 접속하세요."

streamlit run streamlit_app.py --server.port 8501 --server.address 0.0.0.0
