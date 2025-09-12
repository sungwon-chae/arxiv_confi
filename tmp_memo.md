min.choi10@wss-195:/raid1/workspace/kars-agent$ cd weaviate-mcp
min.choi10@wss-195:/raid1/workspace/kars-agent/weaviate-mcp$ source .venv/bin/activate
(.venv) min.choi10@wss-195:/raid1/workspace/kars-agent/weaviate-mcp$ python test_extract_value_tool.py 
🚀 Weaviate MCP 도구 테스트 시작

2025-09-12 16:02:01,889 - mcp_tools - INFO - Weaviate MCP 도구 초기화 완료
2025-09-12 16:02:04,686 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
Test Query Response:  ChatCompletion(id='chatcmpl-4f6bf5cba715454c864df15b2c418d2b', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='<think>\nOkay, the user said "hi!" so I need to respond appropriately. Let me start by acknowledging their greeting. I should keep it friendly and open-ended to encourage them to ask questions or share what\'s on their mind. Maybe something like, "Hello! How can I assist you today?" That\'s simple and inviting. I should make sure the tone is positive and helpful. No need for any complex language here. Just a straightforward, warm response.\n</think>\n\nHello! How can I assist you today? 😊', refusal=None, role='assistant', annotations=None, audio=None, function_call=None, tool_calls=[], reasoning_content=None), stop_reason=None)], created=1757660527, model='/data/models_ckpt/Qwen3-32B', object='chat.completion', service_tier=None, system_fingerprint=None, usage=CompletionUsage(completion_tokens=107, prompt_tokens=10, total_tokens=117, completion_tokens_details=None, prompt_tokens_details=None), prompt_logprobs=None)
✅ OpenAI 클라이언트 설정 완료
🔍 extract_filter_from_query 도구 테스트 시작

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

