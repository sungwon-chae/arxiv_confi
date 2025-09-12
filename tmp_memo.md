(.venv) min.choi10@wss-195:/raid1/workspace/kars-agent/weaviate-mcp/tmp_sungwon_chae$ python test_extract_value_tool_modified.py 
🚀 Weaviate MCP 도구 테스트 시작

2025-09-12 18:38:53,827 - mcp_tools - INFO - Weaviate MCP 도구 초기화 완료
2025-09-12 18:38:54,241 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
Test Query Response:  ChatCompletion(id='chatcmpl-1e2a45f50f514c93a4a400413c1e06cf', choices=[Choice(finish_reason='length', index=0, logprobs=None, message=ChatCompletionMessage(content='<think>\nOkay, the user said "hi!"', refusal=None, role='assistant', annotations=None, audio=None, function_call=None, tool_calls=[], reasoning_content=None), stop_reason=None)], created=1757669939, model='/data/models_ckpt/Qwen3-32B', object='chat.completion', service_tier=None, system_fingerprint=None, usage=CompletionUsage(completion_tokens=10, prompt_tokens=10, total_tokens=20, completion_tokens_details=None, prompt_tokens_details=None), prompt_logprobs=None)
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

테스트 케이스 1: Jeong, Yeeun (191) on behalf of korea_com (191-NPM)가 발신한 메시지를 모두 찾아줘
------------------------------------------------------------
2025-09-12 18:38:54,259 - mcp_tools - INFO - 🔍 필터 추출 시작: 'Jeong, Yeeun (191) on behalf of korea_com (191-NPM)가 발신한 메시지를 모두 찾아줘'
2025-09-12 18:38:56,349 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:38:56,350 - kars_db - INFO - 🚀 RAG 벡터 데이터베이스 초기화 시작
2025-09-12 18:38:56,351 - simple_manager - INFO - Weaviate URL: http://10.10.150.195:8080
2025-09-12 18:38:56,351 - simple_manager - INFO - OpenAI Base URL: http://10.10.190.1:8125
2025-09-12 18:38:56,351 - kars_db - INFO - ✅ VectorDB 매니저 초기화 완료
2025-09-12 18:38:56,396 - httpx - INFO - HTTP Request: GET http://10.10.190.1:8125/v1/models "HTTP/1.1 200 OK"
2025-09-12 18:38:56,397 - weaviate_db - INFO - ✅ vLLM 서버에서 모델명 가져옴: /data/models_ckpt/bge-m3
2025-09-12 18:38:56,410 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8125/v1/embeddings "HTTP/1.1 200 OK"
2025-09-12 18:38:56,414 - weaviate_db - INFO - ✅ 샘플 임베딩 생성 성공 (차원: 1024)
2025-09-12 18:38:56,455 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/.well-known/openid-configuration "HTTP/1.1 404 Not Found"
2025-09-12 18:38:56,481 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/meta "HTTP/1.1 200 OK"
2025-09-12 18:38:58,516 - weaviate_db - INFO - ✅ Weaviate 클라이언트 연결 성공: http://10.10.150.195:8080
2025-09-12 18:38:58,516 - weaviate_db - INFO - 📡 OpenAI Base URL (Python용): http://10.10.190.1:8125/v1
2025-09-12 18:38:58,516 - weaviate_db - INFO - 📡 OpenAI Base URL (Weaviate용): http://10.10.190.1:8125
2025-09-12 18:38:58,516 - weaviate_db - INFO - 🔧 동적 모델명: /data/models_ckpt/bge-m3
2025-09-12 18:38:58,516 - simple_manager - INFO - DB 연결 초기화 완료
2025-09-12 18:38:58,520 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema "HTTP/1.1 200 OK"
2025-09-12 18:38:58,525 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema/DocumentChunk "HTTP/1.1 200 OK"
2025-09-12 18:38:58,532 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema/EnronDocument "HTTP/1.1 200 OK"
2025-09-12 18:38:58,533 - weaviate_db - INFO - 스키마 조회 완료: 2개 클래스
2025-09-12 18:38:58,533 - simple_manager - WARNING - 클래스 매핑 파일이 없습니다. 기본 규칙을 사용합니다.
2025-09-12 18:38:58,533 - simple_manager - INFO - 기존 클래스 등록: chunk_db -> DocumentChunk
2025-09-12 18:38:58,534 - simple_manager - INFO - 기존 클래스 등록: enron_db -> EnronDocument
2025-09-12 18:38:58,534 - simple_manager - INFO - 총 2개 DB에 클래스 등록 완료
2025-09-12 18:38:58,534 - simple_manager - INFO -   chunk_db: ['DocumentChunk']
2025-09-12 18:38:58,534 - simple_manager - INFO -   enron_db: ['EnronDocument']
2025-09-12 18:38:58,537 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema "HTTP/1.1 200 OK"
2025-09-12 18:38:58,540 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema/DocumentChunk "HTTP/1.1 200 OK"
2025-09-12 18:38:58,543 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema/EnronDocument "HTTP/1.1 200 OK"
2025-09-12 18:38:58,544 - weaviate_db - INFO - 스키마 조회 완료: 2개 클래스
2025-09-12 18:38:58,544 - kars_db - INFO - 📊 사용 가능한 클래스들: ['DocumentChunk', 'EnronDocument']
2025-09-12 18:38:58,545 - kars_db - INFO - ✅ 사용할 클래스명: DocumentChunk
2025-09-12 18:38:58,545 - mcp_tools - INFO - ✅ RAG 데이터베이스 초기화 성공: kars_test
2025-09-12 18:38:58,545 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:38:58,545 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:38:58,626 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:38:58,626 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:38:58,700 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:38:58,700 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:38:58,778 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:38:58,779 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:38:58,848 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:38:58,848 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:38:58,848 - mcp_tools - INFO - ✅ from_email 필드 정확한 매칭 발견: 'Jeong, Yeeun (191) on behalf of korea_com (191-NPM)'
2025-09-12 18:38:58,848 - mcp_tools - INFO - ✅ 필터 추출 완료: filter 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email='Jeong, Yeeun (191) on behalf of korea_com (191-NPM)' to_email=None cc=None bcc=None last_author=None extension=None
🔍 DEBUG: result 타입: <class 'dict'>
🔍 DEBUG: result 값: {'filters': {'custodian': None, 'ori_file_name': None, 's_created_date': None, 'sent_date': None, 'from_email': 'Jeong, Yeeun (191) on behalf of korea_com (191-NPM)', 'to_email': None, 'cc': None, 'bcc': None, 'last_author': None, 'extension': None}, 'search_type': 'filter', 'reasoning': "질의에서 구체적인 식별자 'from_email: Jeong, Yeeun (191) on behalf of korea_com (191-NPM)'를 찾았습니다. 조건 필터링을 사용합니다.", 'query': 'Jeong, Yeeun (191) on behalf of korea_com (191-NPM)가 발신한 메시지를 모두 찾아줘'}
📊 추출된 필터:
  - from_email: Jeong, Yeeun (191) on behalf of korea_com (191-NPM)
🔍 검색 방식: filter
💭 판단 근거: 질의에서 구체적인 식별자 'from_email: Jeong, Yeeun (191) on behalf of korea_com (191-NPM)'를 찾았습니다. 조건 필터링을 사용합니다.
  📭 검색할 필터가 없어 단순 RAG 검색을 수행합니다.

================================================================================


