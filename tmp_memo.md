(.venv) min.choi10@wss-195:/raid1/workspace/kars-agent/weaviate-mcp/tmp_sungwon_chae$ python test_extract_value_tool_modified.py 
�� Weaviate MCP 도구 테스트 시작 (수정된 버전)

2025-09-12 18:22:42,930 - mcp_tools - INFO - Weaviate MCP 도구 초기화 완료
2025-09-12 18:22:43,347 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
Test Query Response:  ChatCompletion(id='chatcmpl-505babd56af34ca69f7672f6e24c56b9', choices=[Choice(finish_reason='length', index=0, logprobs=None, message=ChatCompletionMessage(content='<think>\nOkay, the user just said "hi', refusal=None, role='assistant', annotations=None, audio=None, function_call=None, tool_calls=[], reasoning_content=None), stop_reason=None)], created=1757668968, model='/data/models_ckpt/Qwen3-32B', object='chat.completion', service_tier=None, system_fingerprint=None, usage=CompletionUsage(completion_tokens=10, prompt_tokens=10, total_tokens=20, completion_tokens_details=None, prompt_tokens_details=None), prompt_logprobs=None)
✅ OpenAI 클라이언트 설정 완료
🔍 extract_filter_from_query 도구 테스트 시작 (MBG 실제 데이터 기반)

📋 테스트 목적:
  1. Filter 자동 추출 검증
  2. 벡터DB에서 관련 문서 검색 확인
  3. 실제 MBG 데이터 기반 GT 검증
  4. 유사도 기반 검색 성능 확인

테스트 케이스 1: Jeong, Yeeun (191) on behalf of korea_com (191-NPM)가 발신한 메시지를 모두 찾아줘
------------------------------------------------------------
2025-09-12 18:22:43,358 - mcp_tools - INFO - 🔍 필터 추출 시작: 'Jeong, Yeeun (191) on behalf of korea_com (191-NPM)가 발신한 메시지를 모두 찾아줘'
2025-09-12 18:22:45,436 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:22:45,437 - kars_db - INFO - 🚀 RAG 벡터 데이터베이스 초기화 시작
2025-09-12 18:22:45,437 - simple_manager - INFO - Weaviate URL: http://10.10.150.195:8080
2025-09-12 18:22:45,437 - simple_manager - INFO - OpenAI Base URL: http://10.10.190.1:8125
2025-09-12 18:22:45,438 - kars_db - INFO - ✅ VectorDB 매니저 초기화 완료
2025-09-12 18:22:45,484 - httpx - INFO - HTTP Request: GET http://10.10.190.1:8125/v1/models "HTTP/1.1 200 OK"
2025-09-12 18:22:45,485 - weaviate_db - INFO - ✅ vLLM 서버에서 모델명 가져옴: /data/models_ckpt/bge-m3
2025-09-12 18:22:45,499 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8125/v1/embeddings "HTTP/1.1 200 OK"
2025-09-12 18:22:45,502 - weaviate_db - INFO - ✅ 샘플 임베딩 생성 성공 (차원: 1024)
2025-09-12 18:22:45,545 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/.well-known/openid-configuration "HTTP/1.1 404 Not Found"
2025-09-12 18:22:45,571 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/meta "HTTP/1.1 200 OK"
2025-09-12 18:22:47,606 - weaviate_db - INFO - ✅ Weaviate 클라이언트 연결 성공: http://10.10.150.195:8080
2025-09-12 18:22:47,606 - weaviate_db - INFO - 📡 OpenAI Base URL (Python용): http://10.10.190.1:8125/v1
2025-09-12 18:22:47,606 - weaviate_db - INFO - 📡 OpenAI Base URL (Weaviate용): http://10.10.190.1:8125
2025-09-12 18:22:47,606 - weaviate_db - INFO - 🔧 동적 모델명: /data/models_ckpt/bge-m3
2025-09-12 18:22:47,606 - simple_manager - INFO - DB 연결 초기화 완료
2025-09-12 18:22:47,610 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema "HTTP/1.1 200 OK"
2025-09-12 18:22:47,615 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema/DocumentChunk "HTTP/1.1 200 OK"
2025-09-12 18:22:47,622 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema/EnronDocument "HTTP/1.1 200 OK"
2025-09-12 18:22:47,623 - weaviate_db - INFO - 스키마 조회 완료: 2개 클래스
2025-09-12 18:22:47,623 - simple_manager - WARNING - 클래스 매핑 파일이 없습니다. 기본 규칙을 사용합니다.
2025-09-12 18:22:47,623 - simple_manager - INFO - 기존 클래스 등록: chunk_db -> DocumentChunk
2025-09-12 18:22:47,623 - simple_manager - INFO - 기존 클래스 등록: enron_db -> EnronDocument
2025-09-12 18:22:47,623 - simple_manager - INFO - 총 2개 DB에 클래스 등록 완료
2025-09-12 18:22:47,623 - simple_manager - INFO -   chunk_db: ['DocumentChunk']
2025-09-12 18:22:47,623 - simple_manager - INFO -   enron_db: ['EnronDocument']
2025-09-12 18:22:47,626 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema "HTTP/1.1 200 OK"
2025-09-12 18:22:47,630 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema/DocumentChunk "HTTP/1.1 200 OK"
2025-09-12 18:22:47,633 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema/EnronDocument "HTTP/1.1 200 OK"
2025-09-12 18:22:47,634 - weaviate_db - INFO - 스키마 조회 완료: 2개 클래스
2025-09-12 18:22:47,634 - kars_db - INFO - 📊 사용 가능한 클래스들: ['DocumentChunk', 'EnronDocument']
2025-09-12 18:22:47,634 - kars_db - INFO - ✅ 사용할 클래스명: DocumentChunk
2025-09-12 18:22:47,634 - mcp_tools - INFO - ✅ RAG 데이터베이스 초기화 성공: kars_test
2025-09-12 18:22:47,634 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:22:47,634 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:22:47,716 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:22:47,717 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:22:47,792 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:22:47,792 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:22:47,866 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:22:47,867 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:22:47,936 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:22:47,936 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:22:47,936 - mcp_tools - INFO - ✅ from_email 필드 정확한 매칭 발견: 'Jeong, Yeeun (191) on behalf of korea_com (191-NPM)'
2025-09-12 18:22:47,936 - mcp_tools - INFO - ✅ 필터 추출 완료: filter 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email='Jeong, Yeeun (191) on behalf of korea_com (191-NPM)' to_email=None cc=None bcc=None last_author=None extension=None
❌ 필터 추출 실패: 알 수 없는 오류

