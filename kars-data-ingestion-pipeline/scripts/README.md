  🔧 주요 변경사항

  1. generate_enron_schema.py → 일반화된 스키마 생성기

  새로운 기능:
  - 명령행 인터페이스: argparse 기반 CLI
  - 자동 클래스/DB명 생성: CSV 파일명 기반
  - 확장된 타입 매핑: 더 많은 데이터 타입 패턴 지원
  - 유연한 벡터화: 사용자 지정 벡터화 필드

  사용법:
  # 기본 사용 (Enron 전용)
  python script/generate_schema.py
  schema_examples/enron_schema.csv

  # 일반적인 사용
  python script/generate_schema.py my_data.csv
  --class-name MyDocument --vectorize content description

  # 벡터화 필드 지정
  python script/generate_schema.py data.csv --vectorize
  title summary body

  2. setup_database.py → 일반화된 DB 설정 도구

  새로운 기능:
  - 동적 스키마 생성: 모든 CSV 헤더 자동 처리
  - 유연한 텍스트 파일 매핑: 원하는 필드로 외부 텍스트 연결
  - 자동 데이터 타입 변환: 날짜/숫자/텍스트 자동 처리
  - 사용자 정의 검색 테스트: 원하는 쿼리로 테스트

  사용법:
  # Enron 데이터 (기존 방식)
  python script/setup_database.py
  schema_examples/enron_schema.csv \
    --text-dir dummy_texts \
    --text-path-field "Text Precedence"

  # 일반적인 CSV 데이터
  python script/setup_database.py my_data.csv \
    --class-name CustomerDocument \
    --db-name customer_db \
    --vectorize name description

  # 텍스트 파일 없는 경우
  python script/setup_database.py simple_data.csv
  --no-search


  💡 클래스명/DB명 관계 명확화

  자동 생성 규칙:
  CSV 파일: enron_schema.csv
  → 클래스명: EnronDocument (Weaviate 컬렉션명)
  → DB명: enron_db (논리적 식별자)

  CSV 파일: customer_data.csv  
  → 클래스명: CustomerDataDocument
  → DB명: customer_data_db