테스트 케이스 2: Park, Sep (191) on behalf of korea_com (191-NPM)가 발신한 메시지를 모두 찾아줘
------------------------------------------------------------
2025-09-12 18:38:58,849 - mcp_tools - INFO - 🔍 필터 추출 시작: 'Park, Sep (191) on behalf of korea_com (191-NPM)가 발신한 메시지를 모두 찾아줘'
2025-09-12 18:39:00,847 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:39:00,848 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:39:00,848 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:39:00,925 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:39:00,925 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:39:00,988 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:39:00,988 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:39:01,068 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:39:01,069 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:39:01,141 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:39:01,141 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:39:01,141 - mcp_tools - INFO - ✅ from_email 필드 정확한 매칭 발견: 'Park, Sep (191) on behalf of korea_com (191-NPM)'
2025-09-12 18:39:01,141 - mcp_tools - INFO - ✅ 필터 추출 완료: filter 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email='Park, Sep (191) on behalf of korea_com (191-NPM)' to_email=None cc=None bcc=None last_author=None extension=None
🔍 DEBUG: result 타입: <class 'dict'>
🔍 DEBUG: result 값: {'filters': {'custodian': None, 'ori_file_name': None, 's_created_date': None, 'sent_date': None, 'from_email': 'Park, Sep (191) on behalf of korea_com (191-NPM)', 'to_email': None, 'cc': None, 'bcc': None, 'last_author': None, 'extension': None}, 'search_type': 'filter', 'reasoning': "질의에서 구체적인 식별자 'from_email: Park, Sep (191) on behalf of korea_com (191-NPM)'를 찾았습니다. 조건 필터링을 사용합니다.", 'query': 'Park, Sep (191) on behalf of korea_com (191-NPM)가 발신한 메시지를 모두 찾아줘'}
📊 추출된 필터:
  - from_email: Park, Sep (191) on behalf of korea_com (191-NPM)
🔍 검색 방식: filter
💭 판단 근거: 질의에서 구체적인 식별자 'from_email: Park, Sep (191) on behalf of korea_com (191-NPM)'를 찾았습니다. 조건 필터링을 사용합니다.
  📭 검색할 필터가 없어 단순 RAG 검색을 수행합니다.

================================================================================


테스트 케이스 3: 세진 김이 보관한 문서들을 모두 찾아줘
------------------------------------------------------------
2025-09-12 18:39:01,142 - mcp_tools - INFO - 🔍 필터 추출 시작: '세진 김이 보관한 문서들을 모두 찾아줘'
2025-09-12 18:39:02,718 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:39:02,719 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:39:02,719 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:39:02,800 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:39:02,800 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:39:02,867 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:39:02,867 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:39:02,931 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:39:02,932 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:39:03,000 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:39:03,001 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:39:03,001 - mcp_tools - INFO - ✅ custodian 필드 정확한 매칭 발견: '세진 김'
2025-09-12 18:39:03,001 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian='세진 김' ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
🔍 DEBUG: result 타입: <class 'dict'>
🔍 DEBUG: result 값: {'filters': {'custodian': '세진 김', 'ori_file_name': None, 's_created_date': None, 'sent_date': None, 'from_email': None, 'to_email': None, 'cc': None, 'bcc': None, 'last_author': None, 'extension': None}, 'search_type': 'similarity', 'reasoning': '질의에서 구체적인 필터 정보를 찾았지만 단일 필터이므로 유사도 기반 검색을 사용합니다.', 'query': '세진 김이 보관한 문서들을 모두 찾아줘'}
📊 추출된 필터:
  - custodian: 세진 김
🔍 검색 방식: similarity
💭 판단 근거: 질의에서 구체적인 필터 정보를 찾았지만 단일 필터이므로 유사도 기반 검색을 사용합니다.
  📭 검색할 필터가 없어 단순 RAG 검색을 수행합니다.

================================================================================


테스트 케이스 4: Song, Jieun (191)가 최종 작성한 문서들을 모두 찾아줘
------------------------------------------------------------
2025-09-12 18:39:03,001 - mcp_tools - INFO - 🔍 필터 추출 시작: 'Song, Jieun (191)가 최종 작성한 문서들을 모두 찾아줘'
2025-09-12 18:39:04,725 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:39:04,727 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:39:04,727 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:39:04,805 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:39:04,805 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:39:04,876 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:39:04,877 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:39:04,956 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:39:04,956 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:39:05,035 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:39:05,036 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:39:05,036 - mcp_tools - INFO - ✅ last_author 필드 정확한 매칭 발견: 'Song, Jieun (191)'
2025-09-12 18:39:05,036 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author='Song, Jieun (191)' extension=None
🔍 DEBUG: result 타입: <class 'dict'>
🔍 DEBUG: result 값: {'filters': {'custodian': None, 'ori_file_name': None, 's_created_date': None, 'sent_date': None, 'from_email': None, 'to_email': None, 'cc': None, 'bcc': None, 'last_author': 'Song, Jieun (191)', 'extension': None}, 'search_type': 'similarity', 'reasoning': '질의에서 구체적인 필터 정보를 찾았지만 단일 필터이므로 유사도 기반 검색을 사용합니다.', 'query': 'Song, Jieun (191)가 최종 작성한 문서들을 모두 찾아줘'}
📊 추출된 필터:
  - last_author: Song, Jieun (191)
🔍 검색 방식: similarity
💭 판단 근거: 질의에서 구체적인 필터 정보를 찾았지만 단일 필터이므로 유사도 기반 검색을 사용합니다.
  📭 검색할 필터가 없어 단순 RAG 검색을 수행합니다.

================================================================================


테스트 케이스 5: Ju, Hyeyeon (191-Extern-MBK)가 최종 작성한 문서들을 모두 찾아줘
------------------------------------------------------------
2025-09-12 18:39:05,036 - mcp_tools - INFO - 🔍 필터 추출 시작: 'Ju, Hyeyeon (191-Extern-MBK)가 최종 작성한 문서들을 모두 찾아줘'
2025-09-12 18:39:06,035 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:39:06,037 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:39:06,037 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:39:06,117 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:39:06,118 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:39:06,189 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:39:06,189 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:39:06,269 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:39:06,269 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:39:06,330 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:39:06,330 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:39:07,830 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:39:07,832 - mcp_tools - INFO - ⚠️ custodian 필드 유사도 부족: 'Ju, Hyeyeon (191-Extern-MBK)' (최고 유사도: 0.00)
2025-09-12 18:39:07,832 - mcp_tools - INFO - ✅ last_author 필드 정확한 매칭 발견: 'Ju, Hyeyeon (191-Extern-MBK)'
2025-09-12 18:39:07,832 - mcp_tools - INFO - ✅ 필터 추출 완료: filter 검색, 필터: custodian='Ju, Hyeyeon (191-Extern-MBK)' ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author='Ju, Hyeyeon (191-Extern-MBK)' extension=None
🔍 DEBUG: result 타입: <class 'dict'>
🔍 DEBUG: result 값: {'filters': {'custodian': 'Ju, Hyeyeon (191-Extern-MBK)', 'ori_file_name': None, 's_created_date': None, 'sent_date': None, 'from_email': None, 'to_email': None, 'cc': None, 'bcc': None, 'last_author': 'Ju, Hyeyeon (191-Extern-MBK)', 'extension': None}, 'search_type': 'filter', 'reasoning': "질의에서 2개의 구체적인 필터 정보를 찾았습니다: ['custodian', 'last_author']. 조건 필터링을 사용합니다.", 'query': 'Ju, Hyeyeon (191-Extern-MBK)가 최종 작성한 문서들을 모두 찾아줘'}
📊 추출된 필터:
  - custodian: Ju, Hyeyeon (191-Extern-MBK)
  - last_author: Ju, Hyeyeon (191-Extern-MBK)
🔍 검색 방식: filter
💭 판단 근거: 질의에서 2개의 구체적인 필터 정보를 찾았습니다: ['custodian', 'last_author']. 조건 필터링을 사용합니다.
  📭 검색할 필터가 없어 단순 RAG 검색을 수행합니다.

================================================================================


테스트 케이스 6: Kim, Ji-Hyun (191)가 최종 작성한 문서들을 모두 찾아줘
------------------------------------------------------------
2025-09-12 18:39:07,833 - mcp_tools - INFO - 🔍 필터 추출 시작: 'Kim, Ji-Hyun (191)가 최종 작성한 문서들을 모두 찾아줘'
2025-09-12 18:39:09,578 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:39:09,580 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:39:09,580 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:39:09,658 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:39:09,658 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:39:09,736 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:39:09,736 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:39:09,812 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:39:09,813 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:39:09,885 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:39:09,885 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:39:09,886 - mcp_tools - INFO - ✅ last_author 필드 정확한 매칭 발견: 'Kim, Ji-Hyun (191)'
2025-09-12 18:39:09,886 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author='Kim, Ji-Hyun (191)' extension=None
🔍 DEBUG: result 타입: <class 'dict'>
🔍 DEBUG: result 값: {'filters': {'custodian': None, 'ori_file_name': None, 's_created_date': None, 'sent_date': None, 'from_email': None, 'to_email': None, 'cc': None, 'bcc': None, 'last_author': 'Kim, Ji-Hyun (191)', 'extension': None}, 'search_type': 'similarity', 'reasoning': '질의에서 구체적인 필터 정보를 찾았지만 단일 필터이므로 유사도 기반 검색을 사용합니다.', 'query': 'Kim, Ji-Hyun (191)가 최종 작성한 문서들을 모두 찾아줘'}
📊 추출된 필터:
  - last_author: Kim, Ji-Hyun (191)