테스트 케이스 1: 1900년 1월에 생성된 문서를 찾아주세요
------------------------------------------------------------
2025-09-12 16:02:04,703 - mcp_tools - INFO - 🔍 필터 추출 시작: '1900년 1월에 생성된 문서를 찾아주세요'
2025-09-12 16:02:07,411 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 16:02:07,413 - kars_db - INFO - 🚀 RAG 벡터 데이터베이스 초기화 시작
2025-09-12 16:02:07,413 - simple_manager - INFO - Weaviate URL: http://10.10.150.195:8080
2025-09-12 16:02:07,413 - simple_manager - INFO - OpenAI Base URL: http://10.10.190.1:8125
2025-09-12 16:02:07,413 - kars_db - INFO - ✅ VectorDB 매니저 초기화 완료
2025-09-12 16:02:07,464 - httpx - INFO - HTTP Request: GET http://10.10.190.1:8125/v1/models "HTTP/1.1 200 OK"
2025-09-12 16:02:07,465 - weaviate_db - INFO - ✅ vLLM 서버에서 모델명 가져옴: /data/models_ckpt/bge-m3
2025-09-12 16:02:07,478 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8125/v1/embeddings "HTTP/1.1 200 OK"
2025-09-12 16:02:07,479 - weaviate_db - INFO - ✅ 샘플 임베딩 생성 성공 (차원: 1024)
2025-09-12 16:02:07,510 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/.well-known/openid-configuration "HTTP/1.1 404 Not Found"
2025-09-12 16:02:07,536 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/meta "HTTP/1.1 200 OK"
2025-09-12 16:02:09,592 - weaviate_db - INFO - ✅ Weaviate 클라이언트 연결 성공: http://10.10.150.195:8080
2025-09-12 16:02:09,592 - weaviate_db - INFO - 📡 OpenAI Base URL (Python용): http://10.10.190.1:8125/v1
2025-09-12 16:02:09,592 - weaviate_db - INFO - 📡 OpenAI Base URL (Weaviate용): http://10.10.190.1:8125
2025-09-12 16:02:09,592 - weaviate_db - INFO - 🔧 동적 모델명: /data/models_ckpt/bge-m3
2025-09-12 16:02:09,593 - simple_manager - INFO - DB 연결 초기화 완료
2025-09-12 16:02:09,596 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema "HTTP/1.1 200 OK"
2025-09-12 16:02:09,601 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema/DocumentChunk "HTTP/1.1 200 OK"
2025-09-12 16:02:09,608 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema/EnronDocument "HTTP/1.1 200 OK"
2025-09-12 16:02:09,609 - weaviate_db - INFO - 스키마 조회 완료: 2개 클래스
2025-09-12 16:02:09,610 - simple_manager - WARNING - 클래스 매핑 파일이 없습니다. 기본 규칙을 사용합니다.
2025-09-12 16:02:09,610 - simple_manager - INFO - 기존 클래스 등록: chunk_db -> DocumentChunk
2025-09-12 16:02:09,610 - simple_manager - INFO - 기존 클래스 등록: enron_db -> EnronDocument
2025-09-12 16:02:09,610 - simple_manager - INFO - 총 2개 DB에 클래스 등록 완료
2025-09-12 16:02:09,610 - simple_manager - INFO -   chunk_db: ['DocumentChunk']
2025-09-12 16:02:09,610 - simple_manager - INFO -   enron_db: ['EnronDocument']
2025-09-12 16:02:09,613 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema "HTTP/1.1 200 OK"
2025-09-12 16:02:09,617 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema/DocumentChunk "HTTP/1.1 200 OK"
2025-09-12 16:02:09,620 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema/EnronDocument "HTTP/1.1 200 OK"
2025-09-12 16:02:09,621 - weaviate_db - INFO - 스키마 조회 완료: 2개 클래스
2025-09-12 16:02:09,621 - kars_db - INFO - 📊 사용 가능한 클래스들: ['DocumentChunk', 'EnronDocument']
2025-09-12 16:02:09,621 - kars_db - INFO - ✅ 사용할 클래스명: DocumentChunk
2025-09-12 16:02:09,621 - mcp_tools - INFO - ✅ RAG 데이터베이스 초기화 성공: kars_test
2025-09-12 16:02:09,621 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 16:02:09,621 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 16:02:09,701 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 16:02:09,702 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 16:02:09,781 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 16:02:09,781 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 16:02:09,860 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 16:02:09,861 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 16:02:09,936 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 16:02:09,937 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 16:02:09,937 - mcp_tools - INFO - ✅ 필터 추출 완료: filter 검색, 필터: custodian=None ori_file_name=None s_created_date={'gte': '1900-01-01T00:00:00Z', 'lt': '1900-02-01T00:00:00Z'} sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
📊 추출된 필터:
  - custodian: None
  - ori_file_name: None
  - s_created_date: {'gte': '1900-01-01T00:00:00Z', 'lt': '1900-02-01T00:00:00Z'}
  - sent_date: None
  - from_email: None
  - to_email: None
  - cc: None
  - bcc: None
  - last_author: None
  - extension: None
🔍 검색 방식: filter
💭 판단 근거: 질의에서 구체적인 날짜 정보 's_created_date: {'gte': '1900-01-01T00:00:00Z', 'lt': '1900-02-01T00:00:00Z'}'를 찾았습니다. 조건 필터링을 사용합니다.
📋 검색에 사용할 필터: {'s_created_date': {'gte': '1900-01-01T00:00:00Z', 'lt': '1900-02-01T00:00:00Z'}}
2025-09-12 16:02:09,937 - mcp_tools - INFO - 🔍 필터 검색 실행: class_name=DocumentChunk, limit=5, filters={'s_created_date': {'gte': '1900-01-01T00:00:00Z', 'lt': '1900-02-01T00:00:00Z'}}
2025-09-12 16:02:09,937 - kars_db - INFO - 필터 검색 시작: class_name=DocumentChunk, limit=5, filters={'s_created_date': {'gte': '1900-01-01T00:00:00Z', 'lt': '1900-02-01T00:00:00Z'}}
2025-09-12 16:02:09,937 - kars_db - INFO - 필터와 함께 검색: {'s_created_date': {'gte': '1900-01-01T00:00:00Z', 'lt': '1900-02-01T00:00:00Z'}}
2025-09-12 16:02:09,943 - kars_db - INFO - ✅ 필터 검색 완료: 5개 결과 반환
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

