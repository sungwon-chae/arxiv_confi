(.venv) min.choi10@wss-195:/raid1/workspace/kars-agent/weaviate-mcp/tmp_sungwon_chae$ python test_extract_value_tool_modified.py 
🚀 Weaviate MCP 도구 테스트 시작

2025-09-12 18:07:52,323 - mcp_tools - INFO - Weaviate MCP 도구 초기화 완료
2025-09-12 18:07:55,285 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
Test Query Response:  ChatCompletion(id='chatcmpl-8ca826f5b7b646dcbbc0f82c18349670', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='<think>\nOkay, the user just said "hi!" so I need to respond appropriately. Let me think about the best way to reply. Since it\'s a greeting, I should acknowledge their message and offer assistance. Maybe say something like "Hello! How can I help you today?" That\'s friendly and opens the door for them to ask questions or share what they need. I should keep it simple and welcoming. Let me make sure there are no typos and that the tone is positive.\n</think>\n\nHello! How can I help you today? 😊', refusal=None, role='assistant', annotations=None, audio=None, function_call=None, tool_calls=[], reasoning_content=None), stop_reason=None)], created=1757668077, model='/data/models_ckpt/Qwen3-32B', object='chat.completion', service_tier=None, system_fingerprint=None, usage=CompletionUsage(completion_tokens=113, prompt_tokens=10, total_tokens=123, completion_tokens_details=None, prompt_tokens_details=None), prompt_logprobs=None)
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
2025-09-12 18:07:55,302 - mcp_tools - INFO - 🔍 필터 추출 시작: 'Lee Sang-kuk이 언급된 모든 이메일을 찾아주세요'
2025-09-12 18:07:56,825 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:07:56,826 - kars_db - INFO - 🚀 RAG 벡터 데이터베이스 초기화 시작
2025-09-12 18:07:56,826 - simple_manager - INFO - Weaviate URL: http://10.10.150.195:8080
2025-09-12 18:07:56,826 - simple_manager - INFO - OpenAI Base URL: http://10.10.190.1:8125
2025-09-12 18:07:56,827 - kars_db - INFO - ✅ VectorDB 매니저 초기화 완료
2025-09-12 18:07:56,875 - httpx - INFO - HTTP Request: GET http://10.10.190.1:8125/v1/models "HTTP/1.1 200 OK"
2025-09-12 18:07:56,877 - weaviate_db - INFO - ✅ vLLM 서버에서 모델명 가져옴: /data/models_ckpt/bge-m3
2025-09-12 18:07:56,892 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8125/v1/embeddings "HTTP/1.1 200 OK"
2025-09-12 18:07:56,896 - weaviate_db - INFO - ✅ 샘플 임베딩 생성 성공 (차원: 1024)
2025-09-12 18:07:56,934 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/.well-known/openid-configuration "HTTP/1.1 404 Not Found"
2025-09-12 18:07:56,960 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/meta "HTTP/1.1 200 OK"
2025-09-12 18:07:58,995 - weaviate_db - INFO - ✅ Weaviate 클라이언트 연결 성공: http://10.10.150.195:8080
2025-09-12 18:07:58,996 - weaviate_db - INFO - 📡 OpenAI Base URL (Python용): http://10.10.190.1:8125/v1
2025-09-12 18:07:58,996 - weaviate_db - INFO - 📡 OpenAI Base URL (Weaviate용): http://10.10.190.1:8125
2025-09-12 18:07:58,996 - weaviate_db - INFO - 🔧 동적 모델명: /data/models_ckpt/bge-m3
2025-09-12 18:07:58,996 - simple_manager - INFO - DB 연결 초기화 완료
2025-09-12 18:07:59,000 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema "HTTP/1.1 200 OK"
2025-09-12 18:07:59,005 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema/DocumentChunk "HTTP/1.1 200 OK"
2025-09-12 18:07:59,012 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema/EnronDocument "HTTP/1.1 200 OK"
2025-09-12 18:07:59,013 - weaviate_db - INFO - 스키마 조회 완료: 2개 클래스
2025-09-12 18:07:59,013 - simple_manager - WARNING - 클래스 매핑 파일이 없습니다. 기본 규칙을 사용합니다.
2025-09-12 18:07:59,013 - simple_manager - INFO - 기존 클래스 등록: chunk_db -> DocumentChunk
2025-09-12 18:07:59,013 - simple_manager - INFO - 기존 클래스 등록: enron_db -> EnronDocument
2025-09-12 18:07:59,013 - simple_manager - INFO - 총 2개 DB에 클래스 등록 완료
2025-09-12 18:07:59,013 - simple_manager - INFO -   chunk_db: ['DocumentChunk']
2025-09-12 18:07:59,014 - simple_manager - INFO -   enron_db: ['EnronDocument']
2025-09-12 18:07:59,017 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema "HTTP/1.1 200 OK"
2025-09-12 18:07:59,021 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema/DocumentChunk "HTTP/1.1 200 OK"
2025-09-12 18:07:59,024 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema/EnronDocument "HTTP/1.1 200 OK"
2025-09-12 18:07:59,025 - weaviate_db - INFO - 스키마 조회 완료: 2개 클래스
2025-09-12 18:07:59,025 - kars_db - INFO - 📊 사용 가능한 클래스들: ['DocumentChunk', 'EnronDocument']
2025-09-12 18:07:59,025 - kars_db - INFO - ✅ 사용할 클래스명: DocumentChunk
2025-09-12 18:07:59,025 - mcp_tools - INFO - ✅ RAG 데이터베이스 초기화 성공: kars_test
2025-09-12 18:07:59,025 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:07:59,025 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:07:59,113 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:07:59,113 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:07:59,190 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:07:59,190 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:07:59,273 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:07:59,274 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:07:59,352 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:07:59,353 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:07:59,353 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
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
2025-09-12 18:07:59,353 - mcp_tools - INFO - 🔍 단순 RAG 검색 실행: 'Lee Sang-kuk이 언급된 모든 이메일을 찾아주세요' (limit: 5)
2025-09-12 18:07:59,353 - kars_db - INFO - 🔍 검색 시작: 'Lee Sang-kuk이 언급된 모든 이메일을 찾아주세요' (limit: 5)
2025-09-12 18:07:59,414 - weaviate_db - INFO - 🔍 검색 완료: 5개 결과 (쿼리: 'Lee Sang-kuk이 언급된 모든 이메일을 찾아주세요'
2025-09-12 18:07:59,414 - kars_db - INFO - ✅ 검색 완료: 5개 결과 반환
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
2025-09-12 18:07:59,415 - mcp_tools - INFO - 🔍 필터 추출 시작: '메르세데스-벤츠 코리아 홍보팀이 작성한 문서들'
2025-09-12 18:08:01,325 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:08:01,327 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:08:01,327 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:08:01,405 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:08:01,405 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:08:01,472 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:08:01,472 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:08:01,544 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:08:01,544 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:08:01,614 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:08:01,614 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:08:02,826 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:08:02,827 - mcp_tools - INFO - ✅ custodian 필드 수정: '메르세데스-벤츠 코리아 홍보팀' → '세진 김' (유사도: 30.00)
2025-09-12 18:08:02,827 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian='세진 김' ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
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
2025-09-12 18:08:02,828 - mcp_tools - INFO - 🔍 필터 검색 실행: class_name=DocumentChunk, limit=5, filters={'custodian': '세진 김'}
2025-09-12 18:08:02,828 - kars_db - INFO - 필터 검색 시작: class_name=DocumentChunk, limit=5, filters={'custodian': '세진 김'}
2025-09-12 18:08:02,828 - kars_db - INFO - 필터와 함께 검색: {'custodian': '세진 김'}
2025-09-12 18:08:02,839 - kars_db - INFO - ✅ 필터 검색 완료: 5개 결과 반환
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
2025-09-12 18:08:02,841 - mcp_tools - INFO - 🔍 필터 추출 시작: 'EQC 전기차 관련 모든 자료'
2025-09-12 18:08:04,359 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:08:04,361 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:08:04,361 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:08:04,443 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:08:04,444 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:08:04,521 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:08:04,522 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:08:04,596 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:08:04,597 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:08:04,677 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:08:04,678 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:08:04,678 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
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
2025-09-12 18:08:04,678 - mcp_tools - INFO - 🔍 단순 RAG 검색 실행: 'EQC 전기차 관련 모든 자료' (limit: 5)
2025-09-12 18:08:04,678 - kars_db - INFO - 🔍 검색 시작: 'EQC 전기차 관련 모든 자료' (limit: 5)
2025-09-12 18:08:04,721 - weaviate_db - INFO - 🔍 검색 완료: 5개 결과 (쿼리: 'EQC 전기차 관련 모든 자료'
2025-09-12 18:08:04,722 - kars_db - INFO - ✅ 검색 완료: 5개 결과 반환
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

테스트 케이스 4: MBUX 시스템 관련 기술 자료
------------------------------------------------------------
2025-09-12 18:08:04,722 - mcp_tools - INFO - 🔍 필터 추출 시작: 'MBUX 시스템 관련 기술 자료'
2025-09-12 18:08:06,242 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:08:06,243 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:08:06,244 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:08:06,324 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:08:06,324 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:08:06,395 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:08:06,396 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:08:06,468 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:08:06,469 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:08:06,542 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:08:06,542 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:08:06,543 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
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
2025-09-12 18:08:06,543 - mcp_tools - INFO - 🔍 단순 RAG 검색 실행: 'MBUX 시스템 관련 기술 자료' (limit: 5)
2025-09-12 18:08:06,543 - kars_db - INFO - 🔍 검색 시작: 'MBUX 시스템 관련 기술 자료' (limit: 5)
2025-09-12 18:08:06,607 - weaviate_db - INFO - 🔍 검색 완료: 5개 결과 (쿼리: 'MBUX 시스템 관련 기술 자료'
2025-09-12 18:08:06,607 - kars_db - INFO - ✅ 검색 완료: 5개 결과 반환
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

테스트 케이스 5: 4MATIC 사륜구동 시스템 관련 자료
------------------------------------------------------------
2025-09-12 18:08:06,607 - mcp_tools - INFO - 🔍 필터 추출 시작: '4MATIC 사륜구동 시스템 관련 자료'
2025-09-12 18:08:08,127 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:08:08,129 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:08:08,129 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:08:08,210 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:08:08,210 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:08:08,290 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:08:08,290 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:08:08,360 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:08:08,360 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:08:08,429 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:08:08,429 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:08:08,430 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
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
2025-09-12 18:08:08,430 - mcp_tools - INFO - 🔍 단순 RAG 검색 실행: '4MATIC 사륜구동 시스템 관련 자료' (limit: 5)
2025-09-12 18:08:08,430 - kars_db - INFO - 🔍 검색 시작: '4MATIC 사륜구동 시스템 관련 자료' (limit: 5)
2025-09-12 18:08:08,480 - weaviate_db - INFO - 🔍 검색 완료: 5개 결과 (쿼리: '4MATIC 사륜구동 시스템 관련 자료'
2025-09-12 18:08:08,480 - kars_db - INFO - ✅ 검색 완료: 5개 결과 반환
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

테스트 케이스 6: SOCAR와의 카셰어링 협력 관련 자료
------------------------------------------------------------
2025-09-12 18:08:08,480 - mcp_tools - INFO - 🔍 필터 추출 시작: 'SOCAR와의 카셰어링 협력 관련 자료'
2025-09-12 18:08:10,001 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:08:10,002 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:08:10,002 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:08:10,071 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:08:10,072 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:08:10,151 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:08:10,151 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:08:10,223 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:08:10,223 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:08:10,281 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:08:10,281 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:08:10,282 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
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
2025-09-12 18:08:10,282 - mcp_tools - INFO - 🔍 단순 RAG 검색 실행: 'SOCAR와의 카셰어링 협력 관련 자료' (limit: 5)
2025-09-12 18:08:10,282 - kars_db - INFO - 🔍 검색 시작: 'SOCAR와의 카셰어링 협력 관련 자료' (limit: 5)
2025-09-12 18:08:10,326 - weaviate_db - INFO - 🔍 검색 완료: 5개 결과 (쿼리: 'SOCAR와의 카셰어링 협력 관련 자료'
2025-09-12 18:08:10,326 - kars_db - INFO - ✅ 검색 완료: 5개 결과 반환
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

테스트 케이스 7: SOCAR, 몽클레르, 버질 아블로 협력 관련 모든 자료
------------------------------------------------------------
2025-09-12 18:08:10,327 - mcp_tools - INFO - 🔍 필터 추출 시작: 'SOCAR, 몽클레르, 버질 아블로 협력 관련 모든 자료'
2025-09-12 18:08:11,851 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:08:11,853 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:08:11,853 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:08:11,932 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:08:11,933 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:08:11,995 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:08:11,995 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:08:12,074 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:08:12,075 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:08:12,141 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:08:12,141 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:08:12,141 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
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
2025-09-12 18:08:12,142 - mcp_tools - INFO - 🔍 단순 RAG 검색 실행: 'SOCAR, 몽클레르, 버질 아블로 협력 관련 모든 자료' (limit: 5)
2025-09-12 18:08:12,142 - kars_db - INFO - 🔍 검색 시작: 'SOCAR, 몽클레르, 버질 아블로 협력 관련 모든 자료' (limit: 5)
2025-09-12 18:08:12,185 - weaviate_db - INFO - 🔍 검색 완료: 5개 결과 (쿼리: 'SOCAR, 몽클레르, 버질 아블로 협력 관련 모든 자료'
2025-09-12 18:08:12,185 - kars_db - INFO - ✅ 검색 완료: 5개 결과 반환
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

테스트 케이스 8: 전기차 관련 기술 중 MBUX, 4MATIC, 하이브리드 언급된 문서들
------------------------------------------------------------
2025-09-12 18:08:12,188 - mcp_tools - INFO - 🔍 필터 추출 시작: '전기차 관련 기술 중 MBUX, 4MATIC, 하이브리드 언급된 문서들'
2025-09-12 18:08:13,713 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:08:13,714 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:08:13,714 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:08:13,795 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:08:13,795 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:08:13,875 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:08:13,876 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:08:13,952 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:08:13,952 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:08:14,033 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:08:14,033 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:08:14,033 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
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
2025-09-12 18:08:14,033 - mcp_tools - INFO - 🔍 단순 RAG 검색 실행: '전기차 관련 기술 중 MBUX, 4MATIC, 하이브리드 언급된 문서들' (limit: 5)
2025-09-12 18:08:14,033 - kars_db - INFO - 🔍 검색 시작: '전기차 관련 기술 중 MBUX, 4MATIC, 하이브리드 언급된 문서들' (limit: 5)
2025-09-12 18:08:14,079 - weaviate_db - INFO - 🔍 검색 완료: 5개 결과 (쿼리: '전기차 관련 기술 중 MBUX, 4MATIC, 하이브리드 언급된 문서들'
2025-09-12 18:08:14,079 - kars_db - INFO - ✅ 검색 완료: 5개 결과 반환
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

테스트 케이스 9: SOCAR와의 카셰어링 서비스 협약 체결 과정
------------------------------------------------------------
2025-09-12 18:08:14,079 - mcp_tools - INFO - 🔍 필터 추출 시작: 'SOCAR와의 카셰어링 서비스 협약 체결 과정'
2025-09-12 18:08:15,602 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:08:15,603 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:08:15,603 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:08:15,704 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:08:15,705 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:08:15,781 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:08:15,782 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:08:15,861 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:08:15,862 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:08:15,926 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:08:15,926 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:08:15,926 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
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
2025-09-12 18:08:15,926 - mcp_tools - INFO - 🔍 단순 RAG 검색 실행: 'SOCAR와의 카셰어링 서비스 협약 체결 과정' (limit: 5)
2025-09-12 18:08:15,926 - kars_db - INFO - 🔍 검색 시작: 'SOCAR와의 카셰어링 서비스 협약 체결 과정' (limit: 5)
2025-09-12 18:08:15,965 - weaviate_db - INFO - 🔍 검색 완료: 5개 결과 (쿼리: 'SOCAR와의 카셰어링 서비스 협약 체결 과정'
2025-09-12 18:08:15,966 - kars_db - INFO - ✅ 검색 완료: 5개 결과 반환
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

테스트 케이스 10: EQC 모델의 국내 시장 출시 및 홍보 활동
------------------------------------------------------------
2025-09-12 18:08:15,966 - mcp_tools - INFO - 🔍 필터 추출 시작: 'EQC 모델의 국내 시장 출시 및 홍보 활동'
2025-09-12 18:08:17,490 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:08:17,491 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:08:17,491 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:08:17,556 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:08:17,557 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:08:17,634 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:08:17,634 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:08:17,712 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:08:17,713 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:08:17,794 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:08:17,794 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:08:17,794 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
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
2025-09-12 18:08:17,794 - mcp_tools - INFO - 🔍 단순 RAG 검색 실행: 'EQC 모델의 국내 시장 출시 및 홍보 활동' (limit: 5)
2025-09-12 18:08:17,794 - kars_db - INFO - 🔍 검색 시작: 'EQC 모델의 국내 시장 출시 및 홍보 활동' (limit: 5)
2025-09-12 18:08:17,827 - weaviate_db - INFO - 🔍 검색 완료: 5개 결과 (쿼리: 'EQC 모델의 국내 시장 출시 및 홍보 활동'
2025-09-12 18:08:17,827 - kars_db - INFO - ✅ 검색 완료: 5개 결과 반환
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

테스트 케이스 11: 메르세데스-벤츠의 전동화 전략 및 기술 로드맵
------------------------------------------------------------
2025-09-12 18:08:17,827 - mcp_tools - INFO - 🔍 필터 추출 시작: '메르세데스-벤츠의 전동화 전략 및 기술 로드맵'
2025-09-12 18:08:19,351 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:08:19,352 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:08:19,352 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:08:19,431 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:08:19,431 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:08:19,516 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:08:19,516 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:08:19,589 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:08:19,590 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:08:19,659 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:08:19,659 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:08:19,659 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
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
2025-09-12 18:08:19,659 - mcp_tools - INFO - 🔍 단순 RAG 검색 실행: '메르세데스-벤츠의 전동화 전략 및 기술 로드맵' (limit: 5)
2025-09-12 18:08:19,659 - kars_db - INFO - 🔍 검색 시작: '메르세데스-벤츠의 전동화 전략 및 기술 로드맵' (limit: 5)
2025-09-12 18:08:19,696 - weaviate_db - INFO - 🔍 검색 완료: 5개 결과 (쿼리: '메르세데스-벤츠의 전동화 전략 및 기술 로드맵'
2025-09-12 18:08:19,696 - kars_db - INFO - ✅ 검색 완료: 5개 결과 반환
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
/raid1/workspace/kars-agent/weaviate-mcp/tmp_sungwon_chae/test_extract_value_tool_modified.py:336: ResourceWarning: unclosed <socket.socket fd=9, family=2, type=1, proto=6, laddr=('10.10.150.195', 40582), raddr=('10.10.150.195', 8080)>
  await test_extract_filter()
ResourceWarning: Enable tracemalloc to get the object allocation traceback

====================================================================================================

🔍 필터 기반 검색 테스트 시작 (MBG 실제 데이터 기반)

2025-09-12 18:08:19,733 - mcp_tools - INFO - Weaviate MCP 도구 초기화 완료
👤 1단계: 데이터베이스의 unique한 이름 값들 조회
------------------------------------------------------------
2025-09-12 18:08:19,733 - kars_db - INFO - 🚀 RAG 벡터 데이터베이스 초기화 시작
2025-09-12 18:08:19,733 - simple_manager - INFO - Weaviate URL: http://10.10.150.195:8080
2025-09-12 18:08:19,734 - simple_manager - INFO - OpenAI Base URL: http://10.10.190.1:8125
2025-09-12 18:08:19,734 - kars_db - INFO - ✅ VectorDB 매니저 초기화 완료
2025-09-12 18:08:19,761 - httpx - INFO - HTTP Request: GET http://10.10.190.1:8125/v1/models "HTTP/1.1 200 OK"
2025-09-12 18:08:19,761 - weaviate_db - INFO - ✅ vLLM 서버에서 모델명 가져옴: /data/models_ckpt/bge-m3
2025-09-12 18:08:19,773 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8125/v1/embeddings "HTTP/1.1 200 OK"
2025-09-12 18:08:19,773 - weaviate_db - INFO - ✅ 샘플 임베딩 생성 성공 (차원: 1024)
2025-09-12 18:08:19,802 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/.well-known/openid-configuration "HTTP/1.1 404 Not Found"
2025-09-12 18:08:19,826 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/meta "HTTP/1.1 200 OK"
2025-09-12 18:08:21,877 - weaviate_db - INFO - ✅ Weaviate 클라이언트 연결 성공: http://10.10.150.195:8080
2025-09-12 18:08:21,877 - weaviate_db - INFO - 📡 OpenAI Base URL (Python용): http://10.10.190.1:8125/v1
2025-09-12 18:08:21,877 - weaviate_db - INFO - 📡 OpenAI Base URL (Weaviate용): http://10.10.190.1:8125
2025-09-12 18:08:21,877 - weaviate_db - INFO - 🔧 동적 모델명: /data/models_ckpt/bge-m3
2025-09-12 18:08:21,877 - simple_manager - INFO - DB 연결 초기화 완료
2025-09-12 18:08:21,881 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema "HTTP/1.1 200 OK"
2025-09-12 18:08:21,885 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema/DocumentChunk "HTTP/1.1 200 OK"
2025-09-12 18:08:21,889 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema/EnronDocument "HTTP/1.1 200 OK"
2025-09-12 18:08:21,890 - weaviate_db - INFO - 스키마 조회 완료: 2개 클래스
2025-09-12 18:08:21,891 - simple_manager - WARNING - 클래스 매핑 파일이 없습니다. 기본 규칙을 사용합니다.
2025-09-12 18:08:21,891 - simple_manager - INFO - 기존 클래스 등록: chunk_db -> DocumentChunk
2025-09-12 18:08:21,891 - simple_manager - INFO - 기존 클래스 등록: enron_db -> EnronDocument
2025-09-12 18:08:21,891 - simple_manager - INFO - 총 2개 DB에 클래스 등록 완료
2025-09-12 18:08:21,891 - simple_manager - INFO -   chunk_db: ['DocumentChunk']
2025-09-12 18:08:21,891 - simple_manager - INFO -   enron_db: ['EnronDocument']
2025-09-12 18:08:21,894 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema "HTTP/1.1 200 OK"
2025-09-12 18:08:21,898 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema/DocumentChunk "HTTP/1.1 200 OK"
2025-09-12 18:08:21,902 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema/EnronDocument "HTTP/1.1 200 OK"
2025-09-12 18:08:21,903 - weaviate_db - INFO - 스키마 조회 완료: 2개 클래스
2025-09-12 18:08:21,903 - kars_db - INFO - 📊 사용 가능한 클래스들: ['DocumentChunk', 'EnronDocument']
2025-09-12 18:08:21,903 - kars_db - INFO - ✅ 사용할 클래스명: DocumentChunk
2025-09-12 18:08:21,903 - mcp_tools - INFO - ✅ RAG 데이터베이스 초기화 성공: kars_test
2025-09-12 18:08:21,903 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:08:21,904 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:08:21,981 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:08:21,982 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:08:22,054 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:08:22,054 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:08:22,123 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:08:22,123 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:08:22,191 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:08:22,191 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
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

 2단계: 필터 기반 검색 테스트 (MBG 실제 데이터 기반)
------------------------------------------------------------

🧪 테스트 케이스 1: Jeong, Yeeun (191) on behalf of korea_com (191-NPM)가 발신한 메시지를 모두 찾아줘
--------------------------------------------------
2025-09-12 18:08:22,192 - mcp_tools - INFO - 🔍 필터 추출 시작: 'Jeong, Yeeun (191) on behalf of korea_com (191-NPM)가 발신한 메시지를 모두 찾아줘'
2025-09-12 18:08:24,291 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:08:24,293 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:08:24,293 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:08:24,372 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:08:24,372 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:08:24,448 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:08:24,448 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:08:24,525 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:08:24,525 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:08:24,589 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:08:24,589 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:08:24,589 - mcp_tools - INFO - ✅ from_email 필드 정확한 매칭 발견: 'Jeong, Yeeun (191) on behalf of korea_com (191-NPM)'
2025-09-12 18:08:24,589 - mcp_tools - INFO - ✅ 필터 추출 완료: filter 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email='Jeong, Yeeun (191) on behalf of korea_com (191-NPM)' to_email=None cc=None bcc=None last_author=None extension=None
❌ 오류 발생: 'success'


🧪 테스트 케이스 2: Park, Sep (191) on behalf of korea_com (191-NPM)가 발신한 메시지를 모두 찾아줘
--------------------------------------------------
2025-09-12 18:08:24,589 - mcp_tools - INFO - 🔍 필터 추출 시작: 'Park, Sep (191) on behalf of korea_com (191-NPM)가 발신한 메시지를 모두 찾아줘'
2025-09-12 18:08:26,610 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:08:26,611 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:08:26,611 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:08:26,692 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:08:26,692 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:08:26,785 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:08:26,785 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:08:26,860 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:08:26,860 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:08:26,928 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:08:26,928 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:08:26,928 - mcp_tools - INFO - ✅ from_email 필드 정확한 매칭 발견: 'Park, Sep (191) on behalf of korea_com (191-NPM)'
2025-09-12 18:08:26,928 - mcp_tools - INFO - ✅ 필터 추출 완료: filter 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email='Park, Sep (191) on behalf of korea_com (191-NPM)' to_email=None cc=None bcc=None last_author=None extension=None
❌ 오류 발생: 'success'


🧪 테스트 케이스 3: dw_191-MBK_all에게 발송된 메시지를 모두 찾아줘
--------------------------------------------------
2025-09-12 18:08:26,928 - mcp_tools - INFO - 🔍 필터 추출 시작: 'dw_191-MBK_all에게 발송된 메시지를 모두 찾아줘'
2025-09-12 18:08:28,643 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:08:28,645 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:08:28,645 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:08:28,719 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:08:28,719 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:08:28,781 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:08:28,782 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:08:28,846 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:08:28,846 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:08:28,917 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:08:28,917 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:08:30,232 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:08:30,233 - mcp_tools - INFO - ⚠️ custodian 필드 유사도 부족: 'dw_191-MBK_all' (최고 유사도: 0.00)
2025-09-12 18:08:30,233 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian='dw_191-MBK_all' ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
❌ 오류 발생: 'success'


🧪 테스트 케이스 4: 세진 김이 보관한 문서들을 모두 찾아줘
--------------------------------------------------
2025-09-12 18:08:30,234 - mcp_tools - INFO - 🔍 필터 추출 시작: '세진 김이 보관한 문서들을 모두 찾아줘'
2025-09-12 18:08:31,830 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:08:31,831 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:08:31,831 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:08:31,913 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:08:31,913 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:08:31,989 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:08:31,989 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:08:32,062 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:08:32,063 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:08:32,133 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:08:32,133 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:08:32,133 - mcp_tools - INFO - ✅ custodian 필드 정확한 매칭 발견: '세진 김'
2025-09-12 18:08:32,133 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian='세진 김' ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
❌ 오류 발생: 'success'


🧪 테스트 케이스 5: Song, Jieun (191)가 최종 작성한 문서들을 모두 찾아줘
--------------------------------------------------
2025-09-12 18:08:32,134 - mcp_tools - INFO - 🔍 필터 추출 시작: 'Song, Jieun (191)가 최종 작성한 문서들을 모두 찾아줘'
2025-09-12 18:08:33,873 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:08:33,874 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:08:33,875 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:08:33,956 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:08:33,956 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:08:34,035 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:08:34,036 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:08:34,118 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:08:34,118 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:08:34,199 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:08:34,200 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:08:34,200 - mcp_tools - INFO - ✅ last_author 필드 정확한 매칭 발견: 'Song, Jieun (191)'
2025-09-12 18:08:34,200 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author='Song, Jieun (191)' extension=None
❌ 오류 발생: 'success'


🧪 테스트 케이스 6: Ju, Hyeyeon (191-Extern-MBK)가 최종 작성한 문서들을 모두 찾아줘
--------------------------------------------------
2025-09-12 18:08:34,200 - mcp_tools - INFO - 🔍 필터 추출 시작: 'Ju, Hyeyeon (191-Extern-MBK)가 최종 작성한 문서들을 모두 찾아줘'
2025-09-12 18:08:35,207 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:08:35,208 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:08:35,208 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:08:35,288 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:08:35,288 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:08:35,375 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:08:35,376 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:08:35,452 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:08:35,453 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:08:35,535 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:08:35,535 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:08:37,048 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:08:37,049 - mcp_tools - INFO - ⚠️ custodian 필드 유사도 부족: 'Ju, Hyeyeon (191-Extern-MBK)' (최고 유사도: 0.00)
2025-09-12 18:08:37,049 - mcp_tools - INFO - ✅ last_author 필드 정확한 매칭 발견: 'Ju, Hyeyeon (191-Extern-MBK)'
2025-09-12 18:08:37,050 - mcp_tools - INFO - ✅ 필터 추출 완료: filter 검색, 필터: custodian='Ju, Hyeyeon (191-Extern-MBK)' ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author='Ju, Hyeyeon (191-Extern-MBK)' extension=None
❌ 오류 발생: 'success'


🧪 테스트 케이스 7: Kim, Ji-Hyun (191)가 최종 작성한 문서들을 모두 찾아줘
--------------------------------------------------
2025-09-12 18:08:37,050 - mcp_tools - INFO - 🔍 필터 추출 시작: 'Kim, Ji-Hyun (191)가 최종 작성한 문서들을 모두 찾아줘'
2025-09-12 18:08:38,807 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:08:38,808 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:08:38,809 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:08:38,885 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:08:38,885 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:08:38,963 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:08:38,963 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:08:39,038 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:08:39,038 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:08:39,115 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:08:39,116 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:08:39,116 - mcp_tools - INFO - ✅ last_author 필드 정확한 매칭 발견: 'Kim, Ji-Hyun (191)'
2025-09-12 18:08:39,116 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author='Kim, Ji-Hyun (191)' extension=None
❌ 오류 발생: 'success'


🧪 테스트 케이스 8: msg 확장자 파일들을 모두 찾아줘
--------------------------------------------------
2025-09-12 18:08:39,116 - mcp_tools - INFO - 🔍 필터 추출 시작: 'msg 확장자 파일들을 모두 찾아줘'
2025-09-12 18:08:40,661 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:08:40,663 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:08:40,663 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:08:40,738 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:08:40,738 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:08:40,815 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:08:40,816 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:08:40,889 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:08:40,890 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:08:40,970 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:08:40,970 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:08:40,970 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension='msg'
❌ 오류 발생: 'success'


🧪 테스트 케이스 9: pdf 확장자 파일들을 모두 찾아줘
--------------------------------------------------
2025-09-12 18:08:40,970 - mcp_tools - INFO - 🔍 필터 추출 시작: 'pdf 확장자 파일들을 모두 찾아줘'
2025-09-12 18:08:42,515 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:08:42,517 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:08:42,517 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:08:42,595 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:08:42,595 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:08:42,670 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:08:42,671 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:08:42,752 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:08:42,753 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:08:42,830 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:08:42,830 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:08:42,830 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension='pdf'
❌ 오류 발생: 'success'


🧪 테스트 케이스 10: csv 확장자 파일들을 모두 찾아줘
--------------------------------------------------
2025-09-12 18:08:42,830 - mcp_tools - INFO - 🔍 필터 추출 시작: 'csv 확장자 파일들을 모두 찾아줘'
2025-09-12 18:08:44,503 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:08:44,504 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:08:44,504 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:08:44,581 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:08:44,582 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:08:44,659 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:08:44,659 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:08:44,721 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:08:44,721 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:08:44,806 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:08:44,806 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:08:44,806 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension='.csv'
❌ 오류 발생: 'success'


🧪 테스트 케이스 11: 세진 김이 보관한 msg 파일들을 모두 찾아줘
--------------------------------------------------
2025-09-12 18:08:44,806 - mcp_tools - INFO - 🔍 필터 추출 시작: '세진 김이 보관한 msg 파일들을 모두 찾아줘'
2025-09-12 18:08:45,336 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:08:45,338 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:08:45,338 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:08:45,417 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:08:45,418 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:08:45,491 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:08:45,491 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:08:45,558 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:08:45,559 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:08:45,619 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:08:45,619 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:08:45,620 - mcp_tools - INFO - ✅ custodian 필드 정확한 매칭 발견: '세진 김'
2025-09-12 18:08:45,620 - mcp_tools - INFO - ✅ 필터 추출 완료: filter 검색, 필터: custodian='세진 김' ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension='.msg'
❌ 오류 발생: 'success'


🧪 테스트 케이스 12: Song, Jieun (191)가 최종 작성한 pdf 파일들을 모두 찾아줘
--------------------------------------------------
2025-09-12 18:08:45,620 - mcp_tools - INFO - 🔍 필터 추출 시작: 'Song, Jieun (191)가 최종 작성한 pdf 파일들을 모두 찾아줘'
2025-09-12 18:08:47,517 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:08:47,519 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:08:47,519 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:08:47,590 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:08:47,591 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:08:47,661 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:08:47,662 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:08:47,737 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:08:47,737 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:08:47,802 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:08:47,802 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:08:47,802 - mcp_tools - INFO - ✅ last_author 필드 정확한 매칭 발견: 'Song, Jieun (191)'
2025-09-12 18:08:47,802 - mcp_tools - INFO - ✅ 필터 추출 완료: filter 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author='Song, Jieun (191)' extension='.pdf'
❌ 오류 발생: 'success'

✅ 필터 기반 검색 테스트 완료!

🎉 모든 테스트 완료!
sys:1: ResourceWarning: unclosed <socket.socket fd=10, family=2, type=1, proto=6, laddr=('10.10.150.195', 48338), raddr=('10.10.150.195', 8080)>
ResourceWarning: Enable tracemalloc to get the object allocation traceback
(.venv) min.choi10@wss-195:/raid1/workspace/kars-agent/weaviate-mcp/tmp_sungwon_chae$ 
