(.venv) min.choi10@wss-195:/raid1/workspace/kars-agent/weaviate-mcp/tmp_sungwon_chae$ python test_extract_value_tool_modified.py 
🚀 Weaviate MCP 도구 테스트 시작

2025-09-12 17:13:58,801 - mcp_tools - INFO - Weaviate MCP 도구 초기화 완료
2025-09-12 17:14:01,479 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
Test Query Response:  ChatCompletion(id='chatcmpl-bf37451b5ca547dbb97696a74f0db5d2', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='<think>\nOkay, the user said "hi!" so they\'re probably just starting a conversation. I should respond in a friendly and welcoming way. Let me make sure to acknowledge their greeting and offer help. Maybe say something like "Hello! How can I assist you today?" That should cover it. Let me check if there\'s anything else I need to add. No, that\'s probably sufficient. Keep it simple and open-ended.\n</think>\n\nHello! How can I assist you today? 😊', refusal=None, role='assistant', annotations=None, audio=None, function_call=None, tool_calls=[], reasoning_content=None), stop_reason=None)], created=1757664844, model='/data/models_ckpt/Qwen3-32B', object='chat.completion', service_tier=None, system_fingerprint=None, usage=CompletionUsage(completion_tokens=101, prompt_tokens=10, total_tokens=111, completion_tokens_details=None, prompt_tokens_details=None), prompt_logprobs=None)
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
2025-09-12 17:14:01,497 - mcp_tools - INFO - 🔍 필터 추출 시작: 'Lee Sang-kuk이 언급된 모든 이메일을 찾아주세요'
2025-09-12 17:14:03,011 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 17:14:03,013 - kars_db - INFO - 🚀 RAG 벡터 데이터베이스 초기화 시작
2025-09-12 17:14:03,013 - simple_manager - INFO - Weaviate URL: http://10.10.150.195:8080
2025-09-12 17:14:03,013 - simple_manager - INFO - OpenAI Base URL: http://10.10.190.1:8125
2025-09-12 17:14:03,013 - kars_db - INFO - ✅ VectorDB 매니저 초기화 완료
2025-09-12 17:14:03,060 - httpx - INFO - HTTP Request: GET http://10.10.190.1:8125/v1/models "HTTP/1.1 200 OK"
2025-09-12 17:14:03,061 - weaviate_db - INFO - ✅ vLLM 서버에서 모델명 가져옴: /data/models_ckpt/bge-m3
2025-09-12 17:14:03,075 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8125/v1/embeddings "HTTP/1.1 200 OK"
2025-09-12 17:14:03,077 - weaviate_db - INFO - ✅ 샘플 임베딩 생성 성공 (차원: 1024)
2025-09-12 17:14:03,107 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/.well-known/openid-configuration "HTTP/1.1 404 Not Found"
2025-09-12 17:14:03,133 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/meta "HTTP/1.1 200 OK"
2025-09-12 17:14:05,169 - weaviate_db - INFO - ✅ Weaviate 클라이언트 연결 성공: http://10.10.150.195:8080
2025-09-12 17:14:05,169 - weaviate_db - INFO - 📡 OpenAI Base URL (Python용): http://10.10.190.1:8125/v1
2025-09-12 17:14:05,169 - weaviate_db - INFO - 📡 OpenAI Base URL (Weaviate용): http://10.10.190.1:8125
2025-09-12 17:14:05,169 - weaviate_db - INFO - 🔧 동적 모델명: /data/models_ckpt/bge-m3
2025-09-12 17:14:05,169 - simple_manager - INFO - DB 연결 초기화 완료
2025-09-12 17:14:05,173 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema "HTTP/1.1 200 OK"
2025-09-12 17:14:05,178 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema/DocumentChunk "HTTP/1.1 200 OK"
2025-09-12 17:14:05,185 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema/EnronDocument "HTTP/1.1 200 OK"
2025-09-12 17:14:05,186 - weaviate_db - INFO - 스키마 조회 완료: 2개 클래스
2025-09-12 17:14:05,187 - simple_manager - WARNING - 클래스 매핑 파일이 없습니다. 기본 규칙을 사용합니다.
2025-09-12 17:14:05,187 - simple_manager - INFO - 기존 클래스 등록: chunk_db -> DocumentChunk
2025-09-12 17:14:05,187 - simple_manager - INFO - 기존 클래스 등록: enron_db -> EnronDocument
2025-09-12 17:14:05,187 - simple_manager - INFO - 총 2개 DB에 클래스 등록 완료
2025-09-12 17:14:05,187 - simple_manager - INFO -   chunk_db: ['DocumentChunk']
2025-09-12 17:14:05,187 - simple_manager - INFO -   enron_db: ['EnronDocument']
2025-09-12 17:14:05,190 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema "HTTP/1.1 200 OK"
2025-09-12 17:14:05,194 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema/DocumentChunk "HTTP/1.1 200 OK"
2025-09-12 17:14:05,197 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema/EnronDocument "HTTP/1.1 200 OK"
2025-09-12 17:14:05,198 - weaviate_db - INFO - 스키마 조회 완료: 2개 클래스
2025-09-12 17:14:05,198 - kars_db - INFO - 📊 사용 가능한 클래스들: ['DocumentChunk', 'EnronDocument']
2025-09-12 17:14:05,198 - kars_db - INFO - ✅ 사용할 클래스명: DocumentChunk
2025-09-12 17:14:05,198 - mcp_tools - INFO - ✅ RAG 데이터베이스 초기화 성공: kars_test
2025-09-12 17:14:05,198 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 17:14:05,198 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 17:14:05,284 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 17:14:05,284 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 17:14:05,357 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 17:14:05,357 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 17:14:05,410 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 17:14:05,410 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 17:14:05,488 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 17:14:05,488 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 17:14:05,488 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
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
2025-09-12 17:14:05,488 - mcp_tools - INFO - 🔍 단순 RAG 검색 실행: 'Lee Sang-kuk이 언급된 모든 이메일을 찾아주세요' (limit: 5)
2025-09-12 17:14:05,488 - kars_db - INFO - 🔍 검색 시작: 'Lee Sang-kuk이 언급된 모든 이메일을 찾아주세요' (limit: 5)
2025-09-12 17:14:05,546 - weaviate_db - INFO - 🔍 검색 완료: 5개 결과 (쿼리: 'Lee Sang-kuk이 언급된 모든 이메일을 찾아주세요'
2025-09-12 17:14:05,546 - kars_db - INFO - ✅ 검색 완료: 5개 결과 반환
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

테스트 케이스 2: 메르세데스-벤츠 코리아 홍보팀이 작성한 문서들
------------------------------------------------------------
2025-09-12 17:14:05,546 - mcp_tools - INFO - 🔍 필터 추출 시작: '메르세데스-벤츠 코리아 홍보팀이 작성한 문서들'
2025-09-12 17:14:07,450 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 17:14:07,451 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 17:14:07,451 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 17:14:07,528 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 17:14:07,528 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 17:14:07,606 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 17:14:07,607 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 17:14:07,689 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 17:14:07,689 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 17:14:07,757 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 17:14:07,757 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 17:14:08,963 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 17:14:08,965 - mcp_tools - INFO - ✅ custodian 필드 수정: '메르세데스-벤츠 코리아 홍보팀' → '세진 김' (유사도: 30.00)
2025-09-12 17:14:08,965 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian='세진 김' ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
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
2025-09-12 17:14:08,966 - mcp_tools - INFO - 🔍 필터 검색 실행: class_name=DocumentChunk, limit=5, filters={'custodian': '세진 김'}
2025-09-12 17:14:08,966 - kars_db - INFO - 필터 검색 시작: class_name=DocumentChunk, limit=5, filters={'custodian': '세진 김'}
2025-09-12 17:14:08,966 - kars_db - INFO - 필터와 함께 검색: {'custodian': '세진 김'}
2025-09-12 17:14:08,977 - kars_db - INFO - ✅ 필터 검색 완료: 5개 결과 반환
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

테스트 케이스 3: EQC 전기차 관련 모든 자료
------------------------------------------------------------
2025-09-12 17:14:08,979 - mcp_tools - INFO - 🔍 필터 추출 시작: 'EQC 전기차 관련 모든 자료'
2025-09-12 17:14:10,488 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 17:14:10,489 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 17:14:10,490 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 17:14:10,563 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 17:14:10,563 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 17:14:10,629 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 17:14:10,629 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 17:14:10,704 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 17:14:10,704 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 17:14:10,768 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 17:14:10,768 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 17:14:10,768 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
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
2025-09-12 17:14:10,768 - mcp_tools - INFO - 🔍 단순 RAG 검색 실행: 'EQC 전기차 관련 모든 자료' (limit: 5)
2025-09-12 17:14:10,768 - kars_db - INFO - 🔍 검색 시작: 'EQC 전기차 관련 모든 자료' (limit: 5)
2025-09-12 17:14:10,808 - weaviate_db - INFO - 🔍 검색 완료: 5개 결과 (쿼리: 'EQC 전기차 관련 모든 자료'
2025-09-12 17:14:10,808 - kars_db - INFO - ✅ 검색 완료: 5개 결과 반환
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

테스트 케이스 4: SOCAR 관련 모든 문서들
------------------------------------------------------------
2025-09-12 17:14:10,809 - mcp_tools - INFO - 🔍 필터 추출 시작: 'SOCAR 관련 모든 문서들'
2025-09-12 17:14:12,322 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 17:14:12,323 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 17:14:12,323 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 17:14:12,396 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 17:14:12,396 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 17:14:12,454 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 17:14:12,455 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 17:14:12,531 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 17:14:12,531 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 17:14:12,602 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 17:14:12,603 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 17:14:12,603 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
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
2025-09-12 17:14:12,603 - mcp_tools - INFO - 🔍 단순 RAG 검색 실행: 'SOCAR 관련 모든 문서들' (limit: 5)
2025-09-12 17:14:12,603 - kars_db - INFO - 🔍 검색 시작: 'SOCAR 관련 모든 문서들' (limit: 5)
2025-09-12 17:14:12,685 - weaviate_db - INFO - 🔍 검색 완료: 5개 결과 (쿼리: 'SOCAR 관련 모든 문서들'
2025-09-12 17:14:12,685 - kars_db - INFO - ✅ 검색 완료: 5개 결과 반환
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

테스트 케이스 5: MBUX 시스템 관련 기술 자료
------------------------------------------------------------
2025-09-12 17:14:12,685 - mcp_tools - INFO - 🔍 필터 추출 시작: 'MBUX 시스템 관련 기술 자료'
2025-09-12 17:14:14,197 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 17:14:14,198 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 17:14:14,198 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 17:14:14,287 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 17:14:14,287 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 17:14:14,360 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 17:14:14,360 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 17:14:14,428 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 17:14:14,428 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 17:14:14,490 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 17:14:14,490 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 17:14:14,491 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
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
2025-09-12 17:14:14,491 - mcp_tools - INFO - 🔍 단순 RAG 검색 실행: 'MBUX 시스템 관련 기술 자료' (limit: 5)
2025-09-12 17:14:14,491 - kars_db - INFO - 🔍 검색 시작: 'MBUX 시스템 관련 기술 자료' (limit: 5)
2025-09-12 17:14:14,552 - weaviate_db - INFO - 🔍 검색 완료: 5개 결과 (쿼리: 'MBUX 시스템 관련 기술 자료'
2025-09-12 17:14:14,552 - kars_db - INFO - ✅ 검색 완료: 5개 결과 반환
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

테스트 케이스 6: 4MATIC 사륜구동 시스템 관련 자료
------------------------------------------------------------
2025-09-12 17:14:14,553 - mcp_tools - INFO - 🔍 필터 추출 시작: '4MATIC 사륜구동 시스템 관련 자료'
2025-09-12 17:14:16,063 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 17:14:16,065 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 17:14:16,065 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 17:14:16,137 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 17:14:16,137 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 17:14:16,208 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 17:14:16,209 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 17:14:16,283 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 17:14:16,283 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 17:14:16,347 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 17:14:16,347 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 17:14:16,347 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
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
2025-09-12 17:14:16,347 - mcp_tools - INFO - 🔍 단순 RAG 검색 실행: '4MATIC 사륜구동 시스템 관련 자료' (limit: 5)
2025-09-12 17:14:16,347 - kars_db - INFO - 🔍 검색 시작: '4MATIC 사륜구동 시스템 관련 자료' (limit: 5)
2025-09-12 17:14:16,407 - weaviate_db - INFO - 🔍 검색 완료: 5개 결과 (쿼리: '4MATIC 사륜구동 시스템 관련 자료'
2025-09-12 17:14:16,407 - kars_db - INFO - ✅ 검색 완료: 5개 결과 반환
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

테스트 케이스 7: SOCAR와의 카셰어링 협력 관련 자료
------------------------------------------------------------
2025-09-12 17:14:16,408 - mcp_tools - INFO - 🔍 필터 추출 시작: 'SOCAR와의 카셰어링 협력 관련 자료'
2025-09-12 17:14:17,919 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 17:14:17,921 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 17:14:17,921 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 17:14:17,999 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 17:14:17,999 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 17:14:18,059 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 17:14:18,059 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 17:14:18,134 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 17:14:18,134 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 17:14:18,209 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 17:14:18,210 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 17:14:18,210 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
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
2025-09-12 17:14:18,210 - mcp_tools - INFO - 🔍 단순 RAG 검색 실행: 'SOCAR와의 카셰어링 협력 관련 자료' (limit: 5)
2025-09-12 17:14:18,210 - kars_db - INFO - 🔍 검색 시작: 'SOCAR와의 카셰어링 협력 관련 자료' (limit: 5)
2025-09-12 17:14:18,252 - weaviate_db - INFO - 🔍 검색 완료: 5개 결과 (쿼리: 'SOCAR와의 카셰어링 협력 관련 자료'
2025-09-12 17:14:18,253 - kars_db - INFO - ✅ 검색 완료: 5개 결과 반환
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

테스트 케이스 8: SOCAR, 몽클레르, 버질 아블로 협력 관련 모든 자료
------------------------------------------------------------
2025-09-12 17:14:18,253 - mcp_tools - INFO - 🔍 필터 추출 시작: 'SOCAR, 몽클레르, 버질 아블로 협력 관련 모든 자료'
2025-09-12 17:14:19,764 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 17:14:19,765 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 17:14:19,765 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 17:14:19,837 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 17:14:19,837 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 17:14:19,907 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 17:14:19,909 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 17:14:19,976 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 17:14:19,977 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 17:14:20,044 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 17:14:20,045 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 17:14:20,046 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
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
2025-09-12 17:14:20,046 - mcp_tools - INFO - 🔍 단순 RAG 검색 실행: 'SOCAR, 몽클레르, 버질 아블로 협력 관련 모든 자료' (limit: 5)
2025-09-12 17:14:20,046 - kars_db - INFO - 🔍 검색 시작: 'SOCAR, 몽클레르, 버질 아블로 협력 관련 모든 자료' (limit: 5)
2025-09-12 17:14:20,095 - weaviate_db - INFO - 🔍 검색 완료: 5개 결과 (쿼리: 'SOCAR, 몽클레르, 버질 아블로 협력 관련 모든 자료'
2025-09-12 17:14:20,095 - kars_db - INFO - ✅ 검색 완료: 5개 결과 반환
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

테스트 케이스 9: 전기차 관련 기술 중 MBUX, 4MATIC, 하이브리드 언급된 문서들
------------------------------------------------------------
2025-09-12 17:14:20,096 - mcp_tools - INFO - 🔍 필터 추출 시작: '전기차 관련 기술 중 MBUX, 4MATIC, 하이브리드 언급된 문서들'
2025-09-12 17:14:21,608 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 17:14:21,610 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 17:14:21,610 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 17:14:21,671 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 17:14:21,672 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 17:14:21,730 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 17:14:21,730 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 17:14:21,773 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 17:14:21,774 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 17:14:21,815 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 17:14:21,815 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 17:14:21,815 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
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
2025-09-12 17:14:21,815 - mcp_tools - INFO - 🔍 단순 RAG 검색 실행: '전기차 관련 기술 중 MBUX, 4MATIC, 하이브리드 언급된 문서들' (limit: 5)
2025-09-12 17:14:21,815 - kars_db - INFO - 🔍 검색 시작: '전기차 관련 기술 중 MBUX, 4MATIC, 하이브리드 언급된 문서들' (limit: 5)
2025-09-12 17:14:21,860 - weaviate_db - INFO - 🔍 검색 완료: 5개 결과 (쿼리: '전기차 관련 기술 중 MBUX, 4MATIC, 하이브리드 언급된 문서들'
2025-09-12 17:14:21,860 - kars_db - INFO - ✅ 검색 완료: 5개 결과 반환
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

테스트 케이스 10: SOCAR와의 카셰어링 서비스 협약 체결 과정
------------------------------------------------------------
2025-09-12 17:14:21,860 - mcp_tools - INFO - 🔍 필터 추출 시작: 'SOCAR와의 카셰어링 서비스 협약 체결 과정'
2025-09-12 17:14:23,372 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 17:14:23,374 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 17:14:23,374 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 17:14:23,448 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 17:14:23,448 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 17:14:23,509 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 17:14:23,509 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 17:14:23,581 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 17:14:23,582 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 17:14:23,650 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 17:14:23,650 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 17:14:23,650 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
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
2025-09-12 17:14:23,650 - mcp_tools - INFO - 🔍 단순 RAG 검색 실행: 'SOCAR와의 카셰어링 서비스 협약 체결 과정' (limit: 5)
2025-09-12 17:14:23,651 - kars_db - INFO - 🔍 검색 시작: 'SOCAR와의 카셰어링 서비스 협약 체결 과정' (limit: 5)
2025-09-12 17:14:23,683 - weaviate_db - INFO - 🔍 검색 완료: 5개 결과 (쿼리: 'SOCAR와의 카셰어링 서비스 협약 체결 과정'
2025-09-12 17:14:23,683 - kars_db - INFO - ✅ 검색 완료: 5개 결과 반환
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

테스트 케이스 11: EQC 모델의 국내 시장 출시 및 홍보 활동
------------------------------------------------------------
2025-09-12 17:14:23,683 - mcp_tools - INFO - 🔍 필터 추출 시작: 'EQC 모델의 국내 시장 출시 및 홍보 활동'
2025-09-12 17:14:25,195 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 17:14:25,196 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 17:14:25,196 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 17:14:25,274 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 17:14:25,274 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 17:14:25,342 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 17:14:25,342 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 17:14:25,411 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 17:14:25,411 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 17:14:25,491 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 17:14:25,492 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 17:14:25,492 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
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
2025-09-12 17:14:25,492 - mcp_tools - INFO - 🔍 단순 RAG 검색 실행: 'EQC 모델의 국내 시장 출시 및 홍보 활동' (limit: 5)
2025-09-12 17:14:25,492 - kars_db - INFO - 🔍 검색 시작: 'EQC 모델의 국내 시장 출시 및 홍보 활동' (limit: 5)
2025-09-12 17:14:25,524 - weaviate_db - INFO - 🔍 검색 완료: 5개 결과 (쿼리: 'EQC 모델의 국내 시장 출시 및 홍보 활동'
2025-09-12 17:14:25,524 - kars_db - INFO - ✅ 검색 완료: 5개 결과 반환
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

테스트 케이스 12: 메르세데스-벤츠의 전동화 전략 및 기술 로드맵
------------------------------------------------------------
2025-09-12 17:14:25,524 - mcp_tools - INFO - 🔍 필터 추출 시작: '메르세데스-벤츠의 전동화 전략 및 기술 로드맵'
2025-09-12 17:14:27,038 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 17:14:27,040 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 17:14:27,040 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 17:14:27,120 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 17:14:27,120 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 17:14:27,185 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 17:14:27,186 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 17:14:27,260 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 17:14:27,261 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 17:14:27,321 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 17:14:27,323 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 17:14:27,323 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
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
2025-09-12 17:14:27,323 - mcp_tools - INFO - 🔍 단순 RAG 검색 실행: '메르세데스-벤츠의 전동화 전략 및 기술 로드맵' (limit: 5)
2025-09-12 17:14:27,323 - kars_db - INFO - 🔍 검색 시작: '메르세데스-벤츠의 전동화 전략 및 기술 로드맵' (limit: 5)
2025-09-12 17:14:27,362 - weaviate_db - INFO - 🔍 검색 완료: 5개 결과 (쿼리: '메르세데스-벤츠의 전동화 전략 및 기술 로드맵'
2025-09-12 17:14:27,362 - kars_db - INFO - ✅ 검색 완료: 5개 결과 반환
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
/raid1/workspace/kars-agent/weaviate-mcp/tmp_sungwon_chae/test_extract_value_tool_modified.py:472: ResourceWarning: unclosed <socket.socket fd=9, family=2, type=1, proto=6, laddr=('10.10.150.195', 33030), raddr=('10.10.150.195', 8080)>
  await test_extract_filter()
ResourceWarning: Enable tracemalloc to get the object allocation traceback

====================================================================================================

🔍 이름 매칭 기능 테스트 시작

2025-09-12 17:14:27,398 - mcp_tools - INFO - Weaviate MCP 도구 초기화 완료
👤 1단계: 데이터베이스의 unique한 이름 값들 조회
------------------------------------------------------------
2025-09-12 17:14:27,398 - kars_db - INFO - 🚀 RAG 벡터 데이터베이스 초기화 시작
2025-09-12 17:14:27,398 - simple_manager - INFO - Weaviate URL: http://10.10.150.195:8080
2025-09-12 17:14:27,398 - simple_manager - INFO - OpenAI Base URL: http://10.10.190.1:8125
2025-09-12 17:14:27,398 - kars_db - INFO - ✅ VectorDB 매니저 초기화 완료
2025-09-12 17:14:27,427 - httpx - INFO - HTTP Request: GET http://10.10.190.1:8125/v1/models "HTTP/1.1 200 OK"
2025-09-12 17:14:27,427 - weaviate_db - INFO - ✅ vLLM 서버에서 모델명 가져옴: /data/models_ckpt/bge-m3
2025-09-12 17:14:27,439 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8125/v1/embeddings "HTTP/1.1 200 OK"
2025-09-12 17:14:27,440 - weaviate_db - INFO - ✅ 샘플 임베딩 생성 성공 (차원: 1024)
2025-09-12 17:14:27,483 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/.well-known/openid-configuration "HTTP/1.1 404 Not Found"
2025-09-12 17:14:27,509 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/meta "HTTP/1.1 200 OK"
2025-09-12 17:14:29,540 - weaviate_db - INFO - ✅ Weaviate 클라이언트 연결 성공: http://10.10.150.195:8080
2025-09-12 17:14:29,540 - weaviate_db - INFO - 📡 OpenAI Base URL (Python용): http://10.10.190.1:8125/v1
2025-09-12 17:14:29,540 - weaviate_db - INFO - 📡 OpenAI Base URL (Weaviate용): http://10.10.190.1:8125
2025-09-12 17:14:29,540 - weaviate_db - INFO - 🔧 동적 모델명: /data/models_ckpt/bge-m3
2025-09-12 17:14:29,541 - simple_manager - INFO - DB 연결 초기화 완료
2025-09-12 17:14:29,544 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema "HTTP/1.1 200 OK"
2025-09-12 17:14:29,549 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema/DocumentChunk "HTTP/1.1 200 OK"
2025-09-12 17:14:29,552 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema/EnronDocument "HTTP/1.1 200 OK"
2025-09-12 17:14:29,554 - weaviate_db - INFO - 스키마 조회 완료: 2개 클래스
2025-09-12 17:14:29,554 - simple_manager - WARNING - 클래스 매핑 파일이 없습니다. 기본 규칙을 사용합니다.
2025-09-12 17:14:29,554 - simple_manager - INFO - 기존 클래스 등록: chunk_db -> DocumentChunk
2025-09-12 17:14:29,554 - simple_manager - INFO - 기존 클래스 등록: enron_db -> EnronDocument
2025-09-12 17:14:29,554 - simple_manager - INFO - 총 2개 DB에 클래스 등록 완료
2025-09-12 17:14:29,554 - simple_manager - INFO -   chunk_db: ['DocumentChunk']
2025-09-12 17:14:29,554 - simple_manager - INFO -   enron_db: ['EnronDocument']
2025-09-12 17:14:29,557 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema "HTTP/1.1 200 OK"
2025-09-12 17:14:29,561 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema/DocumentChunk "HTTP/1.1 200 OK"
2025-09-12 17:14:29,565 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema/EnronDocument "HTTP/1.1 200 OK"
2025-09-12 17:14:29,566 - weaviate_db - INFO - 스키마 조회 완료: 2개 클래스
2025-09-12 17:14:29,566 - kars_db - INFO - 📊 사용 가능한 클래스들: ['DocumentChunk', 'EnronDocument']
2025-09-12 17:14:29,566 - kars_db - INFO - ✅ 사용할 클래스명: DocumentChunk
2025-09-12 17:14:29,566 - mcp_tools - INFO - ✅ RAG 데이터베이스 초기화 성공: kars_test
2025-09-12 17:14:29,566 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 17:14:29,566 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 17:14:29,642 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 17:14:29,642 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 17:14:29,721 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 17:14:29,721 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 17:14:29,782 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 17:14:29,782 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 17:14:29,848 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 17:14:29,848 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
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

�� 2단계: 이름 유사도 매칭 테스트 (MBG 실제 인물 기반)
------------------------------------------------------------

🧪 테스트 케이스 1: 메르세데스-벤츠 코리아 대표이사
   입력: 'Dimitris Psillakis'
--------------------------------------------------
2025-09-12 17:14:29,849 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 17:14:29,849 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 17:14:29,910 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 17:14:29,910 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 17:14:29,985 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 17:14:29,985 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 17:14:30,052 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 17:14:30,052 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 17:14:30,115 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 17:14:30,115 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 17:14:30,393 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 17:14:30,394 - mcp_tools - INFO - ✅ 이메일 유사도 매칭 완료: 'Dimitris Psillakis' → 0개 매치
✅ 매칭 성공!
  - 총 후보 수: 17개
  - 매치 결과: 0개
  - 검색 필드 타입: all
  📭 매치 결과가 없습니다.


🧪 테스트 케이스 2: 메르세데스-벤츠 코리아 영업 부문 부사장
   입력: 'Lee Sang-kuk'
--------------------------------------------------
2025-09-12 17:14:30,395 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 17:14:30,395 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 17:14:30,489 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 17:14:30,490 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 17:14:30,553 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 17:14:30,553 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 17:14:30,625 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 17:14:30,625 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 17:14:30,691 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 17:14:30,691 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 17:14:37,645 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 17:14:37,647 - mcp_tools - INFO - ✅ 이메일 유사도 매칭 완료: 'Lee Sang-kuk' → 5개 매치
✅ 매칭 성공!
  - 총 후보 수: 17개
  - 매치 결과: 5개
  - 검색 필드 타입: all

🎯 매치 결과:
  1. NaN
     - 유사도 점수: 0
     - 매칭 타입: partial
     - 매칭 이유: 입력된 이름과 관련된 정보가 없습니다.
  2. Microsoft® Word Microsoft 365용
     - 유사도 점수: 0
     - 매칭 타입: partial
     - 매칭 이유: 입력된 이름과 관련된 정보가 없습니다.
  3. Microsoft® Word 2016
     - 유사도 점수: 0
     - 매칭 타입: partial
     - 매칭 이유: 입력된 이름과 관련된 정보가 없습니다.
  4. Microsoft® Word for Microsoft 365
     - 유사도 점수: 0
     - 매칭 타입: partial
     - 매칭 이유: 입력된 이름과 관련된 정보가 없습니다.
  5. 䵩捲潳潦璮⁗潲搠㈰ㄶ㬠浯摩晩敤⁵獩湧⁩呥硴卨慲瀮䱇偌瘲⹃潲攠ㄮ㘮ㄮ
     - 유사도 점수: 0
     - 매칭 타입: partial
     - 매칭 이유: 입력된 이름과 관련된 정보가 없습니다.


🧪 테스트 케이스 3: Lee Sang-kuk의 한국어 이름
   입력: '이상국'
--------------------------------------------------
2025-09-12 17:14:37,648 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 17:14:37,648 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 17:14:37,723 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 17:14:37,723 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 17:14:37,770 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 17:14:37,771 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 17:14:37,841 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 17:14:37,841 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 17:14:37,914 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 17:14:37,914 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 17:14:38,191 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 17:14:38,192 - mcp_tools - INFO - ✅ 이메일 유사도 매칭 완료: '이상국' → 0개 매치
✅ 매칭 성공!
  - 총 후보 수: 17개
  - 매치 결과: 0개
  - 검색 필드 타입: all
  📭 매치 결과가 없습니다.


🧪 테스트 케이스 4: SOCAR 부사장
   입력: 'Wi Hyun-jong'
--------------------------------------------------
2025-09-12 17:14:38,193 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 17:14:38,193 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 17:14:38,257 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 17:14:38,257 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 17:14:38,328 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 17:14:38,328 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 17:14:38,375 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 17:14:38,375 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 17:14:38,450 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 17:14:38,451 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 17:14:47,070 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 17:14:47,071 - mcp_tools - INFO - ✅ 이메일 유사도 매칭 완료: 'Wi Hyun-jong' → 5개 매치
✅ 매칭 성공!
  - 총 후보 수: 17개
  - 매치 결과: 5개
  - 검색 필드 타입: all

🎯 매치 결과:
  1. Ju, Hyeyeon (191-Extern-MBK)
     - 유사도 점수: 30.0
     - 매칭 타입: partial
     - 매칭 이유: 이름의 일부가 유사함 (Hyeyeon과 Hyun-jong의 철자가 부분적으로 일치)
  2. Shim, Ellen (191)
     - 유사도 점수: 30.0
     - 매칭 타입: partial
     - 매칭 이유: 이름의 일부가 유사함 (Ellen과 Hyun-jong의 철자가 부분적으로 일치)
  3. Jeong, Yeeun (191) on behalf of korea_com (191-NPM)
     - 유사도 점수: 30.0
     - 매칭 타입: partial
     - 매칭 이유: 이름의 일부가 유사함 (Yeeun과 Hyun-jong의 철자가 부분적으로 일치)
  4. Song, Jieun (691)
     - 유사도 점수: 30.0
     - 매칭 타입: partial
     - 매칭 이유: 이름의 일부가 유사함 (Jieun과 Hyun-jong의 철자가 부분적으로 일치)
  5. Song, Jieun (191)
     - 유사도 점수: 30.0
     - 매칭 타입: partial
     - 매칭 이유: 이름의 일부가 유사함 (Jieun과 Hyun-jong의 철자가 부분적으로 일치)


🧪 테스트 케이스 5: Wi Hyun-jong의 한국어 이름
   입력: '위현종'
--------------------------------------------------
2025-09-12 17:14:47,072 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 17:14:47,072 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 17:14:47,148 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 17:14:47,148 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 17:14:47,226 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 17:14:47,226 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 17:14:47,291 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 17:14:47,291 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 17:14:47,363 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 17:14:47,363 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 17:14:54,366 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 17:14:54,367 - mcp_tools - INFO - ✅ 이메일 유사도 매칭 완료: '위현종' → 5개 매치
✅ 매칭 성공!
  - 총 후보 수: 17개
  - 매치 결과: 5개
  - 검색 필드 타입: all

🎯 매치 결과:
  1. NaN
     - 유사도 점수: 0
     - 매칭 타입: partial
     - 매칭 이유: 입력된 이름과 관련된 정보가 없습니다.
  2. Microsoft® Word Microsoft 365용
     - 유사도 점수: 0
     - 매칭 타입: partial
     - 매칭 이유: 입력된 이름과 관련된 정보가 없습니다.
  3. Microsoft® Word 2016
     - 유사도 점수: 0
     - 매칭 타입: partial
     - 매칭 이유: 입력된 이름과 관련된 정보가 없습니다.
  4. Microsoft® Word for Microsoft 365
     - 유사도 점수: 0
     - 매칭 타입: partial
     - 매칭 이유: 입력된 이름과 관련된 정보가 없습니다.
  5. 䵩捲潳潦璮⁗潲搠㈰ㄶ㬠浯摩晩敤⁵獩湧⁩呥硴卨慲瀮䱇偌瘲⹃潲攠ㄮ㘮ㄮ
     - 유사도 점수: 0
     - 매칭 타입: partial
     - 매칭 이유: 입력된 이름과 관련된 정보가 없습니다.


🧪 테스트 케이스 6: 메르세데스-벤츠 코리아 홍보팀
   입력: 'Yun-ju Hwang'
--------------------------------------------------
2025-09-12 17:14:54,368 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 17:14:54,368 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 17:14:54,441 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 17:14:54,441 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 17:14:54,503 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 17:14:54,503 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 17:14:54,567 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 17:14:54,567 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 17:14:54,655 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 17:14:54,655 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 17:15:01,942 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 17:15:01,944 - mcp_tools - INFO - ✅ 이메일 유사도 매칭 완료: 'Yun-ju Hwang' → 5개 매치
✅ 매칭 성공!
  - 총 후보 수: 17개
  - 매치 결과: 5개
  - 검색 필드 타입: all

🎯 매치 결과:
  1. Ju, Hyeyeon (191-Extern-MBK)
     - 유사도 점수: 90.0
     - 매칭 타입: name_similar
     - 매칭 이유: 이름의 순서가 바뀐 경우 (예: 'Hyeyeon Ju' ↔ 'Ju, Hyeyeon')
  2. Jeong, Yeeun (191) on behalf of korea_com (191-NPM)
     - 유사도 점수: 30.0
     - 매칭 타입: partial
     - 매칭 이유: 이름의 일부가 일치하거나 유사
  3. Jeong, Yeeun (691)
     - 유사도 점수: 30.0
     - 매칭 타입: partial
     - 매칭 이유: 이름의 일부가 일치하거나 유사
  4. Shim, Ellen (191)
     - 유사도 점수: 30.0
     - 매칭 타입: partial
     - 매칭 이유: 이름의 일부가 일치하거나 유사
  5. Song, Jieun (191)
     - 유사도 점수: 30.0
     - 매칭 타입: partial
     - 매칭 이유: 이름의 일부가 일치하거나 유사


🧪 테스트 케이스 7: Yun-ju Hwang의 한국어 이름
   입력: '황윤주'
--------------------------------------------------
2025-09-12 17:15:01,945 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 17:15:01,945 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 17:15:02,023 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 17:15:02,023 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 17:15:02,094 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 17:15:02,094 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 17:15:02,155 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 17:15:02,155 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 17:15:02,227 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 17:15:02,227 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 17:15:08,721 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 17:15:08,722 - mcp_tools - INFO - ✅ 이메일 유사도 매칭 완료: '황윤주' → 5개 매치
✅ 매칭 성공!
  - 총 후보 수: 17개
  - 매치 결과: 5개
  - 검색 필드 타입: all

🎯 매치 결과:
  1. Ju, Hyeyeon (191-Extern-MBK)
     - 유사도 점수: 30.0
     - 매칭 타입: partial
     - 매칭 이유: 이름의 일부가 일치
  2. Joo, Jaeyool (191)
     - 유사도 점수: 30.0
     - 매칭 타입: partial
     - 매칭 이유: 이름의 일부가 일치
  3. Jeong, Yeeun (191) on behalf of korea_com (191-NPM)
     - 유사도 점수: 30.0
     - 매칭 타입: partial
     - 매칭 이유: 이름의 일부가 일치
  4. Jeong, Yeeun (691)
     - 유사도 점수: 30.0
     - 매칭 타입: partial
     - 매칭 이유: 이름의 일부가 일치
  5. Song, Jieun (191)
     - 유사도 점수: 30.0
     - 매칭 타입: partial
     - 매칭 이유: 이름의 일부가 일치


🧪 테스트 케이스 8: 메르세데스-벤츠 코리아 홍보팀
   입력: 'Jieun Song'
--------------------------------------------------
2025-09-12 17:15:08,723 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 17:15:08,723 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 17:15:08,798 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 17:15:08,798 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 17:15:08,874 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 17:15:08,874 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 17:15:08,947 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 17:15:08,947 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 17:15:09,008 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 17:15:09,008 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 17:15:20,908 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 17:15:20,910 - mcp_tools - INFO - ✅ 이메일 유사도 매칭 완료: 'Jieun Song' → 5개 매치
✅ 매칭 성공!
  - 총 후보 수: 17개
  - 매치 결과: 5개
  - 검색 필드 타입: all

🎯 매치 결과:
  1. Song, Jieun (691)
     - 유사도 점수: 100.0
     - 매칭 타입: exact
     - 매칭 이유: 이름이 완전히 일치합니다. 'Jieun Song'과 'Song, Jieun'은 같은 이름이며, 순서가 바뀐 경우에도 정확한 일치로 간주됩니다.
  2. Song, Jieun (191)
     - 유사도 점수: 100.0
     - 매칭 타입: exact
     - 매칭 이유: 이름이 완전히 일치합니다. 'Jieun Song'과 'Song, Jieun'은 같은 이름이며, 순서가 바뀐 경우에도 정확한 일치로 간주됩니다.
  3. Jeong, Yeeun (691)
     - 유사도 점수: 90.0
     - 매칭 타입: name_similar
     - 매칭 이유: 이름의 일부가 유사합니다. 'Jieun'과 'Yeeun'은 발음이 유사하며, 'Song'과 'Jeong'은 성씨가 다릅니다. 이는 이름 유사로 간주됩니다.
  4. Jeong, Yeeun (191) on behalf of korea_com (191-NPM)
     - 유사도 점수: 90.0
     - 매칭 타입: name_similar
     - 매칭 이유: 이름의 일부가 유사합니다. 'Jieun'과 'Yeeun'은 발음이 유사하며, 'Song'과 'Jeong'은 성씨가 다릅니다. 이는 이름 유사로 간주됩니다.
  5. Joo, Jaeyool (191)
     - 유사도 점수: 30.0
     - 매칭 타입: partial
     - 매칭 이유: 이름의 일부가 일치합니다. 'Jieun'과 'Jaeyool'은 일부가 유사하지만, 전체적으로는 다릅니다. 이는 부분 일치로 간주됩니다.


🧪 테스트 케이스 9: Jieun Song의 한국어 이름
   입력: '송지은'
--------------------------------------------------
2025-09-12 17:15:20,910 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 17:15:20,910 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 17:15:20,984 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 17:15:20,984 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 17:15:21,063 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 17:15:21,063 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 17:15:21,134 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 17:15:21,134 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 17:15:21,207 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 17:15:21,207 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 17:15:31,188 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 17:15:31,190 - mcp_tools - INFO - ✅ 이메일 유사도 매칭 완료: '송지은' → 5개 매치
✅ 매칭 성공!
  - 총 후보 수: 17개
  - 매치 결과: 5개
  - 검색 필드 타입: all

🎯 매치 결과:
  1. Song, Jieun (691)
     - 유사도 점수: 90.0
     - 매칭 타입: name_similar
     - 매칭 이유: 이름의 순서가 바뀌었고, 한글 이름과 영어 이름이 매칭됩니다. '송지은'과 'Song, Jieun'은 같은 이름입니다.
  2. Song, Jieun (191)
     - 유사도 점수: 90.0
     - 매칭 타입: name_similar
     - 매칭 이유: 이름의 순서가 바뀌었고, 한글 이름과 영어 이름이 매칭됩니다. '송지은'과 'Song, Jieun'은 같은 이름입니다.
  3. Jeong, Yeeun (691)
     - 유사도 점수: 30.0
     - 매칭 타입: partial
     - 매칭 이유: 이름의 일부가 유사합니다. '송지은'과 'Jeong, Yeeun'은 일부 글자가 비슷하지만, 다른 이름입니다.
  4. Ju, Hyeyeon (191-Extern-MBK)
     - 유사도 점수: 30.0
     - 매칭 타입: partial
     - 매칭 이유: 이름의 일부가 유사합니다. '송지은'과 'Ju, Hyeyeon'은 일부 글자가 비슷하지만, 다른 이름입니다.
  5. Joo, Jaeyool (191)
     - 유사도 점수: 30.0
     - 매칭 타입: partial
     - 매칭 이유: 이름의 일부가 유사합니다. '송지은'과 'Joo, Jaeyool'은 일부 글자가 비슷하지만, 다른 이름입니다.


🧪 테스트 케이스 10: PRGATE
   입력: 'Eunha Jeong'
--------------------------------------------------
2025-09-12 17:15:31,191 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 17:15:31,191 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 17:15:31,263 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 17:15:31,263 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 17:15:31,334 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 17:15:31,335 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 17:15:31,396 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 17:15:31,396 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 17:15:31,474 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 17:15:31,474 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 17:15:38,912 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 17:15:38,913 - mcp_tools - INFO - ✅ 이메일 유사도 매칭 완료: 'Eunha Jeong' → 5개 매치
✅ 매칭 성공!
  - 총 후보 수: 17개
  - 매치 결과: 5개
  - 검색 필드 타입: all

🎯 매치 결과:
  1. Jeong, Yeeun (191) on behalf of korea_com (191-NPM)
     - 유사도 점수: 90.0
     - 매칭 타입: name_similar
     - 매칭 이유: 이름의 순서가 바뀐 경우 (예: '조효원' ↔ '효원 조')
  2. Jeong, Yeeun (691)
     - 유사도 점수: 90.0
     - 매칭 타입: name_similar
     - 매칭 이유: 이름의 순서가 바뀐 경우 (예: '조효원' ↔ '효원 조')
  3. Song, Jieun (691)
     - 유사도 점수: 30.0
     - 매칭 타입: partial
     - 매칭 이유: 이름의 일부가 일치하거나 유사
  4. Song, Jieun (191)
     - 유사도 점수: 30.0
     - 매칭 타입: partial
     - 매칭 이유: 이름의 일부가 일치하거나 유사
  5. Shim, Ellen (191)
     - 유사도 점수: 5.0
     - 매칭 타입: related
     - 매칭 이유: 업무적, 조직적 관련성이 있는 경우


🧪 테스트 케이스 11: Eunha Jeong의 한국어 이름
   입력: '정은하'
--------------------------------------------------
2025-09-12 17:15:38,914 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 17:15:38,914 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 17:15:38,988 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 17:15:38,988 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 17:15:39,061 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 17:15:39,061 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 17:15:39,137 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 17:15:39,138 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 17:15:39,222 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 17:15:39,222 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 17:15:46,844 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 17:15:46,846 - mcp_tools - INFO - ✅ 이메일 유사도 매칭 완료: '정은하' → 5개 매치
✅ 매칭 성공!
  - 총 후보 수: 17개
  - 매치 결과: 5개
  - 검색 필드 타입: all

🎯 매치 결과:
  1. Jeong, Yeeun (191) on behalf of korea_com (191-NPM)
     - 유사도 점수: 90.0
     - 매칭 타입: name_similar
     - 매칭 이유: 이름의 순서가 바뀐 경우 (예: '정은하' ↔ 'Jeong, Yeeun')
  2. Jeong, Yeeun (691)
     - 유사도 점수: 90.0
     - 매칭 타입: name_similar
     - 매칭 이유: 이름의 순서가 바뀐 경우 (예: '정은하' ↔ 'Jeong, Yeeun')
  3. Song, Jieun (191)
     - 유사도 점수: 30.0
     - 매칭 타입: partial
     - 매칭 이유: 이름의 일부가 일치하거나 유사
  4. Song, Jieun (691)
     - 유사도 점수: 30.0
     - 매칭 타입: partial
     - 매칭 이유: 이름의 일부가 일치하거나 유사
  5. Shim, Ellen (191)
     - 유사도 점수: 30.0
     - 매칭 타입: partial
     - 매칭 이유: 이름의 일부가 일치하거나 유사

✅ 이름 매칭 테스트 완료!

🔍 3단계: 키워드 유사도 매칭 테스트 (MBG 실제 키워드 기반)
------------------------------------------------------------

🧪 키워드 테스트 케이스 1: 배터리 관련 - EQC 모델
   입력: 'EQC'
--------------------------------------------------
2025-09-12 17:15:46,846 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 17:15:46,846 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 17:15:46,923 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 17:15:46,923 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 17:15:46,995 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 17:15:46,995 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 17:15:47,059 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 17:15:47,060 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 17:15:47,132 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 17:15:47,132 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 17:15:55,661 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 17:15:55,663 - mcp_tools - INFO - ✅ 이메일 유사도 매칭 완료: 'EQC' → 5개 매치
✅ 매칭 성공!
  - 총 후보 수: 17개
  - 매치 결과: 5개
  - 검색 필드 타입: all

🎯 매치 결과:
  1. Microsoft® Word Microsoft 365용
     - 유사도 점수: 0
     - 매칭 타입: none
     - 매칭 이유: 이름 또는 이메일 주소에서 'EQC'와 관련된 유사성이 없습니다.
  2. 䵩捲潳潦璮⁗潲搠㈰ㄶ㬠浯摩晩敤⁵獩湧⁩呥硴卨慲瀮䱇偌瘲⹃潲攠ㄮ㘮ㄮ
     - 유사도 점수: 0
     - 매칭 타입: none
     - 매칭 이유: 이름 또는 이메일 주소에서 'EQC'와 관련된 유사성이 없습니다.
  3. Microsoft® Word 2016
     - 유사도 점수: 0
     - 매칭 타입: none
     - 매칭 이유: 이름 또는 이메일 주소에서 'EQC'와 관련된 유사성이 없습니다.
  4. Park, Jaekyung (191)
     - 유사도 점수: 0
     - 매칭 타입: none
     - 매칭 이유: 이름 또는 이메일 주소에서 'EQC'와 관련된 유사성이 없습니다.
  5. Kim, Ji-Hyun (191)
     - 유사도 점수: 0
     - 매칭 타입: none
     - 매칭 이유: 이름 또는 이메일 주소에서 'EQC'와 관련된 유사성이 없습니다.


🧪 키워드 테스트 케이스 2: 배터리 관련 - EQE 모델
   입력: 'EQE'
--------------------------------------------------
2025-09-12 17:15:55,663 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 17:15:55,663 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 17:15:55,741 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 17:15:55,742 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 17:15:55,813 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 17:15:55,813 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 17:15:55,884 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 17:15:55,884 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 17:15:55,954 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 17:15:55,954 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 17:16:03,846 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 17:16:03,848 - mcp_tools - INFO - ✅ 이메일 유사도 매칭 완료: 'EQE' → 5개 매치
✅ 매칭 성공!
  - 총 후보 수: 17개
  - 매치 결과: 5개
  - 검색 필드 타입: all

🎯 매치 결과:
  1. NaN
     - 유사도 점수: 0
     - 매칭 타입: partial
     - 매칭 이유: 입력된 쿼리 'EQE'와 관련된 정보가 없습니다.
  2. Microsoft® Word for Microsoft 365
     - 유사도 점수: 0
     - 매칭 타입: partial
     - 매칭 이유: 입력된 쿼리 'EQE'와 관련된 정보가 없습니다.
  3. Microsoft® Word Microsoft 365용
     - 유사도 점수: 0
     - 매칭 타입: partial
     - 매칭 이유: 입력된 쿼리 'EQE'와 관련된 정보가 없습니다.
  4. Microsoft® Word 2016
     - 유사도 점수: 0
     - 매칭 타입: partial
     - 매칭 이유: 입력된 쿼리 'EQE'와 관련된 정보가 없습니다.
  5. 䵩捲潳潦璮⁗潲搠㈰ㄶ㬠浯摩晩敤⁵獩湧⁩呥硴卨慲瀮䱇偌瘲⹃潲攠ㄮ㘮ㄮ
     - 유사도 점수: 0
     - 매칭 타입: partial
     - 매칭 이유: 입력된 쿼리 'EQE'와 관련된 정보가 없습니다.


🧪 키워드 테스트 케이스 3: 배터리 관련 - EQS 모델
   입력: 'EQS'
--------------------------------------------------
2025-09-12 17:16:03,848 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 17:16:03,848 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 17:16:03,922 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 17:16:03,922 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 17:16:03,994 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 17:16:03,994 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 17:16:04,069 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 17:16:04,069 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 17:16:04,142 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 17:16:04,143 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 17:16:13,045 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 17:16:13,046 - mcp_tools - INFO - ✅ 이메일 유사도 매칭 완료: 'EQS' → 5개 매치
✅ 매칭 성공!
  - 총 후보 수: 17개
  - 매치 결과: 5개
  - 검색 필드 타입: all

🎯 매치 결과:
  1. Microsoft® Word Microsoft 365용
     - 유사도 점수: 0.0
     - 매칭 타입: none
     - 매칭 이유: 이름 또는 이메일 주소에서 'EQS'와 관련된 유사성이 없음
  2. 䵩捲潳潦璮⁗潲搠㈰ㄶ㬠浯摩晩敤⁵獩湧⁩呥硴卨慲瀮䱇偌瘲⹃潲攠ㄮ㘮ㄮ
     - 유사도 점수: 0.0
     - 매칭 타입: none
     - 매칭 이유: 이름 또는 이메일 주소에서 'EQS'와 관련된 유사성이 없음
  3. Microsoft® Word 2016
     - 유사도 점수: 0.0
     - 매칭 타입: none
     - 매칭 이유: 이름 또는 이메일 주소에서 'EQS'와 관련된 유사성이 없음
  4. Park, Jaekyung (191)
     - 유사도 점수: 0.0
     - 매칭 타입: none
     - 매칭 이유: 이름 또는 이메일 주소에서 'EQS'와 관련된 유사성이 없음
  5. Kim, Ji-Hyun (191)
     - 유사도 점수: 0.0
     - 매칭 타입: none
     - 매칭 이유: 이름 또는 이메일 주소에서 'EQS'와 관련된 유사성이 없음


🧪 키워드 테스트 케이스 4: 배터리 관련 - 전기차
   입력: '전기차'
--------------------------------------------------
2025-09-12 17:16:13,047 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 17:16:13,047 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 17:16:13,122 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 17:16:13,123 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 17:16:13,195 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 17:16:13,195 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 17:16:13,269 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 17:16:13,269 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 17:16:13,316 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 17:16:13,316 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 17:16:13,594 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 17:16:13,595 - mcp_tools - INFO - ✅ 이메일 유사도 매칭 완료: '전기차' → 0개 매치
✅ 매칭 성공!
  - 총 후보 수: 17개
  - 매치 결과: 0개
  - 검색 필드 타입: all
  📭 매치 결과가 없습니다.


🧪 키워드 테스트 케이스 5: 배터리 관련 - 배터리
   입력: '배터리'
--------------------------------------------------
2025-09-12 17:16:13,596 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 17:16:13,596 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 17:16:13,654 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 17:16:13,654 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 17:16:13,725 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 17:16:13,726 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 17:16:13,772 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 17:16:13,772 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 17:16:13,845 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 17:16:13,846 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 17:16:14,124 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 17:16:14,126 - mcp_tools - INFO - ✅ 이메일 유사도 매칭 완료: '배터리' → 0개 매치
✅ 매칭 성공!
  - 총 후보 수: 17개
  - 매치 결과: 0개
  - 검색 필드 타입: all
  📭 매치 결과가 없습니다.


🧪 키워드 테스트 케이스 6: 기술 - MBUX 시스템
   입력: 'MBUX'
--------------------------------------------------
2025-09-12 17:16:14,126 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 17:16:14,126 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 17:16:14,221 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 17:16:14,221 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 17:16:14,291 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 17:16:14,292 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 17:16:14,363 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 17:16:14,363 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 17:16:14,434 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 17:16:14,434 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 17:16:22,188 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 17:16:22,189 - mcp_tools - INFO - ✅ 이메일 유사도 매칭 완료: 'MBUX' → 5개 매치
✅ 매칭 성공!
  - 총 후보 수: 17개
  - 매치 결과: 5개
  - 검색 필드 타입: all

🎯 매치 결과:
  1. Microsoft® Word Microsoft 365용
     - 유사도 점수: 0.0
     - 매칭 타입: none
     - 매칭 이유: 이름이 아예 다르며, 관련성이 없음
  2. 䵩捲潳潦璮⁗潲搠㈰ㄶ㬠浯摩晩敤⁵獩湧⁩呥硴卨慲瀮䱇偌瘲⹃潲攠ㄮ㘮ㄮ
     - 유사도 점수: 0.0
     - 매칭 타입: none
     - 매칭 이유: 이름이 아예 다르며, 관련성이 없음
  3. Microsoft® Word 2016
     - 유사도 점수: 0.0
     - 매칭 타입: none
     - 매칭 이유: 이름이 아예 다르며, 관련성이 없음
  4. Park, Jaekyung (191)
     - 유사도 점수: 0.0
     - 매칭 타입: none
     - 매칭 이유: 이름이 아예 다르며, 관련성이 없음
  5. Kim, Ji-Hyun (191)
     - 유사도 점수: 0.0
     - 매칭 타입: none
     - 매칭 이유: 이름이 아예 다르며, 관련성이 없음


🧪 키워드 테스트 케이스 7: 기술 - 4MATIC 사륜구동
   입력: '4MATIC'
--------------------------------------------------
2025-09-12 17:16:22,190 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 17:16:22,190 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 17:16:22,265 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 17:16:22,265 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 17:16:22,332 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 17:16:22,333 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 17:16:22,407 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 17:16:22,407 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 17:16:22,482 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 17:16:22,482 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 17:16:24,350 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 17:16:24,351 - mcp_tools - INFO - ✅ 이메일 유사도 매칭 완료: '4MATIC' → 1개 매치
✅ 매칭 성공!
  - 총 후보 수: 17개
  - 매치 결과: 1개
  - 검색 필드 타입: all

🎯 매치 결과:
  1. 4MATIC
     - 유사도 점수: 0.0
     - 매칭 타입: none
     - 매칭 이유: None of the provided candidates match the query '4MATIC'. The query appears to be a brand or product name, not a person's name or email address.


🧪 키워드 테스트 케이스 8: 기술 - 하이브리드
   입력: '하이브리드'
--------------------------------------------------
2025-09-12 17:16:24,352 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 17:16:24,352 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 17:16:24,424 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 17:16:24,424 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 17:16:24,481 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 17:16:24,481 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 17:16:24,548 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 17:16:24,548 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 17:16:24,610 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 17:16:24,610 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 17:16:33,651 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 17:16:33,653 - mcp_tools - INFO - ✅ 이메일 유사도 매칭 완료: '하이브리드' → 5개 매치
✅ 매칭 성공!
  - 총 후보 수: 17개
  - 매치 결과: 5개
  - 검색 필드 타입: all

🎯 매치 결과:
  1. Microsoft® Word Microsoft 365용
     - 유사도 점수: 0.0
     - 매칭 타입: none
     - 매칭 이유: 이름이 '하이브리드'와 관련이 없으며, 이메일 주소가 아님
  2. 䵩捲潳潦璮⁗潲搠㈰ㄶ㬠浯摩晩敤⁵獩湧⁩呥硴卨慲瀮䱇偌瘲⹃潲攠ㄮ㘮ㄮ
     - 유사도 점수: 0.0
     - 매칭 타입: none
     - 매칭 이유: 이름이 '하이브리드'와 관련이 없으며, 이메일 주소가 아님
  3. Microsoft® Word 2016
     - 유사도 점수: 0.0
     - 매칭 타입: none
     - 매칭 이유: 이름이 '하이브리드'와 관련이 없으며, 이메일 주소가 아님
  4. NaN
     - 유사도 점수: 0.0
     - 매칭 타입: none
     - 매칭 이유: 이름이 '하이브리드'와 관련이 없으며, 이메일 주소가 아님
  5. Microsoft® Word for Microsoft 365
     - 유사도 점수: 0.0
     - 매칭 타입: none
     - 매칭 이유: 이름이 '하이브리드'와 관련이 없으며, 이메일 주소가 아님


🧪 키워드 테스트 케이스 9: 기술 - 전동화
   입력: '전동화'
--------------------------------------------------
2025-09-12 17:16:33,654 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 17:16:33,654 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 17:16:33,724 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 17:16:33,724 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 17:16:33,790 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 17:16:33,790 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 17:16:33,864 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 17:16:33,864 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 17:16:33,926 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 17:16:33,927 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 17:16:39,675 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 17:16:39,677 - mcp_tools - INFO - ✅ 이메일 유사도 매칭 완료: '전동화' → 5개 매치
✅ 매칭 성공!
  - 총 후보 수: 17개
  - 매치 결과: 5개
  - 검색 필드 타입: all

🎯 매치 결과:
  1. 전동화
     - 유사도 점수: 100.0
     - 매칭 타입: exact
     - 매칭 이유: 이름이 완전히 일치합니다.
  2. 전동화
     - 유사도 점수: 100.0
     - 매칭 타입: exact
     - 매칭 이유: 이름이 완전히 일치합니다.
  3. 전동화
     - 유사도 점수: 100.0
     - 매칭 타입: exact
     - 매칭 이유: 이름이 완전히 일치합니다.
  4. 전동화
     - 유사도 점수: 100.0
     - 매칭 타입: exact
     - 매칭 이유: 이름이 완전히 일치합니다.
  5. 전동화
     - 유사도 점수: 100.0
     - 매칭 타입: exact
     - 매칭 이유: 이름이 완전히 일치합니다.


🧪 키워드 테스트 케이스 10: 협력사 - SOCAR
   입력: 'SOCAR'
--------------------------------------------------
2025-09-12 17:16:39,677 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 17:16:39,677 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 17:16:39,751 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 17:16:39,751 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 17:16:39,823 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 17:16:39,823 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 17:16:39,884 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 17:16:39,884 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 17:16:39,954 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 17:16:39,954 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 17:16:44,814 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 17:16:44,815 - mcp_tools - INFO - ✅ 이메일 유사도 매칭 완료: 'SOCAR' → 5개 매치
✅ 매칭 성공!
  - 총 후보 수: 17개
  - 매치 결과: 5개
  - 검색 필드 타입: all

🎯 매치 결과:
  1. SOCAR
     - 유사도 점수: 100.0
     - 매칭 타입: exact
     - 매칭 이유: 정확한 일치
  2. SOCAR
     - 유사도 점수: 90.0
     - 매칭 타입: name_similar
     - 매칭 이유: 이름 유사
  3. SOCAR
     - 유사도 점수: 80.0
     - 매칭 타입: username
     - 매칭 이유: 이메일 사용자명 일치
  4. SOCAR
     - 유사도 점수: 30.0
     - 매칭 타입: partial
     - 매칭 이유: 부분 일치
  5. SOCAR
     - 유사도 점수: 5.0
     - 매칭 타입: related
     - 매칭 이유: 관련성


🧪 키워드 테스트 케이스 11: 협력사 - 몽클레르
   입력: '몽클레르'
--------------------------------------------------
2025-09-12 17:16:44,816 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 17:16:44,816 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 17:16:44,895 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 17:16:44,895 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 17:16:44,986 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 17:16:44,987 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 17:16:45,053 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 17:16:45,053 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 17:16:45,126 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 17:16:45,126 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 17:16:45,405 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 17:16:45,407 - mcp_tools - INFO - ✅ 이메일 유사도 매칭 완료: '몽클레르' → 0개 매치
✅ 매칭 성공!
  - 총 후보 수: 17개
  - 매치 결과: 0개
  - 검색 필드 타입: all
  📭 매치 결과가 없습니다.


🧪 키워드 테스트 케이스 12: 협력사 - 버질 아블로
   입력: '버질 아블로'
--------------------------------------------------
2025-09-12 17:16:45,407 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 17:16:45,407 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 17:16:45,480 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 17:16:45,480 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 17:16:45,552 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 17:16:45,552 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 17:16:45,613 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 17:16:45,613 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 17:16:45,684 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 17:16:45,685 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 17:16:52,694 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 17:16:52,695 - mcp_tools - INFO - ✅ 이메일 유사도 매칭 완료: '버질 아블로' → 5개 매치
✅ 매칭 성공!
  - 총 후보 수: 17개
  - 매치 결과: 5개
  - 검색 필드 타입: all

🎯 매치 결과:
  1. NaN
     - 유사도 점수: 0
     - 매칭 타입: partial
     - 매칭 이유: 입력된 이름과 관련된 정보가 없습니다.
  2. Microsoft® Word Microsoft 365용
     - 유사도 점수: 0
     - 매칭 타입: partial
     - 매칭 이유: 입력된 이름과 관련된 정보가 없습니다.
  3. Microsoft® Word 2016
     - 유사도 점수: 0
     - 매칭 타입: partial
     - 매칭 이유: 입력된 이름과 관련된 정보가 없습니다.
  4. Microsoft® Word for Microsoft 365
     - 유사도 점수: 0
     - 매칭 타입: partial
     - 매칭 이유: 입력된 이름과 관련된 정보가 없습니다.
  5. 䵩捲潳潦璮⁗潲搠㈰ㄶ㬠浯摩晩敤⁵獩湧⁩呥硴卨慲瀮䱇偌瘲⹃潲攠ㄮ㘮ㄮ
     - 유사도 점수: 0
     - 매칭 타입: partial
     - 매칭 이유: 입력된 이름과 관련된 정보가 없습니다.


🧪 키워드 테스트 케이스 13: 모델명 - GLB
   입력: 'GLB'
--------------------------------------------------
2025-09-12 17:16:52,696 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 17:16:52,696 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 17:16:52,767 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 17:16:52,767 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 17:16:52,837 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 17:16:52,837 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 17:16:52,900 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 17:16:52,900 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 17:16:52,974 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 17:16:52,975 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 17:17:01,367 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 17:17:01,369 - mcp_tools - INFO - ✅ 이메일 유사도 매칭 완료: 'GLB' → 5개 매치
✅ 매칭 성공!
  - 총 후보 수: 17개
  - 매치 결과: 5개
  - 검색 필드 타입: all

🎯 매치 결과:
  1. Microsoft® Word Microsoft 365용
     - 유사도 점수: 0.0
     - 매칭 타입: none
     - 매칭 이유: 이름 또는 이메일 주소에 GLB와 관련된 정보가 없습니다.
  2. 䵩捲潳潦璮⁗潲搠㈰ㄶ㬠浯摩晩敤⁵獩湧⁩呥硴卨慲瀮䱇偌瘲⹃潲攠ㄮ㘮ㄮ
     - 유사도 점수: 0.0
     - 매칭 타입: none
     - 매칭 이유: 이름 또는 이메일 주소에 GLB와 관련된 정보가 없습니다.
  3. Microsoft® Word 2016
     - 유사도 점수: 0.0
     - 매칭 타입: none
     - 매칭 이유: 이름 또는 이메일 주소에 GLB와 관련된 정보가 없습니다.
  4. Park, Jaekyung (191)
     - 유사도 점수: 0.0
     - 매칭 타입: none
     - 매칭 이유: 이름 또는 이메일 주소에 GLB와 관련된 정보가 없습니다.
  5. Kim, Ji-Hyun (191)
     - 유사도 점수: 0.0
     - 매칭 타입: none
     - 매칭 이유: 이름 또는 이메일 주소에 GLB와 관련된 정보가 없습니다.


🧪 키워드 테스트 케이스 14: 모델명 - GLA
   입력: 'GLA'
--------------------------------------------------
2025-09-12 17:17:01,370 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 17:17:01,370 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 17:17:01,445 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 17:17:01,445 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 17:17:01,518 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 17:17:01,518 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 17:17:01,589 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 17:17:01,589 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 17:17:01,660 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 17:17:01,660 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 17:17:10,053 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 17:17:10,055 - mcp_tools - INFO - ✅ 이메일 유사도 매칭 완료: 'GLA' → 5개 매치
✅ 매칭 성공!
  - 총 후보 수: 17개
  - 매치 결과: 5개
  - 검색 필드 타입: all

🎯 매치 결과:
  1. Microsoft® Word Microsoft 365용
     - 유사도 점수: 0.0
     - 매칭 타입: none
     - 매칭 이유: 이름 또는 이메일 주소에 GLA와 관련된 정보가 없습니다.
  2. 䵩捲潳潦璮⁗潲搠㈰ㄶ㬠浯摩晩敤⁵獩湧⁩呥硴卨慲瀮䱇偌瘲⹃潲攠ㄮ㘮ㄮ
     - 유사도 점수: 0.0
     - 매칭 타입: none
     - 매칭 이유: 이름 또는 이메일 주소에 GLA와 관련된 정보가 없습니다.
  3. Microsoft® Word 2016
     - 유사도 점수: 0.0
     - 매칭 타입: none
     - 매칭 이유: 이름 또는 이메일 주소에 GLA와 관련된 정보가 없습니다.
  4. Park, Jaekyung (191)
     - 유사도 점수: 0.0
     - 매칭 타입: none
     - 매칭 이유: 이름 또는 이메일 주소에 GLA와 관련된 정보가 없습니다.
  5. Kim, Ji-Hyun (191)
     - 유사도 점수: 0.0
     - 매칭 타입: none
     - 매칭 이유: 이름 또는 이메일 주소에 GLA와 관련된 정보가 없습니다.


🧪 키워드 테스트 케이스 15: 모델명 - GLE
   입력: 'GLE'
--------------------------------------------------
2025-09-12 17:17:10,055 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 17:17:10,055 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 17:17:10,115 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 17:17:10,115 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 17:17:10,186 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 17:17:10,186 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 17:17:10,259 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 17:17:10,259 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 17:17:10,337 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 17:17:10,338 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 17:17:18,800 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 17:17:18,802 - mcp_tools - INFO - ✅ 이메일 유사도 매칭 완료: 'GLE' → 5개 매치
✅ 매칭 성공!
  - 총 후보 수: 17개
  - 매치 결과: 5개
  - 검색 필드 타입: all

🎯 매치 결과:
  1. Ju, Hyeyeon (191-Extern-MBK)
     - 유사도 점수: 30.0
     - 매칭 타입: partial
     - 매칭 이유: 이름의 일부 'Hyeyeon'이 쿼리 'GLE'와 부분적으로 유사함
  2. Jeong, Yeeun (191) on behalf of korea_com (191-NPM)
     - 유사도 점수: 30.0
     - 매칭 타입: partial
     - 매칭 이유: 이름의 일부 'Yeeun'이 쿼리 'GLE'와 부분적으로 유사함
  3. Jeong, Yeeun (691)
     - 유사도 점수: 30.0
     - 매칭 타입: partial
     - 매칭 이유: 이름의 일부 'Yeeun'이 쿼리 'GLE'와 부분적으로 유사함
  4. Song, Jieun (191)
     - 유사도 점수: 30.0
     - 매칭 타입: partial
     - 매칭 이유: 이름의 일부 'Jieun'이 쿼리 'GLE'와 부분적으로 유사함
  5. Song, Jieun (691)
     - 유사도 점수: 30.0
     - 매칭 타입: partial
     - 매칭 이유: 이름의 일부 'Jieun'이 쿼리 'GLE'와 부분적으로 유사함


🧪 키워드 테스트 케이스 16: 모델명 - G-Class
   입력: 'G-Class'
--------------------------------------------------
2025-09-12 17:17:18,803 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 17:17:18,803 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 17:17:18,877 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 17:17:18,877 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 17:17:18,947 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 17:17:18,947 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 17:17:19,035 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 17:17:19,035 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 17:17:19,109 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 17:17:19,110 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 17:17:19,388 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 17:17:19,390 - mcp_tools - INFO - ✅ 이메일 유사도 매칭 완료: 'G-Class' → 0개 매치
✅ 매칭 성공!
  - 총 후보 수: 17개
  - 매치 결과: 0개
  - 검색 필드 타입: all
  📭 매치 결과가 없습니다.


🧪 키워드 테스트 케이스 17: 모델명 - AMG
   입력: 'AMG'
--------------------------------------------------
2025-09-12 17:17:19,390 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 17:17:19,390 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 17:17:19,464 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 17:17:19,464 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 17:17:19,534 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 17:17:19,534 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 17:17:19,595 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 17:17:19,595 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 17:17:19,666 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 17:17:19,666 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 17:17:28,295 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 17:17:28,296 - mcp_tools - INFO - ✅ 이메일 유사도 매칭 완료: 'AMG' → 5개 매치
✅ 매칭 성공!
  - 총 후보 수: 17개
  - 매치 결과: 5개
  - 검색 필드 타입: all

🎯 매치 결과:
  1. Microsoft® Word Microsoft 365용
     - 유사도 점수: 0.0
     - 매칭 타입: none
     - 매칭 이유: 이름 또는 이메일 주소에서 'AMG'와 관련된 정보가 없습니다.
  2. 䵩捲潳潦璮⁗潲搠㈰ㄶ㬠浯摩晩敤⁵獩湧⁩呥硴卨慲瀮䱇偌瘲⹃潲攠ㄮ㘮ㄮ
     - 유사도 점수: 0.0
     - 매칭 타입: none
     - 매칭 이유: 이름 또는 이메일 주소에서 'AMG'와 관련된 정보가 없습니다.
  3. Microsoft® Word 2016
     - 유사도 점수: 0.0
     - 매칭 타입: none
     - 매칭 이유: 이름 또는 이메일 주소에서 'AMG'와 관련된 정보가 없습니다.
  4. Park, Jaekyung (191)
     - 유사도 점수: 0.0
     - 매칭 타입: none
     - 매칭 이유: 이름 또는 이메일 주소에서 'AMG'와 관련된 정보가 없습니다.
  5. Kim, Ji-Hyun (191)
     - 유사도 점수: 0.0
     - 매칭 타입: none
     - 매칭 이유: 이름 또는 이메일 주소에서 'AMG'와 관련된 정보가 없습니다.

✅ 키워드 매칭 테스트 완료!
/raid1/workspace/kars-agent/weaviate-mcp/tmp_sungwon_chae/test_extract_value_tool_modified.py:477: ResourceWarning: unclosed <socket.socket fd=10, family=2, type=1, proto=6, laddr=('10.10.150.195', 50304), raddr=('10.10.150.195', 8080)>
  await test_name_matching()
ResourceWarning: Enable tracemalloc to get the object allocation traceback

🎉 모든 테스트 완료!
(.venv) min.choi10@wss-195:/raid1/workspace/kars-agent/weaviate-mcp/tmp_sungwon_chae$ 