테스트 케이스 2: 황재섭이 작성한 문서를 찾아주세요
------------------------------------------------------------
2025-09-12 16:02:09,943 - mcp_tools - INFO - 🔍 필터 추출 시작: '황재섭이 작성한 문서를 찾아주세요'
2025-09-12 16:02:11,516 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 16:02:11,518 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 16:02:11,518 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 16:02:11,596 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 16:02:11,597 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 16:02:11,679 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 16:02:11,679 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 16:02:11,749 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 16:02:11,750 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 16:02:11,819 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 16:02:11,820 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 16:02:17,414 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 16:02:17,416 - mcp_tools - INFO - ✅ last_author 필드 수정: '황재섭' → 'Joo, Jaeyool (191)' (유사도: 90.00)
2025-09-12 16:02:17,416 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author='Joo, Jaeyool (191)' extension=None
📊 추출된 필터:
  - custodian: None
  - ori_file_name: None
  - s_created_date: None
  - sent_date: None
  - from_email: None
  - to_email: None
  - cc: None
  - bcc: None
  - last_author: Joo, Jaeyool (191)
  - extension: None
🔍 검색 방식: similarity
💭 판단 근거: 질의에서 구체적인 필터 정보를 찾았지만 단일 필터이므로 유사도 기반 검색을 사용합니다.
📋 검색에 사용할 필터: {'last_author': 'Joo, Jaeyool (191)'}
2025-09-12 16:02:17,416 - mcp_tools - INFO - 🔍 필터 검색 실행: class_name=DocumentChunk, limit=5, filters={'last_author': 'Joo, Jaeyool (191)'}
2025-09-12 16:02:17,416 - kars_db - INFO - 필터 검색 시작: class_name=DocumentChunk, limit=5, filters={'last_author': 'Joo, Jaeyool (191)'}
2025-09-12 16:02:17,417 - kars_db - INFO - 필터와 함께 검색: {'last_author': 'Joo, Jaeyool (191)'}
2025-09-12 16:02:17,430 - kars_db - INFO - ✅ 필터 검색 완료: 5개 결과 반환
📊 검색 결과:
  - 성공 여부: True
  - 총 결과 수: 5개
  - 검색 방식: N/A
  - 사용된 필터: N/A

📄 검색된 문서들:
  1. 문서 ID: 4de9b0db-7f78-4c07-b5ae-da9b511d92a6
     파일명: N/A
     보관자: 세진 김
     생성일: N/A
     발송일: 1900-01-01 00:00:00+00:00
     발신자: NaN
     수신자: NaN
     확장자: txt
     내용 미리보기: ustomers. To this end, Mercedes-Benz continues to lead the development of the automotive industry wi...
     최종 작성자: Joo, Jaeyool (191)

  2. 문서 ID: f2d0e5ef-b9ed-4c68-9b0b-160d813bc1d3
     파일명: N/A
     보관자: 세진 김
     생성일: N/A
     발송일: 1900-01-01 00:00:00+00:00
     발신자: NaN
     수신자: NaN
     확장자: txt
     내용 미리보기: [Sales Performance][2023 Sales Result & 2024 Sales Target](in case of winning 1st place) Last year,...
     최종 작성자: Joo, Jaeyool (191)

  3. 문서 ID: f85465e2-fe70-4f87-9ef3-17af957820df
     파일명: N/A
     보관자: 세진 김
     생성일: N/A
     발송일: 1900-01-01 00:00:00+00:00
     발신자: NaN
     수신자: NaN
     확장자: txt
     내용 미리보기: y" in 2023. In particular, last year, we launched EQS SUV and EQE SUV to complete electric vehicle l...
     최종 작성자: Joo, Jaeyool (191)

  4. 문서 ID: 5ebbdef9-868c-4c7f-9079-5f88f6469098
     파일명: N/A
     보관자: 세진 김
     생성일: N/A
     발송일: 1900-01-01 00:00:00+00:00
     발신자: NaN
     수신자: NaN
     확장자: txt
     내용 미리보기: ’의 누적 판매량도 10만대를 돌파하는 등, 탑엔드(TEV; Top-End Vehicle) 모델에 있어서도 괄목할 만한 성과를 달성했다. 우리는 고객 만족을 위해 최고의 럭셔리 차...
     최종 작성자: Joo, Jaeyool (191)

  5. 문서 ID: dc95ada5-3c29-40ee-a1aa-5fe117fc40fb
     파일명: N/A
     보관자: 세진 김
     생성일: N/A
     발송일: 1900-01-01 00:00:00+00:00
     발신자: NaN
     수신자: NaN
     확장자: txt
     내용 미리보기:  team despite difficult situations such as the economic downturn and high-interest rates.However, we...
     최종 작성자: Joo, Jaeyool (191)


