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
