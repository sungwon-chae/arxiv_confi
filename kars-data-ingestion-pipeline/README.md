# Data Ingestion Pipeline

고도화된 데이터 처리 파이프라인으로 CSV 데이터 인제스션, 멀티모달 문서 처리, 지식 그래프 구축을 통합 지원합니다.

## 시스템 아키텍처

### RAG-Anything과의 차이점 및 하이브리드 접근법
이 시스템은 RAG-Anything의 핵심 아이디어를 차용하되, Weaviate + LightRAG 하이브리드 구조에 맞게 재설계되었습니다:

**RAG-Anything과의 주요 차이점:**
- **독립적 구현**: RAG-Anything의 전체 시스템 대신 핵심 컴포넌트만 선택적 적용
- **유연한 아키텍처**: Weaviate 벡터 DB와 LightRAG 그래프 검색의 장점을 모두 활용
- **커스텀 파서 통합**: MinerU/magic-pdf를 직접 통합하여 제어 가능한 문서 처리

**하이브리드 접근법의 장점:**
- Weaviate의 강력한 벡터 검색 + LightRAG의 그래프 기반 컨텍스트 이해
- 멀티모달 요소를 Weaviate 스키마에 맞춰 효율적으로 저장
- 기존 인프라와의 호환성 유지

### 핵심 프로세서 모듈
- **multimodal_processor.py**: 멀티모달 파일 처리 (PDF, 이미지, 테이블 등)
  - MinerU/magic-pdf 기반 고품질 문서 구조 추출 (RAG-Anything과 동일)
  - Marker PDF, pypdf 등 다양한 fallback 옵션
  - OCR 지원 (pytesseract)
  - 요소 간 관계 분석 기능 포함
  
- **lightrag_adapter.py**: LightRAG와 Weaviate 연결
  - Weaviate를 LightRAG의 벡터 스토리지로 사용하는 어댑터
  - BaseVectorStorage 인터페이스 구현
  
- **knowledge_graph_builder.py**: 지식 그래프 구축
  - spaCy 기반 엔티티 추출 (한국어/영어)
  - 관계 추출 및 네트워크 분석
  - 멀티모달 요소 간 관계 분석
  
- **hybrid_rag_processor.py**: 하이브리드 검색 통합
  - 멀티모달 처리 + 지식 그래프 + LightRAG 통합
  - 그래프 기반 검색과 벡터 검색 결합

### 통합 엔진
- **pipeline_engine.py**: 데이터 적재를 위한 통합 엔진
  - 모든 프로세서 모듈 통합 관리
  - CSV 처리, 멀티모달 문서 처리, 지식 그래프 구축 워크플로우

### 데이터베이스 연동
- **weaviate_db.py**: Weaviate 벡터 DB 구현체
  - 동적 임베딩 모델 지원 (vLLM 서버 연동)
  - 스키마 기반 자동 벡터화
  - 지능적 필터링 및 하이브리드 검색
  
- **simple_manager.py**: 다중 스키마 지원 벡터 DB 매니저
  - 여러 데이터베이스/컬렉션 관리
  - 동적 스키마 생성 및 관리
  - MCP 도구와의 통합 (weaviate-mcp 폴더에 위치)

## 주요 기능

- **CSV 데이터 처리**: CSV/Excel 파일을 벡터 DB에 자동 저장
- **멀티모달 문서 처리**: MinerU/magic-pdf 및 RAG-Anything 기반 PDF/Office 문서 처리
- **지식 그래프 구축**: 엔티티 추출 및 관계 분석
- **하이브리드 검색**: LightRAG 그래프 검색 + Weaviate 벡터 검색 통합

## 설치 및 실행

### 1. 설치
```bash
cd data-ingestion-pipeline
uv sync  # 의존성 설치
```

### 2. spaCy 언어 모델 설치 (선택사항)
```bash
# 한국어 모델
uv run python -m spacy download ko_core_news_sm

# 영어 모델
uv run python -m spacy download en_core_web_sm
```

### 3. 사용법

**기존 방식 호환 (간단한 CSV 처리)**
```bash
uv run python main.py csv-legacy data.csv --text-dir texts/
```

**새로운 고급 기능**
```bash
# CSV 파일 고급 처리 (텍스트 분석 + 지식 그래프)
uv run python main.py process-csv data.csv --build-kg --chunk-strategy semantic

# 멀티모달 문서 처리
uv run python main.py process-documents *.pdf --build-kg

# 독립적인 지식 그래프 구축
uv run python main.py build-kg processed_data/ --output kg.json
```

## 사용 예시

### Enron 데이터셋 처리
```bash
uv run python main.py csv-legacy config/schemas/enron_schema.csv \
  --text-dir dummy_texts \
  --text-path-field "Text Precedence"
```

### PDF 문서 일괄 처리
```bash
uv run python main.py process-documents documents/*.pdf \
  --build-kg \
  --output-dir results/
```

## 의존성

### 기본 의존성
- **weaviate-client**: 벡터 데이터베이스
- **pandas, numpy**: 데이터 처리
- **pypdf, python-docx**: 문서 파싱
- **openai**: 임베딩 생성

### 고급 기능 의존성
- **spacy**: 자연어 처리 및 엔티티 추출
- **networkx**: 지식 그래프 분석
- **raganything**: 멀티모달 문서 처리
- **lightrag**: 그래프 기반 RAG 엔진
- **magic-pdf/MinerU**: 고품질 PDF 구조 추출 (선택적)
- **marker-pdf**: PDF to 마크다운 변환 (선택적)

### 선택적 의존성
- **performance**: torch, transformers (고성능 처리)
- **gpu**: GPU 가속화 지원
- **pytesseract**: OCR 기능

## 구조

```
data-ingestion-pipeline/
├── main.py                    # 통합 CLI 인터페이스
├── pipeline_engine.py         # 데이터 적재 통합 엔진
├── weaviate_db.py            # Weaviate DB 구현체
├── processors/               # 고급 처리 모듈들
│   ├── multimodal_processor.py    # 멀티모달 문서 처리
│   ├── lightrag_adapter.py        # LightRAG-Weaviate 어댑터
│   ├── knowledge_graph_builder.py # 지식 그래프 구축
│   └── hybrid_rag_processor.py    # 하이브리드 검색 통합
├── scripts/                  # 기존 호환성 유지
│   ├── setup_database.py
│   └── generate_schema.py
└── config/                   # 설정 파일들
    ├── schemas/
    └── weaviate_schemas/
```

## 데이터 흐름

1. **문서 입력** → multimodal_processor.py
2. **엔티티/관계 추출** → knowledge_graph_builder.py
3. **LightRAG 인덱싱** → lightrag_adapter.py + hybrid_rag_processor.py
4. **Weaviate 저장** → weaviate_db.py + pipeline_engine.py
5. **하이브리드 검색** → weaviate-mcp/hybrid_search_tools.py

## 라이센스

MIT License