================================================================================

테스트 케이스 3: 보관자가 '세진 김'이고 1900년 1월에 생성된 문서
------------------------------------------------------------
2025-09-12 16:02:17,431 - mcp_tools - INFO - 🔍 필터 추출 시작: '보관자가 '세진 김'이고 1900년 1월에 생성된 문서'
2025-09-12 16:02:20,214 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 16:02:20,216 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 16:02:20,216 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 16:02:20,293 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 16:02:20,293 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 16:02:20,364 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 16:02:20,364 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 16:02:20,444 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 16:02:20,444 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 16:02:20,519 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 16:02:20,519 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 16:02:20,519 - mcp_tools - INFO - ✅ custodian 필드 정확한 매칭 발견: '세진 김'
2025-09-12 16:02:20,519 - mcp_tools - INFO - ✅ 필터 추출 완료: filter 검색, 필터: custodian='세진 김' ori_file_name=None s_created_date={'gte': '1900-01-01T00:00:00Z', 'lt': '1900-02-01T00:00:00Z'} sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
📊 추출된 필터:
  - custodian: 세진 김
  - ori_file_name: None
  - s_created_date: {'gte': '1900-01-01T00:00:00Z', 'lt': '1900-02-01T00:00:00Z'}
  - sent_date: None
  - from_email: None
  - to_email: None
  - cc: None
  - bcc: None
  - last_author: None
  - extension: None
🔍 검색 방식: filter
💭 판단 근거: 질의에서 2개의 구체적인 필터 정보를 찾았습니다: ['custodian', 's_created_date']. 조건 필터링을 사용합니다.
📋 검색에 사용할 필터: {'custodian': '세진 김', 's_created_date': {'gte': '1900-01-01T00:00:00Z', 'lt': '1900-02-01T00:00:00Z'}}
2025-09-12 16:02:20,519 - mcp_tools - INFO - 🔍 필터 검색 실행: class_name=DocumentChunk, limit=5, filters={'custodian': '세진 김', 's_created_date': {'gte': '1900-01-01T00:00:00Z', 'lt': '1900-02-01T00:00:00Z'}}
2025-09-12 16:02:20,519 - kars_db - INFO - 필터 검색 시작: class_name=DocumentChunk, limit=5, filters={'custodian': '세진 김', 's_created_date': {'gte': '1900-01-01T00:00:00Z', 'lt': '1900-02-01T00:00:00Z'}}
2025-09-12 16:02:20,520 - kars_db - INFO - 필터와 함께 검색: {'custodian': '세진 김', 's_created_date': {'gte': '1900-01-01T00:00:00Z', 'lt': '1900-02-01T00:00:00Z'}}
2025-09-12 16:02:20,529 - kars_db - INFO - ✅ 필터 검색 완료: 5개 결과 반환
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

