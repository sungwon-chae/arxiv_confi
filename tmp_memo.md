(.venv) min.choi10@wss-195:/raid1/workspace/kars-agent/weaviate-mcp/tmp_sungwon_chae$ python explore_data.py
�� 벡터DB 데이터 구조 및 내용 탐색 시작

2025-09-12 18:19:00,877 - mcp_tools - INFO - Weaviate MCP 도구 초기화 완료
📋 1단계: 데이터베이스 스키마 정보
------------------------------------------------------------
2025-09-12 18:19:00,878 - kars_db - INFO - 🚀 RAG 벡터 데이터베이스 초기화 시작
2025-09-12 18:19:00,878 - simple_manager - INFO - Weaviate URL: http://10.10.150.195:8080
2025-09-12 18:19:00,878 - simple_manager - INFO - OpenAI Base URL: http://10.10.190.1:8125
2025-09-12 18:19:00,878 - kars_db - INFO - ✅ VectorDB 매니저 초기화 완료
2025-09-12 18:19:01,054 - httpx - INFO - HTTP Request: GET http://10.10.190.1:8125/v1/models "HTTP/1.1 200 OK"
2025-09-12 18:19:01,055 - weaviate_db - INFO - ✅ vLLM 서버에서 모델명 가져옴: /data/models_ckpt/bge-m3
2025-09-12 18:19:01,069 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8125/v1/embeddings "HTTP/1.1 200 OK"
2025-09-12 18:19:01,071 - weaviate_db - INFO - ✅ 샘플 임베딩 생성 성공 (차원: 1024)
2025-09-12 18:19:01,103 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/.well-known/openid-configuration "HTTP/1.1 404 Not Found"
2025-09-12 18:19:01,128 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/meta "HTTP/1.1 200 OK"
2025-09-12 18:19:03,164 - weaviate_db - INFO - ✅ Weaviate 클라이언트 연결 성공: http://10.10.150.195:8080
2025-09-12 18:19:03,164 - weaviate_db - INFO - 📡 OpenAI Base URL (Python용): http://10.10.190.1:8125/v1
2025-09-12 18:19:03,164 - weaviate_db - INFO - 📡 OpenAI Base URL (Weaviate용): http://10.10.190.1:8125
2025-09-12 18:19:03,164 - weaviate_db - INFO - 🔧 동적 모델명: /data/models_ckpt/bge-m3
2025-09-12 18:19:03,164 - simple_manager - INFO - DB 연결 초기화 완료
2025-09-12 18:19:03,171 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema "HTTP/1.1 200 OK"
2025-09-12 18:19:03,176 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema/DocumentChunk "HTTP/1.1 200 OK"
2025-09-12 18:19:03,179 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema/EnronDocument "HTTP/1.1 200 OK"
2025-09-12 18:19:03,180 - weaviate_db - INFO - 스키마 조회 완료: 2개 클래스
2025-09-12 18:19:03,181 - simple_manager - WARNING - 클래스 매핑 파일이 없습니다. 기본 규칙을 사용합니다.
2025-09-12 18:19:03,181 - simple_manager - INFO - 기존 클래스 등록: chunk_db -> DocumentChunk
2025-09-12 18:19:03,181 - simple_manager - INFO - 기존 클래스 등록: enron_db -> EnronDocument
2025-09-12 18:19:03,181 - simple_manager - INFO - 총 2개 DB에 클래스 등록 완료
2025-09-12 18:19:03,181 - simple_manager - INFO -   chunk_db: ['DocumentChunk']
2025-09-12 18:19:03,181 - simple_manager - INFO -   enron_db: ['EnronDocument']
2025-09-12 18:19:03,184 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema "HTTP/1.1 200 OK"
2025-09-12 18:19:03,187 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema/DocumentChunk "HTTP/1.1 200 OK"
2025-09-12 18:19:03,191 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema/EnronDocument "HTTP/1.1 200 OK"
2025-09-12 18:19:03,191 - weaviate_db - INFO - 스키마 조회 완료: 2개 클래스
2025-09-12 18:19:03,192 - kars_db - INFO - 📊 사용 가능한 클래스들: ['DocumentChunk', 'EnronDocument']
2025-09-12 18:19:03,192 - kars_db - INFO - ✅ 사용할 클래스명: DocumentChunk
2025-09-12 18:19:03,192 - mcp_tools - INFO - ✅ RAG 데이터베이스 초기화 성공: kars_test
2025-09-12 18:19:03,192 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:19:03,192 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:19:03,274 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:19:03,274 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:19:03,349 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:19:03,349 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:19:03,413 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:19:03,414 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:19:03,480 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:19:03,480 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
✅ 데이터베이스 연결 성공!
  - from_email 개수: 3개
  - to_email 개수: 1개
  - custodian 개수: 1개
  - last_author 개수: 14개

�� 2단계: 실제 데이터 샘플 조회
------------------------------------------------------------

