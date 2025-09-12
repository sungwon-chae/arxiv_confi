(.venv) min.choi10@wss-195:/raid1/workspace/kars-agent/weaviate-mcp/tmp_sungwon_chae$ python test_extract_value_tool_modified.py 
🚀 Weaviate MCP 도구 테스트 시작

2025-09-12 16:21:23,691 - mcp_tools - INFO - Weaviate MCP 도구 초기화 완료
2025-09-12 16:21:26,072 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
Test Query Response:  ChatCompletion(id='chatcmpl-e27bf3e2aa014f4f83b6c34760a61ca2', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='<think>\nOkay, the user said "hi!" so I should respond in a friendly and welcoming way. I need to make sure they feel comfortable and encouraged to ask questions or share what\'s on their mind. Maybe start with a greeting and offer help. Let me keep it simple and open-ended. Something like "Hello! How can I assist you today?" That should work.\n</think>\n\nHello! How can I assist you today? 😊', refusal=None, role='assistant', annotations=None, audio=None, function_call=None, tool_calls=[], reasoning_content=None), stop_reason=None)], created=1757661689, model='/data/models_ckpt/Qwen3-32B', object='chat.completion', service_tier=None, system_fingerprint=None, usage=CompletionUsage(completion_tokens=90, prompt_tokens=10, total_tokens=100, completion_tokens_details=None, prompt_tokens_details=None), prompt_logprobs=None)
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

테스트 케이스 1: 2020년 6월에 작성된 모든 문서들
------------------------------------------------------------
2025-09-12 16:21:26,091 - mcp_tools - INFO - 🔍 필터 추출 시작: '2020년 6월에 작성된 모든 문서들'
2025-09-12 16:21:27,521 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 16:21:27,523 - kars_db - INFO - 🚀 RAG 벡터 데이터베이스 초기화 시작
2025-09-12 16:21:27,523 - simple_manager - INFO - Weaviate URL: http://10.10.150.195:8080
2025-09-12 16:21:27,523 - simple_manager - INFO - OpenAI Base URL: http://10.10.190.1:8125
2025-09-12 16:21:27,523 - kars_db - INFO - ✅ VectorDB 매니저 초기화 완료
2025-09-12 16:21:27,572 - httpx - INFO - HTTP Request: GET http://10.10.190.1:8125/v1/models "HTTP/1.1 200 OK"
2025-09-12 16:21:27,573 - weaviate_db - INFO - ✅ vLLM 서버에서 모델명 가져옴: /data/models_ckpt/bge-m3
2025-09-12 16:21:27,585 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8125/v1/embeddings "HTTP/1.1 200 OK"
2025-09-12 16:21:27,587 - weaviate_db - INFO - ✅ 샘플 임베딩 생성 성공 (차원: 1024)
2025-09-12 16:21:27,623 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/.well-known/openid-configuration "HTTP/1.1 404 Not Found"
2025-09-12 16:21:27,652 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/meta "HTTP/1.1 200 OK"
2025-09-12 16:21:29,710 - weaviate_db - INFO - ✅ Weaviate 클라이언트 연결 성공: http://10.10.150.195:8080
2025-09-12 16:21:29,710 - weaviate_db - INFO - 📡 OpenAI Base URL (Python용): http://10.10.190.1:8125/v1
2025-09-12 16:21:29,711 - weaviate_db - INFO - 📡 OpenAI Base URL (Weaviate용): http://10.10.190.1:8125
2025-09-12 16:21:29,711 - weaviate_db - INFO - 🔧 동적 모델명: /data/models_ckpt/bge-m3
2025-09-12 16:21:29,711 - simple_manager - INFO - DB 연결 초기화 완료
2025-09-12 16:21:29,715 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema "HTTP/1.1 200 OK"
2025-09-12 16:21:29,720 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema/DocumentChunk "HTTP/1.1 200 OK"
2025-09-12 16:21:29,727 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema/EnronDocument "HTTP/1.1 200 OK"
2025-09-12 16:21:29,728 - weaviate_db - INFO - 스키마 조회 완료: 2개 클래스
2025-09-12 16:21:29,728 - simple_manager - WARNING - 클래스 매핑 파일이 없습니다. 기본 규칙을 사용합니다.
2025-09-12 16:21:29,729 - simple_manager - INFO - 기존 클래스 등록: chunk_db -> DocumentChunk
2025-09-12 16:21:29,729 - simple_manager - INFO - 기존 클래스 등록: enron_db -> EnronDocument
2025-09-12 16:21:29,729 - simple_manager - INFO - 총 2개 DB에 클래스 등록 완료
2025-09-12 16:21:29,729 - simple_manager - INFO -   chunk_db: ['DocumentChunk']
2025-09-12 16:21:29,729 - simple_manager - INFO -   enron_db: ['EnronDocument']
2025-09-12 16:21:29,732 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema "HTTP/1.1 200 OK"
2025-09-12 16:21:29,736 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema/DocumentChunk "HTTP/1.1 200 OK"
2025-09-12 16:21:29,740 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema/EnronDocument "HTTP/1.1 200 OK"
2025-09-12 16:21:29,741 - weaviate_db - INFO - 스키마 조회 완료: 2개 클래스
2025-09-12 16:21:29,741 - kars_db - INFO - 📊 사용 가능한 클래스들: ['DocumentChunk', 'EnronDocument']
2025-09-12 16:21:29,741 - kars_db - INFO - ✅ 사용할 클래스명: DocumentChunk
2025-09-12 16:21:29,741 - mcp_tools - INFO - ✅ RAG 데이터베이스 초기화 성공: kars_test
2025-09-12 16:21:29,741 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 16:21:29,741 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 16:21:29,826 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 16:21:29,826 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 16:21:29,910 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 16:21:29,910 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 16:21:29,992 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 16:21:29,993 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 16:21:30,082 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 16:21:30,082 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 16:21:30,082 - mcp_tools - INFO - ✅ 필터 추출 완료: filter 검색, 필터: custodian=None ori_file_name=None s_created_date={'gte': '2020-06-01T00:00:00Z', 'lt': '2020-07-01T00:00:00Z'} sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
📊 추출된 필터:
  - custodian: None
  - ori_file_name: None
  - s_created_date: {'gte': '2020-06-01T00:00:00Z', 'lt': '2020-07-01T00:00:00Z'}
  - sent_date: None
  - from_email: None
  - to_email: None
  - cc: None
  - bcc: None
  - last_author: None
  - extension: None
🔍 검색 방식: filter
💭 판단 근거: 질의에서 구체적인 날짜 정보 's_created_date: {'gte': '2020-06-01T00:00:00Z', 'lt': '2020-07-01T00:00:00Z'}'를 찾았습니다. 조건 필터링을 사용합니다.
📋 검색에 사용할 필터: {'s_created_date': {'gte': '2020-06-01T00:00:00Z', 'lt': '2020-07-01T00:00:00Z'}}
2025-09-12 16:21:30,082 - mcp_tools - INFO - 🔍 필터 검색 실행: class_name=DocumentChunk, limit=5, filters={'s_created_date': {'gte': '2020-06-01T00:00:00Z', 'lt': '2020-07-01T00:00:00Z'}}
2025-09-12 16:21:30,082 - kars_db - INFO - 필터 검색 시작: class_name=DocumentChunk, limit=5, filters={'s_created_date': {'gte': '2020-06-01T00:00:00Z', 'lt': '2020-07-01T00:00:00Z'}}
2025-09-12 16:21:30,082 - kars_db - INFO - 필터와 함께 검색: {'s_created_date': {'gte': '2020-06-01T00:00:00Z', 'lt': '2020-07-01T00:00:00Z'}}
2025-09-12 16:21:30,090 - kars_db - INFO - ✅ 필터 검색 완료: 5개 결과 반환
📊 검색 결과:
  - 성공 여부: True
  - 총 결과 수: 5개
  - 검색 방식: N/A
  - 사용된 필터: N/A