테스트 케이스 4: 조효원과 최민이 주고받은 문서들을 시간 순으로 정리해줘
------------------------------------------------------------
2025-09-12 16:02:20,530 - mcp_tools - INFO - 🔍 필터 추출 시작: '조효원과 최민이 주고받은 문서들을 시간 순으로 정리해줘'
2025-09-12 16:02:22,160 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 16:02:22,162 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 16:02:22,162 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 16:02:22,236 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 16:02:22,237 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 16:02:22,313 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 16:02:22,313 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 16:02:22,379 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 16:02:22,379 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 16:02:22,455 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 16:02:22,455 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 16:02:26,854 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 16:02:26,855 - mcp_tools - INFO - ✅ from_email 필드 수정: '조효원' → 'Jeong, Yeeun (191) on behalf of korea_com (191-NPM)' (유사도: 30.00)
2025-09-12 16:02:27,015 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 16:02:27,017 - mcp_tools - INFO - ℹ️ to_email 필드에 대한 유사한 이름을 찾을 수 없음: '최민'
2025-09-12 16:02:27,018 - mcp_tools - INFO - ✅ 필터 추출 완료: filter 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email='Jeong, Yeeun (191) on behalf of korea_com (191-NPM)' to_email='최민' cc=None bcc=None last_author=None extension=None
📊 추출된 필터:
  - custodian: None
  - ori_file_name: None
  - s_created_date: None
  - sent_date: None
  - from_email: Jeong, Yeeun (191) on behalf of korea_com (191-NPM)
  - to_email: 최민
  - cc: None
  - bcc: None
  - last_author: None
  - extension: None
🔍 검색 방식: filter
💭 판단 근거: 질의에서 2개의 구체적인 필터 정보를 찾았습니다: ['from_email', 'to_email']. 조건 필터링을 사용합니다.
📋 검색에 사용할 필터: {'from_email': 'Jeong, Yeeun (191) on behalf of korea_com (191-NPM)', 'to_email': '최민'}
2025-09-12 16:02:27,018 - mcp_tools - INFO - 🔍 필터 검색 실행: class_name=DocumentChunk, limit=5, filters={'from_email': 'Jeong, Yeeun (191) on behalf of korea_com (191-NPM)', 'to_email': '최민'}
2025-09-12 16:02:27,018 - kars_db - INFO - 필터 검색 시작: class_name=DocumentChunk, limit=5, filters={'from_email': 'Jeong, Yeeun (191) on behalf of korea_com (191-NPM)', 'to_email': '최민'}
2025-09-12 16:02:27,019 - kars_db - INFO - 필터와 함께 검색: {'from_email': 'Jeong, Yeeun (191) on behalf of korea_com (191-NPM)', 'to_email': '최민'}
2025-09-12 16:02:27,024 - kars_db - INFO - ✅ 필터 검색 완료: 0개 결과 반환
📊 검색 결과:
  - 성공 여부: True
  - 총 결과 수: 0개
  - 검색 방식: N/A
  - 사용된 필터: N/A
  📭 검색 결과가 없습니다.

================================================================================

테스트 케이스 5: 김철수가 작성한 보고서를 찾아주세요
------------------------------------------------------------
2025-09-12 16:02:27,024 - mcp_tools - INFO - 🔍 필터 추출 시작: '김철수가 작성한 보고서를 찾아주세요'
2025-09-12 16:02:28,690 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 16:02:28,691 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 16:02:28,692 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 16:02:28,757 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 16:02:28,757 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 16:02:28,799 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 16:02:28,800 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 16:02:28,854 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 16:02:28,855 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 16:02:28,927 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 16:02:28,927 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 16:02:30,057 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 16:02:30,058 - mcp_tools - INFO - ✅ custodian 필드 수정: '김철수' → '세진 김' (유사도: 30.00)
2025-09-12 16:02:38,050 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 16:02:38,051 - mcp_tools - INFO - ✅ last_author 필드 수정: '김철수' → 'Kim, Ji-Hyun (191)' (유사도: 90.00)
2025-09-12 16:02:38,052 - mcp_tools - INFO - ✅ 필터 추출 완료: filter 검색, 필터: custodian='세진 김' ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author='Kim, Ji-Hyun (191)' extension=None
📊 추출된 필터:
  - custodian: 세진 김
  - ori_file_name: None
  - s_created_date: None
  - sent_date: None
  - from_email: None
  - to_email: None
  - cc: None
  - bcc: None
  - last_author: Kim, Ji-Hyun (191)
  - extension: None