🔍 샘플 조회 1: 모든 문서를 5개만 보여줘
----------------------------------------
2025-09-12 18:19:03,480 - mcp_tools - INFO - 🔍 필터 추출 시작: '모든 문서를 5개만 보여줘'
2025-09-12 18:19:05,251 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:19:05,268 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:19:05,268 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:19:05,344 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:19:05,345 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:19:05,424 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:19:05,424 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:19:05,485 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:19:05,486 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:19:05,565 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:19:05,565 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:19:05,565 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
❌ 조회 실패: 알 수 없는 오류


🔍 샘플 조회 2: Jeong, Yeeun이 발신한 문서들을 보여줘
----------------------------------------
2025-09-12 18:19:05,565 - mcp_tools - INFO - 🔍 필터 추출 시작: 'Jeong, Yeeun이 발신한 문서들을 보여줘'
2025-09-12 18:19:07,330 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:19:07,331 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:19:07,331 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:19:07,406 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:19:07,407 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:19:07,484 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:19:07,484 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:19:07,561 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:19:07,561 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:19:07,641 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:19:07,641 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:19:09,955 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:19:09,956 - mcp_tools - INFO - ✅ from_email 필드 수정: 'Jeong, Yeeun' → 'Jeong, Yeeun (191) on behalf of korea_com (191-NPM)' (유사도: 100.00)
2025-09-12 18:19:09,956 - mcp_tools - INFO - ✅ 필터 추출 완료: filter 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email='Jeong, Yeeun (191) on behalf of korea_com (191-NPM)' to_email=None cc=None bcc=None last_author=None extension=None
❌ 조회 실패: 알 수 없는 오류


🔍 샘플 조회 3: Park, Sep이 발신한 문서들을 보여줘
----------------------------------------
2025-09-12 18:19:09,957 - mcp_tools - INFO - 🔍 필터 추출 시작: 'Park, Sep이 발신한 문서들을 보여줘'
2025-09-12 18:19:11,655 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:19:11,657 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:19:11,657 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:19:11,736 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:19:11,736 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:19:11,801 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:19:11,802 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:19:11,881 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:19:11,881 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:19:11,951 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:19:11,951 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:19:14,865 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:19:14,867 - mcp_tools - INFO - ✅ from_email 필드 수정: 'Park, Sep' → 'Park, Sep (191) on behalf of korea_com (191-NPM)' (유사도: 100.00)
2025-09-12 18:19:14,867 - mcp_tools - INFO - ✅ 필터 추출 완료: filter 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email='Park, Sep (191) on behalf of korea_com (191-NPM)' to_email=None cc=None bcc=None last_author=None extension=None
❌ 조회 실패: 알 수 없는 오류


🔍 샘플 조회 4: 세진 김이 보관한 문서들을 보여줘
----------------------------------------
2025-09-12 18:19:14,867 - mcp_tools - INFO - 🔍 필터 추출 시작: '세진 김이 보관한 문서들을 보여줘'
2025-09-12 18:19:16,577 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:19:16,579 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:19:16,579 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:19:16,656 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:19:16,656 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:19:16,734 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:19:16,735 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:19:16,800 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:19:16,800 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:19:16,896 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:19:16,896 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:19:16,896 - mcp_tools - INFO - ✅ custodian 필드 정확한 매칭 발견: '세진 김'
2025-09-12 18:19:16,897 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian='세진 김' ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
❌ 조회 실패: 알 수 없는 오류


🔍 샘플 조회 5: msg 파일들을 보여줘
----------------------------------------
2025-09-12 18:19:16,897 - mcp_tools - INFO - 🔍 필터 추출 시작: 'msg 파일들을 보여줘'
2025-09-12 18:19:18,522 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:19:18,523 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:19:18,524 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:19:18,600 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:19:18,600 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:19:18,675 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:19:18,675 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:19:18,748 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:19:18,749 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:19:18,819 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:19:18,819 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:19:18,819 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
❌ 조회 실패: 알 수 없는 오류


🔍 샘플 조회 6: pdf 파일들을 보여줘
----------------------------------------
2025-09-12 18:19:18,819 - mcp_tools - INFO - 🔍 필터 추출 시작: 'pdf 파일들을 보여줘'
2025-09-12 18:19:20,472 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:19:20,473 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:19:20,473 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:19:20,551 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:19:20,551 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:19:20,621 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:19:20,621 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:19:20,697 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:19:20,697 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:19:20,771 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:19:20,771 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:19:20,771 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension='.pdf'
❌ 조회 실패: 알 수 없는 오류


🔍 샘플 조회 7: csv 파일들을 보여줘
----------------------------------------
2025-09-12 18:19:20,771 - mcp_tools - INFO - 🔍 필터 추출 시작: 'csv 파일들을 보여줘'
2025-09-12 18:19:22,400 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:19:22,402 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:19:22,402 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:19:22,482 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:19:22,482 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:19:22,561 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:19:22,561 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:19:22,627 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:19:22,627 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:19:22,699 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:19:22,699 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:19:22,700 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
❌ 조회 실패: 알 수 없는 오류