================================================================================


테스트 케이스 2: Park, Sep (191) on behalf of korea_com (191-NPM)가 발신한 메시지를 모두 찾아줘
------------------------------------------------------------
2025-09-12 18:22:47,937 - mcp_tools - INFO - 🔍 필터 추출 시작: 'Park, Sep (191) on behalf of korea_com (191-NPM)가 발신한 메시지를 모두 찾아줘'
2025-09-12 18:22:49,928 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:22:49,930 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:22:49,930 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:22:50,007 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:22:50,007 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:22:50,072 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:22:50,072 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:22:50,137 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:22:50,137 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:22:50,201 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:22:50,201 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:22:50,201 - mcp_tools - INFO - ✅ from_email 필드 정확한 매칭 발견: 'Park, Sep (191) on behalf of korea_com (191-NPM)'
2025-09-12 18:22:50,201 - mcp_tools - INFO - ✅ 필터 추출 완료: filter 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email='Park, Sep (191) on behalf of korea_com (191-NPM)' to_email=None cc=None bcc=None last_author=None extension=None
❌ 필터 추출 실패: 알 수 없는 오류

================================================================================


테스트 케이스 3: 세진 김이 보관한 문서들을 모두 찾아줘
------------------------------------------------------------
2025-09-12 18:22:50,201 - mcp_tools - INFO - 🔍 필터 추출 시작: '세진 김이 보관한 문서들을 모두 찾아줘'
2025-09-12 18:22:51,771 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:22:51,773 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:22:51,773 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:22:51,848 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:22:51,848 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:22:51,907 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:22:51,907 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:22:51,979 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:22:51,980 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:22:52,054 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:22:52,054 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:22:52,054 - mcp_tools - INFO - ✅ custodian 필드 정확한 매칭 발견: '세진 김'
2025-09-12 18:22:52,054 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian='세진 김' ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
❌ 필터 추출 실패: 알 수 없는 오류

================================================================================


테스트 케이스 4: Song, Jieun (191)가 최종 작성한 문서들을 모두 찾아줘
------------------------------------------------------------
2025-09-12 18:22:52,054 - mcp_tools - INFO - 🔍 필터 추출 시작: 'Song, Jieun (191)가 최종 작성한 문서들을 모두 찾아줘'
2025-09-12 18:22:53,774 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:22:53,775 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:22:53,775 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:22:53,853 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:22:53,854 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:22:53,927 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:22:53,928 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:22:53,996 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:22:53,997 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:22:54,067 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:22:54,068 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:22:54,068 - mcp_tools - INFO - ✅ last_author 필드 정확한 매칭 발견: 'Song, Jieun (191)'
2025-09-12 18:22:54,068 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author='Song, Jieun (191)' extension=None
❌ 필터 추출 실패: 알 수 없는 오류

================================================================================