🔍 검색 방식: similarity
💭 판단 근거: 질의에서 구체적인 필터 정보를 찾았지만 단일 필터이므로 유사도 기반 검색을 사용합니다.
  📭 검색할 필터가 없어 단순 RAG 검색을 수행합니다.

================================================================================


테스트 케이스 7: Joo, Jaeyool (191)가 최종 작성한 문서들을 모두 찾아줘
------------------------------------------------------------
2025-09-12 18:39:09,886 - mcp_tools - INFO - 🔍 필터 추출 시작: 'Joo, Jaeyool (191)가 최종 작성한 문서들을 모두 찾아줘'
2025-09-12 18:39:11,640 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:39:11,642 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:39:11,642 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:39:11,718 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:39:11,719 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:39:11,798 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:39:11,799 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:39:11,865 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:39:11,866 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:39:11,940 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:39:11,940 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:39:11,940 - mcp_tools - INFO - ✅ last_author 필드 정확한 매칭 발견: 'Joo, Jaeyool (191)'
2025-09-12 18:39:11,940 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author='Joo, Jaeyool (191)' extension=None
🔍 DEBUG: result 타입: <class 'dict'>
🔍 DEBUG: result 값: {'filters': {'custodian': None, 'ori_file_name': None, 's_created_date': None, 'sent_date': None, 'from_email': None, 'to_email': None, 'cc': None, 'bcc': None, 'last_author': 'Joo, Jaeyool (191)', 'extension': None}, 'search_type': 'similarity', 'reasoning': '질의에서 구체적인 필터 정보를 찾았지만 단일 필터이므로 유사도 기반 검색을 사용합니다.', 'query': 'Joo, Jaeyool (191)가 최종 작성한 문서들을 모두 찾아줘'}
📊 추출된 필터:
  - last_author: Joo, Jaeyool (191)
🔍 검색 방식: similarity
💭 판단 근거: 질의에서 구체적인 필터 정보를 찾았지만 단일 필터이므로 유사도 기반 검색을 사용합니다.
  📭 검색할 필터가 없어 단순 RAG 검색을 수행합니다.

================================================================================


테스트 케이스 8: Park, Jaekyung (191)가 최종 작성한 문서들을 모두 찾아줘
------------------------------------------------------------
2025-09-12 18:39:11,940 - mcp_tools - INFO - 🔍 필터 추출 시작: 'Park, Jaekyung (191)가 최종 작성한 문서들을 모두 찾아줘'
2025-09-12 18:39:13,695 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:39:13,696 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:39:13,697 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:39:13,773 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:39:13,774 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:39:13,843 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:39:13,844 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:39:13,923 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:39:13,924 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:39:13,990 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:39:13,991 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:39:13,991 - mcp_tools - INFO - ✅ last_author 필드 정확한 매칭 발견: 'Park, Jaekyung (191)'
2025-09-12 18:39:13,991 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author='Park, Jaekyung (191)' extension=None
🔍 DEBUG: result 타입: <class 'dict'>
🔍 DEBUG: result 값: {'filters': {'custodian': None, 'ori_file_name': None, 's_created_date': None, 'sent_date': None, 'from_email': None, 'to_email': None, 'cc': None, 'bcc': None, 'last_author': 'Park, Jaekyung (191)', 'extension': None}, 'search_type': 'similarity', 'reasoning': '질의에서 구체적인 필터 정보를 찾았지만 단일 필터이므로 유사도 기반 검색을 사용합니다.', 'query': 'Park, Jaekyung (191)가 최종 작성한 문서들을 모두 찾아줘'}
📊 추출된 필터:
  - last_author: Park, Jaekyung (191)
🔍 검색 방식: similarity
💭 판단 근거: 질의에서 구체적인 필터 정보를 찾았지만 단일 필터이므로 유사도 기반 검색을 사용합니다.
  📭 검색할 필터가 없어 단순 RAG 검색을 수행합니다.

================================================================================


테스트 케이스 9: Shim, Ellen (191)가 최종 작성한 문서들을 모두 찾아줘
------------------------------------------------------------
2025-09-12 18:39:13,991 - mcp_tools - INFO - 🔍 필터 추출 시작: 'Shim, Ellen (191)가 최종 작성한 문서들을 모두 찾아줘'
2025-09-12 18:39:15,696 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:39:15,698 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:39:15,698 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:39:15,775 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:39:15,775 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:39:15,842 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:39:15,842 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:39:15,916 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:39:15,917 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:39:16,000 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:39:16,000 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:39:16,000 - mcp_tools - INFO - ✅ last_author 필드 정확한 매칭 발견: 'Shim, Ellen (191)'
2025-09-12 18:39:16,000 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author='Shim, Ellen (191)' extension=None
🔍 DEBUG: result 타입: <class 'dict'>
🔍 DEBUG: result 값: {'filters': {'custodian': None, 'ori_file_name': None, 's_created_date': None, 'sent_date': None, 'from_email': None, 'to_email': None, 'cc': None, 'bcc': None, 'last_author': 'Shim, Ellen (191)', 'extension': None}, 'search_type': 'similarity', 'reasoning': '질의에서 구체적인 필터 정보를 찾았지만 단일 필터이므로 유사도 기반 검색을 사용합니다.', 'query': 'Shim, Ellen (191)가 최종 작성한 문서들을 모두 찾아줘'}
📊 추출된 필터:
  - last_author: Shim, Ellen (191)
🔍 검색 방식: similarity
💭 판단 근거: 질의에서 구체적인 필터 정보를 찾았지만 단일 필터이므로 유사도 기반 검색을 사용합니다.
  📭 검색할 필터가 없어 단순 RAG 검색을 수행합니다.

================================================================================


테스트 케이스 10: msg 확장자 파일들을 모두 찾아줘
------------------------------------------------------------
2025-09-12 18:39:16,000 - mcp_tools - INFO - 🔍 필터 추출 시작: 'msg 확장자 파일들을 모두 찾아줘'
2025-09-12 18:39:17,533 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:39:17,535 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:39:17,535 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:39:17,616 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:39:17,617 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:39:17,700 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:39:17,700 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:39:17,779 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:39:17,779 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:39:17,858 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:39:17,859 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:39:17,859 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension='msg'
🔍 DEBUG: result 타입: <class 'dict'>
🔍 DEBUG: result 값: {'filters': {'custodian': None, 'ori_file_name': None, 's_created_date': None, 'sent_date': None, 'from_email': None, 'to_email': None, 'cc': None, 'bcc': None, 'last_author': None, 'extension': 'msg'}, 'search_type': 'similarity', 'reasoning': '질의에서 구체적인 필터 정보를 찾았지만 단일 필터이므로 유사도 기반 검색을 사용합니다.', 'query': 'msg 확장자 파일들을 모두 찾아줘'}
📊 추출된 필터:
  - extension: msg
🔍 검색 방식: similarity
💭 판단 근거: 질의에서 구체적인 필터 정보를 찾았지만 단일 필터이므로 유사도 기반 검색을 사용합니다.
  📭 검색할 필터가 없어 단순 RAG 검색을 수행합니다.

================================================================================


테스트 케이스 11: pdf 확장자 파일들을 모두 찾아줘
------------------------------------------------------------
2025-09-12 18:39:17,859 - mcp_tools - INFO - 🔍 필터 추출 시작: 'pdf 확장자 파일들을 모두 찾아줘'
2025-09-12 18:39:19,396 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:39:19,397 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:39:19,397 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:39:19,477 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:39:19,478 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:39:19,537 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:39:19,538 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:39:19,620 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:39:19,620 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:39:19,690 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:39:19,690 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:39:19,691 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension='pdf'
🔍 DEBUG: result 타입: <class 'dict'>
🔍 DEBUG: result 값: {'filters': {'custodian': None, 'ori_file_name': None, 's_created_date': None, 'sent_date': None, 'from_email': None, 'to_email': None, 'cc': None, 'bcc': None, 'last_author': None, 'extension': 'pdf'}, 'search_type': 'similarity', 'reasoning': '질의에서 구체적인 필터 정보를 찾았지만 단일 필터이므로 유사도 기반 검색을 사용합니다.', 'query': 'pdf 확장자 파일들을 모두 찾아줘'}
📊 추출된 필터:
  - extension: pdf
