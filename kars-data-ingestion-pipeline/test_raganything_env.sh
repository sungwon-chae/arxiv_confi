#!/bin/bash
# RAG-Anything 테스트를 위한 별도 환경 설정 스크립트

echo "🔧 RAG-Anything 테스트 환경 설정"
echo ""

# 색상 정의
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Python 버전 확인
PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
echo "📌 Python 버전: $PYTHON_VERSION"

# 가상환경이 이미 존재하는지 확인
if [ -d ".venv_raganything" ]; then
    echo -e "${YELLOW}⚠️  기존 가상환경이 존재합니다.${NC}"
    read -p "삭제하고 새로 생성하시겠습니까? (y/N): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        rm -rf .venv_raganything
        echo "🗑️  기존 환경 삭제됨"
    else
        echo "기존 환경을 유지합니다."
        source .venv_raganything/bin/activate
        echo -e "${GREEN}✅ 기존 환경 활성화됨${NC}"
        exit 0
    fi
fi

# 별도 가상환경 생성
echo "📦 별도 가상환경 생성 중..."
python3 -m venv .venv_raganything

# 가상환경 활성화
source .venv_raganything/bin/activate

# pip 업그레이드
echo "📥 pip 업그레이드 중..."
pip install --upgrade pip setuptools wheel

# raganything 최신 버전 설치 (lightrag는 자동으로 호환 버전 설치됨)
echo ""
echo "📦 RAG-Anything 최신 버전 설치 중..."
echo "   (lightrag는 자동으로 호환 버전이 설치됩니다)"
pip install "raganything[all]"

# 추가 필수 패키지
echo ""
echo "📦 추가 패키지 설치 중..."
pip install python-dotenv loguru

# 로컬 임베딩 서버를 위한 패키지 (선택적)
echo ""
echo "📦 로컬 임베딩 서버 관련 패키지 설치 중..."
pip install httpx tenacity

# 설치된 버전 확인
echo ""
echo "📋 설치된 주요 패키지 버전:"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
pip list | grep -E "(raganything|lightrag|loguru|dotenv)" | while read line; do
    echo "  $line"
done
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# 환경 변수 파일 확인
if [ ! -f "config.env" ]; then
    echo ""
    echo -e "${YELLOW}⚠️  config.env 파일이 없습니다.${NC}"
    echo "   test_baseline.py 실행 전에 config.env 파일을 생성하세요."
fi

echo ""
echo -e "${GREEN}✅ RAG-Anything 테스트 환경 준비 완료!${NC}"
echo ""
echo "📌 사용법:"
echo "   1. source .venv_raganything/bin/activate"
echo "   2. python test_baseline.py"
echo ""
echo "📌 환경 전환:"
echo "   - 원래 환경으로: deactivate"
echo "   - 메인 프로젝트 환경으로: source .venv/bin/activate"
echo ""
echo "⚠️  주의: 이 환경은 기본 프로젝트 환경과 분리되어 있습니다."