테스트 케이스 5: Ju, Hyeyeon (191-Extern-MBK)가 최종 작성한 문서들을 모두 찾아줘
------------------------------------------------------------
2025-09-12 18:22:54,068 - mcp_tools - INFO - 🔍 필터 추출 시작: 'Ju, Hyeyeon (191-Extern-MBK)가 최종 작성한 문서들을 모두 찾아줘'
2025-09-12 18:22:55,067 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:22:55,068 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:22:55,068 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:22:55,147 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:22:55,147 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:22:55,219 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:22:55,220 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:22:55,283 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:22:55,284 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:22:55,362 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:22:55,363 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:22:57,002 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:22:57,003 - mcp_tools - INFO - ⚠️ custodian 필드 유사도 부족: 'Ju, Hyeyeon (191-Extern-MBK)' (최고 유사도: 0.00)
2025-09-12 18:22:57,003 - mcp_tools - INFO - ✅ last_author 필드 정확한 매칭 발견: 'Ju, Hyeyeon (191-Extern-MBK)'
2025-09-12 18:22:57,004 - mcp_tools - INFO - ✅ 필터 추출 완료: filter 검색, 필터: custodian='Ju, Hyeyeon (191-Extern-MBK)' ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author='Ju, Hyeyeon (191-Extern-MBK)' extension=None
❌ 필터 추출 실패: 알 수 없는 오류

================================================================================


테스트 케이스 6: Kim, Ji-Hyun (191)가 최종 작성한 문서들을 모두 찾아줘
------------------------------------------------------------
2025-09-12 18:22:57,004 - mcp_tools - INFO - 🔍 필터 추출 시작: 'Kim, Ji-Hyun (191)가 최종 작성한 문서들을 모두 찾아줘'
2025-09-12 18:22:58,742 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:22:58,744 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:22:58,744 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:22:58,823 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:22:58,824 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:22:58,910 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:22:58,910 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:22:58,981 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:22:58,982 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:22:59,057 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:22:59,057 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:22:59,057 - mcp_tools - INFO - ✅ last_author 필드 정확한 매칭 발견: 'Kim, Ji-Hyun (191)'
2025-09-12 18:22:59,057 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author='Kim, Ji-Hyun (191)' extension=None
❌ 필터 추출 실패: 알 수 없는 오류

================================================================================


테스트 케이스 7: msg 확장자 파일들을 모두 찾아줘
------------------------------------------------------------
2025-09-12 18:22:59,057 - mcp_tools - INFO - 🔍 필터 추출 시작: 'msg 확장자 파일들을 모두 찾아줘'
2025-09-12 18:23:00,581 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:23:00,583 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:23:00,583 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:23:00,660 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:23:00,660 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:23:00,735 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:23:00,736 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:23:00,815 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:23:00,816 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:23:00,896 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:23:00,896 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:23:00,897 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension='msg'
❌ 필터 추출 실패: 알 수 없는 오류

================================================================================


테스트 케이스 8: pdf 확장자 파일들을 모두 찾아줘
------------------------------------------------------------
2025-09-12 18:23:00,897 - mcp_tools - INFO - 🔍 필터 추출 시작: 'pdf 확장자 파일들을 모두 찾아줘'
2025-09-12 18:23:02,424 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:23:02,426 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:23:02,426 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:23:02,496 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:23:02,496 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:23:02,561 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:23:02,561 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:23:02,638 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:23:02,638 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:23:02,713 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:23:02,713 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:23:02,713 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension='pdf'
❌ 필터 추출 실패: 알 수 없는 오류

================================================================================


테스트 케이스 9: csv 확장자 파일들을 모두 찾아줘
------------------------------------------------------------
2025-09-12 18:23:02,714 - mcp_tools - INFO - 🔍 필터 추출 시작: 'csv 확장자 파일들을 모두 찾아줘'
2025-09-12 18:23:04,243 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:23:04,244 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:23:04,245 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:23:04,320 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:23:04,322 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:23:04,399 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:23:04,400 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:23:04,469 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:23:04,469 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:23:04,545 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:23:04,545 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:23:04,545 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension='.csv'
❌ 필터 추출 실패: 알 수 없는 오류

================================================================================


테스트 케이스 10: EQC 전기차 관련 모든 자료
------------------------------------------------------------
2025-09-12 18:23:04,545 - mcp_tools - INFO - 🔍 필터 추출 시작: 'EQC 전기차 관련 모든 자료'
2025-09-12 18:23:06,051 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:23:06,052 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:23:06,052 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:23:06,127 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:23:06,128 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:23:06,206 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:23:06,207 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:23:06,271 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:23:06,272 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:23:06,348 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:23:06,348 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:23:06,348 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
❌ 필터 추출 실패: 알 수 없는 오류

================================================================================


테스트 케이스 11: MBUX 시스템 관련 기술 자료
------------------------------------------------------------
2025-09-12 18:23:06,348 - mcp_tools - INFO - 🔍 필터 추출 시작: 'MBUX 시스템 관련 기술 자료'
2025-09-12 18:23:07,856 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:23:07,857 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:23:07,858 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:23:07,961 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:23:07,961 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:23:08,039 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:23:08,039 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:23:08,097 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:23:08,097 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:23:08,171 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:23:08,172 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:23:08,172 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
❌ 필터 추출 실패: 알 수 없는 오류