🔍 검색 방식: similarity
💭 판단 근거: 질의에서 구체적인 필터 정보를 찾았지만 단일 필터이므로 유사도 기반 검색을 사용합니다.
  📭 검색할 필터가 없어 단순 RAG 검색을 수행합니다.

================================================================================


테스트 케이스 12: csv 확장자 파일들을 모두 찾아줘
------------------------------------------------------------
2025-09-12 18:39:19,691 - mcp_tools - INFO - 🔍 필터 추출 시작: 'csv 확장자 파일들을 모두 찾아줘'
2025-09-12 18:39:21,224 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:39:21,226 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:39:21,226 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:39:21,307 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:39:21,307 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:39:21,383 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:39:21,384 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:39:21,450 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:39:21,451 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:39:21,519 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:39:21,520 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:39:21,520 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension='.csv'
🔍 DEBUG: result 타입: <class 'dict'>
🔍 DEBUG: result 값: {'filters': {'custodian': None, 'ori_file_name': None, 's_created_date': None, 'sent_date': None, 'from_email': None, 'to_email': None, 'cc': None, 'bcc': None, 'last_author': None, 'extension': '.csv'}, 'search_type': 'similarity', 'reasoning': '질의에서 구체적인 필터 정보를 찾았지만 단일 필터이므로 유사도 기반 검색을 사용합니다.', 'query': 'csv 확장자 파일들을 모두 찾아줘'}
📊 추출된 필터:
  - extension: .csv
🔍 검색 방식: similarity
💭 판단 근거: 질의에서 구체적인 필터 정보를 찾았지만 단일 필터이므로 유사도 기반 검색을 사용합니다.
  📭 검색할 필터가 없어 단순 RAG 검색을 수행합니다.

================================================================================


테스트 케이스 13: 세진 김이 보관한 msg 파일들을 모두 찾아줘
------------------------------------------------------------
2025-09-12 18:39:21,520 - mcp_tools - INFO - 🔍 필터 추출 시작: '세진 김이 보관한 msg 파일들을 모두 찾아줘'
2025-09-12 18:39:21,921 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:39:21,923 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:39:21,923 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:39:21,996 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:39:21,997 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:39:22,066 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:39:22,067 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:39:22,159 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:39:22,159 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:39:22,226 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:39:22,227 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:39:22,227 - mcp_tools - INFO - ✅ custodian 필드 정확한 매칭 발견: '세진 김'
2025-09-12 18:39:22,227 - mcp_tools - INFO - ✅ 필터 추출 완료: filter 검색, 필터: custodian='세진 김' ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension='.msg'
🔍 DEBUG: result 타입: <class 'dict'>
🔍 DEBUG: result 값: {'filters': {'custodian': '세진 김', 'ori_file_name': None, 's_created_date': None, 'sent_date': None, 'from_email': None, 'to_email': None, 'cc': None, 'bcc': None, 'last_author': None, 'extension': '.msg'}, 'search_type': 'filter', 'reasoning': "질의에서 2개의 구체적인 필터 정보를 찾았습니다: ['custodian', 'extension']. 조건 필터링을 사용합니다.", 'query': '세진 김이 보관한 msg 파일들을 모두 찾아줘'}
📊 추출된 필터:
  - custodian: 세진 김
  - extension: .msg
🔍 검색 방식: filter
💭 판단 근거: 질의에서 2개의 구체적인 필터 정보를 찾았습니다: ['custodian', 'extension']. 조건 필터링을 사용합니다.
  📭 검색할 필터가 없어 단순 RAG 검색을 수행합니다.

================================================================================


테스트 케이스 14: Song, Jieun (191)가 최종 작성한 pdf 파일들을 모두 찾아줘
------------------------------------------------------------
2025-09-12 18:39:22,227 - mcp_tools - INFO - 🔍 필터 추출 시작: 'Song, Jieun (191)가 최종 작성한 pdf 파일들을 모두 찾아줘'
2025-09-12 18:39:23,980 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:39:23,982 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:39:23,982 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:39:24,057 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:39:24,057 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:39:24,133 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:39:24,134 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:39:24,198 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:39:24,198 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:39:24,270 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:39:24,271 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:39:24,271 - mcp_tools - INFO - ✅ last_author 필드 정확한 매칭 발견: 'Song, Jieun (191)'
2025-09-12 18:39:24,271 - mcp_tools - INFO - ✅ 필터 추출 완료: filter 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author='Song, Jieun (191)' extension='.pdf'
🔍 DEBUG: result 타입: <class 'dict'>
🔍 DEBUG: result 값: {'filters': {'custodian': None, 'ori_file_name': None, 's_created_date': None, 'sent_date': None, 'from_email': None, 'to_email': None, 'cc': None, 'bcc': None, 'last_author': 'Song, Jieun (191)', 'extension': '.pdf'}, 'search_type': 'filter', 'reasoning': "질의에서 2개의 구체적인 필터 정보를 찾았습니다: ['last_author', 'extension']. 조건 필터링을 사용합니다.", 'query': 'Song, Jieun (191)가 최종 작성한 pdf 파일들을 모두 찾아줘'}
📊 추출된 필터:
  - last_author: Song, Jieun (191)
  - extension: .pdf
🔍 검색 방식: filter
💭 판단 근거: 질의에서 2개의 구체적인 필터 정보를 찾았습니다: ['last_author', 'extension']. 조건 필터링을 사용합니다.
  📭 검색할 필터가 없어 단순 RAG 검색을 수행합니다.

================================================================================


테스트 케이스 15: Ju, Hyeyeon (191-Extern-MBK)가 최종 작성한 msg 파일들을 모두 찾아줘
------------------------------------------------------------
2025-09-12 18:39:24,271 - mcp_tools - INFO - 🔍 필터 추출 시작: 'Ju, Hyeyeon (191-Extern-MBK)가 최종 작성한 msg 파일들을 모두 찾아줘'
2025-09-12 18:39:25,431 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:39:25,432 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:39:25,433 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:39:25,503 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:39:25,503 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:39:25,565 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:39:25,565 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:39:25,642 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:39:25,642 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:39:25,704 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:39:25,704 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:39:27,209 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:39:27,211 - mcp_tools - INFO - ⚠️ custodian 필드 유사도 부족: 'Ju, Hyeyeon (191-Extern-MBK)' (최고 유사도: 0.00)
2025-09-12 18:39:27,211 - mcp_tools - INFO - ✅ last_author 필드 정확한 매칭 발견: 'Ju, Hyeyeon (191-Extern-MBK)'
2025-09-12 18:39:27,211 - mcp_tools - INFO - ✅ 필터 추출 완료: filter 검색, 필터: custodian='Ju, Hyeyeon (191-Extern-MBK)' ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author='Ju, Hyeyeon (191-Extern-MBK)' extension='msg'
🔍 DEBUG: result 타입: <class 'dict'>
🔍 DEBUG: result 값: {'filters': {'custodian': 'Ju, Hyeyeon (191-Extern-MBK)', 'ori_file_name': None, 's_created_date': None, 'sent_date': None, 'from_email': None, 'to_email': None, 'cc': None, 'bcc': None, 'last_author': 'Ju, Hyeyeon (191-Extern-MBK)', 'extension': 'msg'}, 'search_type': 'filter', 'reasoning': "질의에서 3개의 구체적인 필터 정보를 찾았습니다: ['custodian', 'last_author', 'extension']. 조건 필터링을 사용합니다.", 'query': 'Ju, Hyeyeon (191-Extern-MBK)가 최종 작성한 msg 파일들을 모두 찾아줘'}
📊 추출된 필터:
  - custodian: Ju, Hyeyeon (191-Extern-MBK)
  - last_author: Ju, Hyeyeon (191-Extern-MBK)
  - extension: msg
🔍 검색 방식: filter
💭 판단 근거: 질의에서 3개의 구체적인 필터 정보를 찾았습니다: ['custodian', 'last_author', 'extension']. 조건 필터링을 사용합니다.
  📭 검색할 필터가 없어 단순 RAG 검색을 수행합니다.

