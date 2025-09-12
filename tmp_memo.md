(.venv) min.choi10@wss-195:/raid1/workspace/kars-agent/weaviate-mcp/tmp_sungwon_chae$ python test_extract_value_tool_modified.py 
🚀 Weaviate MCP 도구 테스트 시작

2025-09-12 18:15:17,036 - mcp_tools - INFO - Weaviate MCP 도구 초기화 완료
2025-09-12 18:15:17,453 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
Test Query Response:  ChatCompletion(id='chatcmpl-36dfd21cb4214d8eb18132b17b6850dd', choices=[Choice(finish_reason='length', index=0, logprobs=None, message=ChatCompletionMessage(content='<think>\nOkay, the user just said "hi', refusal=None, role='assistant', annotations=None, audio=None, function_call=None, tool_calls=[], reasoning_content=None), stop_reason=None)], created=1757668522, model='/data/models_ckpt/Qwen3-32B', object='chat.completion', service_tier=None, system_fingerprint=None, usage=CompletionUsage(completion_tokens=10, prompt_tokens=10, total_tokens=20, completion_tokens_details=None, prompt_tokens_details=None), prompt_logprobs=None)
✅ OpenAI 클라이언트 설정 완료
🔍 extract_filter_from_query 도구 테스트 시작 (MBG 실제 데이터 기반)

📋 테스트 목적:
  1. Filter 자동 추출 검증
  2. 벡터DB에서 관련 문서 검색 확인
  3. 실제 MBG 데이터 기반 GT 검증
  4. 유사도 기반 검색 성능 확인

📋 FilterExtractionResult 필드:
  - custodian: 보관자
  - ori_file_name: 원본 파일명
  - s_created_date: 생성일
  - sent_date: 발송일
  - from_name: 발신자 이름
  - to_name: 수신자 이름
  - cc: 참조자 이름
  - bcc: 숨은참조자 이름
  - last_author: 최종 작성자
  - extension: 파일 확장자

테스트 케이스 1: Lee Sang-kuk이 언급된 모든 이메일을 찾아주세요
------------------------------------------------------------
2025-09-12 18:15:17,471 - mcp_tools - INFO - 🔍 필터 추출 시작: 'Lee Sang-kuk이 언급된 모든 이메일을 찾아주세요'
2025-09-12 18:15:18,968 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:15:18,970 - kars_db - INFO - 🚀 RAG 벡터 데이터베이스 초기화 시작
2025-09-12 18:15:18,970 - simple_manager - INFO - Weaviate URL: http://10.10.150.195:8080
2025-09-12 18:15:18,970 - simple_manager - INFO - OpenAI Base URL: http://10.10.190.1:8125
2025-09-12 18:15:18,970 - kars_db - INFO - ✅ VectorDB 매니저 초기화 완료
2025-09-12 18:15:19,018 - httpx - INFO - HTTP Request: GET http://10.10.190.1:8125/v1/models "HTTP/1.1 200 OK"
2025-09-12 18:15:19,019 - weaviate_db - INFO - ✅ vLLM 서버에서 모델명 가져옴: /data/models_ckpt/bge-m3
2025-09-12 18:15:19,034 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8125/v1/embeddings "HTTP/1.1 200 OK"
2025-09-12 18:15:19,038 - weaviate_db - INFO - ✅ 샘플 임베딩 생성 성공 (차원: 1024)
2025-09-12 18:15:19,078 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/.well-known/openid-configuration "HTTP/1.1 404 Not Found"
2025-09-12 18:15:19,105 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/meta "HTTP/1.1 200 OK"
2025-09-12 18:15:21,140 - weaviate_db - INFO - ✅ Weaviate 클라이언트 연결 성공: http://10.10.150.195:8080
2025-09-12 18:15:21,141 - weaviate_db - INFO - 📡 OpenAI Base URL (Python용): http://10.10.190.1:8125/v1
2025-09-12 18:15:21,141 - weaviate_db - INFO - 📡 OpenAI Base URL (Weaviate용): http://10.10.190.1:8125
2025-09-12 18:15:21,141 - weaviate_db - INFO - 🔧 동적 모델명: /data/models_ckpt/bge-m3
2025-09-12 18:15:21,141 - simple_manager - INFO - DB 연결 초기화 완료
2025-09-12 18:15:21,145 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema "HTTP/1.1 200 OK"
2025-09-12 18:15:21,150 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema/DocumentChunk "HTTP/1.1 200 OK"
2025-09-12 18:15:21,157 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema/EnronDocument "HTTP/1.1 200 OK"
2025-09-12 18:15:21,158 - weaviate_db - INFO - 스키마 조회 완료: 2개 클래스
2025-09-12 18:15:21,158 - simple_manager - WARNING - 클래스 매핑 파일이 없습니다. 기본 규칙을 사용합니다.
2025-09-12 18:15:21,158 - simple_manager - INFO - 기존 클래스 등록: chunk_db -> DocumentChunk
2025-09-12 18:15:21,158 - simple_manager - INFO - 기존 클래스 등록: enron_db -> EnronDocument
2025-09-12 18:15:21,158 - simple_manager - INFO - 총 2개 DB에 클래스 등록 완료
2025-09-12 18:15:21,158 - simple_manager - INFO -   chunk_db: ['DocumentChunk']
2025-09-12 18:15:21,159 - simple_manager - INFO -   enron_db: ['EnronDocument']
2025-09-12 18:15:21,161 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema "HTTP/1.1 200 OK"
2025-09-12 18:15:21,166 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema/DocumentChunk "HTTP/1.1 200 OK"
2025-09-12 18:15:21,170 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema/EnronDocument "HTTP/1.1 200 OK"
2025-09-12 18:15:21,171 - weaviate_db - INFO - 스키마 조회 완료: 2개 클래스
2025-09-12 18:15:21,171 - kars_db - INFO - 📊 사용 가능한 클래스들: ['DocumentChunk', 'EnronDocument']
2025-09-12 18:15:21,171 - kars_db - INFO - ✅ 사용할 클래스명: DocumentChunk
2025-09-12 18:15:21,171 - mcp_tools - INFO - ✅ RAG 데이터베이스 초기화 성공: kars_test
2025-09-12 18:15:21,171 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:15:21,171 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:15:21,254 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:15:21,254 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:15:21,326 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:15:21,326 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:15:21,408 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:15:21,409 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:15:21,478 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:15:21,479 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:15:21,479 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
❌ 오류 발생: 'error'