================================================================================


테스트 케이스 12: 4MATIC 사륜구동 시스템 관련 자료
------------------------------------------------------------
2025-09-12 18:23:08,172 - mcp_tools - INFO - 🔍 필터 추출 시작: '4MATIC 사륜구동 시스템 관련 자료'
2025-09-12 18:23:09,680 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:23:09,682 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:23:09,682 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:23:09,759 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:23:09,760 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:23:09,839 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:23:09,839 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:23:09,904 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:23:09,905 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:23:09,981 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:23:09,981 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:23:09,982 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
❌ 필터 추출 실패: 알 수 없는 오류

================================================================================


테스트 케이스 13: SOCAR와의 카셰어링 협력 관련 자료
------------------------------------------------------------
2025-09-12 18:23:09,982 - mcp_tools - INFO - 🔍 필터 추출 시작: 'SOCAR와의 카셰어링 협력 관련 자료'
2025-09-12 18:23:11,492 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:23:11,493 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:23:11,494 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:23:11,570 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:23:11,570 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:23:11,647 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:23:11,648 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:23:11,718 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:23:11,719 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:23:11,790 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:23:11,791 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:23:11,792 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
❌ 필터 추출 실패: 알 수 없는 오류

================================================================================


테스트 케이스 14: SOCAR, 몽클레르, 버질 아블로 협력 관련 모든 자료
------------------------------------------------------------
2025-09-12 18:23:11,792 - mcp_tools - INFO - 🔍 필터 추출 시작: 'SOCAR, 몽클레르, 버질 아블로 협력 관련 모든 자료'
2025-09-12 18:23:13,302 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:23:13,304 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:23:13,304 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:23:13,381 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:23:13,382 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:23:13,451 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:23:13,452 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:23:13,527 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:23:13,527 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:23:13,599 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:23:13,599 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:23:13,599 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
❌ 필터 추출 실패: 알 수 없는 오류

================================================================================


테스트 케이스 15: 전기차 관련 기술 중 MBUX, 4MATIC, 하이브리드 언급된 문서들
------------------------------------------------------------
2025-09-12 18:23:13,599 - mcp_tools - INFO - 🔍 필터 추출 시작: '전기차 관련 기술 중 MBUX, 4MATIC, 하이브리드 언급된 문서들'
2025-09-12 18:23:15,112 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:23:15,114 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:23:15,114 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:23:15,189 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:23:15,190 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:23:15,260 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:23:15,260 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:23:15,325 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:23:15,325 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:23:15,402 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:23:15,403 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:23:15,403 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
❌ 필터 추출 실패: 알 수 없는 오류

================================================================================


테스트 케이스 16: SOCAR와의 카셰어링 서비스 협약 체결 과정
------------------------------------------------------------
2025-09-12 18:23:15,403 - mcp_tools - INFO - 🔍 필터 추출 시작: 'SOCAR와의 카셰어링 서비스 협약 체결 과정'
2025-09-12 18:23:16,918 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:23:16,919 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:23:16,919 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:23:17,004 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:23:17,004 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:23:17,082 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:23:17,083 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:23:17,161 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:23:17,161 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:23:17,241 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:23:17,241 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:23:17,241 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
❌ 필터 추출 실패: 알 수 없는 오류

================================================================================


테스트 케이스 17: EQC 모델의 국내 시장 출시 및 홍보 활동
------------------------------------------------------------
2025-09-12 18:23:17,242 - mcp_tools - INFO - 🔍 필터 추출 시작: 'EQC 모델의 국내 시장 출시 및 홍보 활동'
2025-09-12 18:23:18,754 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:23:18,755 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:23:18,755 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:23:18,827 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:23:18,827 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:23:18,900 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:23:18,900 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:23:18,966 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:23:18,966 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:23:19,042 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:23:19,042 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:23:19,042 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
❌ 필터 추출 실패: 알 수 없는 오류

================================================================================


테스트 케이스 18: 메르세데스-벤츠의 전동화 전략 및 기술 로드맵
------------------------------------------------------------
2025-09-12 18:23:19,043 - mcp_tools - INFO - 🔍 필터 추출 시작: '메르세데스-벤츠의 전동화 전략 및 기술 로드맵'
2025-09-12 18:23:20,556 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:23:20,557 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:23:20,557 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:23:20,631 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:23:20,631 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:23:20,697 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:23:20,697 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:23:20,769 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:23:20,769 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:23:20,840 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:23:20,840 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:23:20,841 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
❌ 필터 추출 실패: 알 수 없는 오류

================================================================================