================================================================================


테스트 케이스 16: EQC 전기차 관련 모든 자료
------------------------------------------------------------
2025-09-12 18:39:27,211 - mcp_tools - INFO - 🔍 필터 추출 시작: 'EQC 전기차 관련 모든 자료'
2025-09-12 18:39:28,726 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:39:28,727 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:39:28,727 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:39:28,807 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:39:28,807 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:39:28,872 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:39:28,873 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:39:28,958 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:39:28,959 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:39:29,042 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:39:29,042 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:39:29,042 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
🔍 DEBUG: result 타입: <class 'dict'>
🔍 DEBUG: result 값: {'filters': {'custodian': None, 'ori_file_name': None, 's_created_date': None, 'sent_date': None, 'from_email': None, 'to_email': None, 'cc': None, 'bcc': None, 'last_author': None, 'extension': None}, 'search_type': 'similarity', 'reasoning': '질의에서 구체적인 필터 정보를 찾을 수 없어 유사도 기반 검색을 사용합니다.', 'query': 'EQC 전기차 관련 모든 자료'}
📊 추출된 필터:
🔍 검색 방식: similarity
💭 판단 근거: 질의에서 구체적인 필터 정보를 찾을 수 없어 유사도 기반 검색을 사용합니다.
  📭 검색할 필터가 없어 단순 RAG 검색을 수행합니다.

================================================================================


테스트 케이스 17: MBUX 시스템 관련 기술 자료
------------------------------------------------------------
2025-09-12 18:39:29,042 - mcp_tools - INFO - 🔍 필터 추출 시작: 'MBUX 시스템 관련 기술 자료'
2025-09-12 18:39:30,551 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:39:30,552 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:39:30,553 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:39:30,624 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:39:30,624 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:39:30,687 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:39:30,687 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:39:30,761 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:39:30,761 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:39:30,841 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:39:30,841 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:39:30,841 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
🔍 DEBUG: result 타입: <class 'dict'>
🔍 DEBUG: result 값: {'filters': {'custodian': None, 'ori_file_name': None, 's_created_date': None, 'sent_date': None, 'from_email': None, 'to_email': None, 'cc': None, 'bcc': None, 'last_author': None, 'extension': None}, 'search_type': 'similarity', 'reasoning': '질의에서 구체적인 필터 정보를 찾을 수 없어 유사도 기반 검색을 사용합니다.', 'query': 'MBUX 시스템 관련 기술 자료'}
📊 추출된 필터:
🔍 검색 방식: similarity
💭 판단 근거: 질의에서 구체적인 필터 정보를 찾을 수 없어 유사도 기반 검색을 사용합니다.
  📭 검색할 필터가 없어 단순 RAG 검색을 수행합니다.

================================================================================


테스트 케이스 18: 4MATIC 사륜구동 시스템 관련 자료
------------------------------------------------------------
2025-09-12 18:39:30,841 - mcp_tools - INFO - 🔍 필터 추출 시작: '4MATIC 사륜구동 시스템 관련 자료'
2025-09-12 18:39:32,348 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:39:32,349 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:39:32,350 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:39:32,425 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:39:32,426 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:39:32,497 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:39:32,497 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:39:32,558 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:39:32,559 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:39:32,633 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:39:32,634 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:39:32,634 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
🔍 DEBUG: result 타입: <class 'dict'>
🔍 DEBUG: result 값: {'filters': {'custodian': None, 'ori_file_name': None, 's_created_date': None, 'sent_date': None, 'from_email': None, 'to_email': None, 'cc': None, 'bcc': None, 'last_author': None, 'extension': None}, 'search_type': 'similarity', 'reasoning': '질의에서 구체적인 필터 정보를 찾을 수 없어 유사도 기반 검색을 사용합니다.', 'query': '4MATIC 사륜구동 시스템 관련 자료'}
📊 추출된 필터:
🔍 검색 방식: similarity
💭 판단 근거: 질의에서 구체적인 필터 정보를 찾을 수 없어 유사도 기반 검색을 사용합니다.
  📭 검색할 필터가 없어 단순 RAG 검색을 수행합니다.

================================================================================


테스트 케이스 19: SOCAR와의 카셰어링 협력 관련 자료
------------------------------------------------------------
2025-09-12 18:39:32,634 - mcp_tools - INFO - 🔍 필터 추출 시작: 'SOCAR와의 카셰어링 협력 관련 자료'
2025-09-12 18:39:34,143 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:39:34,145 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:39:34,145 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:39:34,222 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:39:34,223 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:39:34,291 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:39:34,291 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:39:34,360 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:39:34,360 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:39:34,436 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:39:34,436 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:39:34,436 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
🔍 DEBUG: result 타입: <class 'dict'>
🔍 DEBUG: result 값: {'filters': {'custodian': None, 'ori_file_name': None, 's_created_date': None, 'sent_date': None, 'from_email': None, 'to_email': None, 'cc': None, 'bcc': None, 'last_author': None, 'extension': None}, 'search_type': 'similarity', 'reasoning': '질의에서 구체적인 필터 정보를 찾을 수 없어 유사도 기반 검색을 사용합니다.', 'query': 'SOCAR와의 카셰어링 협력 관련 자료'}
📊 추출된 필터:
🔍 검색 방식: similarity
💭 판단 근거: 질의에서 구체적인 필터 정보를 찾을 수 없어 유사도 기반 검색을 사용합니다.
  📭 검색할 필터가 없어 단순 RAG 검색을 수행합니다.

================================================================================


테스트 케이스 20: SOCAR, 몽클레르, 버질 아블로 협력 관련 모든 자료
------------------------------------------------------------
2025-09-12 18:39:34,436 - mcp_tools - INFO - 🔍 필터 추출 시작: 'SOCAR, 몽클레르, 버질 아블로 협력 관련 모든 자료'
2025-09-12 18:39:35,945 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:39:35,947 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:39:35,947 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:39:36,025 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:39:36,026 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:39:36,090 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:39:36,090 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:39:36,165 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:39:36,165 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:39:36,236 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:39:36,236 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:39:36,237 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
🔍 DEBUG: result 타입: <class 'dict'>
🔍 DEBUG: result 값: {'filters': {'custodian': None, 'ori_file_name': None, 's_created_date': None, 'sent_date': None, 'from_email': None, 'to_email': None, 'cc': None, 'bcc': None, 'last_author': None, 'extension': None}, 'search_type': 'similarity', 'reasoning': '질의에서 구체적인 필터 정보를 찾을 수 없어 유사도 기반 검색을 사용합니다.', 'query': 'SOCAR, 몽클레르, 버질 아블로 협력 관련 모든 자료'}
📊 추출된 필터:
🔍 검색 방식: similarity
💭 판단 근거: 질의에서 구체적인 필터 정보를 찾을 수 없어 유사도 기반 검색을 사용합니다.
  📭 검색할 필터가 없어 단순 RAG 검색을 수행합니다.

================================================================================


테스트 케이스 21: 전기차 관련 기술 중 MBUX, 4MATIC, 하이브리드 언급된 문서들
------------------------------------------------------------
2025-09-12 18:39:36,237 - mcp_tools - INFO - 🔍 필터 추출 시작: '전기차 관련 기술 중 MBUX, 4MATIC, 하이브리드 언급된 문서들'
2025-09-12 18:39:37,746 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:39:37,747 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:39:37,748 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:39:37,819 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:39:37,819 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:39:37,896 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:39:37,896 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:39:37,976 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:39:37,976 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:39:38,055 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:39:38,055 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:39:38,056 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
🔍 DEBUG: result 타입: <class 'dict'>
🔍 DEBUG: result 값: {'filters': {'custodian': None, 'ori_file_name': None, 's_created_date': None, 'sent_date': None, 'from_email': None, 'to_email': None, 'cc': None, 'bcc': None, 'last_author': None, 'extension': None}, 'search_type': 'similarity', 'reasoning': '질의에서 구체적인 필터 정보를 찾을 수 없어 유사도 기반 검색을 사용합니다.', 'query': '전기차 관련 기술 중 MBUX, 4MATIC, 하이브리드 언급된 문서들'}
📊 추출된 필터:
🔍 검색 방식: similarity
💭 판단 근거: 질의에서 구체적인 필터 정보를 찾을 수 없어 유사도 기반 검색을 사용합니다.
  📭 검색할 필터가 없어 단순 RAG 검색을 수행합니다.

