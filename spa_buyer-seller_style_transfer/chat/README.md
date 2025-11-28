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

## 평가용 배치 처리 (UI 없이 실행)

평가를 위한 예측 생성은 **Streamlit UI와 FastAPI 서버 없이** CLI로 실행(vLLM 서버에 직접 연결하므로 FastAPI가 필요 없음)

### 1. 예측 생성

```bash
# 기본 버전 (v1)
python generate_predictions.py \
  --test_data test_data/test_data_template\(손해배상\)_filled.json \
  --output predictions_v1.json

# 개선 버전 (v2 - 개선된 샘플 선택 로직)
python generate_predictions.py \
  --test_data test_data/test_data_template\(손해배상\)_filled.json \
  --output predictions_v2.json \
  --use_v2
```

### 2. 평가 실행

```bash
# v1 결과 평가
python evaluate.py \
  --test_data test_data/test_data_template\(손해배상\)_filled.json \
  --predictions predictions_v1.json \
  --output_dir evaluation_results_v1

# v2 결과 평가
python evaluate.py \
  --test_data test_data/test_data_template\(손해배상\)_filled.json \
  --predictions predictions_v2.json \
  --output_dir evaluation_results_v2
```

### 주요 차이점

| 항목 | Streamlit 앱 | 배치 처리 (평가용) |
|------|-------------|------------------|
| **목적** | 대화형 UI로 실시간 조항 변환 및 분석 | 평가를 위한 대량 예측 생성 |
| **필요한 서버** | vLLM 서버 + **FastAPI 서버** | **vLLM 서버만** (FastAPI 불필요) |
| **실행 방법** | `streamlit run streamlit_app.py` | `python generate_predictions.py` |
| **UI** | 웹 인터페이스 필요 | 불필요 (CLI) |

### 평가용 실행 시 필요한 것

```bash
# 1. vLLM 서버만 실행 (FastAPI 불필요)
CUDA_VISIBLE_DEVICES=6,7 python -m vllm.entrypoints.openai.api_server \
  --model /data/models/Qwen3-Next-80B-A3B-Instruct \
  --host 0.0.0.0 --port 8000

# 2. 환경 변수 설정 (.env 파일 또는 환경 변수)
LLM_API_BASE=http://10.10.190.10:8124  # vLLM 서버 주소
LLM_API_KEY=token-abc123
LLM_MODEL=/data/models/Qwen3-Next-80B-A3B-Instruct

# 3. 배치 처리 실행
python generate_predictions.py \
  --test_data test_data/test_data_template\(손해배상\)_filled.json \
  --output predictions_v1.json
```

자세한 평가 가이드는 `EVALUATION_GUIDE.md`를 참고.
