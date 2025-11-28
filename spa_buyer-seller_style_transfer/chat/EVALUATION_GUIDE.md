# SPA 매수인-매도인 친화 Style Transfer 평가 Guideline

M&A SPA Style Transfer 평가를 위한 전체 프로세스 및 폐쇄망 환경에서의 배포 및 실행 방법 정리 (251126: 10번 서버 다운 이슈로 미리 정리해봄)

## Table of Contents

1. [개요](#개요)
2. [사전 준비](#사전-준비)
3. [전체 워크플로우](#전체-워크플로우)
4. [단계별 상세 가이드](#단계별-상세-가이드)
5. [결과 해석](#결과-해석)
6. [트러블슈팅](#트러블슈팅)

---

## 개요

이 평가 시스템은 다음을 수행:

- **입력**: 원본 조항 (변환 전)
- **목표**: 목표 점수(0~4)에 맞는 변환된 조항; 핵심 string 요소를 포함 (GT)
- **예측**: LLM이 생성한 변환된 조항
- **평가**: ROUGE 점수 + Accuracy

### 평가 메트릭

- **ROUGE-1, ROUGE-2, ROUGE-L**: 생성된 조항의 품질 평가
- **Accuracy**: 점수 예측 정확도 (±0.5 이내 비율)
- **Category Accuracy**: 구간 기반 정확도 (매수인/중립/매도인 구간 일치 비율)
  - 매수인 친화: 0.0 ~ 1.5
  - 중립: 1.5 ~ 2.5
  - 매도인 친화: 2.5 ~ 4.0

---

## 사전 준비

### 1. 필수 파일 확인

```
chat/
├── generate_predictions.py          # ✅ 예측 생성 스크립트
├── evaluate.py                       # ✅ 평가 스크립트
├── test_data_manager.py              # ✅ 테스트 데이터 관리
├── spa_prompt_utils.py               # ✅ 프롬프트 유틸 (v1)
├── spa_prompt_utils_v2.py            # ✅ 프롬프트 유틸 (v2)
├── spa_term_context.py               # ✅ SPA 용어 컨텍스트
├── test_data/
│   └── test_data_template(손해배상)_filled.json  # 실제 GT 데이터 (수작업 완료)
├── requirements.txt                  # ✅ 패키지 목록
└── .env                              # ⚠️ 환경 변수 (생성 필요)
```

### 2. 환경 설정

```bash
# 필요한 패키지 설치
cd chat
pip install -r requirements.txt
# pip install rouge-score numpy
```

### 3. 환경 변수 설정 (.env 파일)

```bash
# chat/.env 파일 생성
LLM_API_BASE=http://10.10.190.10:8124  # vLLM 서버 주소
LLM_API_KEY=token-abc123                # vLLM 서버 API 키 (필요시)
LLM_MODEL=/data/models/Qwen3-Next-80B-A3B-Instruct  # 모델 경로
```

### 4. vLLM 서버 실행

```bash
# GPU 서버에서 실행 (별도 터미널/서버)
# 아래 CUDA_VISIBLE_DEVICES는 확인하고 설정
CUDA_VISIBLE_DEVICES=6,7 python -m vllm.entrypoints.openai.api_server \
  --model /data/models/Qwen3-Next-80B-A3B-Instruct \
  --host 0.0.0.0 --port 8124  # 포트는 환경에 맞게 조정

# 서버 상태 확인
curl http://10.10.190.10:8124/health
```

**Remark**: 평가용 배치 처리는 **vLLM 서버만 필요**하므로, FastAPI 서버는 불필요함.

---

## 전체 워크플로우

```mermaid
graph TD
    A[1. 테스트 데이터 준비(완료)] --> B[2. LLM 예측 생성]
    B --> C[3. 평가 실행]
    C --> D[4. 결과 분석]
```

### 빠른 시작 (전체 프로세스)

```bash
# 1. LLM 예측 생성 (v1 - 기본 버전)
python generate_predictions.py \
  --test_data test_data/test_data_template\(손해배상\)_filled.json \
  --output predictions_v1.json

# 2. LLM 예측 생성 (v2 - 개선 버전)
python generate_predictions.py \
  --test_data test_data/test_data_template\(손해배상\)_filled.json \
  --output predictions_v2.json \
  --use_v2

# 3. 평가 실행 (v1)
python evaluate.py \
  --test_data test_data/test_data_template\(손해배상\)_filled.json \
  --predictions predictions_v1.json \
  --output_dir evaluation_results_v1

# 4. 평가 실행 (v2)
python evaluate.py \
  --test_data test_data/test_data_template\(손해배상\)_filled.json \
  --predictions predictions_v2.json \
  --output_dir evaluation_results_v2

# 5. 결과 비교
python -c "
import json
with open('evaluation_results_v1/evaluation_results.json') as f:
    v1 = json.load(f)
with open('evaluation_results_v2/evaluation_results.json') as f:
    v2 = json.load(f)
print('='*60)
print('v1 vs v2 비교 결과')
print('='*60)
print(f'ROUGE-1: v1={v1[\"rouge_1\"]:.4f}, v2={v2[\"rouge_1\"]:.4f}, 차이={v2[\"rouge_1\"]-v1[\"rouge_1\"]:+.4f}')
print(f'ROUGE-2: v1={v1[\"rouge_2\"]:.4f}, v2={v2[\"rouge_2\"]:.4f}, 차이={v2[\"rouge_2\"]-v1[\"rouge_2\"]:+.4f}')
print(f'ROUGE-L: v1={v1[\"rouge_l\"]:.4f}, v2={v2[\"rouge_l\"]:.4f}, 차이={v2[\"rouge_l\"]-v1[\"rouge_l\"]:+.4f}')
print(f'Accuracy: v1={v1[\"accuracy\"]:.4f}, v2={v2[\"accuracy\"]:.4f}, 차이={v2[\"accuracy\"]-v1[\"accuracy\"]:+.4f}')
print(f'Category Accuracy: v1={v1.get(\"category_accuracy\", 0):.4f}, v2={v2.get(\"category_accuracy\", 0):.4f}, 차이={v2.get(\"category_accuracy\", 0)-v1.get(\"category_accuracy\", 0):+.4f}')
"
```

**참고**: 맥북 로컬(openai api 기반) 테스트는 `LOCAL_TEST_GUIDE.md` 참조

---

## 단계별 상세 가이드

### Step 1: 테스트 데이터 확인 (추후 디벨롭 여지 존재)

`test_data_template(손해배상)_filled.json` 파일을 실제 GT로 수정(현재는 임의로 채성원 컨설턴트가 작성, 추후 M&A 변호사님 검수 통해서 golden answer dataset 필요).

**현재 상태:**
- `spa_term_context.py`의 샘플 데이터를 참조하여 완성한 상태
- 실제 데이터에서 추출한 GT이긴 함

**검토 완료된 GT로 수정:**
```bash
# 파일 열어서 target_clause를 실제 GT로 수정
vim test_data/test_data_template\(손해배상\)_filled.json
# 또는
code test_data/test_data_template\(손해배상\)_filled.json
```
**확인 사항:**
- `target_clause`: M&A 변호사님이 검수 완료한 golden GT인지
- `input`: M&A 변호사님이 검수 완료한 실제 계약서의 주요 원본 조항인지
- `target_score`: M&A 변호사님이 검수 완료한 점수인지

**검증:**
```bash
python -m test_data_manager validate \
  --path test_data/test_data_template\(손해배상\)_filled.json
```

### Step 2: LLM 예측 생성

#### 2-1. 기본 버전 (v1) 사용

```bash
python generate_predictions.py \
  --test_data test_data/test_data_template\(손해배상\)_filled.json \
  --output predictions_v1.json \
  --temperature 0.0
```

#### 2-2. 개선 버전 (v2) 사용

```bash
python generate_predictions.py \
  --test_data test_data/test_data_template\(손해배상\)_filled.json \
  --output predictions_v2.json \
  --use_v2 \
  --temperature 0.0
```

**주요 옵션:**
- `--test_data`: 테스트 데이터 파일 경로
- `--output`: 예측 결과 저장 경로
- `--use_v2`: 개선된 샘플 선택 로직 사용 (spa_prompt_utils_v2)
- `--temperature`: LLM temperature (기본값: 0.0)

**중간 저장:**
- 매 5개 항목마다 자동으로 중간 저장 파일 생성
- `predictions_*_temp_5.json`, `predictions_*_temp_10.json` 등
- 중단 시 마지막 중간 저장 파일 확인 후 재시작 가능

**v2의 차이점:**
- `spa_prompt_utils_v2.py` 사용
- 목표 점수에 정확히 일치하는 샘플 우선 선택 (효원님과 논의했던 exact-filter few-shot 로직)

### Step 3: 평가 실행

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

**출력:**
- 콘솔에 평가 결과 요약 출력
- `evaluation_results_*/evaluation_results.json` 파일 저장

### Step 4: 결과 비교

```bash
# JSON 파일 직접 비교
diff evaluation_results_v1/evaluation_results.json \
     evaluation_results_v2/evaluation_results.json
```

### GT 데이터 구조 예시

```json
{
  "input": "실제 계약서의 원본 조항 텍스트",
  "target_clause": "전문가가 작성한 목표 조항 (실제 GT)",
  "target_score": 4.0,
  "spa_term": "손해배상(존속기간)",
  "description": "실제 계약서에서 추출한 손해배상(존속기간) - 4점 목표",
  "metadata": {
    "source": "real_contract",  # 실제 계약서에서 추출
    "contract_id": "SPA-2024-001",  # 계약서 ID (선택)
    "expert_reviewed": true,  # 전문가 검토 여부
    "extracted_date": "2024-11-26"  # 추출 일자
  }
}
```

### GT 데이터 품질 체크리스트

- [ ] `input`: 실제 계약서의 원본 조항 (변환 전)
- [ ] `target_clause`: 전문가가 작성/검토한 목표 조항 (GT)
- [ ] `target_score`: 전문가가 평가한 점수 (0.0~4.0)
- [ ] `spa_term`: 올바른 SPA 용어 카테고리
- [ ] `metadata.source`: "real_contract" 또는 "expert_curated"
- [ ] 모든 필수 필드 존재
- [ ] JSON 형식 검증 통과

**추후 업데이트**: `test_data_template(손해배상)_filled.json` 파일의 `target_clause` 필드를 실제 계약서에서 추출한 M&A 변호사님 검토 GT로 고도화

---

## 결과 해석

### 평가 결과 예시

```json
{
  "rouge_1": 0.8667,
  "rouge_2": 0.8000,
  "rouge_l": 0.8667,
  "accuracy": 1.0000,
  "category_accuracy": 1.0000,
  "total_samples": 15,
  "excluded_samples": 0
}
```

### 메트릭 설명

#### ROUGE 점수

- **ROUGE-1**: 단어 단위 겹침 비율 (0.0~1.0)
  - 높을수록 좋음
  - 0.8 이상이면 양호

- **ROUGE-2**: 2-gram 겹침 비율 (0.0~1.0)
  - 문맥/구문 수준 유사도
  - 0.7 이상이면 양호

- **ROUGE-L**: 문장 구조 유사도 (0.0~1.0)
  - 순서와 구조 유사도
  - 0.8 이상이면 양호

  ('양호' threshold는 나중에 정의해보아야 함; 현재는 최적화 상대비교)

#### Accuracy

- **Accuracy**: 점수 예측 정확도 (±0.5 이내 비율)
  - 예: GT=4.0, 예측=3.7 → 정확 (차이 0.3 ≤ 0.5)
  - 0.8 이상이면 양호

#### Category Accuracy

- **Category Accuracy**: 구간 기반 정확도 (매수인/중립/매도인 구간 일치 비율)
  - **매수인 친화 구간**: 0.0 ~ 1.5
  - **중립 구간**: 1.5 ~ 2.5
  - **매도인 친화 구간**: 2.5 ~ 4.0
  - 예: GT=0.0, 예측=1.2 → 정확 (둘 다 매수인 친화 구간)
  - 예: GT=2.0, 예측=2.3 → 정확 (둘 다 중립 구간)
  - 예: GT=4.0, 예측=3.0 → 정확 (둘 다 매도인 친화 구간)
  - 0.8 이상이면 양호

### 최적화 개선 효과 판단

v1 vs v2 비교 시:

- **ROUGE 점수 증가**: 생성 품질 개선
- **Accuracy 증가**: 점수 예측 정확도 개선
- **Category Accuracy 증가**: 구간 분류 정확도 개선
- **전반적 향상**: 로직 개선 효과 good

**참고**: 로컬 테스트(OpenAI API) 시 토큰 제한 오류가 발생한 항목은 자동으로 평가에서 제외함!

---

## 트러블슈팅

### 1. vLLM 서버 연결 실패

```bash
# 서버 상태 확인
curl http://10.10.190.10:8124/health

# 환경 변수 확인
echo $LLM_API_BASE
cat .env

# 방화벽/네트워크 확인
ping 10.10.190.10
```

### 2. 예측 생성 중 오류

```bash
# 중간 저장 파일 확인
ls -lh predictions_*_temp_*.json

# 오류 발생 항목의 raw_response 확인
python -c "
import json
with open('predictions_v1.json') as f:
    data = json.load(f)
    for i, pred in enumerate(data['predictions']):
        if 'error' in pred.get('metadata', {}):
            print(f'항목 {i+1}:', pred['metadata']['error'])
"
```

### 3. 평가 오류

```bash
# 데이터 개수 확인
python -c "
import json
with open('test_data/test_data_template(손해배상)_filled.json') as f:
    test = json.load(f)
with open('predictions_v1.json') as f:
    pred = json.load(f)
print(f'테스트 데이터: {len(test[\"test_data\"])}개')
print(f'예측 결과: {len(pred[\"predictions\"])}개')
"

# JSON 형식 검증
python -m json.tool test_data/test_data_template\(손해배상\)_filled.json > /dev/null && echo "OK"
```

---

## 파일 구조

```
chat/
├── test_data/
│   └── test_data_template(손해배상)_filled.json   # 실제 GT 데이터 (수작업으로 수정)
├── predictions_v1.json                             # v1 예측 결과 (온프렘)
├── predictions_v2.json                             # v2 예측 결과 (온프렘)
├── predictions_local_v1.json                       # v1 예측 결과 (로컬 테스트)
├── predictions_local_v2.json                       # v2 예측 결과 (로컬 테스트)
├── evaluation_results_v1/
│   └── evaluation_results.json                    # v1 평가 결과 (온프렘)
├── evaluation_results_v2/
│   └── evaluation_results.json                     # v2 평가 결과 (온프렘)
├── evaluation_results_local_v1/
│   └── evaluation_results.json                    # v1 평가 결과 (로컬)
├── evaluation_results_local_v2/
│   └── evaluation_results.json                     # v2 평가 결과 (로컬)
├── generate_predictions.py                         # 예측 생성 (온프렘 vLLM)
├── generate_predictions_local.py                   # 예측 생성 (OpenAI API)
└── evaluate.py                                     # 평가 실행
```

---

## ✅ 최종 체크리스트

폐쇄망에 코드베이스 clone:

- [ ] 모든 필수 파일 존재
- [ ] `.env` 파일 생성 및 환경 변수 설정
- [ ] `requirements.txt` 패키지 설치 완료
- [ ] vLLM 서버 실행 중
- [ ] 네트워크 연결 확인
- [ ] 테스트 데이터 준비 완료 (실제 GT)

폐쇄망에서 예측+평가 실행 후:

- [ ] 예측 생성 완료 (`predictions_*.json` 파일 존재)
- [ ] 평가 완료 (`evaluation_results_*/evaluation_results.json` 파일 존재)
- [ ] 결과 확인 및 비교,, (+ 정성 평가)

---

## 📝 다음 단계 (부제: 10번 서버 언제 문제 해결되냐를 기다리며 써본 메모)

1. **일단**: `test_data_template(손해배상)_filled.json` 파일이 실제 GT로 준비됨 (수작업 완료)
2. **10번 서버 문제 해결되면**: 실제 GT 기반 예측 생성 및 평가 (지금 251126 오후 3시인데,, 아직도 해결이 안 됐음 으아ㅏㅏㅏ)
3. **최종**: 실제 GT 기반 성능 측정 및 개선 효과 검증