✅ 테스트 완료!
/raid1/workspace/kars-agent/weaviate-mcp/.venv/lib/python3.12/site-packages/weaviate/warnings.py:302: ResourceWarning: Con004: The connection to Weaviate was not closed properly. This can lead to memory leaks.
            Please make sure to close the connection using `client.close()`.
  warnings.warn(
/raid1/workspace/kars-agent/weaviate-mcp/tmp_sungwon_chae/test_extract_value_tool_modified.py:306: ResourceWarning: unclosed <socket.socket fd=9, family=2, type=1, proto=6, laddr=('10.10.150.195', 38160), raddr=('10.10.150.195', 8080)>
  await test_extract_filter()
ResourceWarning: Enable tracemalloc to get the object allocation traceback

====================================================================================================

2025-09-12 18:23:20,871 - mcp_tools - INFO - Weaviate MCP 도구 초기화 완료
 필터 기반 검색 테스트 시작 (MBG 실제 데이터 기반)

👤 1단계: 데이터베이스의 unique한 이름 값들 조회
------------------------------------------------------------
2025-09-12 18:23:20,872 - kars_db - INFO - 🚀 RAG 벡터 데이터베이스 초기화 시작
2025-09-12 18:23:20,872 - simple_manager - INFO - Weaviate URL: http://10.10.150.195:8080
2025-09-12 18:23:20,872 - simple_manager - INFO - OpenAI Base URL: http://10.10.190.1:8125
2025-09-12 18:23:20,872 - kars_db - INFO - ✅ VectorDB 매니저 초기화 완료
2025-09-12 18:23:20,900 - httpx - INFO - HTTP Request: GET http://10.10.190.1:8125/v1/models "HTTP/1.1 200 OK"
2025-09-12 18:23:20,901 - weaviate_db - INFO - ✅ vLLM 서버에서 모델명 가져옴: /data/models_ckpt/bge-m3
2025-09-12 18:23:20,914 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8125/v1/embeddings "HTTP/1.1 200 OK"
2025-09-12 18:23:20,916 - weaviate_db - INFO - ✅ 샘플 임베딩 생성 성공 (차원: 1024)
2025-09-12 18:23:20,958 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/.well-known/openid-configuration "HTTP/1.1 404 Not Found"
2025-09-12 18:23:20,983 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/meta "HTTP/1.1 200 OK"
2025-09-12 18:23:23,013 - weaviate_db - INFO - ✅ Weaviate 클라이언트 연결 성공: http://10.10.150.195:8080
2025-09-12 18:23:23,013 - weaviate_db - INFO - 📡 OpenAI Base URL (Python용): http://10.10.190.1:8125/v1
2025-09-12 18:23:23,014 - weaviate_db - INFO - 📡 OpenAI Base URL (Weaviate용): http://10.10.190.1:8125
2025-09-12 18:23:23,014 - weaviate_db - INFO - 🔧 동적 모델명: /data/models_ckpt/bge-m3
2025-09-12 18:23:23,014 - simple_manager - INFO - DB 연결 초기화 완료
2025-09-12 18:23:23,017 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema "HTTP/1.1 200 OK"
2025-09-12 18:23:23,026 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema/DocumentChunk "HTTP/1.1 200 OK"
2025-09-12 18:23:23,029 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema/EnronDocument "HTTP/1.1 200 OK"
2025-09-12 18:23:23,031 - weaviate_db - INFO - 스키마 조회 완료: 2개 클래스
2025-09-12 18:23:23,031 - simple_manager - WARNING - 클래스 매핑 파일이 없습니다. 기본 규칙을 사용합니다.
2025-09-12 18:23:23,031 - simple_manager - INFO - 기존 클래스 등록: chunk_db -> DocumentChunk
2025-09-12 18:23:23,031 - simple_manager - INFO - 기존 클래스 등록: enron_db -> EnronDocument
2025-09-12 18:23:23,031 - simple_manager - INFO - 총 2개 DB에 클래스 등록 완료
2025-09-12 18:23:23,031 - simple_manager - INFO -   chunk_db: ['DocumentChunk']
2025-09-12 18:23:23,031 - simple_manager - INFO -   enron_db: ['EnronDocument']
2025-09-12 18:23:23,035 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema "HTTP/1.1 200 OK"
2025-09-12 18:23:23,038 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema/DocumentChunk "HTTP/1.1 200 OK"
2025-09-12 18:23:23,041 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema/EnronDocument "HTTP/1.1 200 OK"
2025-09-12 18:23:23,042 - weaviate_db - INFO - 스키마 조회 완료: 2개 클래스
2025-09-12 18:23:23,042 - kars_db - INFO - 📊 사용 가능한 클래스들: ['DocumentChunk', 'EnronDocument']
2025-09-12 18:23:23,042 - kars_db - INFO - ✅ 사용할 클래스명: DocumentChunk
2025-09-12 18:23:23,042 - mcp_tools - INFO - ✅ RAG 데이터베이스 초기화 성공: kars_test
2025-09-12 18:23:23,042 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:23:23,042 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:23:23,118 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:23:23,118 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:23:23,193 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:23:23,194 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:23:23,256 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:23:23,257 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:23:23,332 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:23:23,332 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
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
2025-09-12 18:23:23,332 - mcp_tools - INFO - 🔍 필터 추출 시작: 'Jeong, Yeeun (191) on behalf of korea_com (191-NPM)가 발신한 메시지를 모두 찾아줘'
2025-09-12 18:23:25,423 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:23:25,424 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:23:25,425 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:23:25,503 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:23:25,503 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:23:25,580 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:23:25,580 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:23:25,654 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:23:25,654 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:23:25,715 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:23:25,716 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:23:25,716 - mcp_tools - INFO - ✅ from_email 필드 정확한 매칭 발견: 'Jeong, Yeeun (191) on behalf of korea_com (191-NPM)'
2025-09-12 18:23:25,716 - mcp_tools - INFO - ✅ 필터 추출 완료: filter 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email='Jeong, Yeeun (191) on behalf of korea_com (191-NPM)' to_email=None cc=None bcc=None last_author=None extension=None
❌ 필터 추출 실패: 알 수 없는 오류


🧪 테스트 케이스 2: Park, Sep (191) on behalf of korea_com (191-NPM)가 발신한 메시지를 모두 찾아줘
--------------------------------------------------
2025-09-12 18:23:25,716 - mcp_tools - INFO - 🔍 필터 추출 시작: 'Park, Sep (191) on behalf of korea_com (191-NPM)가 발신한 메시지를 모두 찾아줘'
2025-09-12 18:23:27,730 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:23:27,731 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:23:27,731 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:23:27,811 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:23:27,811 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:23:27,875 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:23:27,876 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:23:27,955 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:23:27,956 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:23:28,035 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:23:28,036 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:23:28,036 - mcp_tools - INFO - ✅ from_email 필드 정확한 매칭 발견: 'Park, Sep (191) on behalf of korea_com (191-NPM)'
2025-09-12 18:23:28,036 - mcp_tools - INFO - ✅ 필터 추출 완료: filter 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email='Park, Sep (191) on behalf of korea_com (191-NPM)' to_email=None cc=None bcc=None last_author=None extension=None
❌ 필터 추출 실패: 알 수 없는 오류


🧪 테스트 케이스 3: 세진 김이 보관한 문서들을 모두 찾아줘
--------------------------------------------------
2025-09-12 18:23:28,036 - mcp_tools - INFO - 🔍 필터 추출 시작: '세진 김이 보관한 문서들을 모두 찾아줘'
2025-09-12 18:23:29,622 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:23:29,624 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:23:29,624 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:23:29,703 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:23:29,703 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:23:29,765 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:23:29,765 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:23:29,824 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:23:29,825 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:23:29,886 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:23:29,887 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:23:29,887 - mcp_tools - INFO - ✅ custodian 필드 정확한 매칭 발견: '세진 김'
2025-09-12 18:23:29,887 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian='세진 김' ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
❌ 필터 추출 실패: 알 수 없는 오류


🧪 테스트 케이스 4: Song, Jieun (191)가 최종 작성한 문서들을 모두 찾아줘
--------------------------------------------------
2025-09-12 18:23:29,887 - mcp_tools - INFO - 🔍 필터 추출 시작: 'Song, Jieun (191)가 최종 작성한 문서들을 모두 찾아줘'
2025-09-12 18:23:31,621 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:23:31,622 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:23:31,623 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:23:31,700 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:23:31,700 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:23:31,768 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:23:31,769 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:23:31,848 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:23:31,848 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:23:31,910 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:23:31,910 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:23:31,911 - mcp_tools - INFO - ✅ last_author 필드 정확한 매칭 발견: 'Song, Jieun (191)'
2025-09-12 18:23:31,911 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author='Song, Jieun (191)' extension=None
❌ 필터 추출 실패: 알 수 없는 오류


🧪 테스트 케이스 5: Ju, Hyeyeon (191-Extern-MBK)가 최종 작성한 문서들을 모두 찾아줘
--------------------------------------------------
2025-09-12 18:23:31,911 - mcp_tools - INFO - 🔍 필터 추출 시작: 'Ju, Hyeyeon (191-Extern-MBK)가 최종 작성한 문서들을 모두 찾아줘'
2025-09-12 18:23:32,916 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:23:32,918 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:23:32,918 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:23:32,993 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:23:32,993 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:23:33,063 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:23:33,063 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:23:33,141 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:23:33,141 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:23:33,203 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:23:33,203 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:23:34,515 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:23:34,516 - mcp_tools - INFO - ⚠️ custodian 필드 유사도 부족: 'Ju, Hyeyeon (191-Extern-MBK)' (최고 유사도: 0.00)
2025-09-12 18:23:34,516 - mcp_tools - INFO - ✅ last_author 필드 정확한 매칭 발견: 'Ju, Hyeyeon (191-Extern-MBK)'
2025-09-12 18:23:34,517 - mcp_tools - INFO - ✅ 필터 추출 완료: filter 검색, 필터: custodian='Ju, Hyeyeon (191-Extern-MBK)' ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author='Ju, Hyeyeon (191-Extern-MBK)' extension=None
❌ 필터 추출 실패: 알 수 없는 오류


🧪 테스트 케이스 6: Kim, Ji-Hyun (191)가 최종 작성한 문서들을 모두 찾아줘
--------------------------------------------------
2025-09-12 18:23:34,517 - mcp_tools - INFO - 🔍 필터 추출 시작: 'Kim, Ji-Hyun (191)가 최종 작성한 문서들을 모두 찾아줘'
2025-09-12 18:23:36,266 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:23:36,268 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:23:36,268 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:23:36,349 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:23:36,349 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:23:36,424 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:23:36,424 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:23:36,491 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:23:36,491 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:23:36,556 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:23:36,557 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:23:36,557 - mcp_tools - INFO - ✅ last_author 필드 정확한 매칭 발견: 'Kim, Ji-Hyun (191)'
2025-09-12 18:23:36,557 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author='Kim, Ji-Hyun (191)' extension=None
❌ 필터 추출 실패: 알 수 없는 오류


🧪 테스트 케이스 7: Joo, Jaeyool (191)가 최종 작성한 문서들을 모두 찾아줘
--------------------------------------------------
2025-09-12 18:23:36,557 - mcp_tools - INFO - 🔍 필터 추출 시작: 'Joo, Jaeyool (191)가 최종 작성한 문서들을 모두 찾아줘'
2025-09-12 18:23:38,451 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:23:38,452 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:23:38,453 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:23:38,528 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:23:38,528 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:23:38,595 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:23:38,595 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:23:38,671 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:23:38,672 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:23:38,753 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:23:38,754 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:23:38,754 - mcp_tools - INFO - ✅ last_author 필드 정확한 매칭 발견: 'Joo, Jaeyool (191)'
2025-09-12 18:23:38,754 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author='Joo, Jaeyool (191)' extension=None
❌ 필터 추출 실패: 알 수 없는 오류


🧪 테스트 케이스 8: Park, Jaekyung (191)가 최종 작성한 문서들을 모두 찾아줘
--------------------------------------------------
2025-09-12 18:23:38,754 - mcp_tools - INFO - 🔍 필터 추출 시작: 'Park, Jaekyung (191)가 최종 작성한 문서들을 모두 찾아줘'
2025-09-12 18:23:40,645 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:23:40,646 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:23:40,646 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:23:40,728 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:23:40,728 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:23:40,803 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:23:40,803 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:23:40,876 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:23:40,876 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:23:40,941 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:23:40,942 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:23:40,942 - mcp_tools - INFO - ✅ last_author 필드 정확한 매칭 발견: 'Park, Jaekyung (191)'
2025-09-12 18:23:40,943 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author='Park, Jaekyung (191)' extension=None
❌ 필터 추출 실패: 알 수 없는 오류


🧪 테스트 케이스 9: Shim, Ellen (191)가 최종 작성한 문서들을 모두 찾아줘
--------------------------------------------------
2025-09-12 18:23:40,943 - mcp_tools - INFO - 🔍 필터 추출 시작: 'Shim, Ellen (191)가 최종 작성한 문서들을 모두 찾아줘'
2025-09-12 18:23:42,781 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:23:42,782 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:23:42,782 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:23:42,861 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:23:42,861 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:23:42,930 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:23:42,930 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:23:43,005 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:23:43,005 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:23:43,072 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:23:43,072 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:23:43,072 - mcp_tools - INFO - ✅ last_author 필드 정확한 매칭 발견: 'Shim, Ellen (191)'
2025-09-12 18:23:43,073 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author='Shim, Ellen (191)' extension=None
❌ 필터 추출 실패: 알 수 없는 오류


🧪 테스트 케이스 10: msg 확장자 파일들을 모두 찾아줘
--------------------------------------------------
2025-09-12 18:23:43,073 - mcp_tools - INFO - 🔍 필터 추출 시작: 'msg 확장자 파일들을 모두 찾아줘'
2025-09-12 18:23:44,613 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:23:44,615 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:23:44,615 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:23:44,690 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:23:44,690 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:23:44,762 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:23:44,763 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:23:44,846 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:23:44,846 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:23:44,911 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:23:44,911 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:23:44,911 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension='msg'
❌ 필터 추출 실패: 알 수 없는 오류


🧪 테스트 케이스 11: pdf 확장자 파일들을 모두 찾아줘
--------------------------------------------------
2025-09-12 18:23:44,911 - mcp_tools - INFO - 🔍 필터 추출 시작: 'pdf 확장자 파일들을 모두 찾아줘'
2025-09-12 18:23:46,452 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:23:46,454 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:23:46,454 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:23:46,530 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:23:46,531 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:23:46,592 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:23:46,592 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:23:46,654 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:23:46,654 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:23:46,730 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:23:46,730 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:23:46,731 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension='pdf'
❌ 필터 추출 실패: 알 수 없는 오류


🧪 테스트 케이스 12: csv 확장자 파일들을 모두 찾아줘
--------------------------------------------------
2025-09-12 18:23:46,731 - mcp_tools - INFO - 🔍 필터 추출 시작: 'csv 확장자 파일들을 모두 찾아줘'
2025-09-12 18:23:48,272 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:23:48,273 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:23:48,273 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:23:48,351 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:23:48,351 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:23:48,412 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:23:48,412 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:23:48,485 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:23:48,485 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:23:48,548 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:23:48,548 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:23:48,548 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension='.csv'
❌ 필터 추출 실패: 알 수 없는 오류


🧪 테스트 케이스 13: 세진 김이 보관한 msg 파일들을 모두 찾아줘
--------------------------------------------------
2025-09-12 18:23:48,548 - mcp_tools - INFO - 🔍 필터 추출 시작: '세진 김이 보관한 msg 파일들을 모두 찾아줘'
2025-09-12 18:23:48,953 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:23:48,954 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:23:48,954 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:23:49,033 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:23:49,033 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:23:49,124 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:23:49,124 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:23:49,191 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:23:49,191 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:23:49,260 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:23:49,260 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:23:49,260 - mcp_tools - INFO - ✅ custodian 필드 정확한 매칭 발견: '세진 김'
2025-09-12 18:23:49,261 - mcp_tools - INFO - ✅ 필터 추출 완료: filter 검색, 필터: custodian='세진 김' ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension='.msg'
❌ 필터 추출 실패: 알 수 없는 오류


🧪 테스트 케이스 14: Song, Jieun (191)가 최종 작성한 pdf 파일들을 모두 찾아줘
--------------------------------------------------
2025-09-12 18:23:49,261 - mcp_tools - INFO - 🔍 필터 추출 시작: 'Song, Jieun (191)가 최종 작성한 pdf 파일들을 모두 찾아줘'
2025-09-12 18:23:51,025 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:23:51,027 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:23:51,027 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:23:51,104 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:23:51,104 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:23:51,179 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:23:51,180 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:23:51,259 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:23:51,260 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:23:51,327 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:23:51,328 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:23:51,328 - mcp_tools - INFO - ✅ last_author 필드 정확한 매칭 발견: 'Song, Jieun (191)'
2025-09-12 18:23:51,328 - mcp_tools - INFO - ✅ 필터 추출 완료: filter 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author='Song, Jieun (191)' extension='.pdf'
❌ 필터 추출 실패: 알 수 없는 오류


🧪 테스트 케이스 15: Ju, Hyeyeon (191-Extern-MBK)가 최종 작성한 msg 파일들을 모두 찾아줘
--------------------------------------------------
2025-09-12 18:23:51,328 - mcp_tools - INFO - 🔍 필터 추출 시작: 'Ju, Hyeyeon (191-Extern-MBK)가 최종 작성한 msg 파일들을 모두 찾아줘'
2025-09-12 18:23:53,664 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:23:53,665 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:23:53,665 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:23:53,736 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:23:53,736 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:23:53,796 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:23:53,796 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:23:53,857 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:23:53,857 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:23:53,917 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:23:53,918 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:23:55,581 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:23:55,582 - mcp_tools - INFO - ⚠️ custodian 필드 유사도 부족: 'Ju, Hyeyeon (191-Extern-MBK)' (최고 유사도: 0.00)
2025-09-12 18:23:55,582 - mcp_tools - INFO - ✅ last_author 필드 정확한 매칭 발견: 'Ju, Hyeyeon (191-Extern-MBK)'
2025-09-12 18:23:55,583 - mcp_tools - INFO - ✅ 필터 추출 완료: filter 검색, 필터: custodian='Ju, Hyeyeon (191-Extern-MBK)' ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author='Ju, Hyeyeon (191-Extern-MBK)' extension='msg'
❌ 필터 추출 실패: 알 수 없는 오류

✅ 필터 기반 검색 테스트 완료!
/raid1/workspace/kars-agent/weaviate-mcp/tmp_sungwon_chae/test_extract_value_tool_modified.py:311: ResourceWarning: unclosed <socket.socket fd=10, family=2, type=1, proto=6, laddr=('10.10.150.195', 34868), raddr=('10.10.150.195', 8080)>
  await test_filter_based_search()
ResourceWarning: Enable tracemalloc to get the object allocation traceback

🎉 모든 테스트 완료!
(.venv) min.choi10@wss-195:/raid1/workspace/kars-agent/weaviate-mcp/tmp_sungwon_chae$ 