================================================================================


테스트 케이스 22: SOCAR와의 카셰어링 서비스 협약 체결 과정
------------------------------------------------------------
2025-09-12 18:39:38,056 - mcp_tools - INFO - 🔍 필터 추출 시작: 'SOCAR와의 카셰어링 서비스 협약 체결 과정'
2025-09-12 18:39:39,566 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:39:39,567 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:39:39,567 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:39:39,646 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:39:39,647 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:39:39,709 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:39:39,710 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:39:39,779 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:39:39,779 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:39:39,854 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:39:39,854 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:39:39,854 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
🔍 DEBUG: result 타입: <class 'dict'>
🔍 DEBUG: result 값: {'filters': {'custodian': None, 'ori_file_name': None, 's_created_date': None, 'sent_date': None, 'from_email': None, 'to_email': None, 'cc': None, 'bcc': None, 'last_author': None, 'extension': None}, 'search_type': 'similarity', 'reasoning': '질의에서 구체적인 필터 정보를 찾을 수 없어 유사도 기반 검색을 사용합니다.', 'query': 'SOCAR와의 카셰어링 서비스 협약 체결 과정'}
📊 추출된 필터:
🔍 검색 방식: similarity
💭 판단 근거: 질의에서 구체적인 필터 정보를 찾을 수 없어 유사도 기반 검색을 사용합니다.
  📭 검색할 필터가 없어 단순 RAG 검색을 수행합니다.

================================================================================


테스트 케이스 23: EQC 모델의 국내 시장 출시 및 홍보 활동
------------------------------------------------------------
2025-09-12 18:39:39,854 - mcp_tools - INFO - 🔍 필터 추출 시작: 'EQC 모델의 국내 시장 출시 및 홍보 활동'
2025-09-12 18:39:41,362 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:39:41,364 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:39:41,364 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:39:41,443 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:39:41,444 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:39:41,509 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:39:41,510 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:39:41,588 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:39:41,588 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:39:41,648 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:39:41,649 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:39:41,649 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
🔍 DEBUG: result 타입: <class 'dict'>
🔍 DEBUG: result 값: {'filters': {'custodian': None, 'ori_file_name': None, 's_created_date': None, 'sent_date': None, 'from_email': None, 'to_email': None, 'cc': None, 'bcc': None, 'last_author': None, 'extension': None}, 'search_type': 'similarity', 'reasoning': '질의에서 구체적인 필터 정보를 찾을 수 없어 유사도 기반 검색을 사용합니다.', 'query': 'EQC 모델의 국내 시장 출시 및 홍보 활동'}
📊 추출된 필터:
🔍 검색 방식: similarity
💭 판단 근거: 질의에서 구체적인 필터 정보를 찾을 수 없어 유사도 기반 검색을 사용합니다.
  📭 검색할 필터가 없어 단순 RAG 검색을 수행합니다.

================================================================================


테스트 케이스 24: 메르세데스-벤츠의 전동화 전략 및 기술 로드맵
------------------------------------------------------------
2025-09-12 18:39:41,649 - mcp_tools - INFO - 🔍 필터 추출 시작: '메르세데스-벤츠의 전동화 전략 및 기술 로드맵'
2025-09-12 18:39:43,158 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:39:43,160 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:39:43,160 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:39:43,237 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:39:43,238 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:39:43,313 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:39:43,314 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:39:43,380 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:39:43,381 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:39:43,451 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:39:43,451 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:39:43,451 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
🔍 DEBUG: result 타입: <class 'dict'>
🔍 DEBUG: result 값: {'filters': {'custodian': None, 'ori_file_name': None, 's_created_date': None, 'sent_date': None, 'from_email': None, 'to_email': None, 'cc': None, 'bcc': None, 'last_author': None, 'extension': None}, 'search_type': 'similarity', 'reasoning': '질의에서 구체적인 필터 정보를 찾을 수 없어 유사도 기반 검색을 사용합니다.', 'query': '메르세데스-벤츠의 전동화 전략 및 기술 로드맵'}
📊 추출된 필터:
🔍 검색 방식: similarity
💭 판단 근거: 질의에서 구체적인 필터 정보를 찾을 수 없어 유사도 기반 검색을 사용합니다.
  📭 검색할 필터가 없어 단순 RAG 검색을 수행합니다.

================================================================================