📄 검색된 문서들:
  1. 문서 ID: 84e3b894-4f16-4b8d-bf39-5bbcd95837b2
     파일명: N/A
     보관자: 세진 김
     생성일: N/A
     발송일: 1900-01-01 00:00:00+00:00
     발신자: NaN
     수신자: NaN
     확장자: csv
     내용 미리보기: {'*ID': 260381, '*docNo': 'otov-230327-0001', '상태': '등록', '등록자': '홍성진 (hsj@mercedes-benz.com)', '딜러사...
     최종 작성자: NaN

  2. 문서 ID: 6a1eca77-af00-4be9-96d6-dc28a1a68b7a
     파일명: N/A
     보관자: 세진 김
     생성일: N/A
     발송일: 1900-01-01 00:00:00+00:00
     발신자: NaN
     수신자: NaN
     확장자: csv
     내용 미리보기: {'*ID': 260452, '*docNo': 'otov-230327-0002', '상태': '등록', '등록자': '최하정 (ha-jeong.choi@mercedes-benz.c...
     최종 작성자: NaN

  3. 문서 ID: 9e25d34e-9fd9-4a4e-a966-3a4abed89cb4
     파일명: N/A
     보관자: 세진 김
     생성일: N/A
     발송일: 1900-01-01 00:00:00+00:00
     발신자: NaN
     수신자: NaN
     확장자: csv
     내용 미리보기: {'*ID': 259876, '*docNo': 'otov-230320-0002', '상태': '등록', '등록자': '이윤희 (youn-hee.lee@mercedes-benz.co...
     최종 작성자: NaN

  4. 문서 ID: ee730a17-2b97-4d51-a901-99d74fd56e49
     파일명: N/A
     보관자: 세진 김
     생성일: N/A
     발송일: 1900-01-01 00:00:00+00:00
     발신자: NaN
     수신자: NaN
     확장자: csv
     내용 미리보기: {'*ID': 259922, '*docNo': 'otov-230320-0005', '상태': '등록', '등록자': '조영옥 (young-ok.cho@mercedes-benz.co...
     최종 작성자: NaN

  5. 문서 ID: 637074c2-8b6f-4c24-895f-256e2139ae14
     파일명: N/A
     보관자: 세진 김
     생성일: N/A
     발송일: 1900-01-01 00:00:00+00:00
     발신자: NaN
     수신자: NaN
     확장자: csv
     내용 미리보기: {'*ID': 259189, '*docNo': 'otov-230309-0002', '상태': '등록', '등록자': '김창훈 (chang-hoon.kim@mercedes-benz....
     최종 작성자: NaN


================================================================================

테스트 케이스 2: Dimitris Psillakis가 작성한 모든 문서를 찾아주세요
------------------------------------------------------------
2025-09-12 16:21:30,091 - mcp_tools - INFO - 🔍 필터 추출 시작: 'Dimitris Psillakis가 작성한 모든 문서를 찾아주세요'
2025-09-12 16:21:31,741 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 16:21:31,742 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 16:21:31,742 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 16:21:31,824 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 16:21:31,825 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 16:21:31,905 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 16:21:31,906 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 16:21:32,005 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 16:21:32,006 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 16:21:32,088 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 16:21:32,089 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 16:21:32,360 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 16:21:32,361 - mcp_tools - INFO - ℹ️ last_author 필드에 대한 유사한 이름을 찾을 수 없음: 'Dimitris Psillakis'
2025-09-12 16:21:32,361 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author='Dimitris Psillakis' extension=None
📊 추출된 필터:
  - custodian: None
  - ori_file_name: None
  - s_created_date: None
  - sent_date: None
  - from_email: None
  - to_email: None
  - cc: None
  - bcc: None
  - last_author: Dimitris Psillakis
  - extension: None
🔍 검색 방식: similarity
💭 판단 근거: 질의에서 구체적인 필터 정보를 찾았지만 단일 필터이므로 유사도 기반 검색을 사용합니다.
📋 검색에 사용할 필터: {'last_author': 'Dimitris Psillakis'}
2025-09-12 16:21:32,362 - mcp_tools - INFO - 🔍 필터 검색 실행: class_name=DocumentChunk, limit=5, filters={'last_author': 'Dimitris Psillakis'}
2025-09-12 16:21:32,362 - kars_db - INFO - 필터 검색 시작: class_name=DocumentChunk, limit=5, filters={'last_author': 'Dimitris Psillakis'}
2025-09-12 16:21:32,363 - kars_db - INFO - 필터와 함께 검색: {'last_author': 'Dimitris Psillakis'}
2025-09-12 16:21:32,365 - kars_db - INFO - ✅ 필터 검색 완료: 0개 결과 반환
📊 검색 결과:
  - 성공 여부: True
  - 총 결과 수: 0개
  - 검색 방식: N/A
  - 사용된 필터: N/A
  📭 검색 결과가 없습니다.

================================================================================

테스트 케이스 3: Lee Sang-kuk이 언급된 모든 이메일을 찾아주세요
------------------------------------------------------------
2025-09-12 16:21:32,366 - mcp_tools - INFO - 🔍 필터 추출 시작: 'Lee Sang-kuk이 언급된 모든 이메일을 찾아주세요'
2025-09-12 16:21:33,866 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 16:21:33,868 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 16:21:33,868 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 16:21:33,951 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 16:21:33,952 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 16:21:34,033 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 16:21:34,033 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 16:21:34,113 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 16:21:34,114 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 16:21:34,184 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 16:21:34,184 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 16:21:34,184 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
📊 추출된 필터:
  - custodian: None
  - ori_file_name: None
  - s_created_date: None
  - sent_date: None
  - from_email: None
  - to_email: None
  - cc: None
  - bcc: None
  - last_author: None
  - extension: None
🔍 검색 방식: similarity
💭 판단 근거: 질의에서 구체적인 필터 정보를 찾을 수 없어 유사도 기반 검색을 사용합니다.
  📭 검색할 필터가 없어 단순 RAG 검색을 수행합니다.
2025-09-12 16:21:34,185 - mcp_tools - INFO - 🔍 단순 RAG 검색 실행: 'Lee Sang-kuk이 언급된 모든 이메일을 찾아주세요' (limit: 5)
2025-09-12 16:21:34,185 - kars_db - INFO - 🔍 검색 시작: 'Lee Sang-kuk이 언급된 모든 이메일을 찾아주세요' (limit: 5)
2025-09-12 16:21:34,241 - weaviate_db - INFO - 🔍 검색 완료: 5개 결과 (쿼리: 'Lee Sang-kuk이 언급된 모든 이메일을 찾아주세요'
2025-09-12 16:21:34,241 - kars_db - INFO - ✅ 검색 완료: 5개 결과 반환
📊 RAG 검색 결과:
  - 성공 여부: True
  - 총 결과 수: 5개
  - 검색 방식: N/A

📄 검색된 문서들:
  1. 문서 ID: 9f40c789-b76f-4f67-aa8d-be1b68f783a2
     파일명: MBK-ND  CSI Newsletter Vol 16.msg
     내용 미리보기: From:Kim, Young-Jin (191) on behalf of MBK-ND (191-NPM)
Sent:Fri 11/15/2019
To:dw_191-MBK_all
Cc:Ch...

  2. 문서 ID: 2989a80b-1949-4598-9f17-71cdda1e0e86
     파일명: Request for information from National Assemblyman about EQE 350+ Thermal Incident case.msg
     내용 미리보기: From:Han, Sung-Ho (191)
Sent:Thu 8/08/2024
To:Maurer, Jan-Philipp (059); Gmoser, Michael (059); Lie...

  3. 문서 ID: 78fccbc7-9c35-4f7b-ba78-4c12a53930c6
     파일명: Answer # 38  EQE 350+ battery cell.msg
     내용 미리보기: From:Lieb, Sven (059)
Sent:Fri 9/06/2024
To:Kim, Young-Joon (191); Han, Sung-Ho (191); Kim, Doosun ...

  4. 문서 ID: 872b35fc-f9bd-443a-bd7a-80319f1d9f86
     파일명: Answer #41 NA  Battery cell supplier for German and Chinese market.msg
     내용 미리보기: From:Lieb, Sven (059)
Sent:Mon 9/09/2024
To:Kim, Young-Joon (191); Han, Sung-Ho (191); Kim, Doosun ...

  5. 문서 ID: 18a4585b-b4db-47c6-9c48-11fd87488707
     파일명: RE EV Südkorea  EQE 500 4MATIC SUV (including upcoming EVA2 model).msg
     내용 미리보기: From:Kim, Young-Joon (191)
Sent:Thu 9/05/2024
To:Lee, Jin-Won (191)
Cc:Kwak, Dio (191); Lieb, Sven ...


================================================================================

테스트 케이스 4: SOCAR 관련 모든 문서들
------------------------------------------------------------
2025-09-12 16:21:34,241 - mcp_tools - INFO - 🔍 필터 추출 시작: 'SOCAR 관련 모든 문서들'
2025-09-12 16:21:35,740 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 16:21:35,742 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 16:21:35,742 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 16:21:35,825 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 16:21:35,826 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 16:21:35,908 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 16:21:35,908 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 16:21:35,982 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 16:21:35,982 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 16:21:36,060 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 16:21:36,061 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 16:21:36,061 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
📊 추출된 필터:
  - custodian: None
  - ori_file_name: None
  - s_created_date: None
  - sent_date: None
  - from_email: None
  - to_email: None
  - cc: None
  - bcc: None
  - last_author: None
  - extension: None
🔍 검색 방식: similarity
💭 판단 근거: 질의에서 구체적인 필터 정보를 찾을 수 없어 유사도 기반 검색을 사용합니다.
  📭 검색할 필터가 없어 단순 RAG 검색을 수행합니다.
2025-09-12 16:21:36,061 - mcp_tools - INFO - 🔍 단순 RAG 검색 실행: 'SOCAR 관련 모든 문서들' (limit: 5)
2025-09-12 16:21:36,061 - kars_db - INFO - 🔍 검색 시작: 'SOCAR 관련 모든 문서들' (limit: 5)
2025-09-12 16:21:36,151 - weaviate_db - INFO - 🔍 검색 완료: 5개 결과 (쿼리: 'SOCAR 관련 모든 문서들'
2025-09-12 16:21:36,151 - kars_db - INFO - ✅ 검색 완료: 5개 결과 반환
📊 RAG 검색 결과:
  - 성공 여부: True
  - 총 결과 수: 5개
  - 검색 방식: N/A

📄 검색된 문서들:
  1. 문서 ID: d88d5e04-dfa0-4da5-8787-5cb00a0bccd9
     파일명: Microsoft_Excel_Worksheet5.xlsx
     내용 미리보기:  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
...

  2. 문서 ID: be123ea2-f72d-4f50-ab4c-37013c71f018
     파일명: Microsoft_Excel_Worksheet5.xlsx
     내용 미리보기:  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
...

  3. 문서 ID: ba737986-4809-472c-83b1-b50d8155e5df
     파일명: Microsoft_Excel_Worksheet5.xlsx
     내용 미리보기:  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
...

  4. 문서 ID: b5ecd1e5-9a88-483f-9c81-065cc742a6b9
     파일명: Microsoft_Excel_Worksheet5.xlsx
     내용 미리보기:  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
...

  5. 문서 ID: abfd342d-560f-4b2a-a8a5-714d18ed1b3b
     파일명: Microsoft_Excel_Worksheet5.xlsx
     내용 미리보기:  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
...


================================================================================

테스트 케이스 5: 메르세데스-벤츠 코리아 홍보팀이 작성한 문서들
------------------------------------------------------------
2025-09-12 16:21:36,152 - mcp_tools - INFO - 🔍 필터 추출 시작: '메르세데스-벤츠 코리아 홍보팀이 작성한 문서들'
2025-09-12 16:21:38,047 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 16:21:38,048 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 16:21:38,048 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 16:21:38,130 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 16:21:38,130 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 16:21:38,203 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 16:21:38,204 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 16:21:38,281 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 16:21:38,281 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 16:21:38,359 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 16:21:38,359 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 16:21:39,559 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 16:21:39,561 - mcp_tools - INFO - ✅ custodian 필드 수정: '메르세데스-벤츠 코리아 홍보팀' → '세진 김' (유사도: 30.00)
2025-09-12 16:21:39,561 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian='세진 김' ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
📊 추출된 필터:
  - custodian: 세진 김
  - ori_file_name: None
  - s_created_date: None
  - sent_date: None
  - from_email: None
  - to_email: None
  - cc: None
  - bcc: None
  - last_author: None
  - extension: None
🔍 검색 방식: similarity
💭 판단 근거: 질의에서 구체적인 필터 정보를 찾았지만 단일 필터이므로 유사도 기반 검색을 사용합니다.
📋 검색에 사용할 필터: {'custodian': '세진 김'}
2025-09-12 16:21:39,561 - mcp_tools - INFO - 🔍 필터 검색 실행: class_name=DocumentChunk, limit=5, filters={'custodian': '세진 김'}
2025-09-12 16:21:39,562 - kars_db - INFO - 필터 검색 시작: class_name=DocumentChunk, limit=5, filters={'custodian': '세진 김'}
2025-09-12 16:21:39,562 - kars_db - INFO - 필터와 함께 검색: {'custodian': '세진 김'}
2025-09-12 16:21:39,574 - kars_db - INFO - ✅ 필터 검색 완료: 5개 결과 반환
📊 검색 결과:
  - 성공 여부: True
  - 총 결과 수: 5개
  - 검색 방식: N/A
  - 사용된 필터: N/A

📄 검색된 문서들:
  1. 문서 ID: 84e3b894-4f16-4b8d-bf39-5bbcd95837b2
     파일명: N/A
     보관자: 세진 김
     생성일: N/A
     발송일: 1900-01-01 00:00:00+00:00
     발신자: NaN
     수신자: NaN
     확장자: csv
     내용 미리보기: {'*ID': 260381, '*docNo': 'otov-230327-0001', '상태': '등록', '등록자': '홍성진 (hsj@mercedes-benz.com)', '딜러사...
     최종 작성자: NaN

  2. 문서 ID: 6a1eca77-af00-4be9-96d6-dc28a1a68b7a
     파일명: N/A
     보관자: 세진 김
     생성일: N/A
     발송일: 1900-01-01 00:00:00+00:00
     발신자: NaN
     수신자: NaN
     확장자: csv
     내용 미리보기: {'*ID': 260452, '*docNo': 'otov-230327-0002', '상태': '등록', '등록자': '최하정 (ha-jeong.choi@mercedes-benz.c...
     최종 작성자: NaN

  3. 문서 ID: 9e25d34e-9fd9-4a4e-a966-3a4abed89cb4
     파일명: N/A
     보관자: 세진 김
     생성일: N/A
     발송일: 1900-01-01 00:00:00+00:00
     발신자: NaN
     수신자: NaN
     확장자: csv
     내용 미리보기: {'*ID': 259876, '*docNo': 'otov-230320-0002', '상태': '등록', '등록자': '이윤희 (youn-hee.lee@mercedes-benz.co...
     최종 작성자: NaN

  4. 문서 ID: ee730a17-2b97-4d51-a901-99d74fd56e49
     파일명: N/A
     보관자: 세진 김
     생성일: N/A
     발송일: 1900-01-01 00:00:00+00:00
     발신자: NaN
     수신자: NaN
     확장자: csv
     내용 미리보기: {'*ID': 259922, '*docNo': 'otov-230320-0005', '상태': '등록', '등록자': '조영옥 (young-ok.cho@mercedes-benz.co...
     최종 작성자: NaN

  5. 문서 ID: 637074c2-8b6f-4c24-895f-256e2139ae14
     파일명: N/A
     보관자: 세진 김
     생성일: N/A
     발송일: 1900-01-01 00:00:00+00:00
     발신자: NaN
     수신자: NaN
     확장자: csv
     내용 미리보기: {'*ID': 259189, '*docNo': 'otov-230309-0002', '상태': '등록', '등록자': '김창훈 (chang-hoon.kim@mercedes-benz....
     최종 작성자: NaN


================================================================================

테스트 케이스 6: EQC 전기차 관련 모든 자료
------------------------------------------------------------
2025-09-12 16:21:39,575 - mcp_tools - INFO - 🔍 필터 추출 시작: 'EQC 전기차 관련 모든 자료'
2025-09-12 16:21:41,082 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 16:21:41,083 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 16:21:41,084 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 16:21:41,156 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 16:21:41,156 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 16:21:41,217 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 16:21:41,217 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 16:21:41,294 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 16:21:41,294 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 16:21:41,358 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 16:21:41,358 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 16:21:41,358 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
📊 추출된 필터:
  - custodian: None
  - ori_file_name: None
  - s_created_date: None
  - sent_date: None
  - from_email: None
  - to_email: None
  - cc: None
  - bcc: None
  - last_author: None
  - extension: None
🔍 검색 방식: similarity
💭 판단 근거: 질의에서 구체적인 필터 정보를 찾을 수 없어 유사도 기반 검색을 사용합니다.
  📭 검색할 필터가 없어 단순 RAG 검색을 수행합니다.
2025-09-12 16:21:41,358 - mcp_tools - INFO - 🔍 단순 RAG 검색 실행: 'EQC 전기차 관련 모든 자료' (limit: 5)
2025-09-12 16:21:41,358 - kars_db - INFO - 🔍 검색 시작: 'EQC 전기차 관련 모든 자료' (limit: 5)
2025-09-12 16:21:41,407 - weaviate_db - INFO - 🔍 검색 완료: 5개 결과 (쿼리: 'EQC 전기차 관련 모든 자료'
2025-09-12 16:21:41,407 - kars_db - INFO - ✅ 검색 완료: 5개 결과 반환
📊 RAG 검색 결과:
  - 성공 여부: True
  - 총 결과 수: 5개
  - 검색 방식: N/A

📄 검색된 문서들:
  1. 문서 ID: 7726899e-4d43-4746-b7ff-90b2b4bef517
     파일명: 2019_11_07_Dealer_circular_MY20_The_new_EQC_ver._.pdf
     내용 미리보기: 메르세데스-벤츠 코리아(주)의 사전 동의 없이 외부 기업이나 개인에게 무단 배포하거나 복사할 수 없습니다. 전기차 충전소 정보 " 전기차 충전소 위치, 이용 가능 시간, 현재 이용...

  2. 문서 ID: 64d24a13-d470-4cb1-8de2-4148662a567c
     파일명: 2019_12_02_Dealer_circular_MY20_The_new_EQC_ver.6.pdf
     내용 미리보기: 메르세데스-벤츠 코리아(주)의 사전 동의 없이 외부 기업이나 개인에게 무단 배포하거나 복사할 수 없습니다. 전기차 충전소 정보 " 전기차 충전소 위치, 이용 가능 시간, 현재 이용...

  3. 문서 ID: a0452118-e1e5-4075-97d4-782e812327a6
     파일명: 2019_10_28_Dealer_circular_MY20_The_new_EQC_ver.3.pdf
     내용 미리보기: 메르세데스-벤츠 코리아(주)의 사전 동의 없이 외부 기업이나 개인에게 무단 배포하거나 복사할 수 없습니다. EQ 전용 내비게이션 " 충전 된 배터리 양을 바탕으로 최적의 길을 안내...

  4. 문서 ID: 58329035-2512-46b1-b975-d4f7a6d2f6dc
     파일명: Mercedes-Benz_EQC_Catalogue_20210108.pdf
     내용 미리보기: The new EQC2021년 1월 8일 기준 업데이트된 컨텐츠 입니다.Mercedes-BenzThe new EQC in detailIndexFacts & ColoursSafety...

  5. 문서 ID: 5d10fc9a-4d30-4cb7-9fa3-45adeb74e7bb
     파일명: 2019_10_28_Dealer_circular_MY20_The_new_EQC_ver.3.pdf
     내용 미리보기: (page\s+\d+) of 38 Dealer Circular에 기재된 정보 및 이미지는 메르세데스-벤츠 공식 판매 및 영업사원, 메르세데스-벤츠 직원들을 위한 것으로 메르세데스-...


================================================================================

테스트 케이스 7: SOCAR와의 카셰어링 협력 관련 자료
------------------------------------------------------------
2025-09-12 16:21:41,408 - mcp_tools - INFO - 🔍 필터 추출 시작: 'SOCAR와의 카셰어링 협력 관련 자료'
2025-09-12 16:21:42,916 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 16:21:42,917 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 16:21:42,917 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 16:21:42,993 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 16:21:42,993 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 16:21:43,059 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 16:21:43,060 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 16:21:43,140 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 16:21:43,140 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 16:21:43,209 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 16:21:43,209 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 16:21:43,209 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
📊 추출된 필터:
  - custodian: None
  - ori_file_name: None
  - s_created_date: None
  - sent_date: None
  - from_email: None
  - to_email: None
  - cc: None
  - bcc: None
  - last_author: None
  - extension: None
🔍 검색 방식: similarity
💭 판단 근거: 질의에서 구체적인 필터 정보를 찾을 수 없어 유사도 기반 검색을 사용합니다.
  📭 검색할 필터가 없어 단순 RAG 검색을 수행합니다.
2025-09-12 16:21:43,209 - mcp_tools - INFO - 🔍 단순 RAG 검색 실행: 'SOCAR와의 카셰어링 협력 관련 자료' (limit: 5)
2025-09-12 16:21:43,209 - kars_db - INFO - 🔍 검색 시작: 'SOCAR와의 카셰어링 협력 관련 자료' (limit: 5)
2025-09-12 16:21:43,250 - weaviate_db - INFO - 🔍 검색 완료: 5개 결과 (쿼리: 'SOCAR와의 카셰어링 협력 관련 자료'
2025-09-12 16:21:43,250 - kars_db - INFO - ✅ 검색 완료: 5개 결과 반환
📊 RAG 검색 결과:
  - 성공 여부: True
  - 총 결과 수: 5개
  - 검색 방식: N/A

📄 검색된 문서들:
  1. 문서 ID: 46b2a513-9392-4a8a-88a3-7c00f24fcfae
     파일명: 2024 08 12 Issue Report_Cheongna Thermal Incident_v12_F.pptx
     내용 미리보기:  Article – Support from SOCAR8SOCAR to provide 100 support vehicles to residents affected by recent ...

  2. 문서 ID: 3774fab8-b8e6-4138-a5c3-e8cbf9310ad3
     파일명: 2024 08 13 Issue Report_Cheongna Thermal Incident_v13 (1).pptx
     내용 미리보기: n at 10 different temporary shelters as of 11 a.m. on August 9.Yonhap News (Aug. 10)Summary of Repre...

  3. 문서 ID: b2678df2-3e9b-4c02-9140-d3ecf1055d50
     파일명: 2024 08 14 Issue Report_Cheongna Thermal Incident_v14.pptx
     내용 미리보기: (Page\s+\d+)
Summary of Representative Article – Support from SOCAR19SOCAR to provide 100 support v...

  4. 문서 ID: 812cfd8c-c12d-4ddc-b134-154024f0f710
     파일명: 2024 08 19 Issue Report_Cheongna Thermal Incident_v17.pptx
     내용 미리보기: ill provide 100 free monthly car-sharing service SOCAR Plan vehicles for a month to residents who ar...

  5. 문서 ID: f3ee6fb4-bece-4d4f-ac91-5cdc33fafce7
     파일명: 2024 08 19 Issue Report_Cheongna Thermal Incident_v17.pptx
     내용 미리보기: vehicles in Korea disclose battery supplier information. The website of the Motor Vehicle Recall Cen...


================================================================================

테스트 케이스 8: MBUX 시스템 관련 기술 자료
------------------------------------------------------------
2025-09-12 16:21:43,250 - mcp_tools - INFO - 🔍 필터 추출 시작: 'MBUX 시스템 관련 기술 자료'
2025-09-12 16:21:44,758 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 16:21:44,759 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 16:21:44,760 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 16:21:44,836 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 16:21:44,836 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 16:21:44,911 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 16:21:44,911 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 16:21:44,979 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 16:21:44,979 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 16:21:45,058 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 16:21:45,058 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 16:21:45,058 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
📊 추출된 필터:
  - custodian: None
  - ori_file_name: None
  - s_created_date: None
  - sent_date: None
  - from_email: None
  - to_email: None
  - cc: None
  - bcc: None
  - last_author: None
  - extension: None
🔍 검색 방식: similarity
💭 판단 근거: 질의에서 구체적인 필터 정보를 찾을 수 없어 유사도 기반 검색을 사용합니다.
  📭 검색할 필터가 없어 단순 RAG 검색을 수행합니다.
2025-09-12 16:21:45,058 - mcp_tools - INFO - 🔍 단순 RAG 검색 실행: 'MBUX 시스템 관련 기술 자료' (limit: 5)
2025-09-12 16:21:45,059 - kars_db - INFO - 🔍 검색 시작: 'MBUX 시스템 관련 기술 자료' (limit: 5)
2025-09-12 16:21:45,128 - weaviate_db - INFO - 🔍 검색 완료: 5개 결과 (쿼리: 'MBUX 시스템 관련 기술 자료'
2025-09-12 16:21:45,128 - kars_db - INFO - ✅ 검색 완료: 5개 결과 반환
📊 RAG 검색 결과:
  - 성공 여부: True
  - 총 결과 수: 5개
  - 검색 방식: N/A

📄 검색된 문서들:
  1. 문서 ID: 5a75ffa7-f9c8-40e8-8c3f-7f868765e5e5
     파일명: 2905841802_buchblock.pdf
     내용 미리보기: /빼기(실내 방향 시스템) ..... 116설정(MBUX 멀티미디어 시스템) ............... 114송풍 방향 설정 ................................

  2. 문서 ID: b62ff4bc-1e27-4613-a562-e79082282e13
     파일명: _-20_GLC_MY20_GLC_dealer_circular_ver._ (1).pdf
     내용 미리보기: 메르세데스-벤츠 코리아(주)의 사전 동의 없이 외부 기업이나 개인에게 무단 배포하거나 복사할 수 없습니다. MBUX Multimedia, NTG 6 (355) 메르세데스-벤츠의 새...

  3. 문서 ID: 5841d6e1-719e-470c-a3ca-1e74181d33ab
     파일명: 2-20_MY20_GLC_dealer_circular_ver.2.pdf
     내용 미리보기: 메르세데스-벤츠 코리아(주)의 사전 동의 없이 외부 기업이나 개인에게 무단 배포하거나 복사할 수 없습니다. MBUX Multimedia, NTG 6 (355) 메르세데스-벤츠의 새...

  4. 문서 ID: 3f8d9670-5d50-4263-9bbe-f55967cfe5e4
     파일명: 1-20_MY20_GLC_dealer_circular_ver.1.pdf
     내용 미리보기: 메르세데스-벤츠 코리아(주)의 사전 동의 없이 외부 기업이나 개인에게 무단 배포하거나 복사할 수 없습니다. MBUX Multimedia, NTG 6 (355) 메르세데스-벤츠의 새...

  5. 문서 ID: bd9a354d-8cca-4512-8088-76f4c8336270
     파일명: 2905841802_buchblock.pdf
     내용 미리보기:  ........................... 65닫기 ....................................................... 63열기 ........


================================================================================

테스트 케이스 9: 4MATIC 사륜구동 시스템 관련 자료
------------------------------------------------------------
2025-09-12 16:21:45,129 - mcp_tools - INFO - 🔍 필터 추출 시작: '4MATIC 사륜구동 시스템 관련 자료'
2025-09-12 16:21:46,636 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 16:21:46,637 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 16:21:46,638 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 16:21:46,720 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 16:21:46,720 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 16:21:46,796 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 16:21:46,797 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 16:21:46,867 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 16:21:46,867 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 16:21:46,938 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 16:21:46,939 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 16:21:46,939 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
📊 추출된 필터:
  - custodian: None
  - ori_file_name: None
  - s_created_date: None
  - sent_date: None
  - from_email: None
  - to_email: None
  - cc: None
  - bcc: None
  - last_author: None
  - extension: None
🔍 검색 방식: similarity
💭 판단 근거: 질의에서 구체적인 필터 정보를 찾을 수 없어 유사도 기반 검색을 사용합니다.
  📭 검색할 필터가 없어 단순 RAG 검색을 수행합니다.
2025-09-12 16:21:46,939 - mcp_tools - INFO - 🔍 단순 RAG 검색 실행: '4MATIC 사륜구동 시스템 관련 자료' (limit: 5)
2025-09-12 16:21:46,939 - kars_db - INFO - 🔍 검색 시작: '4MATIC 사륜구동 시스템 관련 자료' (limit: 5)
2025-09-12 16:21:46,985 - weaviate_db - INFO - 🔍 검색 완료: 5개 결과 (쿼리: '4MATIC 사륜구동 시스템 관련 자료'
2025-09-12 16:21:46,985 - kars_db - INFO - ✅ 검색 완료: 5개 결과 반환
📊 RAG 검색 결과:
  - 성공 여부: True
  - 총 결과 수: 5개
  - 검색 방식: N/A

📄 검색된 문서들:
  1. 문서 ID: dadccea7-c2be-4cfe-b694-9407897e6042
     파일명: 2020 03 31 WVX222 MY20 S-Class (ver.15).pdf
     내용 미리보기: page 67 of 100 Dealer Circular에 기재된 정보 및 이미지는 메르세데스-벤츠 공식 판매 및 영업사원, 메르세데스-벤츠 직원들을 위한 것으로 메르세데스-벤츠 코...

  2. 문서 ID: 09f47ac9-a4f0-4e73-aab4-147ed30a7033
     파일명: 2020 03 31 WVX222 MY20 S-Class (ver.15).pdf
     내용 미리보기: page 17 of 100 Dealer Circular에 기재된 정보 및 이미지는 메르세데스-벤츠 공식 판매 및 영업사원, 메르세데스-벤츠 직원들을 위한 것으로 메르세데스-벤츠 코...

  3. 문서 ID: 66835a14-be70-40c1-9306-1b37464c8d4a
     파일명: 2020 03 31 WVX222 MY20 S-Class (ver.15).pdf
     내용 미리보기: page 11 of 100 Dealer Circular에 기재된 정보 및 이미지는 메르세데스-벤츠 공식 판매 및 영업사원, 메르세데스-벤츠 직원들을 위한 것으로 메르세데스-벤츠 코...

  4. 문서 ID: 26aec033-3016-4d83-a5b3-a3dd04478d7f
     파일명: 2019_10_29_WVX222_MY20_S-Class_(ver.1).pdf
     내용 미리보기: t S S오디오 COMAND Online COMAND Online음향 시스템 부메스터® 서라운드 부메스터® 서라운드 Touchpad Controller S SHead Up Disp...

  5. 문서 ID: 89f5d419-3caa-48b7-a67c-731c1de0005a
     파일명: 2020 03 31 WVX222 MY20 S-Class (ver.15).pdf
     내용 미리보기: page 19 of 100 Dealer Circular에 기재된 정보 및 이미지는 메르세데스-벤츠 공식 판매 및 영업사원, 메르세데스-벤츠 직원들을 위한 것으로 메르세데스-벤츠 코...


================================================================================

테스트 케이스 10: 2020년에 작성된 EQC 관련 문서들
------------------------------------------------------------
2025-09-12 16:21:46,986 - mcp_tools - INFO - 🔍 필터 추출 시작: '2020년에 작성된 EQC 관련 문서들'
2025-09-12 16:21:48,694 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 16:21:48,696 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 16:21:48,696 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 16:21:48,770 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 16:21:48,771 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 16:21:48,832 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 16:21:48,832 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 16:21:48,892 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 16:21:48,893 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 16:21:48,962 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 16:21:48,962 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 16:21:48,962 - mcp_tools - INFO - ✅ 필터 추출 완료: filter 검색, 필터: custodian=None ori_file_name='EQC 관련 문서들' s_created_date={'gte': '2020-01-01T00:00:00Z', 'lt': '2021-01-01T00:00:00Z'} sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
📊 추출된 필터:
  - custodian: None
  - ori_file_name: EQC 관련 문서들
  - s_created_date: {'gte': '2020-01-01T00:00:00Z', 'lt': '2021-01-01T00:00:00Z'}
  - sent_date: None
  - from_email: None
  - to_email: None
  - cc: None
  - bcc: None
  - last_author: None
  - extension: None
🔍 검색 방식: filter
💭 판단 근거: 질의에서 2개의 구체적인 필터 정보를 찾았습니다: ['ori_file_name', 's_created_date']. 조건 필터링을 사용합니다.
📋 검색에 사용할 필터: {'ori_file_name': 'EQC 관련 문서들', 's_created_date': {'gte': '2020-01-01T00:00:00Z', 'lt': '2021-01-01T00:00:00Z'}}
2025-09-12 16:21:48,962 - mcp_tools - INFO - 🔍 필터 검색 실행: class_name=DocumentChunk, limit=5, filters={'ori_file_name': 'EQC 관련 문서들', 's_created_date': {'gte': '2020-01-01T00:00:00Z', 'lt': '2021-01-01T00:00:00Z'}}
2025-09-12 16:21:48,962 - kars_db - INFO - 필터 검색 시작: class_name=DocumentChunk, limit=5, filters={'ori_file_name': 'EQC 관련 문서들', 's_created_date': {'gte': '2020-01-01T00:00:00Z', 'lt': '2021-01-01T00:00:00Z'}}
2025-09-12 16:21:48,963 - kars_db - INFO - 필터와 함께 검색: {'ori_file_name': 'EQC 관련 문서들', 's_created_date': {'gte': '2020-01-01T00:00:00Z', 'lt': '2021-01-01T00:00:00Z'}}
2025-09-12 16:21:48,965 - kars_db - INFO - ✅ 필터 검색 완료: 0개 결과 반환
📊 검색 결과:
  - 성공 여부: True
  - 총 결과 수: 0개
  - 검색 방식: N/A
  - 사용된 필터: N/A
  📭 검색 결과가 없습니다.

================================================================================

테스트 케이스 11: Dimitris Psillakis가 언급한 전기차 전략
------------------------------------------------------------
2025-09-12 16:21:48,965 - mcp_tools - INFO - 🔍 필터 추출 시작: 'Dimitris Psillakis가 언급한 전기차 전략'
2025-09-12 16:21:50,626 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 16:21:50,628 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 16:21:50,628 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 16:21:50,702 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 16:21:50,702 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 16:21:50,774 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 16:21:50,774 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 16:21:50,833 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 16:21:50,833 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 16:21:50,896 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 16:21:50,896 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 16:21:54,533 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 16:21:54,534 - mcp_tools - INFO - ✅ last_author 필드 수정: 'Dimitris Psillakis' → 'Dimitris Psillakis' (유사도: 100.00)
2025-09-12 16:21:54,535 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author='Dimitris Psillakis' extension=None
📊 추출된 필터:
  - custodian: None
  - ori_file_name: None
  - s_created_date: None
  - sent_date: None
  - from_email: None
  - to_email: None
  - cc: None
  - bcc: None
  - last_author: Dimitris Psillakis
  - extension: None
🔍 검색 방식: similarity
💭 판단 근거: 질의에서 구체적인 필터 정보를 찾았지만 단일 필터이므로 유사도 기반 검색을 사용합니다.
📋 검색에 사용할 필터: {'last_author': 'Dimitris Psillakis'}
2025-09-12 16:21:54,535 - mcp_tools - INFO - 🔍 필터 검색 실행: class_name=DocumentChunk, limit=5, filters={'last_author': 'Dimitris Psillakis'}
2025-09-12 16:21:54,535 - kars_db - INFO - 필터 검색 시작: class_name=DocumentChunk, limit=5, filters={'last_author': 'Dimitris Psillakis'}
2025-09-12 16:21:54,536 - kars_db - INFO - 필터와 함께 검색: {'last_author': 'Dimitris Psillakis'}
2025-09-12 16:21:54,538 - kars_db - INFO - ✅ 필터 검색 완료: 0개 결과 반환
📊 검색 결과:
  - 성공 여부: True
  - 총 결과 수: 0개
  - 검색 방식: N/A
  - 사용된 필터: N/A
  📭 검색 결과가 없습니다.

================================================================================

테스트 케이스 12: SOCAR 협력 관련 2020년 6월 문서
------------------------------------------------------------
2025-09-12 16:21:54,538 - mcp_tools - INFO - 🔍 필터 추출 시작: 'SOCAR 협력 관련 2020년 6월 문서'
2025-09-12 16:21:57,283 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 16:21:57,285 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 16:21:57,285 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 16:21:57,359 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 16:21:57,359 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 16:21:57,420 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 16:21:57,420 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 16:21:57,510 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 16:21:57,510 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 16:21:57,579 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 16:21:57,579 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 16:21:57,579 - mcp_tools - INFO - ✅ 필터 추출 완료: filter 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date={'gte': '2020-06-01T00:00:00Z', 'lt': '2020-07-01T00:00:00Z'} from_email=None to_email=None cc=None bcc=None last_author=None extension=None
📊 추출된 필터:
  - custodian: None
  - ori_file_name: None
  - s_created_date: None
  - sent_date: {'gte': '2020-06-01T00:00:00Z', 'lt': '2020-07-01T00:00:00Z'}
  - from_email: None
  - to_email: None
  - cc: None
  - bcc: None
  - last_author: None
  - extension: None
🔍 검색 방식: filter
💭 판단 근거: 질의에서 구체적인 날짜 정보 'sent_date: {'gte': '2020-06-01T00:00:00Z', 'lt': '2020-07-01T00:00:00Z'}'를 찾았습니다. 조건 필터링을 사용합니다.
📋 검색에 사용할 필터: {'sent_date': {'gte': '2020-06-01T00:00:00Z', 'lt': '2020-07-01T00:00:00Z'}}
2025-09-12 16:21:57,580 - mcp_tools - INFO - 🔍 필터 검색 실행: class_name=DocumentChunk, limit=5, filters={'sent_date': {'gte': '2020-06-01T00:00:00Z', 'lt': '2020-07-01T00:00:00Z'}}
2025-09-12 16:21:57,580 - kars_db - INFO - 필터 검색 시작: class_name=DocumentChunk, limit=5, filters={'sent_date': {'gte': '2020-06-01T00:00:00Z', 'lt': '2020-07-01T00:00:00Z'}}
2025-09-12 16:21:57,580 - kars_db - INFO - 필터와 함께 검색: {'sent_date': {'gte': '2020-06-01T00:00:00Z', 'lt': '2020-07-01T00:00:00Z'}}
2025-09-12 16:21:57,587 - kars_db - INFO - ✅ 필터 검색 완료: 5개 결과 반환
📊 검색 결과:
  - 성공 여부: True
  - 총 결과 수: 5개
  - 검색 방식: N/A
  - 사용된 필터: N/A

📄 검색된 문서들:
  1. 문서 ID: 84e3b894-4f16-4b8d-bf39-5bbcd95837b2
     파일명: N/A
     보관자: 세진 김
     생성일: N/A
     발송일: 1900-01-01 00:00:00+00:00
     발신자: NaN
     수신자: NaN
     확장자: csv
     내용 미리보기: {'*ID': 260381, '*docNo': 'otov-230327-0001', '상태': '등록', '등록자': '홍성진 (hsj@mercedes-benz.com)', '딜러사...
     최종 작성자: NaN

  2. 문서 ID: 6a1eca77-af00-4be9-96d6-dc28a1a68b7a
     파일명: N/A
     보관자: 세진 김
     생성일: N/A
     발송일: 1900-01-01 00:00:00+00:00
     발신자: NaN
     수신자: NaN
     확장자: csv
     내용 미리보기: {'*ID': 260452, '*docNo': 'otov-230327-0002', '상태': '등록', '등록자': '최하정 (ha-jeong.choi@mercedes-benz.c...
     최종 작성자: NaN

  3. 문서 ID: 9e25d34e-9fd9-4a4e-a966-3a4abed89cb4
     파일명: N/A
     보관자: 세진 김
     생성일: N/A
     발송일: 1900-01-01 00:00:00+00:00
     발신자: NaN
     수신자: NaN
     확장자: csv
     내용 미리보기: {'*ID': 259876, '*docNo': 'otov-230320-0002', '상태': '등록', '등록자': '이윤희 (youn-hee.lee@mercedes-benz.co...
     최종 작성자: NaN

  4. 문서 ID: ee730a17-2b97-4d51-a901-99d74fd56e49
     파일명: N/A
     보관자: 세진 김
     생성일: N/A
     발송일: 1900-01-01 00:00:00+00:00
     발신자: NaN
     수신자: NaN
     확장자: csv
     내용 미리보기: {'*ID': 259922, '*docNo': 'otov-230320-0005', '상태': '등록', '등록자': '조영옥 (young-ok.cho@mercedes-benz.co...
     최종 작성자: NaN

  5. 문서 ID: 637074c2-8b6f-4c24-895f-256e2139ae14
     파일명: N/A
     보관자: 세진 김
     생성일: N/A
     발송일: 1900-01-01 00:00:00+00:00
     발신자: NaN
     수신자: NaN
     확장자: csv
     내용 미리보기: {'*ID': 259189, '*docNo': 'otov-230309-0002', '상태': '등록', '등록자': '김창훈 (chang-hoon.kim@mercedes-benz....
     최종 작성자: NaN


================================================================================

테스트 케이스 13: 메르세데스-벤츠 코리아 홍보팀의 EQC 관련 자료
------------------------------------------------------------
2025-09-12 16:21:57,587 - mcp_tools - INFO - 🔍 필터 추출 시작: '메르세데스-벤츠 코리아 홍보팀의 EQC 관련 자료'
2025-09-12 16:21:59,644 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 16:21:59,646 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 16:21:59,646 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 16:21:59,721 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 16:21:59,721 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 16:21:59,784 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 16:21:59,784 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 16:21:59,845 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 16:21:59,845 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 16:21:59,904 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 16:21:59,904 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 16:22:01,126 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 16:22:01,127 - mcp_tools - INFO - ✅ custodian 필드 수정: '메르세데스-벤츠 코리아 홍보팀' → '세진 김' (유사도: 30.00)
2025-09-12 16:22:01,127 - mcp_tools - INFO - ✅ 필터 추출 완료: filter 검색, 필터: custodian='세진 김' ori_file_name='EQC 관련 자료' s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
📊 추출된 필터:
  - custodian: 세진 김
  - ori_file_name: EQC 관련 자료
  - s_created_date: None
  - sent_date: None
  - from_email: None
  - to_email: None
  - cc: None
  - bcc: None
  - last_author: None
  - extension: None
🔍 검색 방식: filter
💭 판단 근거: 질의에서 2개의 구체적인 필터 정보를 찾았습니다: ['custodian', 'ori_file_name']. 조건 필터링을 사용합니다.
📋 검색에 사용할 필터: {'custodian': '세진 김', 'ori_file_name': 'EQC 관련 자료'}
2025-09-12 16:22:01,128 - mcp_tools - INFO - 🔍 필터 검색 실행: class_name=DocumentChunk, limit=5, filters={'custodian': '세진 김', 'ori_file_name': 'EQC 관련 자료'}
2025-09-12 16:22:01,128 - kars_db - INFO - 필터 검색 시작: class_name=DocumentChunk, limit=5, filters={'custodian': '세진 김', 'ori_file_name': 'EQC 관련 자료'}
2025-09-12 16:22:01,128 - kars_db - INFO - 필터와 함께 검색: {'custodian': '세진 김', 'ori_file_name': 'EQC 관련 자료'}
2025-09-12 16:22:01,131 - kars_db - INFO - ✅ 필터 검색 완료: 0개 결과 반환
📊 검색 결과:
  - 성공 여부: True
  - 총 결과 수: 0개
  - 검색 방식: N/A
  - 사용된 필터: N/A
  📭 검색 결과가 없습니다.

================================================================================

테스트 케이스 14: 2020년 6월에 Dimitris Psillakis가 작성한 SOCAR 협력 관련 문서
------------------------------------------------------------
2025-09-12 16:22:01,131 - mcp_tools - INFO - 🔍 필터 추출 시작: '2020년 6월에 Dimitris Psillakis가 작성한 SOCAR 협력 관련 문서'
2025-09-12 16:22:04,045 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 16:22:04,047 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 16:22:04,047 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 16:22:04,123 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 16:22:04,123 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 16:22:04,186 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 16:22:04,186 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 16:22:04,258 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 16:22:04,258 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 16:22:04,331 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 16:22:04,331 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 16:22:04,490 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 16:22:04,492 - mcp_tools - INFO - ℹ️ last_author 필드에 대한 유사한 이름을 찾을 수 없음: 'Dimitris Psillakis'
2025-09-12 16:22:04,492 - mcp_tools - INFO - ✅ 필터 추출 완료: filter 검색, 필터: custodian=None ori_file_name=None s_created_date={'gte': '2020-06-01T00:00:00Z', 'lt': '2020-07-01T00:00:00Z'} sent_date=None from_email=None to_email=None cc=None bcc=None last_author='Dimitris Psillakis' extension=None
📊 추출된 필터:
  - custodian: None
  - ori_file_name: None
  - s_created_date: {'gte': '2020-06-01T00:00:00Z', 'lt': '2020-07-01T00:00:00Z'}
  - sent_date: None
  - from_email: None
  - to_email: None
  - cc: None
  - bcc: None
  - last_author: Dimitris Psillakis
  - extension: None
🔍 검색 방식: filter
💭 판단 근거: 질의에서 2개의 구체적인 필터 정보를 찾았습니다: ['s_created_date', 'last_author']. 조건 필터링을 사용합니다.
📋 검색에 사용할 필터: {'s_created_date': {'gte': '2020-06-01T00:00:00Z', 'lt': '2020-07-01T00:00:00Z'}, 'last_author': 'Dimitris Psillakis'}
2025-09-12 16:22:04,492 - mcp_tools - INFO - 🔍 필터 검색 실행: class_name=DocumentChunk, limit=5, filters={'s_created_date': {'gte': '2020-06-01T00:00:00Z', 'lt': '2020-07-01T00:00:00Z'}, 'last_author': 'Dimitris Psillakis'}
2025-09-12 16:22:04,492 - kars_db - INFO - 필터 검색 시작: class_name=DocumentChunk, limit=5, filters={'s_created_date': {'gte': '2020-06-01T00:00:00Z', 'lt': '2020-07-01T00:00:00Z'}, 'last_author': 'Dimitris Psillakis'}
2025-09-12 16:22:04,493 - kars_db - INFO - 필터와 함께 검색: {'s_created_date': {'gte': '2020-06-01T00:00:00Z', 'lt': '2020-07-01T00:00:00Z'}, 'last_author': 'Dimitris Psillakis'}
2025-09-12 16:22:04,495 - kars_db - INFO - ✅ 필터 검색 완료: 0개 결과 반환
📊 검색 결과:
  - 성공 여부: True
  - 총 결과 수: 0개
  - 검색 방식: N/A
  - 사용된 필터: N/A
  📭 검색 결과가 없습니다.

================================================================================

테스트 케이스 15: EQC와 EQE 모델 관련 2020년 이후 작성된 모든 문서
------------------------------------------------------------
2025-09-12 16:22:04,496 - mcp_tools - INFO - 🔍 필터 추출 시작: 'EQC와 EQE 모델 관련 2020년 이후 작성된 모든 문서'
2025-09-12 16:22:06,756 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 16:22:06,757 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 16:22:06,757 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 16:22:06,829 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 16:22:06,829 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 16:22:06,888 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 16:22:06,888 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 16:22:06,963 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 16:22:06,964 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 16:22:07,038 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 16:22:07,039 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 16:22:07,039 - mcp_tools - INFO - ✅ 필터 추출 완료: filter 검색, 필터: custodian=None ori_file_name=None s_created_date={'gte': '2020-01-01T00:00:00Z'} sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
📊 추출된 필터:
  - custodian: None
  - ori_file_name: None
  - s_created_date: {'gte': '2020-01-01T00:00:00Z'}
  - sent_date: None
  - from_email: None
  - to_email: None
  - cc: None
  - bcc: None
  - last_author: None
  - extension: None
🔍 검색 방식: filter
💭 판단 근거: 질의에서 구체적인 날짜 정보 's_created_date: {'gte': '2020-01-01T00:00:00Z'}'를 찾았습니다. 조건 필터링을 사용합니다.
📋 검색에 사용할 필터: {'s_created_date': {'gte': '2020-01-01T00:00:00Z'}}
2025-09-12 16:22:07,039 - mcp_tools - INFO - 🔍 필터 검색 실행: class_name=DocumentChunk, limit=5, filters={'s_created_date': {'gte': '2020-01-01T00:00:00Z'}}
2025-09-12 16:22:07,039 - kars_db - INFO - 필터 검색 시작: class_name=DocumentChunk, limit=5, filters={'s_created_date': {'gte': '2020-01-01T00:00:00Z'}}
2025-09-12 16:22:07,040 - kars_db - INFO - 필터와 함께 검색: {'s_created_date': {'gte': '2020-01-01T00:00:00Z'}}
2025-09-12 16:22:07,066 - kars_db - INFO - ✅ 필터 검색 완료: 5개 결과 반환
📊 검색 결과:
  - 성공 여부: True
  - 총 결과 수: 5개
  - 검색 방식: N/A
  - 사용된 필터: N/A

📄 검색된 문서들:
  1. 문서 ID: 65edd917-93fd-4c44-8d24-eea555c8a6c6
     파일명: N/A
     보관자: 세진 김
     생성일: N/A
     발송일: 1900-01-01 00:00:00+00:00
     발신자: NaN
     수신자: NaN
     확장자: txt
     내용 미리보기: (page\s+\d+) of 56 Dealer Circular에 기재된 정보 및 이미지는 메르세데스-벤츠 공식 판매 및 영업사원, 메르세데스-벤츠 직원들을 위한 것으로 메르세데스-...
     최종 작성자: Microsoft® Word 2016

  2. 문서 ID: ee3a05ff-4add-4cfa-8aa9-47badded4b86
     파일명: N/A
     보관자: 세진 김
     생성일: N/A
     발송일: 1900-01-01 00:00:00+00:00
     발신자: NaN
     수신자: NaN
     확장자: txt
     내용 미리보기: 메르세데스-벤츠 코리아(주)의 사전 동의 없이 외부 기업이나 개인에게 무단 배포하거나 복사할 수 없습니다. GLC 300 4MATIC 코드 품목 공급가액 기재사항218 후방 카메라...
     최종 작성자: Microsoft® Word 2016

  3. 문서 ID: 00b6ffde-b76b-4df5-a7a1-7622422dde5a
     파일명: N/A
     보관자: 세진 김
     생성일: N/A
     발송일: 1900-01-01 00:00:00+00:00
     발신자: NaN
     수신자: NaN
     확장자: txt
     내용 미리보기: (page\s+\d+) of 56 Dealer Circular에 기재된 정보 및 이미지는 메르세데스-벤츠 공식 판매 및 영업사원, 메르세데스-벤츠 직원들을 위한 것으로 메르세데스-...
     최종 작성자: Microsoft® Word 2016

  4. 문서 ID: 03e590ec-26da-4b67-af1d-9392a7a77e27
     파일명: N/A
     보관자: 세진 김
     생성일: N/A
     발송일: 1900-01-01 00:00:00+00:00
     발신자: NaN
     수신자: NaN
     확장자: txt
     내용 미리보기: (page\s+\d+) of 56 Dealer Circular에 기재된 정보 및 이미지는 메르세데스-벤츠 공식 판매 및 영업사원, 메르세데스-벤츠 직원들을 위한 것으로 메르세데스-...
     최종 작성자: Microsoft® Word 2016

  5. 문서 ID: 5d3390b1-5c75-438c-a676-cd312480c7c4
     파일명: N/A
     보관자: 세진 김
     생성일: N/A
     발송일: 1900-01-01 00:00:00+00:00
     발신자: NaN
     수신자: NaN
     확장자: txt
     내용 미리보기: 리-인스톨레이션 디지털 라디오800 2020년식835 국가 번호846 알루미늄 피니시 러닝보드859 미디어 디스플레이871 핸즈 프리 액세스872 열선 시트 (뒤)873 열선 시트...
     최종 작성자: Microsoft® Word 2016


================================================================================

테스트 케이스 16: SOCAR, 몽클레르, 버질 아블로 협력 관련 모든 자료
------------------------------------------------------------
2025-09-12 16:22:07,068 - mcp_tools - INFO - 🔍 필터 추출 시작: 'SOCAR, 몽클레르, 버질 아블로 협력 관련 모든 자료'
2025-09-12 16:22:08,729 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 16:22:08,730 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 16:22:08,730 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 16:22:08,809 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 16:22:08,809 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 16:22:08,881 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 16:22:08,882 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 16:22:08,944 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 16:22:08,944 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 16:22:09,010 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 16:22:09,010 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 16:22:09,010 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
📊 추출된 필터:
  - custodian: None
  - ori_file_name: None
  - s_created_date: None
  - sent_date: None
  - from_email: None
  - to_email: None
  - cc: None
  - bcc: None
  - last_author: None
  - extension: None
🔍 검색 방식: similarity
💭 판단 근거: 질의에서 구체적인 필터 정보를 찾을 수 없어 유사도 기반 검색을 사용합니다.
  📭 검색할 필터가 없어 단순 RAG 검색을 수행합니다.
2025-09-12 16:22:09,011 - mcp_tools - INFO - 🔍 단순 RAG 검색 실행: 'SOCAR, 몽클레르, 버질 아블로 협력 관련 모든 자료' (limit: 5)
2025-09-12 16:22:09,011 - kars_db - INFO - 🔍 검색 시작: 'SOCAR, 몽클레르, 버질 아블로 협력 관련 모든 자료' (limit: 5)
2025-09-12 16:22:09,067 - weaviate_db - INFO - 🔍 검색 완료: 5개 결과 (쿼리: 'SOCAR, 몽클레르, 버질 아블로 협력 관련 모든 자료'
2025-09-12 16:22:09,067 - kars_db - INFO - ✅ 검색 완료: 5개 결과 반환
📊 RAG 검색 결과:
  - 성공 여부: True
  - 총 결과 수: 5개
  - 검색 방식: N/A

📄 검색된 문서들:
  1. 문서 ID: 92eab4c9-4855-42d4-9ad6-74a06aaacd5f
     파일명: Press Kit_2023 서울모빌리티쇼_메르세데스-벤츠 코리아_0318.doc
     내용 미리보기:  그만의 스타일을 결합했다. 몽클레르 아우터웨어 컬렉션은 극한의 자연 환경과 도시 생활 모두에 적합하게 제작되었다. 몽클레르 브랜드는 의류 및 액세서리 컬렉션을 직접 운영하는 온오...

  2. 문서 ID: c8ba16d9-ec57-44af-bcc5-1a99595f07d2
     파일명: Press Kit_2023 서울모빌리티쇼_메르세데스-벤츠 코리아_0316.doc
     내용 미리보기: 했다. 몽클레르 (Moncler)몽클레르는 1952년 프랑스 그르노블 인근의 소도시 모네스티에르 드 클레르(Monestier-de-Clermont)에 설립되었으며 현재는 이탈리아에...

  3. 문서 ID: 585a0165-ccb4-4515-9b63-046ac3b768fa
     파일명: Press Kit_2023 서울모빌리티쇼_메르세데스-벤츠 코리아_0318.doc EJ comment.doc
     내용 미리보기: 와 그만의 스타일을 결합했다. 몽클레르 아우터웨어 컬렉션은 극한의 자연 환경과 도시 생활 모두에 적합하게 제작되었다. 몽클레르 브랜드는 의류 및 액세서리 컬렉션을 직접 운영하는 온...

  4. 문서 ID: dca883e0-8312-46ef-97ac-88b5b9f1536e
     파일명: Press Kit_2023 서울모빌리티쇼_메르세데스-벤츠 코리아_0324.docx
     내용 미리보기: 이 지원하는 지속적인 기술 연구와 그만의 스타일을 결합했다. 몽클레르 아우터웨어 컬렉션은 극한의 자연 환경과 도시 생활 모두에 적합하게 제작되었다. 몽클레르 브랜드는 의류 및 액세...

  5. 문서 ID: c99ad5bf-c56c-45fc-8ffd-39ce902031ad
     파일명: Press Kit_2023 서울모빌리티쇼_메르세데스-벤츠 코리아_0315-1.doc
     내용 미리보기: 기술 연구와 그만의 스타일을 결합했다. 몽클레어르 아우터웨어 컬렉션은 극한의 자연 환경과 도시 생활 모두에 적합하게 제작되었다. 몽클레르어 브랜드는 의류 및 액세서리 컬렉션을 직접...


================================================================================

테스트 케이스 17: 전기차 관련 기술 중 MBUX, 4MATIC, 하이브리드 언급된 문서들
------------------------------------------------------------
2025-09-12 16:22:09,069 - mcp_tools - INFO - 🔍 필터 추출 시작: '전기차 관련 기술 중 MBUX, 4MATIC, 하이브리드 언급된 문서들'
2025-09-12 16:22:10,729 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 16:22:10,730 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 16:22:10,730 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 16:22:10,805 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 16:22:10,806 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 16:22:10,882 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 16:22:10,882 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 16:22:10,955 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 16:22:10,955 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 16:22:11,017 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 16:22:11,017 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 16:22:11,017 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
📊 추출된 필터:
  - custodian: None
  - ori_file_name: None
  - s_created_date: None
  - sent_date: None
  - from_email: None
  - to_email: None
  - cc: None
  - bcc: None
  - last_author: None
  - extension: None
🔍 검색 방식: similarity
💭 판단 근거: 질의에서 구체적인 필터 정보를 찾을 수 없어 유사도 기반 검색을 사용합니다.
  📭 검색할 필터가 없어 단순 RAG 검색을 수행합니다.
2025-09-12 16:22:11,018 - mcp_tools - INFO - 🔍 단순 RAG 검색 실행: '전기차 관련 기술 중 MBUX, 4MATIC, 하이브리드 언급된 문서들' (limit: 5)
2025-09-12 16:22:11,018 - kars_db - INFO - 🔍 검색 시작: '전기차 관련 기술 중 MBUX, 4MATIC, 하이브리드 언급된 문서들' (limit: 5)
2025-09-12 16:22:11,078 - weaviate_db - INFO - 🔍 검색 완료: 5개 결과 (쿼리: '전기차 관련 기술 중 MBUX, 4MATIC, 하이브리드 언급된 문서들'
2025-09-12 16:22:11,078 - kars_db - INFO - ✅ 검색 완료: 5개 결과 반환
📊 RAG 검색 결과:
  - 성공 여부: True
  - 총 결과 수: 5개
  - 검색 방식: N/A

📄 검색된 문서들:
  1. 문서 ID: bcd860ce-2d11-462a-95d3-970ec7623f14
     파일명: [PRGATE] 메르세데스-벤츠 코리아 모니터링 가이드.docx
     내용 미리보기:  & Policy News (업계기사 및 기타 경쟁사)Industry & Policy NewsBMW, 메르세데스-벤츠 '600대'까지 추격…하반기 '전기차'로 자존심 싸움 (전자신...

  2. 문서 ID: 2a88afbf-03d4-4178-9c31-1d2895b98cae
     파일명: 2023 06 09 Brand Committee COM_Summary, competitor.pptx
     내용 미리보기: UV, proves that EVs can be luxurious when Mercedes-Benz makes them News 1 (Apr17)[Interview] Mercede...

  3. 문서 ID: 14f6907e-bfcc-4c72-b445-346a8bb35c04
     파일명: KPR  7월 협찬 증빙 기사 송부.msg
     내용 미리보기: From:이 승연(Yonnie Lee)
Sent:Fri 7/29/2022
To:Hwang, Yun-Ju (191); Kim, Hyunji (191)
Cc:MBK
Bcc:
Subj...

  4. 문서 ID: e7a2335c-a501-4359-b0f1-f6349c1b8621
     파일명: Press Release-메르세데스-벤츠 코리아, 메르세데스-AMG의 첫번째 순수 전기차 ‘더 뉴 메르세데스-AMG EQS 53 4MATIC+’ 출시_draft.docx
     내용 미리보기: s pedalsAMG floor mats and door sill trims with "AMG" lettering (illuminated with interchangeable co...

  5. 문서 ID: 8010a334-5d38-408c-aa2f-ad604ac6f190
     파일명: Press Release-메르세데스-벤츠 코리아 메르세데스-AMG의 첫번째 순수 전기차 더 뉴 메르세데스-AMG EQS 53 4MATIC+ 출시_v2.docx
     내용 미리보기: MBUX Hyperscreen)’이 적용됐다. MBUX 하이퍼스크린은 학습이 가능한 인공지능 시스템을 탑재해 다양한 인포테인먼트 및 편의사양 등 차량 내 다채로운 기능을 맞춤형으로...


================================================================================

테스트 케이스 18: 메르세데스-벤츠 코리아의 2020년 전기차 시장 진출 전략
------------------------------------------------------------
2025-09-12 16:22:11,078 - mcp_tools - INFO - 🔍 필터 추출 시작: '메르세데스-벤츠 코리아의 2020년 전기차 시장 진출 전략'
2025-09-12 16:22:13,968 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 16:22:13,969 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 16:22:13,969 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 16:22:14,045 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 16:22:14,045 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 16:22:14,109 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 16:22:14,109 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 16:22:14,183 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 16:22:14,183 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 16:22:14,246 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 16:22:14,246 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 16:22:14,247 - mcp_tools - INFO - ✅ 필터 추출 완료: filter 검색, 필터: custodian=None ori_file_name=None s_created_date={'gte': '2020-01-01T00:00:00Z', 'lt': '2021-01-01T00:00:00Z'} sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
📊 추출된 필터:
  - custodian: None
  - ori_file_name: None
  - s_created_date: {'gte': '2020-01-01T00:00:00Z', 'lt': '2021-01-01T00:00:00Z'}
  - sent_date: None
  - from_email: None
  - to_email: None
  - cc: None
  - bcc: None
  - last_author: None
  - extension: None
🔍 검색 방식: filter
💭 판단 근거: 질의에서 구체적인 날짜 정보 's_created_date: {'gte': '2020-01-01T00:00:00Z', 'lt': '2021-01-01T00:00:00Z'}'를 찾았습니다. 조건 필터링을 사용합니다.
📋 검색에 사용할 필터: {'s_created_date': {'gte': '2020-01-01T00:00:00Z', 'lt': '2021-01-01T00:00:00Z'}}
2025-09-12 16:22:14,247 - mcp_tools - INFO - 🔍 필터 검색 실행: class_name=DocumentChunk, limit=5, filters={'s_created_date': {'gte': '2020-01-01T00:00:00Z', 'lt': '2021-01-01T00:00:00Z'}}
2025-09-12 16:22:14,247 - kars_db - INFO - 필터 검색 시작: class_name=DocumentChunk, limit=5, filters={'s_created_date': {'gte': '2020-01-01T00:00:00Z', 'lt': '2021-01-01T00:00:00Z'}}
2025-09-12 16:22:14,247 - kars_db - INFO - 필터와 함께 검색: {'s_created_date': {'gte': '2020-01-01T00:00:00Z', 'lt': '2021-01-01T00:00:00Z'}}
2025-09-12 16:22:14,256 - kars_db - INFO - ✅ 필터 검색 완료: 5개 결과 반환
📊 검색 결과:
  - 성공 여부: True
  - 총 결과 수: 5개
  - 검색 방식: N/A
  - 사용된 필터: N/A

📄 검색된 문서들:
  1. 문서 ID: 84e3b894-4f16-4b8d-bf39-5bbcd95837b2
     파일명: N/A
     보관자: 세진 김
     생성일: N/A
     발송일: 1900-01-01 00:00:00+00:00
     발신자: NaN
     수신자: NaN
     확장자: csv
     내용 미리보기: {'*ID': 260381, '*docNo': 'otov-230327-0001', '상태': '등록', '등록자': '홍성진 (hsj@mercedes-benz.com)', '딜러사...
     최종 작성자: NaN

  2. 문서 ID: 6a1eca77-af00-4be9-96d6-dc28a1a68b7a
     파일명: N/A
     보관자: 세진 김
     생성일: N/A
     발송일: 1900-01-01 00:00:00+00:00
     발신자: NaN
     수신자: NaN
     확장자: csv
     내용 미리보기: {'*ID': 260452, '*docNo': 'otov-230327-0002', '상태': '등록', '등록자': '최하정 (ha-jeong.choi@mercedes-benz.c...
     최종 작성자: NaN

  3. 문서 ID: 9e25d34e-9fd9-4a4e-a966-3a4abed89cb4
     파일명: N/A
     보관자: 세진 김
     생성일: N/A
     발송일: 1900-01-01 00:00:00+00:00
     발신자: NaN
     수신자: NaN
     확장자: csv
     내용 미리보기: {'*ID': 259876, '*docNo': 'otov-230320-0002', '상태': '등록', '등록자': '이윤희 (youn-hee.lee@mercedes-benz.co...
     최종 작성자: NaN

  4. 문서 ID: ee730a17-2b97-4d51-a901-99d74fd56e49
     파일명: N/A
     보관자: 세진 김
     생성일: N/A
     발송일: 1900-01-01 00:00:00+00:00
     발신자: NaN
     수신자: NaN
     확장자: csv
     내용 미리보기: {'*ID': 259922, '*docNo': 'otov-230320-0005', '상태': '등록', '등록자': '조영옥 (young-ok.cho@mercedes-benz.co...
     최종 작성자: NaN

  5. 문서 ID: 637074c2-8b6f-4c24-895f-256e2139ae14
     파일명: N/A
     보관자: 세진 김
     생성일: N/A
     발송일: 1900-01-01 00:00:00+00:00
     발신자: NaN
     수신자: NaN
     확장자: csv
     내용 미리보기: {'*ID': 259189, '*docNo': 'otov-230309-0002', '상태': '등록', '등록자': '김창훈 (chang-hoon.kim@mercedes-benz....
     최종 작성자: NaN


================================================================================

테스트 케이스 19: SOCAR와의 카셰어링 서비스 협약 체결 과정
------------------------------------------------------------
2025-09-12 16:22:14,257 - mcp_tools - INFO - 🔍 필터 추출 시작: 'SOCAR와의 카셰어링 서비스 협약 체결 과정'
2025-09-12 16:22:15,916 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 16:22:15,918 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 16:22:15,918 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 16:22:15,996 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 16:22:15,996 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 16:22:16,059 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 16:22:16,059 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 16:22:16,134 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 16:22:16,134 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 16:22:16,195 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 16:22:16,196 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 16:22:16,196 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
📊 추출된 필터:
  - custodian: None
  - ori_file_name: None
  - s_created_date: None
  - sent_date: None
  - from_email: None
  - to_email: None
  - cc: None
  - bcc: None
  - last_author: None
  - extension: None
🔍 검색 방식: similarity
💭 판단 근거: 질의에서 구체적인 필터 정보를 찾을 수 없어 유사도 기반 검색을 사용합니다.
  📭 검색할 필터가 없어 단순 RAG 검색을 수행합니다.
2025-09-12 16:22:16,197 - mcp_tools - INFO - 🔍 단순 RAG 검색 실행: 'SOCAR와의 카셰어링 서비스 협약 체결 과정' (limit: 5)
2025-09-12 16:22:16,197 - kars_db - INFO - 🔍 검색 시작: 'SOCAR와의 카셰어링 서비스 협약 체결 과정' (limit: 5)
2025-09-12 16:22:16,246 - weaviate_db - INFO - 🔍 검색 완료: 5개 결과 (쿼리: 'SOCAR와의 카셰어링 서비스 협약 체결 과정'
2025-09-12 16:22:16,246 - kars_db - INFO - ✅ 검색 완료: 5개 결과 반환
📊 RAG 검색 결과:
  - 성공 여부: True
  - 총 결과 수: 5개
  - 검색 방식: N/A

📄 검색된 문서들:
  1. 문서 ID: 46b2a513-9392-4a8a-88a3-7c00f24fcfae
     파일명: 2024 08 12 Issue Report_Cheongna Thermal Incident_v12_F.pptx
     내용 미리보기:  Article – Support from SOCAR8SOCAR to provide 100 support vehicles to residents affected by recent ...

  2. 문서 ID: b2678df2-3e9b-4c02-9140-d3ecf1055d50
     파일명: 2024 08 14 Issue Report_Cheongna Thermal Incident_v14.pptx
     내용 미리보기: (Page\s+\d+)
Summary of Representative Article – Support from SOCAR19SOCAR to provide 100 support v...

  3. 문서 ID: 1eb91ecc-36e7-43ee-94de-047fb00a3df8
     파일명: V2_Press Release-Mercedes-Benz Korea signs MoU with Socar to bring the larg.._ (003).doc
     내용 미리보기: Mercedes-Benz Korea partners up with SOCAR for bringing the largest supply of electric vehicles to t...

  4. 문서 ID: 812cfd8c-c12d-4ddc-b134-154024f0f710
     파일명: 2024 08 19 Issue Report_Cheongna Thermal Incident_v17.pptx
     내용 미리보기: ill provide 100 free monthly car-sharing service SOCAR Plan vehicles for a month to residents who ar...

  5. 문서 ID: 8e5ca30d-824a-4410-bd4e-8a22a8395ff4
     파일명: Press Release  Mercedes-Benz Korea partners up with SOCAR for bringing the largest supply of electric vehicles to the car-sharing industry.msg
     내용 미리보기: From:정은하
Sent:Mon 6/01/2020
To:Dear Journalist
Cc:
Bcc:
Subject:[Press Release] Mercedes-Benz Korea...


================================================================================

테스트 케이스 20: EQC 모델의 국내 시장 출시 및 홍보 활동
------------------------------------------------------------
2025-09-12 16:22:16,247 - mcp_tools - INFO - 🔍 필터 추출 시작: 'EQC 모델의 국내 시장 출시 및 홍보 활동'
2025-09-12 16:22:17,909 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 16:22:17,911 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 16:22:17,911 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 16:22:17,989 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 16:22:17,989 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 16:22:18,086 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 16:22:18,086 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 16:22:18,157 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 16:22:18,157 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 16:22:18,232 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 16:22:18,232 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 16:22:18,232 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
📊 추출된 필터:
  - custodian: None
  - ori_file_name: None
  - s_created_date: None
  - sent_date: None
  - from_email: None
  - to_email: None
  - cc: None
  - bcc: None
  - last_author: None
  - extension: None
🔍 검색 방식: similarity
💭 판단 근거: 질의에서 구체적인 필터 정보를 찾을 수 없어 유사도 기반 검색을 사용합니다.
  📭 검색할 필터가 없어 단순 RAG 검색을 수행합니다.
2025-09-12 16:22:18,232 - mcp_tools - INFO - 🔍 단순 RAG 검색 실행: 'EQC 모델의 국내 시장 출시 및 홍보 활동' (limit: 5)
2025-09-12 16:22:18,232 - kars_db - INFO - 🔍 검색 시작: 'EQC 모델의 국내 시장 출시 및 홍보 활동' (limit: 5)
2025-09-12 16:22:18,275 - weaviate_db - INFO - 🔍 검색 완료: 5개 결과 (쿼리: 'EQC 모델의 국내 시장 출시 및 홍보 활동'
2025-09-12 16:22:18,276 - kars_db - INFO - ✅ 검색 완료: 5개 결과 반환
📊 RAG 검색 결과:
  - 성공 여부: True
  - 총 결과 수: 5개
  - 검색 방식: N/A

📄 검색된 문서들:
  1. 문서 ID: b5004cc8-74d4-46cd-86a8-a0e0077aca7b
     파일명: Dealer Award EQ Session Template Consolidated V2.pptx
     내용 미리보기: een of Tear)Mar~Social MediaEQ 제품 USP 마케팅(EQ USP contents)인플루언서 브랜드 마케팅(Branded contents w/Influence...

  2. 문서 ID: e592e179-2f43-4477-af39-ee1722d318c5
     파일명: 20191217 eMC Meeting.pdf
     내용 미리보기: via menu ba r: Alte rna tin g be tween whi te an d blac k sli de lay outs via menu ba r: Wrap-up Rep...

  3. 문서 ID: 1b403fc7-ffd1-4ead-b070-1436c19fb9a0
     파일명: Dealer Award EQ Session Template Consolidated.pptx
     내용 미리보기: Q 차량에 적용된 최첨단 안전 사양 홍보충돌테스트 키트 전시및 온라인 광고 캠페인(Crash test kit display and online Campaign)May~EQPop-u...

  4. 문서 ID: 590ed758-8b59-474c-be19-4e9c3e4062a2
     파일명: 2023 0719 Monthly EQ STECO Meeting.pdf
     내용 미리보기: 라인 마케팅 강화" 보다 많은 기자 시승 및 보도자료를 통한EQ차량에 대한 긍정적 이미지 제고" MBK 및 딜러사와 함께하는 EQ 리테일마케팅 강화" MB 브랜드의 차별화된 충전 ...

  5. 문서 ID: ed18f143-36bd-4e3c-9cbf-3be8567b9d4e
     파일명: 2023 Dealer Conference_Business Update_draft_v1.pptx
     내용 미리보기: Product LaunchRetail ActivationBrand ExperienceDigital Lead GenerationOnline StoreAlways-on AEM/Onli...


================================================================================

테스트 케이스 21: 메르세데스-벤츠의 전동화 전략 및 기술 로드맵
------------------------------------------------------------
2025-09-12 16:22:18,276 - mcp_tools - INFO - 🔍 필터 추출 시작: '메르세데스-벤츠의 전동화 전략 및 기술 로드맵'
2025-09-12 16:22:19,934 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 16:22:19,936 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 16:22:19,936 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 16:22:19,999 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 16:22:19,999 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 16:22:20,070 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 16:22:20,070 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 16:22:20,146 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 16:22:20,146 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 16:22:20,221 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 16:22:20,221 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 16:22:20,221 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
📊 추출된 필터:
  - custodian: None
  - ori_file_name: None
  - s_created_date: None
  - sent_date: None
  - from_email: None
  - to_email: None
  - cc: None
  - bcc: None
  - last_author: None
  - extension: None
🔍 검색 방식: similarity
💭 판단 근거: 질의에서 구체적인 필터 정보를 찾을 수 없어 유사도 기반 검색을 사용합니다.
  📭 검색할 필터가 없어 단순 RAG 검색을 수행합니다.
2025-09-12 16:22:20,222 - mcp_tools - INFO - 🔍 단순 RAG 검색 실행: '메르세데스-벤츠의 전동화 전략 및 기술 로드맵' (limit: 5)
2025-09-12 16:22:20,222 - kars_db - INFO - 🔍 검색 시작: '메르세데스-벤츠의 전동화 전략 및 기술 로드맵' (limit: 5)
2025-09-12 16:22:20,270 - weaviate_db - INFO - 🔍 검색 완료: 5개 결과 (쿼리: '메르세데스-벤츠의 전동화 전략 및 기술 로드맵'
2025-09-12 16:22:20,270 - kars_db - INFO - ✅ 검색 완료: 5개 결과 반환
📊 RAG 검색 결과:
  - 성공 여부: True
  - 총 결과 수: 5개
  - 검색 방식: N/A

📄 검색된 문서들:
  1. 문서 ID: 648e4ef1-5023-45f7-9f8e-24956cfeca5d
     파일명: Press Kit_2023 서울모빌리티쇼_메르세데스-벤츠 코리아_0315-1.doc
     내용 미리보기: r.co.krI. 메르세데스-벤츠의 럭셔리 & 전동화 & 지속가능성 전략메르세데스-벤츠는 지속 가능한 미래 모빌리티 시대를 위해 혁신 기술 개발부터, 생산, 서비스 등 에 이르기까...

  2. 문서 ID: f35de869-05ce-4f9e-99ba-a7b11fdae671
     파일명: Press Kit_KAIDA Presskit_230508.docx
     내용 미리보기: 매한 메르세데스-벤츠 코리아는 고객들에게 차별화된 온라인 경험을 제공하는 것을 목표로, 온라인을 통한 제품 선택의 폭을 확대한다는 계획이다. 그 일환으로, 메르세데스-벤츠 코리아 ...

  3. 문서 ID: 13f9fd3c-acc1-44e2-9a0d-ae5dc9e06aca
     파일명: Press Kit_2023 서울모빌리티쇼_메르세데스-벤츠 코리아_0316.doc
     내용 미리보기: o.krI. 메르세데스-벤츠의 럭셔리 & 전동화 & 지속가능성 전략메르세데스-벤츠는 지속 가능한 미래 모빌리티 시대를 위해 혁신 기술 개발부터, 생산, 서비스 등에 이르기까지 자동...

  4. 문서 ID: d5581f73-2d87-40bf-96a6-c9ad992646a3
     파일명: Press Kit_2023 서울모빌리티쇼_메르세데스-벤츠 코리아_0315.doc
     내용 미리보기: o.krI. 메르세데스-벤츠의 럭셔리 & 전동화 & 지속가능성 전략메르세데스-벤츠는 지속 가능한 미래 모빌리티 시대를 위해 혁신 기술 개발부터, 생산, 서비스 등 에 이르기까지 자...

  5. 문서 ID: 5f17a797-4420-4e27-b50c-6ed4a4cb159d
     파일명: 애드버토리얼 자료-전기 모빌리티 시대 청사진을 제시하는 메르세데스-벤츠의 전기 구동화 로드맵.docx
     내용 미리보기: 전기 모빌리티 시대 청사진을 제시하는 메르세데스-벤츠의 전기 구동화 로드맵2022.08.23메르세데스-벤츠는 지난 2021년 7월 제품 포트폴리오 전략과 투자 계획을 포함한 새로...


================================================================================

✅ 테스트 완료!
/raid1/workspace/kars-agent/weaviate-mcp/.venv/lib/python3.12/site-packages/weaviate/warnings.py:302: ResourceWarning: Con004: The connection to Weaviate was not closed properly. This can lead to memory leaks.
            Please make sure to close the connection using `client.close()`.
  warnings.warn(
/raid1/workspace/kars-agent/weaviate-mcp/tmp_sungwon_chae/test_extract_value_tool_modified.py:326: ResourceWarning: unclosed <socket.socket fd=9, family=2, type=1, proto=6, laddr=('10.10.150.195', 53806), raddr=('10.10.150.195', 8080)>
  await test_extract_filter()
ResourceWarning: Enable tracemalloc to get the object allocation traceback

====================================================================================================

🔍 이름 매칭 기능 테스트 시작

2025-09-12 16:22:20,305 - mcp_tools - INFO - Weaviate MCP 도구 초기화 완료
👤 1단계: 데이터베이스의 unique한 이름 값들 조회
------------------------------------------------------------
2025-09-12 16:22:20,305 - kars_db - INFO - 🚀 RAG 벡터 데이터베이스 초기화 시작
2025-09-12 16:22:20,305 - simple_manager - INFO - Weaviate URL: http://10.10.150.195:8080
2025-09-12 16:22:20,305 - simple_manager - INFO - OpenAI Base URL: http://10.10.190.1:8125
2025-09-12 16:22:20,305 - kars_db - INFO - ✅ VectorDB 매니저 초기화 완료
2025-09-12 16:22:20,334 - httpx - INFO - HTTP Request: GET http://10.10.190.1:8125/v1/models "HTTP/1.1 200 OK"
2025-09-12 16:22:20,335 - weaviate_db - INFO - ✅ vLLM 서버에서 모델명 가져옴: /data/models_ckpt/bge-m3
2025-09-12 16:22:20,347 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8125/v1/embeddings "HTTP/1.1 200 OK"
2025-09-12 16:22:20,349 - weaviate_db - INFO - ✅ 샘플 임베딩 생성 성공 (차원: 1024)
2025-09-12 16:22:20,392 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/.well-known/openid-configuration "HTTP/1.1 404 Not Found"
2025-09-12 16:22:20,417 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/meta "HTTP/1.1 200 OK"
2025-09-12 16:22:22,450 - weaviate_db - INFO - ✅ Weaviate 클라이언트 연결 성공: http://10.10.150.195:8080
2025-09-12 16:22:22,450 - weaviate_db - INFO - 📡 OpenAI Base URL (Python용): http://10.10.190.1:8125/v1
2025-09-12 16:22:22,450 - weaviate_db - INFO - 📡 OpenAI Base URL (Weaviate용): http://10.10.190.1:8125
2025-09-12 16:22:22,450 - weaviate_db - INFO - 🔧 동적 모델명: /data/models_ckpt/bge-m3
2025-09-12 16:22:22,450 - simple_manager - INFO - DB 연결 초기화 완료
2025-09-12 16:22:22,454 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema "HTTP/1.1 200 OK"
2025-09-12 16:22:22,458 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema/DocumentChunk "HTTP/1.1 200 OK"
2025-09-12 16:22:22,462 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema/EnronDocument "HTTP/1.1 200 OK"
2025-09-12 16:22:22,463 - weaviate_db - INFO - 스키마 조회 완료: 2개 클래스
2025-09-12 16:22:22,463 - simple_manager - WARNING - 클래스 매핑 파일이 없습니다. 기본 규칙을 사용합니다.
2025-09-12 16:22:22,464 - simple_manager - INFO - 기존 클래스 등록: chunk_db -> DocumentChunk
2025-09-12 16:22:22,464 - simple_manager - INFO - 기존 클래스 등록: enron_db -> EnronDocument
2025-09-12 16:22:22,464 - simple_manager - INFO - 총 2개 DB에 클래스 등록 완료
2025-09-12 16:22:22,464 - simple_manager - INFO -   chunk_db: ['DocumentChunk']
2025-09-12 16:22:22,464 - simple_manager - INFO -   enron_db: ['EnronDocument']
2025-09-12 16:22:22,467 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema "HTTP/1.1 200 OK"
2025-09-12 16:22:22,471 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema/DocumentChunk "HTTP/1.1 200 OK"
2025-09-12 16:22:22,474 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema/EnronDocument "HTTP/1.1 200 OK"
2025-09-12 16:22:22,475 - weaviate_db - INFO - 스키마 조회 완료: 2개 클래스
2025-09-12 16:22:22,475 - kars_db - INFO - 📊 사용 가능한 클래스들: ['DocumentChunk', 'EnronDocument']
2025-09-12 16:22:22,475 - kars_db - INFO - ✅ 사용할 클래스명: DocumentChunk
2025-09-12 16:22:22,475 - mcp_tools - INFO - ✅ RAG 데이터베이스 초기화 성공: kars_test
2025-09-12 16:22:22,476 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 16:22:22,476 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 16:22:22,537 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 16:22:22,537 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 16:22:22,607 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 16:22:22,607 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 16:22:22,680 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 16:22:22,680 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 16:22:22,741 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 16:22:22,741 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
✅ Unique 이름 조회 성공!
  - from_email 개수: 3개
  - to_email 개수: 1개
  - custodian 개수: 1개
  - last_author 개수: 14개

📤 from_email 샘플 (처음 10개):
  1. Jeong, Yeeun (191) on behalf of korea_com (191-NPM)
  2. NaN
  3. Park, Sep (191) on behalf of korea_com (191-NPM)

📥 to_email 샘플 (처음 10개):
  1. NaN

👤 custodian 샘플 (처음 10개):
  1. 세진 김

✍️ last_author 샘플 (처음 10개):
  1. Jeong, Yeeun (691)
  2. Joo, Jaeyool (191)
  3. Ju, Hyeyeon (191-Extern-MBK)
  4. Kim, Ji-Hyun (191)
  5. Microsoft® Word 2016
  6. Microsoft® Word Microsoft 365용
  7. Microsoft® Word for Microsoft 365
  8. NaN
  9. Park, Jaekyung (191)
  10. Shim, Ellen (191)

================================================================================

🔍 2단계: 이름 유사도 매칭 테스트
------------------------------------------------------------

🧪 테스트 케이스 1: 한글 이름으로 검색
   입력: '조효원'
--------------------------------------------------
2025-09-12 16:22:22,742 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 16:22:22,742 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 16:22:22,814 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 16:22:22,815 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 16:22:22,886 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 16:22:22,886 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 16:22:22,956 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 16:22:22,956 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 16:22:23,035 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 16:22:23,035 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 16:22:32,185 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 16:22:32,187 - mcp_tools - INFO - ✅ 이메일 유사도 매칭 완료: '조효원' → 5개 매치
✅ 매칭 성공!
  - 총 후보 수: 17개
  - 매치 결과: 5개
  - 검색 필드 타입: all

🎯 매치 결과:
  1. Jeong, Yeeun (191)
     - 유사도 점수: 90.0
     - 매칭 타입: name_similar
     - 매칭 이유: 이름의 순서가 바뀐 경우로, 'Jeong, Yeeun'은 '조효원'과 유사한 발음일 수 있습니다.
  2. Jeong, Yeeun (691)
     - 유사도 점수: 90.0
     - 매칭 타입: name_similar
     - 매칭 이유: 이름의 순서가 바뀐 경우로, 'Jeong, Yeeun'은 '조효원'과 유사한 발음일 수 있습니다.
  3. Song, Jieun (191)
     - 유사도 점수: 90.0
     - 매칭 타입: name_similar
     - 매칭 이유: 이름의 일부가 유사하며, 'Song, Jieun'은 '조효원'과 유사한 발음일 수 있습니다.
  4. Song, Jieun (691)
     - 유사도 점수: 90.0
     - 매칭 타입: name_similar
     - 매칭 이유: 이름의 일부가 유사하며, 'Song, Jieun'은 '조효원'과 유사한 발음일 수 있습니다.
  5. Ju, Hyeyeon (191-Extern-MBK)
     - 유사도 점수: 30.0
     - 매칭 타입: partial
     - 매칭 이유: 'Hyeyeon'은 '효원'과 일부가 일치합니다.


🧪 테스트 케이스 2: 영어 이름으로 검색
   입력: 'hyowon cho'
--------------------------------------------------
2025-09-12 16:22:32,187 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 16:22:32,187 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 16:22:32,264 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 16:22:32,264 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 16:22:32,346 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 16:22:32,346 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 16:22:32,426 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 16:22:32,426 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 16:22:32,497 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 16:22:32,497 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 16:22:42,013 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 16:22:42,015 - mcp_tools - INFO - ✅ 이메일 유사도 매칭 완료: 'hyowon cho' → 5개 매치
✅ 매칭 성공!
  - 총 후보 수: 17개
  - 매치 결과: 5개
  - 검색 필드 타입: all

🎯 매치 결과:
  1. NaN
     - 유사도 점수: 0
     - 매칭 타입: partial
     - 매칭 이유: 입력된 정보와 관련성이 없으며, 이름이나 이메일 주소가 제공되지 않았습니다.
  2. Microsoft® Word for Microsoft 365
     - 유사도 점수: 0
     - 매칭 타입: partial
     - 매칭 이유: 입력된 정보와 관련성이 없으며, 이름이나 이메일 주소가 제공되지 않았습니다.
  3. Microsoft® Word 2016
     - 유사도 점수: 0
     - 매칭 타입: partial
     - 매칭 이유: 입력된 정보와 관련성이 없으며, 이름이나 이메일 주소가 제공되지 않았습니다.
  4. Microsoft® Word Microsoft 365용
     - 유사도 점수: 0
     - 매칭 타입: partial
     - 매칭 이유: 입력된 정보와 관련성이 없으며, 이름이나 이메일 주소가 제공되지 않았습니다.
  5. 䵩捲潳潦璮⁗潲搠㈰ㄶ㬠浯摩晩敤⁵獩湧⁩呥硴卨慲瀮䱇偌瘲⹃潲攠ㄮ㘮ㄮ
     - 유사도 점수: 0
     - 매칭 타입: partial
     - 매칭 이유: 입력된 정보와 관련성이 없으며, 이름이나 이메일 주소가 제공되지 않았습니다.


🧪 테스트 케이스 3: 이름 순서가 바뀐 경우
   입력: '효원 조'
--------------------------------------------------
2025-09-12 16:22:42,015 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 16:22:42,015 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 16:22:42,091 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 16:22:42,092 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 16:22:42,172 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 16:22:42,172 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 16:22:42,250 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 16:22:42,250 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 16:22:42,311 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 16:22:42,312 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 16:22:49,638 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 16:22:49,639 - mcp_tools - INFO - ✅ 이메일 유사도 매칭 완료: '효원 조' → 5개 매치
✅ 매칭 성공!
  - 총 후보 수: 17개
  - 매치 결과: 5개
  - 검색 필드 타입: all

🎯 매치 결과:
  1. Jeong, Yeeun (191)
     - 유사도 점수: 90.0
     - 매칭 타입: name_similar
     - 매칭 이유: 이름의 순서가 바뀐 경우 (예: '조효원' ↔ '효원 조')
  2. Jeong, Yeeun (691)
     - 유사도 점수: 90.0
     - 매칭 타입: name_similar
     - 매칭 이유: 이름의 순서가 바뀐 경우 (예: '조효원' ↔ '효원 조')
  3. Song, Jieun (191)
     - 유사도 점수: 30.0
     - 매칭 타입: partial
     - 매칭 이유: 이름의 일부가 일치하거나 유사
  4. Song, Jieun (691)
     - 유사도 점수: 30.0
     - 매칭 타입: partial
     - 매칭 이유: 이름의 일부가 일치하거나 유사
  5. Ju, Hyeyeon (191-Extern-MBK)
     - 유사도 점수: 30.0
     - 매칭 타입: partial
     - 매칭 이유: 이름의 일부가 일치하거나 유사


🧪 테스트 케이스 4: 약어/별칭이 포함된 경우
   입력: 'hyowon cho (KC)'
--------------------------------------------------
2025-09-12 16:22:49,640 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 16:22:49,640 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 16:22:49,712 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 16:22:49,713 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 16:22:49,791 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 16:22:49,791 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 16:22:49,858 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 16:22:49,858 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 16:22:49,930 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 16:22:49,931 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 16:22:58,513 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 16:22:58,515 - mcp_tools - INFO - ✅ 이메일 유사도 매칭 완료: 'hyowon cho (KC)' → 5개 매치
✅ 매칭 성공!
  - 총 후보 수: 17개
  - 매치 결과: 5개
  - 검색 필드 타입: all

🎯 매치 결과:
  1. NaN
     - 유사도 점수: 0
     - 매칭 타입: none
     - 매칭 이유: 입력된 정보와 관련성이 없으며, 이름이나 이메일 주소가 제공되지 않았습니다.
  2. Microsoft® Word for Microsoft 365
     - 유사도 점수: 0
     - 매칭 타입: none
     - 매칭 이유: 입력된 정보와 관련성이 없으며, 이름이나 이메일 주소가 제공되지 않았습니다.
  3. Microsoft® Word 2016
     - 유사도 점수: 0
     - 매칭 타입: none
     - 매칭 이유: 입력된 정보와 관련성이 없으며, 이름이나 이메일 주소가 제공되지 않았습니다.
  4. Microsoft® Word Microsoft 365용
     - 유사도 점수: 0
     - 매칭 타입: none
     - 매칭 이유: 입력된 정보와 관련성이 없으며, 이름이나 이메일 주소가 제공되지 않았습니다.
  5. 䵩捲潳潦璮⁗潲搠㈰ㄶ㬠浯摩晩敤⁵獩湧⁩呥硴卨慲瀮䱇偌瘲⹃潲攠ㄮ㘮ㄮ
     - 유사도 점수: 0
     - 매칭 타입: none
     - 매칭 이유: 입력된 정보와 관련성이 없으며, 이름이나 이메일 주소가 제공되지 않았습니다.


🧪 테스트 케이스 5: 일반적인 한글 이름
   입력: '김철수'
--------------------------------------------------
2025-09-12 16:22:58,515 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 16:22:58,515 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 16:22:58,582 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 16:22:58,583 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 16:22:58,628 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 16:22:58,628 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 16:22:58,703 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 16:22:58,703 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 16:22:58,777 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 16:22:58,777 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 16:23:07,346 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 16:23:07,347 - mcp_tools - INFO - ✅ 이메일 유사도 매칭 완료: '김철수' → 5개 매치
✅ 매칭 성공!
  - 총 후보 수: 17개
  - 매치 결과: 5개
  - 검색 필드 타입: all

🎯 매치 결과:
  1. 세진 김
     - 유사도 점수: 90.0
     - 매칭 타입: name_similar
     - 매칭 이유: 이름의 순서가 바뀐 경우입니다. '김철수'와 '세진 김'은 이름의 순서가 바뀐 경우로 간주됩니다.
  2. Kim, Ji-Hyun (191)
     - 유사도 점수: 30.0
     - 매칭 타입: partial
     - 매칭 이유: 이름의 일부가 일치합니다. '김' 성씨가 일치하지만, 'Ji-Hyun'은 '철수'와 관련이 없습니다.
  3. Jeong, Yeeun (191)
     - 유사도 점수: 30.0
     - 매칭 타입: partial
     - 매칭 이유: 이름의 일부가 일치합니다. 'Jeong' 성씨는 '김'과 관련이 없습니다.
  4. Jeong, Yeeun (691)
     - 유사도 점수: 30.0
     - 매칭 타입: partial
     - 매칭 이유: 이름의 일부가 일치합니다. 'Jeong' 성씨는 '김'과 관련이 없습니다.
  5. Shim, Ellen (191)
     - 유사도 점수: 30.0
     - 매칭 타입: partial
     - 매칭 이유: 


 🧪 테스트 케이스 6: 영어 이름 (하이픈 포함)
   입력: 'Park Young-hee'
--------------------------------------------------
2025-09-12 16:23:07,348 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 16:23:07,348 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 16:23:07,413 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 16:23:07,414 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 16:23:07,486 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 16:23:07,486 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 16:23:07,550 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 16:23:07,550 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 16:23:07,622 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 16:23:07,622 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 16:23:20,186 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 16:23:20,188 - mcp_tools - INFO - ✅ 이메일 유사도 매칭 완료: 'Park Young-hee' → 5개 매치
✅ 매칭 성공!
  - 총 후보 수: 17개
  - 매치 결과: 5개
  - 검색 필드 타입: all

🎯 매치 결과:
  1. Park, Jaekyung (191)
     - 유사도 점수: 90.0
     - 매칭 타입: name_similar
     - 매칭 이유: 이름의 성이 'Park'으로 일치하며, 'Young-hee'와 'Jaekyung'은 모두 한국식 이름으로 유사한 발음과 의미를 가질 수 있습니다. 영어 이름과 한글 이름의 매칭을 우선적으로 고려해야 하며, 이름의 순서가 바뀐 경우도 고려합니다.
  2. Park, Sep (191) on behalf of korea_com (191-NPM)
     - 유사도 점수: 90.0
     - 매칭 타입: name_similar
     - 매칭 이유: 이름의 성이 'Park'으로 일치하며, 'Young-hee'와 'Sep'은 모두 한국식 이름으로 유사한 발음과 의미를 가질 수 있습니다. 영어 이름과 한글 이름의 매칭을 우선적으로 고려해야 하며, 이름의 순서가 바뀐 경우도 고려합니다.
  3. Jeong, Yeeun (191)
     - 유사도 점수: 30.0
     - 매칭 타입: partial
     - 매칭 이유: 이름의 일부가 일치하거나 유사할 수 있습니다. 'Young-hee'와 'Yeeun'은 모두 한국식 이름으로 유사한 발음과 의미를 가질 수 있습니다.
  4. Jeong, Yeeun (691)
     - 유사도 점수: 30.0
     - 매칭 타입: partial
     - 매칭 이유: 이름의 일부가 일치하거나 유사할 수 있습니다. 'Young-hee'와 'Yeeun'은 모두 한국식 이름으로 유사한 발음과 의미를 가질 수 있습니다.
  5. Song, Jieun (191)
     - 유사도 점수: 30.0
     - 매칭 타입: partial
     - 매칭 이유: 이름의 일부가 일치하거나 유사할 수 있습니다. 'Young-hee'와 'Jieun'은 모두 한국식 이름으로 유사한 발음과 의미를 가질 수 있습니다.

✅ 이름 매칭 테스트 완료!
/raid1/workspace/kars-agent/weaviate-mcp/tmp_sungwon_chae/test_extract_value_tool_modified.py:331: ResourceWarning: unclosed <socket.socket fd=10, family=2, type=1, proto=6, laddr=('10.10.150.195', 38866), raddr=('10.10.150.195', 8080)>
  await test_name_matching()
ResourceWarning: Enable tracemalloc to get the object allocation traceback

🎉 모든 테스트 완료!
(.venv) min.choi10@wss-195:/raid1/workspace/kars-agent/weaviate-mcp/tmp_sungwon_chae$ 