🔍 샘플 조회 8: Song, Jieun이 작성한 문서들을 보여줘
----------------------------------------
2025-09-12 18:19:22,700 - mcp_tools - INFO - 🔍 필터 추출 시작: 'Song, Jieun이 작성한 문서들을 보여줘'
2025-09-12 18:19:24,451 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:19:24,452 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:19:24,452 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:19:24,532 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:19:24,532 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:19:24,597 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:19:24,598 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:19:24,673 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:19:24,673 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:19:24,744 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:19:24,744 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:19:29,356 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:19:29,357 - mcp_tools - INFO - ✅ last_author 필드 수정: 'Song, Jieun' → 'Song, Jieun (191)' (유사도: 100.00)
2025-09-12 18:19:29,358 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author='Song, Jieun (191)' extension=None
❌ 조회 실패: 알 수 없는 오류


🔍 샘플 조회 9: Ju, Hyeyeon이 작성한 문서들을 보여줘
----------------------------------------
2025-09-12 18:19:29,358 - mcp_tools - INFO - 🔍 필터 추출 시작: 'Ju, Hyeyeon이 작성한 문서들을 보여줘'
2025-09-12 18:19:31,129 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:19:31,130 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:19:31,130 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:19:31,205 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:19:31,206 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:19:31,287 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:19:31,287 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:19:31,362 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:19:31,363 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:19:31,422 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:19:31,422 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:19:36,074 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:19:36,075 - mcp_tools - INFO - ✅ last_author 필드 수정: 'Ju, Hyeyeon' → 'Ju, Hyeyeon (191-Extern-MBK)' (유사도: 100.00)
2025-09-12 18:19:36,075 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author='Ju, Hyeyeon (191-Extern-MBK)' extension=None
❌ 조회 실패: 알 수 없는 오류


📋 3단계: 필드별 고유값 상세 조회
------------------------------------------------------------

📤 from_email 전체 목록 (3개):
  1. Jeong, Yeeun (191) on behalf of korea_com (191-NPM)
  2. NaN
  3. Park, Sep (191) on behalf of korea_com (191-NPM)

📥 to_email 전체 목록 (1개):
  1. NaN

👤 custodian 전체 목록 (1개):
  1. 세진 김

✍️ last_author 전체 목록 (14개):
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
  11. Song, Jieun (191)
  12. Song, Jieun (691)
  13. 䵩捲潳潦璮⁗潲搠㈰ㄶ㬠浯摩晩敤⁵獩湧⁩呥硴卨慲瀮䱇偌瘲⹃潲攠ㄮ㘮ㄮ
  14. 䵩捲潳潦璮⁗潲搠㈰ㄶ㬠浯摩晩敤⁵獩湧⁩呥硴卨慲瀮䱇偌瘲⹃潲攠ㄮ㘮ㄮ�

�� 4단계: 추천 테스트 쿼리
------------------------------------------------------------
실제 데이터를 바탕으로 한 추천 테스트 쿼리들:

�� 필터 기반 검색 쿼리:
  1. 'Jeong, Yeeun (191) on behalf of korea_com (191-NPM)가 발신한 메시지를 모두 찾아줘'
  2. 'Park, Sep (191) on behalf of korea_com (191-NPM)가 발신한 메시지를 모두 찾아줘'
  3. '세진 김이 보관한 문서들을 모두 찾아줘'
  4. 'Song, Jieun (191)가 최종 작성한 문서들을 모두 찾아줘'
  5. 'msg 확장자 파일들을 모두 찾아줘'
  6. 'pdf 확장자 파일들을 모두 찾아줘'
  7. 'csv 확장자 파일들을 모두 찾아줘'

🔍 복합 필터 검색 쿼리:
  8. '세진 김이 보관한 msg 파일들을 모두 찾아줘'
  9. 'Song, Jieun (191)가 최종 작성한 pdf 파일들을 모두 찾아줘'

🔍 RAG 벡터 검색 쿼리:
  10. 'EQC 전기차 관련 모든 자료'
  11. 'MBUX 시스템 관련 기술 자료'
  12. 'SOCAR와의 카셰어링 협력 관련 자료'

✅ 데이터 탐색 완료!

💡 이제 위의 추천 쿼리들을 바탕으로 테스트 쿼리를 작성하세요!
/raid1/workspace/kars-agent/weaviate-mcp/.venv/lib/python3.12/site-packages/weaviate/warnings.py:302: ResourceWarning: Con004: The connection to Weaviate was not closed properly. This can lead to memory leaks.
            Please make sure to close the connection using `client.close()`.
  warnings.warn(
/raid1/workspace/kars-agent/weaviate-mcp/tmp_sungwon_chae/explore_data.py:190: ResourceWarning: unclosed <socket.socket fd=7, family=2, type=1, proto=6, laddr=('10.10.150.195', 49522), raddr=('10.10.150.195', 8080)>
  await explore_database()
ResourceWarning: Enable tracemalloc to get the object allocation traceback
(.venv) min.choi10@wss-195:/raid1/workspace/kars-agent/weaviate-mcp/tmp_sungwon_chae$ 