✅ 테스트 완료!
/raid1/workspace/kars-agent/weaviate-mcp/.venv/lib/python3.12/site-packages/weaviate/warnings.py:302: ResourceWarning: Con004: The connection to Weaviate was not closed properly. This can lead to memory leaks.
            Please make sure to close the connection using `client.close()`.
  warnings.warn(
/raid1/workspace/kars-agent/weaviate-mcp/tmp_sungwon_chae/test_extract_value_tool_modified.py:333: ResourceWarning: unclosed <socket.socket fd=9, family=2, type=1, proto=6, laddr=('10.10.150.195', 36682), raddr=('10.10.150.195', 8080)>
  await test_extract_filter()
ResourceWarning: Enable tracemalloc to get the object allocation traceback

====================================================================================================

2025-09-12 18:39:43,480 - mcp_tools - INFO - Weaviate MCP 도구 초기화 완료
🔍 필터 기반 검색 테스트 시작 (MBG 실제 데이터 기반)

👤 1단계: 데이터베이스의 unique한 이름 값들 조회
------------------------------------------------------------
2025-09-12 18:39:43,480 - kars_db - INFO - 🚀 RAG 벡터 데이터베이스 초기화 시작
2025-09-12 18:39:43,480 - simple_manager - INFO - Weaviate URL: http://10.10.150.195:8080
2025-09-12 18:39:43,480 - simple_manager - INFO - OpenAI Base URL: http://10.10.190.1:8125
2025-09-12 18:39:43,480 - kars_db - INFO - ✅ VectorDB 매니저 초기화 완료
2025-09-12 18:39:43,509 - httpx - INFO - HTTP Request: GET http://10.10.190.1:8125/v1/models "HTTP/1.1 200 OK"
2025-09-12 18:39:43,510 - weaviate_db - INFO - ✅ vLLM 서버에서 모델명 가져옴: /data/models_ckpt/bge-m3
2025-09-12 18:39:43,524 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8125/v1/embeddings "HTTP/1.1 200 OK"
2025-09-12 18:39:43,525 - weaviate_db - INFO - ✅ 샘플 임베딩 생성 성공 (차원: 1024)
2025-09-12 18:39:43,568 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/.well-known/openid-configuration "HTTP/1.1 404 Not Found"
2025-09-12 18:39:43,592 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/meta "HTTP/1.1 200 OK"
2025-09-12 18:39:45,624 - weaviate_db - INFO - ✅ Weaviate 클라이언트 연결 성공: http://10.10.150.195:8080
2025-09-12 18:39:45,624 - weaviate_db - INFO - 📡 OpenAI Base URL (Python용): http://10.10.190.1:8125/v1
2025-09-12 18:39:45,624 - weaviate_db - INFO - 📡 OpenAI Base URL (Weaviate용): http://10.10.190.1:8125
2025-09-12 18:39:45,625 - weaviate_db - INFO - 🔧 동적 모델명: /data/models_ckpt/bge-m3
2025-09-12 18:39:45,625 - simple_manager - INFO - DB 연결 초기화 완료
2025-09-12 18:39:45,628 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema "HTTP/1.1 200 OK"
2025-09-12 18:39:45,633 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema/DocumentChunk "HTTP/1.1 200 OK"
2025-09-12 18:39:45,637 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema/EnronDocument "HTTP/1.1 200 OK"
2025-09-12 18:39:45,638 - weaviate_db - INFO - 스키마 조회 완료: 2개 클래스
2025-09-12 18:39:45,638 - simple_manager - WARNING - 클래스 매핑 파일이 없습니다. 기본 규칙을 사용합니다.
2025-09-12 18:39:45,638 - simple_manager - INFO - 기존 클래스 등록: chunk_db -> DocumentChunk
2025-09-12 18:39:45,638 - simple_manager - INFO - 기존 클래스 등록: enron_db -> EnronDocument
2025-09-12 18:39:45,638 - simple_manager - INFO - 총 2개 DB에 클래스 등록 완료
2025-09-12 18:39:45,638 - simple_manager - INFO -   chunk_db: ['DocumentChunk']
2025-09-12 18:39:45,638 - simple_manager - INFO -   enron_db: ['EnronDocument']
2025-09-12 18:39:45,641 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema "HTTP/1.1 200 OK"
2025-09-12 18:39:45,646 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema/DocumentChunk "HTTP/1.1 200 OK"
2025-09-12 18:39:45,650 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema/EnronDocument "HTTP/1.1 200 OK"
2025-09-12 18:39:45,651 - weaviate_db - INFO - 스키마 조회 완료: 2개 클래스
2025-09-12 18:39:45,651 - kars_db - INFO - 📊 사용 가능한 클래스들: ['DocumentChunk', 'EnronDocument']
2025-09-12 18:39:45,651 - kars_db - INFO - ✅ 사용할 클래스명: DocumentChunk
2025-09-12 18:39:45,652 - mcp_tools - INFO - ✅ RAG 데이터베이스 초기화 성공: kars_test
2025-09-12 18:39:45,652 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:39:45,652 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:39:45,728 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:39:45,728 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:39:45,803 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:39:45,803 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:39:45,876 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:39:45,876 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:39:45,938 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:39:45,938 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
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

🔍 2단계: 필터 기반 검색 테스트 (MBG 실제 데이터 기반)
------------------------------------------------------------

🧪 테스트 케이스 1: Jeong, Yeeun (191) on behalf of korea_com (191-NPM)가 발신한 메시지를 모두 찾아줘
--------------------------------------------------
2025-09-12 18:39:45,939 - mcp_tools - INFO - 🔍 필터 추출 시작: 'Jeong, Yeeun (191) on behalf of korea_com (191-NPM)가 발신한 메시지를 모두 찾아줘'
2025-09-12 18:39:48,027 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:39:48,028 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:39:48,028 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:39:48,100 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:39:48,101 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:39:48,162 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:39:48,162 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:39:48,223 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:39:48,223 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:39:48,283 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:39:48,283 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:39:48,283 - mcp_tools - INFO - ✅ from_email 필드 정확한 매칭 발견: 'Jeong, Yeeun (191) on behalf of korea_com (191-NPM)'
2025-09-12 18:39:48,284 - mcp_tools - INFO - ✅ 필터 추출 완료: filter 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email='Jeong, Yeeun (191) on behalf of korea_com (191-NPM)' to_email=None cc=None bcc=None last_author=None extension=None
❌ 필터 추출 실패: 알 수 없는 오류


🧪 테스트 케이스 2: Park, Sep (191) on behalf of korea_com (191-NPM)가 발신한 메시지를 모두 찾아줘
--------------------------------------------------
2025-09-12 18:39:48,284 - mcp_tools - INFO - 🔍 필터 추출 시작: 'Park, Sep (191) on behalf of korea_com (191-NPM)가 발신한 메시지를 모두 찾아줘'
2025-09-12 18:39:50,293 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:39:50,294 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:39:50,294 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:39:50,386 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:39:50,386 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:39:50,458 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:39:50,459 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:39:50,529 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:39:50,529 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:39:50,578 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:39:50,578 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:39:50,578 - mcp_tools - INFO - ✅ from_email 필드 정확한 매칭 발견: 'Park, Sep (191) on behalf of korea_com (191-NPM)'
2025-09-12 18:39:50,578 - mcp_tools - INFO - ✅ 필터 추출 완료: filter 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email='Park, Sep (191) on behalf of korea_com (191-NPM)' to_email=None cc=None bcc=None last_author=None extension=None
❌ 필터 추출 실패: 알 수 없는 오류


🧪 테스트 케이스 3: dw_191-MBK_all에게 발송된 메시지를 모두 찾아줘
--------------------------------------------------
2025-09-12 18:39:50,578 - mcp_tools - INFO - 🔍 필터 추출 시작: 'dw_191-MBK_all에게 발송된 메시지를 모두 찾아줘'
2025-09-12 18:39:52,282 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:39:52,283 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:39:52,283 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:39:52,359 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:39:52,359 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:39:52,420 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:39:52,420 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:39:52,481 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:39:52,481 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:39:52,552 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:39:52,552 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:39:53,860 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:39:53,861 - mcp_tools - INFO - ⚠️ custodian 필드 유사도 부족: 'dw_191-MBK_all' (최고 유사도: 0.00)
2025-09-12 18:39:53,861 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian='dw_191-MBK_all' ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
❌ 필터 추출 실패: 알 수 없는 오류


🧪 테스트 케이스 4: 세진 김이 보관한 문서들을 모두 찾아줘
--------------------------------------------------
2025-09-12 18:39:53,862 - mcp_tools - INFO - 🔍 필터 추출 시작: '세진 김이 보관한 문서들을 모두 찾아줘'
2025-09-12 18:39:55,449 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:39:55,450 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:39:55,450 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:39:55,529 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:39:55,529 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:39:55,602 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:39:55,602 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:39:55,668 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:39:55,668 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:39:55,728 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:39:55,728 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:39:55,728 - mcp_tools - INFO - ✅ custodian 필드 정확한 매칭 발견: '세진 김'
2025-09-12 18:39:55,729 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian='세진 김' ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
❌ 필터 추출 실패: 알 수 없는 오류


🧪 테스트 케이스 5: Song, Jieun (191)가 최종 작성한 문서들을 모두 찾아줘
--------------------------------------------------
2025-09-12 18:39:55,729 - mcp_tools - INFO - 🔍 필터 추출 시작: 'Song, Jieun (191)가 최종 작성한 문서들을 모두 찾아줘'
2025-09-12 18:39:57,462 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:39:57,463 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:39:57,463 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:39:57,537 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:39:57,538 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:39:57,584 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:39:57,584 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:39:57,657 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:39:57,657 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:39:57,729 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:39:57,729 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:39:57,729 - mcp_tools - INFO - ✅ last_author 필드 정확한 매칭 발견: 'Song, Jieun (191)'
2025-09-12 18:39:57,729 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author='Song, Jieun (191)' extension=None
❌ 필터 추출 실패: 알 수 없는 오류


🧪 테스트 케이스 6: Ju, Hyeyeon (191-Extern-MBK)가 최종 작성한 문서들을 모두 찾아줘
--------------------------------------------------
2025-09-12 18:39:57,729 - mcp_tools - INFO - 🔍 필터 추출 시작: 'Ju, Hyeyeon (191-Extern-MBK)가 최종 작성한 문서들을 모두 찾아줘'
2025-09-12 18:39:58,731 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:39:58,733 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:39:58,733 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:39:58,811 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:39:58,811 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:39:58,882 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:39:58,882 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:39:58,953 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:39:58,953 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:39:59,015 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:39:59,015 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:40:00,669 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:40:00,670 - mcp_tools - INFO - ⚠️ custodian 필드 유사도 부족: 'Ju, Hyeyeon (191-Extern-MBK)' (최고 유사도: 0.00)
2025-09-12 18:40:00,671 - mcp_tools - INFO - ✅ last_author 필드 정확한 매칭 발견: 'Ju, Hyeyeon (191-Extern-MBK)'
2025-09-12 18:40:00,671 - mcp_tools - INFO - ✅ 필터 추출 완료: filter 검색, 필터: custodian='Ju, Hyeyeon (191-Extern-MBK)' ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author='Ju, Hyeyeon (191-Extern-MBK)' extension=None
❌ 필터 추출 실패: 알 수 없는 오류


🧪 테스트 케이스 7: Kim, Ji-Hyun (191)가 최종 작성한 문서들을 모두 찾아줘
--------------------------------------------------
2025-09-12 18:40:00,671 - mcp_tools - INFO - 🔍 필터 추출 시작: 'Kim, Ji-Hyun (191)가 최종 작성한 문서들을 모두 찾아줘'
2025-09-12 18:40:02,420 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:40:02,421 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:40:02,421 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:40:02,494 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:40:02,494 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:40:02,556 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:40:02,556 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:40:02,637 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:40:02,637 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:40:02,696 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:40:02,696 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:40:02,697 - mcp_tools - INFO - ✅ last_author 필드 정확한 매칭 발견: 'Kim, Ji-Hyun (191)'
2025-09-12 18:40:02,697 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author='Kim, Ji-Hyun (191)' extension=None
❌ 필터 추출 실패: 알 수 없는 오류


🧪 테스트 케이스 8: Joo, Jaeyool (191)가 최종 작성한 문서들을 모두 찾아줘
--------------------------------------------------
2025-09-12 18:40:02,697 - mcp_tools - INFO - 🔍 필터 추출 시작: 'Joo, Jaeyool (191)가 최종 작성한 문서들을 모두 찾아줘'
2025-09-12 18:40:04,453 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:40:04,455 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:40:04,455 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:40:04,530 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:40:04,530 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:40:04,600 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:40:04,601 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:40:04,672 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:40:04,673 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:40:04,735 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:40:04,735 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:40:04,736 - mcp_tools - INFO - ✅ last_author 필드 정확한 매칭 발견: 'Joo, Jaeyool (191)'
2025-09-12 18:40:04,736 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author='Joo, Jaeyool (191)' extension=None
❌ 필터 추출 실패: 알 수 없는 오류


🧪 테스트 케이스 9: Park, Jaekyung (191)가 최종 작성한 문서들을 모두 찾아줘
--------------------------------------------------
2025-09-12 18:40:04,736 - mcp_tools - INFO - 🔍 필터 추출 시작: 'Park, Jaekyung (191)가 최종 작성한 문서들을 모두 찾아줘'
2025-09-12 18:40:06,494 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:40:06,495 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:40:06,495 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:40:06,572 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:40:06,572 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:40:06,633 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:40:06,633 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:40:06,693 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:40:06,693 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:40:06,755 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:40:06,755 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:40:06,755 - mcp_tools - INFO - ✅ last_author 필드 정확한 매칭 발견: 'Park, Jaekyung (191)'
2025-09-12 18:40:06,755 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author='Park, Jaekyung (191)' extension=None
❌ 필터 추출 실패: 알 수 없는 오류


🧪 테스트 케이스 10: Shim, Ellen (191)가 최종 작성한 문서들을 모두 찾아줘
--------------------------------------------------
2025-09-12 18:40:06,755 - mcp_tools - INFO - 🔍 필터 추출 시작: 'Shim, Ellen (191)가 최종 작성한 문서들을 모두 찾아줘'
2025-09-12 18:40:08,464 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:40:08,466 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:40:08,466 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:40:08,540 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:40:08,540 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:40:08,615 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:40:08,615 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:40:08,676 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:40:08,676 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:40:08,746 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:40:08,747 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:40:08,747 - mcp_tools - INFO - ✅ last_author 필드 정확한 매칭 발견: 'Shim, Ellen (191)'
2025-09-12 18:40:08,747 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author='Shim, Ellen (191)' extension=None
❌ 필터 추출 실패: 알 수 없는 오류


🧪 테스트 케이스 11: msg 확장자 파일들을 모두 찾아줘
--------------------------------------------------
2025-09-12 18:40:08,747 - mcp_tools - INFO - 🔍 필터 추출 시작: 'msg 확장자 파일들을 모두 찾아줘'
2025-09-12 18:40:10,285 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:40:10,286 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:40:10,286 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:40:10,363 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:40:10,363 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:40:10,433 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:40:10,433 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:40:10,493 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:40:10,494 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:40:10,564 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:40:10,564 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:40:10,565 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension='msg'
❌ 필터 추출 실패: 알 수 없는 오류


🧪 테스트 케이스 12: pdf 확장자 파일들을 모두 찾아줘
--------------------------------------------------
2025-09-12 18:40:10,565 - mcp_tools - INFO - 🔍 필터 추출 시작: 'pdf 확장자 파일들을 모두 찾아줘'
2025-09-12 18:40:12,103 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:40:12,104 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:40:12,104 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:40:12,161 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:40:12,161 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:40:12,218 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:40:12,218 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:40:12,276 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:40:12,276 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:40:12,335 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:40:12,335 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:40:12,335 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension='pdf'
❌ 필터 추출 실패: 알 수 없는 오류


🧪 테스트 케이스 13: csv 확장자 파일들을 모두 찾아줘
--------------------------------------------------
2025-09-12 18:40:12,336 - mcp_tools - INFO - 🔍 필터 추출 시작: 'csv 확장자 파일들을 모두 찾아줘'
2025-09-12 18:40:13,872 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:40:13,873 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:40:13,873 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:40:13,930 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:40:13,930 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:40:13,987 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:40:13,988 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:40:14,052 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:40:14,053 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:40:14,110 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:40:14,110 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:40:14,110 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension='csv'
❌ 필터 추출 실패: 알 수 없는 오류


🧪 테스트 케이스 14: 세진 김이 보관한 msg 파일들을 모두 찾아줘
--------------------------------------------------
2025-09-12 18:40:14,110 - mcp_tools - INFO - 🔍 필터 추출 시작: '세진 김이 보관한 msg 파일들을 모두 찾아줘'
2025-09-12 18:40:14,512 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:40:14,513 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:40:14,513 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:40:14,571 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:40:14,571 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:40:14,628 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:40:14,628 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:40:14,685 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:40:14,686 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:40:14,742 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:40:14,742 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:40:14,743 - mcp_tools - INFO - ✅ custodian 필드 정확한 매칭 발견: '세진 김'
2025-09-12 18:40:14,743 - mcp_tools - INFO - ✅ 필터 추출 완료: filter 검색, 필터: custodian='세진 김' ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension='.msg'
❌ 필터 추출 실패: 알 수 없는 오류


🧪 테스트 케이스 15: Song, Jieun (191)가 최종 작성한 pdf 파일들을 모두 찾아줘
--------------------------------------------------
2025-09-12 18:40:14,743 - mcp_tools - INFO - 🔍 필터 추출 시작: 'Song, Jieun (191)가 최종 작성한 pdf 파일들을 모두 찾아줘'
2025-09-12 18:40:16,503 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:40:16,504 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:40:16,504 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:40:16,561 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:40:16,561 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:40:16,618 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:40:16,618 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:40:16,675 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:40:16,676 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:40:16,732 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:40:16,732 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:40:16,733 - mcp_tools - INFO - ✅ last_author 필드 정확한 매칭 발견: 'Song, Jieun (191)'
2025-09-12 18:40:16,733 - mcp_tools - INFO - ✅ 필터 추출 완료: filter 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author='Song, Jieun (191)' extension='.pdf'
❌ 필터 추출 실패: 알 수 없는 오류


🧪 테스트 케이스 16: Ju, Hyeyeon (191-Extern-MBK)가 최종 작성한 msg 파일들을 모두 찾아줘
--------------------------------------------------
2025-09-12 18:40:16,733 - mcp_tools - INFO - 🔍 필터 추출 시작: 'Ju, Hyeyeon (191-Extern-MBK)가 최종 작성한 msg 파일들을 모두 찾아줘'
2025-09-12 18:40:17,898 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:40:17,899 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:40:17,899 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:40:17,956 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:40:17,956 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:40:18,013 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:40:18,014 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:40:18,070 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:40:18,071 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:40:18,128 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:40:18,128 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:40:19,636 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:40:19,637 - mcp_tools - INFO - ⚠️ custodian 필드 유사도 부족: 'Ju, Hyeyeon (191-Extern-MBK)' (최고 유사도: 0.00)
2025-09-12 18:40:19,638 - mcp_tools - INFO - ✅ last_author 필드 정확한 매칭 발견: 'Ju, Hyeyeon (191-Extern-MBK)'
2025-09-12 18:40:19,638 - mcp_tools - INFO - ✅ 필터 추출 완료: filter 검색, 필터: custodian='Ju, Hyeyeon (191-Extern-MBK)' ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author='Ju, Hyeyeon (191-Extern-MBK)' extension='msg'
❌ 필터 추출 실패: 알 수 없는 오류

✅ 필터 기반 검색 테스트 완료!
/raid1/workspace/kars-agent/weaviate-mcp/tmp_sungwon_chae/test_extract_value_tool_modified.py:338: ResourceWarning: unclosed <socket.socket fd=10, family=2, type=1, proto=6, laddr=('10.10.150.195', 37450), raddr=('10.10.150.195', 8080)>
  await test_filter_based_search()
ResourceWarning: Enable tracemalloc to get the object allocation traceback

🎉 모든 테스트 완료!
(.venv) min.choi10@wss-195:/raid1/workspace/kars-agent/weaviate-mcp/tmp_sungwon_chae$ 
