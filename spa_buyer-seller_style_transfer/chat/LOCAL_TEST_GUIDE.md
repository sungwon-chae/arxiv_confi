# 로컬 테스트 가이드 (OpenAI API 사용)

vLLM 서버 없이 로컬에서 OpenAI API를 사용하여 테스트하는 방법입니다.

## 사전 준비

### 1. OpenAI API 키 설정

`.env` 파일에 OpenAI API 키 추가:

```bash
# chat/.env 파일
OPENAI_API_KEY=sk-your-openai-api-key-here
OPENAI_MODEL=gpt-4o-mini  # 기본값: gpt-4o-mini (가격 효율적)
# 또는 다른 모델: gpt-4o, gpt-4-turbo 등
```

### 2. 패키지 확인

필요한 패키지는 이미 `requirements.txt`에 포함되어 있습니다:
- `langchain-openai`
- `langchain-core`
- `pydantic`
- `python-dotenv`

## 모델 선택 가이드

### 추천 모델: GPT-4o-mini
- **가격**: 입력 $0.14/1M 토큰, 출력 $0.28/1M 토큰 (gpt-4o 대비 약 35배 저렴)
- **토큰 제한**: 128K 컨텍스트, max_tokens 16,384
- **특징**: 가격 대비 성능 우수, 실험에 적합

### 다른 옵션
- **gpt-4o**: 더 높은 성능, 가격 $5/$15 per 1M 토큰
- **gpt-4-turbo**: 일부 버전에서 더 큰 max_tokens 가능, 가격 $10/$30 per 1M 토큰

## 사용 방법

### 기본 사용

```bash
# v1 (기본 버전)
python generate_predictions_local.py \
  --test_data test_data/test_data_template\(손해배상\)_filled.json \
  --output predictions_local_v1.json

# v2 (개선 버전)
python generate_predictions_local.py \
  --test_data test_data/test_data_template\(손해배상\)_filled.json \
  --output predictions_local_v2.json \
  --use_v2
```

### 옵션

- `--test_data`: 테스트 데이터 파일 경로 (필수)
- `--output`: 예측 결과 저장 경로 (기본값: `predictions_local_<version>_<timestamp>.json`)
- `--use_v2`: 개선된 샘플 선택 로직 사용
- `--temperature`: LLM temperature (기본값: 0.7)
- `--model`: OpenAI 모델명 (기본값: .env의 OPENAI_MODEL 또는 gpt-4o)

### 예시

```bash
# v2 + 낮은 temperature
python generate_predictions_local.py \
  --test_data test_data/test_data_template\(손해배상\)_filled.json \
  --output predictions_local_v2_t05.json \
  --use_v2 \
  --temperature 0.5
```

## 평가 실행

생성된 예측 결과를 평가:

```bash
# 로컬 예측 결과 평가
python evaluate.py \
  --test_data test_data/test_data_template\(손해배상\)_filled.json \
  --predictions predictions_local_v1.json \
  --output_dir evaluation_results_local_v1
```

## 주요 차이점

| 항목 | `generate_predictions.py` | `generate_predictions_local.py` |
|------|---------------------------|--------------------------------|
| **API** | vLLM 서버 (온프레미스) | OpenAI API (클라우드) |
| **모델** | Qwen3-Next-80B-A3B-Instruct | gpt-4o, gpt-4-turbo 등 |
| **환경 변수** | `LLM_API_BASE`, `LLM_MODEL` | `OPENAI_API_KEY`, `OPENAI_MODEL` |
| **용도** | 폐쇄망 프로덕션 | 로컬 테스트 |

## 주의사항

1. **API 비용**: OpenAI API는 사용량에 따라 비용이 발생합니다
2. **속도**: OpenAI API는 vLLM 서버보다 느릴 수 있습니다
3. **제한**: OpenAI API에는 rate limit이 있습니다
4. **프라이버시**: 민감한 데이터는 OpenAI API로 전송하지 않는 것이 좋습니다

## 트러블슈팅

### API 키 오류

```bash
❌ 오류: OPENAI_API_KEY 환경 변수가 설정되지 않았습니다.
```

**해결:**
```bash
# .env 파일 확인
cat .env | grep OPENAI_API_KEY

# 또는 환경 변수로 직접 설정
export OPENAI_API_KEY=sk-your-key-here
python generate_predictions_local.py ...
```

### 모델 오류

```bash
# 사용 가능한 모델 확인
# gpt-4o, gpt-4-turbo, gpt-4 등
```

### Rate Limit 오류

OpenAI API rate limit에 걸리면 잠시 대기 후 재시도하세요.