🔍 검색 방식: filter
💭 판단 근거: 질의에서 2개의 구체적인 필터 정보를 찾았습니다: ['custodian', 'last_author']. 조건 필터링을 사용합니다.
📋 검색에 사용할 필터: {'custodian': '세진 김', 'last_author': 'Kim, Ji-Hyun (191)'}
2025-09-12 16:02:38,052 - mcp_tools - INFO - 🔍 필터 검색 실행: class_name=DocumentChunk, limit=5, filters={'custodian': '세진 김', 'last_author': 'Kim, Ji-Hyun (191)'}
2025-09-12 16:02:38,052 - kars_db - INFO - 필터 검색 시작: class_name=DocumentChunk, limit=5, filters={'custodian': '세진 김', 'last_author': 'Kim, Ji-Hyun (191)'}
2025-09-12 16:02:38,053 - kars_db - INFO - 필터와 함께 검색: {'custodian': '세진 김', 'last_author': 'Kim, Ji-Hyun (191)'}
2025-09-12 16:02:38,059 - kars_db - INFO - ✅ 필터 검색 완료: 5개 결과 반환
📊 검색 결과:
  - 성공 여부: True
  - 총 결과 수: 5개
  - 검색 방식: N/A
  - 사용된 필터: N/A

📄 검색된 문서들:
  1. 문서 ID: 5e0dda4f-2876-40e3-a719-4aefa148be96
     파일명: N/A
     보관자: 세진 김
     생성일: N/A
     발송일: 1900-01-01 00:00:00+00:00
     발신자: NaN
     수신자: NaN
     확장자: txt
     내용 미리보기: -Class. Therefore, the new E-Class is the most Koreanized model ever. (If asked) Korea is the first ...
     최종 작성자: Kim, Ji-Hyun (191)

  2. 문서 ID: 3c7b24ea-1991-4837-8cf3-2142118135c0
     파일명: N/A
     보관자: 세진 김
     생성일: N/A
     발송일: 1900-01-01 00:00:00+00:00
     발신자: NaN
     수신자: NaN
     확장자: txt
     내용 미리보기: Expected Q&A_EQA/EQB FL Launch & EV SafetySales Performance2024 Jan-Apr MB’s overall EV sales have ...
     최종 작성자: Kim, Ji-Hyun (191)

  3. 문서 ID: 2bd775f6-5abe-476f-956b-36e9f21bfb8e
     파일명: N/A
     보관자: 세진 김
     생성일: N/A
     발송일: 1900-01-01 00:00:00+00:00
     발신자: NaN
     수신자: NaN
     확장자: txt
     내용 미리보기: EV market in Korea. [EQ Sales 2021 ~ 2024 Apr. YTD]Total EQ Sales - 28% (2024 Apr. YTD vs. 2023 Apr....
     최종 작성자: Kim, Ji-Hyun (191)

  4. 문서 ID: 0ed387d9-0bb5-4181-bff0-27f5e60bef57
     파일명: N/A
     보관자: 세진 김
     생성일: N/A
     발송일: 1900-01-01 00:00:00+00:00
     발신자: NaN
     수신자: NaN
     확장자: txt
     내용 미리보기: tive. Battery cells are supplied by external partners, but overall procedures including battery asse...
     최종 작성자: Kim, Ji-Hyun (191)

  5. 문서 ID: cdffd7e7-5c05-44a3-8812-38ff3e09d4e2
     파일명: N/A
     보관자: 세진 김
     생성일: N/A
     발송일: 1900-01-01 00:00:00+00:00
     발신자: NaN
     수신자: NaN
     확장자: txt
     내용 미리보기: ge is … (Need to check with relevant departments)[EQA EQB driving range]Pre FL (domestic)FL (domesti...
     최종 작성자: Kim, Ji-Hyun (191)


================================================================================

테스트 케이스 6: 박영희가 참여한 프로젝트 문서
------------------------------------------------------------
2025-09-12 16:02:38,060 - mcp_tools - INFO - 🔍 필터 추출 시작: '박영희가 참여한 프로젝트 문서'
2025-09-12 16:02:39,652 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 16:02:39,654 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 16:02:39,654 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 16:02:39,730 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 16:02:39,732 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 16:02:39,796 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 16:02:39,796 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 16:02:39,864 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 16:02:39,864 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 16:02:39,930 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 16:02:39,930 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
