# 테스트 데이터 디렉토리

이 디렉토리는 Style Transfer 평가를 위한 Ground Truth (GT) 데이터를 저장합니다.

## 파일 구조

```
test_data/
├── README.md (이 파일)
├── test_data.json (메인 테스트 데이터)
└── test_data.json.backup.* (자동 백업 파일)
```

## 데이터 형식

`test_data.json` 파일은 다음 형식을 따릅니다:

```json
{
  "version": "1.0",
  "created_at": "2024-01-01T00:00:00",
  "total_samples": 10,
  "test_data": [
    {
      "input": "원본 조항 텍스트",
      "target_clause": "목표 조항 텍스트 (GT)",
      "target_score": 4.0,
      "spa_term": "부담",
      "description": "매도인 친화로 변환 (4점 목표)",
      "metadata": {
        "source": "spa_term_context.py",
        "original_score": 0.0
      }
    }
  ]
}
```

### 필수 필드

- `input`: 원본 조항 (변환 전)
- `target_clause`: 목표 조항 (GT, ROUGE 비교용)
- `target_score`: 목표 점수 (0.0~4.0, Accuracy 비교용)

### 선택 필드

- `spa_term`: SPA 용어 (예: "부담", "우려")
- `description`: 설명
- `metadata`: 추가 메타데이터

## 사용 방법

### 1. 테스트 데이터 생성/관리

```bash
# 템플릿 생성
python -m test_data_manager create

# 검증
python -m test_data_manager validate

# 정보 조회
python -m test_data_manager info

# 목록 조회
python -m test_data_manager list
```

### 2. 평가 실행

```bash
# 기본 경로 사용 (test_data/test_data.json)
python evaluate.py --predictions predictions.json

# 커스텀 경로 사용
python evaluate.py --test_data custom_test_data.json --predictions predictions.json
```

## 데이터 추가 방법

1. `test_data_manager.py`의 `create_test_data_template()` 함수를 참고하여 형식 확인
2. `test_data.json` 파일에 새 항목 추가
3. `python -m test_data_manager validate`로 검증
4. 평가 실행

## 주의사항

- `target_score`는 반드시 0.0~4.0 범위여야 합니다
- 모든 필수 필드가 있어야 합니다
- 파일 저장 시 자동 백업이 생성됩니다

