(.venv) min.choi10@wss-195:/raid1/workspace/kars-agent/weaviate-mcp/tmp_sungwon_chae$ python test_extract_value_tool_modified.py 
🚀 Weaviate MCP 도구 테스트 시작

2025-09-12 18:49:38,491 - mcp_tools - INFO - Weaviate MCP 도구 초기화 완료
2025-09-12 18:49:38,904 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
Test Query Response:  ChatCompletion(id='chatcmpl-51b43ddd817a4e44a0df024bec1938b6', choices=[Choice(finish_reason='length', index=0, logprobs=None, message=ChatCompletionMessage(content='<think>\nOkay, the user said "hi!".', refusal=None, role='assistant', annotations=None, audio=None, function_call=None, tool_calls=[], reasoning_content=None), stop_reason=None)], created=1757670584, model='/data/models_ckpt/Qwen3-32B', object='chat.completion', service_tier=None, system_fingerprint=None, usage=CompletionUsage(completion_tokens=10, prompt_tokens=10, total_tokens=20, completion_tokens_details=None, prompt_tokens_details=None), prompt_logprobs=None)
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
2025-09-12 18:49:38,922 - mcp_tools - INFO - 🔍 필터 추출 시작: 'Jeong, Yeeun (191) on behalf of korea_com (191-NPM)가 발신한 메시지를 모두 찾아줘'
2025-09-12 18:49:40,997 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:49:40,999 - kars_db - INFO - 🚀 RAG 벡터 데이터베이스 초기화 시작
2025-09-12 18:49:40,999 - simple_manager - INFO - Weaviate URL: http://10.10.150.195:8080
2025-09-12 18:49:40,999 - simple_manager - INFO - OpenAI Base URL: http://10.10.190.1:8125
2025-09-12 18:49:40,999 - kars_db - INFO - ✅ VectorDB 매니저 초기화 완료
2025-09-12 18:49:41,046 - httpx - INFO - HTTP Request: GET http://10.10.190.1:8125/v1/models "HTTP/1.1 200 OK"
2025-09-12 18:49:41,047 - weaviate_db - INFO - ✅ vLLM 서버에서 모델명 가져옴: /data/models_ckpt/bge-m3
2025-09-12 18:49:41,060 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8125/v1/embeddings "HTTP/1.1 200 OK"
2025-09-12 18:49:41,064 - weaviate_db - INFO - ✅ 샘플 임베딩 생성 성공 (차원: 1024)
2025-09-12 18:49:41,103 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/.well-known/openid-configuration "HTTP/1.1 404 Not Found"
2025-09-12 18:49:41,129 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/meta "HTTP/1.1 200 OK"
2025-09-12 18:49:43,164 - weaviate_db - INFO - ✅ Weaviate 클라이언트 연결 성공: http://10.10.150.195:8080
2025-09-12 18:49:43,165 - weaviate_db - INFO - 📡 OpenAI Base URL (Python용): http://10.10.190.1:8125/v1
2025-09-12 18:49:43,165 - weaviate_db - INFO - 📡 OpenAI Base URL (Weaviate용): http://10.10.190.1:8125
2025-09-12 18:49:43,165 - weaviate_db - INFO - 🔧 동적 모델명: /data/models_ckpt/bge-m3
2025-09-12 18:49:43,165 - simple_manager - INFO - DB 연결 초기화 완료
2025-09-12 18:49:43,168 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema "HTTP/1.1 200 OK"
2025-09-12 18:49:43,174 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema/DocumentChunk "HTTP/1.1 200 OK"
2025-09-12 18:49:43,181 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema/EnronDocument "HTTP/1.1 200 OK"
2025-09-12 18:49:43,182 - weaviate_db - INFO - 스키마 조회 완료: 2개 클래스
2025-09-12 18:49:43,182 - simple_manager - WARNING - 클래스 매핑 파일이 없습니다. 기본 규칙을 사용합니다.
2025-09-12 18:49:43,182 - simple_manager - INFO - 기존 클래스 등록: chunk_db -> DocumentChunk
2025-09-12 18:49:43,182 - simple_manager - INFO - 기존 클래스 등록: enron_db -> EnronDocument
2025-09-12 18:49:43,182 - simple_manager - INFO - 총 2개 DB에 클래스 등록 완료
2025-09-12 18:49:43,183 - simple_manager - INFO -   chunk_db: ['DocumentChunk']
2025-09-12 18:49:43,183 - simple_manager - INFO -   enron_db: ['EnronDocument']
2025-09-12 18:49:43,186 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema "HTTP/1.1 200 OK"
2025-09-12 18:49:43,189 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema/DocumentChunk "HTTP/1.1 200 OK"
2025-09-12 18:49:43,192 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema/EnronDocument "HTTP/1.1 200 OK"
2025-09-12 18:49:43,193 - weaviate_db - INFO - 스키마 조회 완료: 2개 클래스
2025-09-12 18:49:43,193 - kars_db - INFO - 📊 사용 가능한 클래스들: ['DocumentChunk', 'EnronDocument']
2025-09-12 18:49:43,193 - kars_db - INFO - ✅ 사용할 클래스명: DocumentChunk
2025-09-12 18:49:43,193 - mcp_tools - INFO - ✅ RAG 데이터베이스 초기화 성공: kars_test
2025-09-12 18:49:43,193 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:49:43,193 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:49:43,282 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:49:43,282 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:49:43,359 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:49:43,359 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:49:43,444 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:49:43,445 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:49:43,520 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:49:43,520 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:49:43,520 - mcp_tools - INFO - ✅ from_email 필드 정확한 매칭 발견: 'Jeong, Yeeun (191) on behalf of korea_com (191-NPM)'
2025-09-12 18:49:43,521 - mcp_tools - INFO - ✅ 필터 추출 완료: filter 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email='Jeong, Yeeun (191) on behalf of korea_com (191-NPM)' to_email=None cc=None bcc=None last_author=None extension=None
📊 추출된 필터:
  - custodian: None
  - ori_file_name: None
  - s_created_date: None
  - sent_date: None
  - from_email: Jeong, Yeeun (191) on behalf of korea_com (191-NPM)
  - to_email: None
  - cc: None
  - bcc: None
  - last_author: None
  - extension: None
🔍 검색 방식: filter
💭 판단 근거: 질의에서 구체적인 식별자 'from_email: Jeong, Yeeun (191) on behalf of korea_com (191-NPM)'를 찾았습니다. 조건 필터링을 사용합니다.
📋 검색에 사용할 필터: {'from_email': 'Jeong, Yeeun (191) on behalf of korea_com (191-NPM)'}
2025-09-12 18:49:43,521 - mcp_tools - INFO - 🔍 필터 검색 실행: class_name=DocumentChunk, limit=5, filters={'from_email': 'Jeong, Yeeun (191) on behalf of korea_com (191-NPM)'}
2025-09-12 18:49:43,521 - kars_db - INFO - 필터 검색 시작: class_name=DocumentChunk, limit=5, filters={'from_email': 'Jeong, Yeeun (191) on behalf of korea_com (191-NPM)'}
2025-09-12 18:49:43,521 - kars_db - INFO - 필터와 함께 검색: {'from_email': 'Jeong, Yeeun (191) on behalf of korea_com (191-NPM)'}
2025-09-12 18:49:43,526 - kars_db - INFO - ✅ 필터 검색 완료: 5개 결과 반환
📊 검색 결과:
  - 성공 여부: True
  - 총 결과 수: 5개
  - 검색 방식: N/A
  - 사용된 필터: {'from_email': 'Jeong, Yeeun (191) on behalf of korea_com (191-NPM)'}

📄 검색된 문서들:
  1. 문서 ID: f17cfc84-1149-4cc7-b51b-230afad00ce4
     파일명: 탑기어_MERCEDES-BENZ GLE 450 4MATIC_6월호.jpg
     보관자: 세진 김
     생성일: 1900-01-01 00:00:00+00:00
     발송일: 2021-06-22 10:30:00+00:00
     발신자: Jeong, Yeeun (191) on behalf of korea_com (191-NPM)
     수신자: NaN
     확장자: jpg
     내용 미리보기:    璹一一 


 一一刪 
        來b 楓 



            揭 


















































  MERCEDES-BENZ                        야기 시작에 앞서 메롸 뎨스＝벤츠에거r 

  GLE 450 4MATIC                   Ul'...
     최종 작성자: NaN

  2. 문서 ID: 4eb27e66-e850-4b76-974e-b3da7ad1b6d0
     파일명: 탑기어_MERCEDES-BENZ GLE 450 4MATIC_6월호.jpg
     보관자: 세진 김
     생성일: 1900-01-01 00:00:00+00:00
     발송일: 2021-06-22 10:30:00+00:00
     발신자: Jeong, Yeeun (191) on behalf of korea_com (191-NPM)
     수신자: NaN
     확장자: jpg
     내용 미리보기:    璹一一 


 一一刪 
        來b 楓 



            揭 


















































  MERCEDES-BENZ                        야기 시작에 앞서 메롸 뎨스＝벤츠에거r 

  GLE 450 4MATIC                   Ul'...
     최종 작성자: NaN

  3. 문서 ID: 51dbaae4-acee-4edb-8419-4c0953a161df
     파일명: 아시아투데이_사회공헌도 '으뜸'… 6년간 누적기부 300억_기업 13면_20210428.jpg
     보관자: 세진 김
     생성일: 1900-01-01 00:00:00+00:00
     발송일: 2021-04-28 10:27:05+00:00
     발신자: Jeong, Yeeun (191) on behalf of korea_com (191-NPM)
     수신자: NaN
     확장자: jpg
     내용 미리보기:                                                          2021년 04월 28일 
아시아투데이                                                     13면 （기업） 



 사회공헌도 ‘으뜸’…6년간 누적기부 300억 








             ○ 


  ...
     최종 작성자: NaN

  4. 문서 ID: dcbea691-f247-46d0-b101-224673910d5e
     파일명: 채널A_달리다 시동 꺼지는데…벤츠 측 “도울 방법 없어요”_20210423.jpg
     보관자: 세진 김
     생성일: 1900-01-01 00:00:00+00:00
     발송일: 2021-04-26 10:38:32+00:00
     발신자: Jeong, Yeeun (191) on behalf of korea_com (191-NPM)
     수신자: NaN
     확장자: jpg
     내용 미리보기:                   4개월동안여러ㅊ뻬 
                   주행중사동꺼져 
                    서비스센터 
                     수리10회 
                  수리 마차고냐온 지 
    孔｝19크2월춥고    5분 맨게시동꺼지기도 
   새키월중고로구매 


            ...
     최종 작성자: NaN

  5. 문서 ID: 975b92e9-f188-4f3a-a01c-22657f52e3d4
     파일명: 카앤테크_The new Mercedes-AMG GT R_5월호.jpg
     보관자: 세진 김
     생성일: 1900-01-01 00:00:00+00:00
     발송일: 2021-05-26 10:43:55+00:00
     발신자: Jeong, Yeeun (191) on behalf of korea_com (191-NPM)
     수신자: NaN
     확장자: jpg
     내용 미리보기: 레이싱 DNA와 모터스포츠 가술 빈뼝된 ㅅㅉㅊ카  
The new Mercedes-AMG GT R  
메르세더1스벤츠 코리아가 지난 4철 레이싱 DNA와 모터스포츠 가슬이 반영된 고甛 스포츠카 더，뉴 머嶋세더．스－AMG CT R(The new  
Me1cedes-AMG CT R）올 국내（게 공식 츌시했다． 메르세데스－AMG CT R은AMG CT 2도어 쿠...
     최종 작성자: NaN


================================================================================

테스트 케이스 2: Park, Sep (191) on behalf of korea_com (191-NPM)가 발신한 메시지를 모두 찾아줘
------------------------------------------------------------
2025-09-12 18:49:43,527 - mcp_tools - INFO - 🔍 필터 추출 시작: 'Park, Sep (191) on behalf of korea_com (191-NPM)가 발신한 메시지를 모두 찾아줘'
2025-09-12 18:49:45,514 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:49:45,516 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:49:45,516 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:49:45,598 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:49:45,598 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:49:45,672 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:49:45,672 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:49:45,744 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:49:45,745 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:49:45,819 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:49:45,820 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:49:45,820 - mcp_tools - INFO - ✅ from_email 필드 정확한 매칭 발견: 'Park, Sep (191) on behalf of korea_com (191-NPM)'
2025-09-12 18:49:45,820 - mcp_tools - INFO - ✅ 필터 추출 완료: filter 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email='Park, Sep (191) on behalf of korea_com (191-NPM)' to_email=None cc=None bcc=None last_author=None extension=None
📊 추출된 필터:
  - custodian: None
  - ori_file_name: None
  - s_created_date: None
  - sent_date: None
  - from_email: Park, Sep (191) on behalf of korea_com (191-NPM)
  - to_email: None
  - cc: None
  - bcc: None
  - last_author: None
  - extension: None
🔍 검색 방식: filter
💭 판단 근거: 질의에서 구체적인 식별자 'from_email: Park, Sep (191) on behalf of korea_com (191-NPM)'를 찾았습니다. 조건 필터링을 사용합니다.
📋 검색에 사용할 필터: {'from_email': 'Park, Sep (191) on behalf of korea_com (191-NPM)'}
2025-09-12 18:49:45,820 - mcp_tools - INFO - 🔍 필터 검색 실행: class_name=DocumentChunk, limit=5, filters={'from_email': 'Park, Sep (191) on behalf of korea_com (191-NPM)'}
2025-09-12 18:49:45,820 - kars_db - INFO - 필터 검색 시작: class_name=DocumentChunk, limit=5, filters={'from_email': 'Park, Sep (191) on behalf of korea_com (191-NPM)'}
2025-09-12 18:49:45,820 - kars_db - INFO - 필터와 함께 검색: {'from_email': 'Park, Sep (191) on behalf of korea_com (191-NPM)'}
2025-09-12 18:49:45,834 - kars_db - INFO - ✅ 필터 검색 완료: 5개 결과 반환
📊 검색 결과:
  - 성공 여부: True
  - 총 결과 수: 5개
  - 검색 방식: N/A
  - 사용된 필터: {'from_email': 'Park, Sep (191) on behalf of korea_com (191-NPM)'}

📄 검색된 문서들:
  1. 문서 ID: 908c3e0b-91d0-4411-9a0e-6e896902ca24
     파일명: [매일경제] 1회 충전으로 400km… 어딜가도 폼나는 럭셔리 전기 SUV_자동차 B02_20230719.jpg
     보관자: 세진 김
     생성일: 1900-01-01 00:00:00+00:00
     발송일: 2023-07-19 10:32:08+00:00
     발신자: Park, Sep (191) on behalf of korea_com (191-NPM)
     수신자: NaN
     확장자: jpg
     내용 미리보기:                                                                                                                                                                   2023i 07뭘 1咆 
                       ...
     최종 작성자: NaN

  2. 문서 ID: a5848f74-f104-4aa9-bd93-b63d133c693f
     파일명: [매일경제] 1회 충전으로 400km… 어딜가도 폼나는 럭셔리 전기 SUV_자동차 B02_20230719.jpg
     보관자: 세진 김
     생성일: 1900-01-01 00:00:00+00:00
     발송일: 2023-07-19 10:32:08+00:00
     발신자: Park, Sep (191) on behalf of korea_com (191-NPM)
     수신자: NaN
     확장자: jpg
     내용 미리보기:                                                                                                                                                                   2023i 07뭘 1咆 
                       ...
     최종 작성자: NaN

  3. 문서 ID: 888fa4e7-5397-49a0-af46-aa0e7363858f
     파일명: [행복이 가득한 집] CAR NEWS_메르세데스-벤츠, 메르세데스-AMG EQE_6월호.jpg
     보관자: 세진 김
     생성일: 1900-01-01 00:00:00+00:00
     발송일: 2023-06-29 11:12:24+00:00
     발신자: Park, Sep (191) on behalf of korea_com (191-NPM)
     수신자: NaN
     확장자: jpg
     내용 미리보기:                                                     1 볼보． 썬라이크 LED 탑채 뷴보가 업계 
                                                    최초로 자연광（〕뀀 가까운 빛읖 내는 혁신적 조명 
                                        ...
     최종 작성자: NaN

  4. 문서 ID: f9b474d0-7c7d-42bb-91ff-be3a1df9ba83
     파일명: [행복이 가득한 집] CAR NEWS_메르세데스-벤츠, 메르세데스-AMG EQE_6월호.jpg
     보관자: 세진 김
     생성일: 1900-01-01 00:00:00+00:00
     발송일: 2023-06-29 11:12:24+00:00
     발신자: Park, Sep (191) on behalf of korea_com (191-NPM)
     수신자: NaN
     확장자: jpg
     내용 미리보기:                                                     1 볼보． 썬라이크 LED 탑채 뷴보가 업계 
                                                    최초로 자연광（〕뀀 가까운 빛읖 내는 혁신적 조명 
                                        ...
     최종 작성자: NaN

  5. 문서 ID: 0bc582c6-b2ac-4bd2-a515-68a6370bf1e9
     파일명: [한국경제] 메르세데스-벤츠, 베스트 모델 ‘더 뉴 GLC·더 뉴 EQE’로 SUV 시장 공략_자동차 B05_20230628.jpg
     보관자: 세진 김
     생성일: 1900-01-01 00:00:00+00:00
     발송일: 2023-06-28 11:16:44+00:00
     발신자: Park, Sep (191) on behalf of korea_com (191-NPM)
     수신자: NaN
     확장자: jpg
     내용 미리보기:                                                                                                                                                                 2c23년 m· 2曜 
한국경체                      ...
     최종 작성자: NaN


================================================================================

테스트 케이스 3: 세진 김이 보관한 문서들을 모두 찾아줘
------------------------------------------------------------
2025-09-12 18:49:45,835 - mcp_tools - INFO - 🔍 필터 추출 시작: '세진 김이 보관한 문서들을 모두 찾아줘'
2025-09-12 18:49:47,404 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:49:47,405 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:49:47,405 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:49:47,487 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:49:47,487 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:49:47,581 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:49:47,581 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:49:47,650 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:49:47,650 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:49:47,716 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:49:47,717 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:49:47,718 - mcp_tools - INFO - ✅ custodian 필드 정확한 매칭 발견: '세진 김'
2025-09-12 18:49:47,718 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian='세진 김' ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
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
2025-09-12 18:49:47,718 - mcp_tools - INFO - 🔍 필터 검색 실행: class_name=DocumentChunk, limit=5, filters={'custodian': '세진 김'}
2025-09-12 18:49:47,718 - kars_db - INFO - 필터 검색 시작: class_name=DocumentChunk, limit=5, filters={'custodian': '세진 김'}
2025-09-12 18:49:47,718 - kars_db - INFO - 필터와 함께 검색: {'custodian': '세진 김'}
2025-09-12 18:49:47,726 - kars_db - INFO - ✅ 필터 검색 완료: 5개 결과 반환
📊 검색 결과:
  - 성공 여부: True
  - 총 결과 수: 5개
  - 검색 방식: N/A
  - 사용된 필터: {'custodian': '세진 김'}

📄 검색된 문서들:
  1. 문서 ID: 84e3b894-4f16-4b8d-bf39-5bbcd95837b2
     파일명: One Team One Voice_20230327.csv
     보관자: 세진 김
     생성일: 1900-01-01 00:00:00+00:00
     발송일: 1900-01-01 00:00:00+00:00
     발신자: NaN
     수신자: NaN
     확장자: csv
     내용 미리보기: "*ID","*docNo","상태","등록자","딜러사","연락처","고객명","직업","연락처","차대번호","차량번호","모델/연식","등록일자","운행거리","불만내용","세부내용","세부내용","세부내용","세부내용","세부내용","기타","불만정도","요구사항","특이사항","정비이력","취재여부","보도예정","취재내용","MBK 지원 요청",...
     최종 작성자: NaN

  2. 문서 ID: 6a1eca77-af00-4be9-96d6-dc28a1a68b7a
     파일명: One Team One Voice_20230327.csv
     보관자: 세진 김
     생성일: 1900-01-01 00:00:00+00:00
     발송일: 1900-01-01 00:00:00+00:00
     발신자: NaN
     수신자: NaN
     확장자: csv
     내용 미리보기: "*ID","*docNo","상태","등록자","딜러사","연락처","고객명","직업","연락처","차대번호","차량번호","모델/연식","등록일자","운행거리","불만내용","세부내용","세부내용","세부내용","세부내용","세부내용","기타","불만정도","요구사항","특이사항","정비이력","취재여부","보도예정","취재내용","MBK 지원 요청",...
     최종 작성자: NaN

  3. 문서 ID: 9e25d34e-9fd9-4a4e-a966-3a4abed89cb4
     파일명: One Team One Voice_20230327.csv
     보관자: 세진 김
     생성일: 1900-01-01 00:00:00+00:00
     발송일: 1900-01-01 00:00:00+00:00
     발신자: NaN
     수신자: NaN
     확장자: csv
     내용 미리보기: "*ID","*docNo","상태","등록자","딜러사","연락처","고객명","직업","연락처","차대번호","차량번호","모델/연식","등록일자","운행거리","불만내용","세부내용","세부내용","세부내용","세부내용","세부내용","기타","불만정도","요구사항","특이사항","정비이력","취재여부","보도예정","취재내용","MBK 지원 요청",...
     최종 작성자: NaN

  4. 문서 ID: ee730a17-2b97-4d51-a901-99d74fd56e49
     파일명: One Team One Voice_20230327.csv
     보관자: 세진 김
     생성일: 1900-01-01 00:00:00+00:00
     발송일: 1900-01-01 00:00:00+00:00
     발신자: NaN
     수신자: NaN
     확장자: csv
     내용 미리보기: "*ID","*docNo","상태","등록자","딜러사","연락처","고객명","직업","연락처","차대번호","차량번호","모델/연식","등록일자","운행거리","불만내용","세부내용","세부내용","세부내용","세부내용","세부내용","기타","불만정도","요구사항","특이사항","정비이력","취재여부","보도예정","취재내용","MBK 지원 요청",...
     최종 작성자: NaN

  5. 문서 ID: 637074c2-8b6f-4c24-895f-256e2139ae14
     파일명: One Team One Voice_20230327.csv
     보관자: 세진 김
     생성일: 1900-01-01 00:00:00+00:00
     발송일: 1900-01-01 00:00:00+00:00
     발신자: NaN
     수신자: NaN
     확장자: csv
     내용 미리보기: "*ID","*docNo","상태","등록자","딜러사","연락처","고객명","직업","연락처","차대번호","차량번호","모델/연식","등록일자","운행거리","불만내용","세부내용","세부내용","세부내용","세부내용","세부내용","기타","불만정도","요구사항","특이사항","정비이력","취재여부","보도예정","취재내용","MBK 지원 요청",...
     최종 작성자: NaN


================================================================================

테스트 케이스 4: Song, Jieun (191)가 최종 작성한 문서들을 모두 찾아줘
------------------------------------------------------------
2025-09-12 18:49:47,727 - mcp_tools - INFO - 🔍 필터 추출 시작: 'Song, Jieun (191)가 최종 작성한 문서들을 모두 찾아줘'
2025-09-12 18:49:49,442 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:49:49,443 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:49:49,444 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:49:49,520 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:49:49,520 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:49:49,588 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:49:49,588 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:49:49,649 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:49:49,649 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:49:49,720 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:49:49,720 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:49:49,720 - mcp_tools - INFO - ✅ last_author 필드 정확한 매칭 발견: 'Song, Jieun (191)'
2025-09-12 18:49:49,721 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author='Song, Jieun (191)' extension=None
📊 추출된 필터:
  - custodian: None
  - ori_file_name: None
  - s_created_date: None
  - sent_date: None
  - from_email: None
  - to_email: None
  - cc: None
  - bcc: None
  - last_author: Song, Jieun (191)
  - extension: None
🔍 검색 방식: similarity
💭 판단 근거: 질의에서 구체적인 필터 정보를 찾았지만 단일 필터이므로 유사도 기반 검색을 사용합니다.
📋 검색에 사용할 필터: {'last_author': 'Song, Jieun (191)'}
2025-09-12 18:49:49,721 - mcp_tools - INFO - 🔍 필터 검색 실행: class_name=DocumentChunk, limit=5, filters={'last_author': 'Song, Jieun (191)'}
2025-09-12 18:49:49,721 - kars_db - INFO - 필터 검색 시작: class_name=DocumentChunk, limit=5, filters={'last_author': 'Song, Jieun (191)'}
2025-09-12 18:49:49,721 - kars_db - INFO - 필터와 함께 검색: {'last_author': 'Song, Jieun (191)'}
2025-09-12 18:49:49,728 - kars_db - INFO - ✅ 필터 검색 완료: 5개 결과 반환
📊 검색 결과:
  - 성공 여부: True
  - 총 결과 수: 5개
  - 검색 방식: N/A
  - 사용된 필터: {'last_author': 'Song, Jieun (191)'}

📄 검색된 문서들:
  1. 문서 ID: 1bf89f2d-9c66-4a92-a304-13fc37ae8ae5
     파일명: AMG TecDay E Performance_KO_revised_v2.docx
     보관자: 세진 김
     생성일: 2021-03-24 16:08:00+00:00
     발송일: 1900-01-01 00:00:00+00:00
     발신자: NaN
     수신자: NaN
     확장자: docx
     내용 미리보기: Philipp Schiemer

Mercedes-AMG TecDay "Future of Driving Performance"
Strategy (Powertrain Electrification)

February 2021
Press briefing
Location: Stuttgart Trade Fair Centre

Language: English

Sta...
     최종 작성자: Song, Jieun (191)

  2. 문서 ID: 58568cc9-16bb-420b-9cbc-1acfca75d0a6
     파일명: AMG TecDay E Performance_KO_revised_v2.docx
     보관자: 세진 김
     생성일: 2021-03-24 16:08:00+00:00
     발송일: 1900-01-01 00:00:00+00:00
     발신자: NaN
     수신자: NaN
     확장자: docx
     내용 미리보기: Philipp Schiemer

Mercedes-AMG TecDay "Future of Driving Performance"
Strategy (Powertrain Electrification)

February 2021
Press briefing
Location: Stuttgart Trade Fair Centre

Language: English

Sta...
     최종 작성자: Song, Jieun (191)

  3. 문서 ID: c15c5dd3-dbbd-4cc3-b962-f0855f4c6917
     파일명: AMG TecDay E Performance_KO_revised_v2.docx
     보관자: 세진 김
     생성일: 2021-03-24 16:08:00+00:00
     발송일: 1900-01-01 00:00:00+00:00
     발신자: NaN
     수신자: NaN
     확장자: docx
     내용 미리보기: Philipp Schiemer

Mercedes-AMG TecDay "Future of Driving Performance"
Strategy (Powertrain Electrification)

February 2021
Press briefing
Location: Stuttgart Trade Fair Centre

Language: English

Sta...
     최종 작성자: Song, Jieun (191)

  4. 문서 ID: 101be7ba-c443-4e9f-8953-5aa4708abde3
     파일명: AMG TecDay E Performance_KO_revised_v2.docx
     보관자: 세진 김
     생성일: 2021-03-24 16:08:00+00:00
     발송일: 1900-01-01 00:00:00+00:00
     발신자: NaN
     수신자: NaN
     확장자: docx
     내용 미리보기: Philipp Schiemer

Mercedes-AMG TecDay "Future of Driving Performance"
Strategy (Powertrain Electrification)

February 2021
Press briefing
Location: Stuttgart Trade Fair Centre

Language: English

Sta...
     최종 작성자: Song, Jieun (191)

  5. 문서 ID: 89e38f95-4e5d-48d8-8148-75eb19007473
     파일명: AMG TecDay E Performance_KO_revised_v2.docx
     보관자: 세진 김
     생성일: 2021-03-24 16:08:00+00:00
     발송일: 1900-01-01 00:00:00+00:00
     발신자: NaN
     수신자: NaN
     확장자: docx
     내용 미리보기: Philipp Schiemer

Mercedes-AMG TecDay "Future of Driving Performance"
Strategy (Powertrain Electrification)

February 2021
Press briefing
Location: Stuttgart Trade Fair Centre

Language: English

Sta...
     최종 작성자: Song, Jieun (191)


================================================================================

테스트 케이스 5: Ju, Hyeyeon (191-Extern-MBK)가 최종 작성한 문서들을 모두 찾아줘
------------------------------------------------------------
2025-09-12 18:49:49,729 - mcp_tools - INFO - 🔍 필터 추출 시작: 'Ju, Hyeyeon (191-Extern-MBK)가 최종 작성한 문서들을 모두 찾아줘'
2025-09-12 18:49:50,723 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:49:50,725 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:49:50,725 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:49:50,804 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:49:50,805 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:49:50,874 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:49:50,875 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:49:50,936 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:49:50,937 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:49:51,007 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:49:51,007 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:49:52,504 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:49:52,506 - mcp_tools - INFO - ⚠️ custodian 필드 유사도 부족: 'Ju, Hyeyeon (191-Extern-MBK)' (최고 유사도: 0.00)
2025-09-12 18:49:52,506 - mcp_tools - INFO - ✅ last_author 필드 정확한 매칭 발견: 'Ju, Hyeyeon (191-Extern-MBK)'
2025-09-12 18:49:52,506 - mcp_tools - INFO - ✅ 필터 추출 완료: filter 검색, 필터: custodian='Ju, Hyeyeon (191-Extern-MBK)' ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author='Ju, Hyeyeon (191-Extern-MBK)' extension=None
📊 추출된 필터:
  - custodian: Ju, Hyeyeon (191-Extern-MBK)
  - ori_file_name: None
  - s_created_date: None
  - sent_date: None
  - from_email: None
  - to_email: None
  - cc: None
  - bcc: None
  - last_author: Ju, Hyeyeon (191-Extern-MBK)
  - extension: None
🔍 검색 방식: filter
💭 판단 근거: 질의에서 2개의 구체적인 필터 정보를 찾았습니다: ['custodian', 'last_author']. 조건 필터링을 사용합니다.
📋 검색에 사용할 필터: {'custodian': 'Ju, Hyeyeon (191-Extern-MBK)', 'last_author': 'Ju, Hyeyeon (191-Extern-MBK)'}
2025-09-12 18:49:52,507 - mcp_tools - INFO - 🔍 필터 검색 실행: class_name=DocumentChunk, limit=5, filters={'custodian': 'Ju, Hyeyeon (191-Extern-MBK)', 'last_author': 'Ju, Hyeyeon (191-Extern-MBK)'}
2025-09-12 18:49:52,507 - kars_db - INFO - 필터 검색 시작: class_name=DocumentChunk, limit=5, filters={'custodian': 'Ju, Hyeyeon (191-Extern-MBK)', 'last_author': 'Ju, Hyeyeon (191-Extern-MBK)'}
2025-09-12 18:49:52,507 - kars_db - INFO - 필터와 함께 검색: {'custodian': 'Ju, Hyeyeon (191-Extern-MBK)', 'last_author': 'Ju, Hyeyeon (191-Extern-MBK)'}
2025-09-12 18:49:52,510 - kars_db - INFO - ✅ 필터 검색 완료: 0개 결과 반환
📊 검색 결과:
  - 성공 여부: True
  - 총 결과 수: 0개
  - 검색 방식: N/A
  - 사용된 필터: {'custodian': 'Ju, Hyeyeon (191-Extern-MBK)', 'last_author': 'Ju, Hyeyeon (191-Extern-MBK)'}
  📭 검색 결과가 없습니다.

================================================================================

테스트 케이스 6: Kim, Ji-Hyun (191)가 최종 작성한 문서들을 모두 찾아줘
------------------------------------------------------------
2025-09-12 18:49:52,510 - mcp_tools - INFO - 🔍 필터 추출 시작: 'Kim, Ji-Hyun (191)가 최종 작성한 문서들을 모두 찾아줘'
2025-09-12 18:49:54,246 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:49:54,248 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:49:54,248 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:49:54,328 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:49:54,328 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:49:54,399 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:49:54,399 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:49:54,463 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:49:54,463 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:49:54,538 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:49:54,538 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:49:54,538 - mcp_tools - INFO - ✅ last_author 필드 정확한 매칭 발견: 'Kim, Ji-Hyun (191)'
2025-09-12 18:49:54,539 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author='Kim, Ji-Hyun (191)' extension=None
📊 추출된 필터:
  - custodian: None
  - ori_file_name: None
  - s_created_date: None
  - sent_date: None
  - from_email: None
  - to_email: None
  - cc: None
  - bcc: None
  - last_author: Kim, Ji-Hyun (191)
  - extension: None
🔍 검색 방식: similarity
💭 판단 근거: 질의에서 구체적인 필터 정보를 찾았지만 단일 필터이므로 유사도 기반 검색을 사용합니다.
📋 검색에 사용할 필터: {'last_author': 'Kim, Ji-Hyun (191)'}
2025-09-12 18:49:54,539 - mcp_tools - INFO - 🔍 필터 검색 실행: class_name=DocumentChunk, limit=5, filters={'last_author': 'Kim, Ji-Hyun (191)'}
2025-09-12 18:49:54,539 - kars_db - INFO - 필터 검색 시작: class_name=DocumentChunk, limit=5, filters={'last_author': 'Kim, Ji-Hyun (191)'}
2025-09-12 18:49:54,539 - kars_db - INFO - 필터와 함께 검색: {'last_author': 'Kim, Ji-Hyun (191)'}
2025-09-12 18:49:54,544 - kars_db - INFO - ✅ 필터 검색 완료: 5개 결과 반환
📊 검색 결과:
  - 성공 여부: True
  - 총 결과 수: 5개
  - 검색 방식: N/A
  - 사용된 필터: {'last_author': 'Kim, Ji-Hyun (191)'}

📄 검색된 문서들:
  1. 문서 ID: 5e0dda4f-2876-40e3-a719-4aefa148be96
     파일명: Expected QAs_2024 W214 Media Conference_20240112_Clean_v2.docx
     보관자: 세진 김
     생성일: 2024-01-12 09:34:00+00:00
     발송일: 1900-01-01 00:00:00+00:00
     발신자: NaN
     수신자: NaN
     확장자: docx
     내용 미리보기: Q&A: Only Critical Questions
[CEO]
(MV) It has been about 4 months since you were appointed to Korea. Please share your views on the Korean market as well as your goals and plans for your term. 
The ...
     최종 작성자: Kim, Ji-Hyun (191)

  2. 문서 ID: 3c7b24ea-1991-4837-8cf3-2142118135c0
     파일명: Expected QA_EQA EQB FL_240516_v2.docx
     보관자: 세진 김
     생성일: 2024-05-16 21:15:00+00:00
     발송일: 1900-01-01 00:00:00+00:00
     발신자: NaN
     수신자: NaN
     확장자: docx
     내용 미리보기: Expected Q&A_EQA/EQB FL Launch & EV Safety

Sales Performance
2024 Jan-Apr MB’s overall EV sales have dropped by almost 30% this year compared to the same period last year. Especially, the EQA and EQ...
     최종 작성자: Kim, Ji-Hyun (191)

  3. 문서 ID: 2bd775f6-5abe-476f-956b-36e9f21bfb8e
     파일명: Expected QA_EQA EQB FL_240516_v2.docx
     보관자: 세진 김
     생성일: 2024-05-16 21:15:00+00:00
     발송일: 1900-01-01 00:00:00+00:00
     발신자: NaN
     수신자: NaN
     확장자: docx
     내용 미리보기: Expected Q&A_EQA/EQB FL Launch & EV Safety

Sales Performance
2024 Jan-Apr MB’s overall EV sales have dropped by almost 30% this year compared to the same period last year. Especially, the EQA and EQ...
     최종 작성자: Kim, Ji-Hyun (191)

  4. 문서 ID: 0ed387d9-0bb5-4181-bff0-27f5e60bef57
     파일명: Expected QA_EQA EQB FL_240516_v2.docx
     보관자: 세진 김
     생성일: 2024-05-16 21:15:00+00:00
     발송일: 1900-01-01 00:00:00+00:00
     발신자: NaN
     수신자: NaN
     확장자: docx
     내용 미리보기: Expected Q&A_EQA/EQB FL Launch & EV Safety

Sales Performance
2024 Jan-Apr MB’s overall EV sales have dropped by almost 30% this year compared to the same period last year. Especially, the EQA and EQ...
     최종 작성자: Kim, Ji-Hyun (191)

  5. 문서 ID: cdffd7e7-5c05-44a3-8812-38ff3e09d4e2
     파일명: Expected QA_EQA EQB FL_240516_v2.docx
     보관자: 세진 김
     생성일: 2024-05-16 21:15:00+00:00
     발송일: 1900-01-01 00:00:00+00:00
     발신자: NaN
     수신자: NaN
     확장자: docx
     내용 미리보기: Expected Q&A_EQA/EQB FL Launch & EV Safety

Sales Performance
2024 Jan-Apr MB’s overall EV sales have dropped by almost 30% this year compared to the same period last year. Especially, the EQA and EQ...
     최종 작성자: Kim, Ji-Hyun (191)


================================================================================

테스트 케이스 7: Joo, Jaeyool (191)가 최종 작성한 문서들을 모두 찾아줘

(중략)

테스트 케이스 18: 4MATIC 사륜구동 시스템 관련 자료
------------------------------------------------------------
2025-09-12 18:50:15,806 - mcp_tools - INFO - 🔍 필터 추출 시작: '4MATIC 사륜구동 시스템 관련 자료'
2025-09-12 18:50:17,315 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:50:17,317 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:50:17,317 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:50:17,388 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:50:17,388 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:50:17,459 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:50:17,459 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:50:17,508 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:50:17,508 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:50:17,578 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:50:17,578 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:50:17,578 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
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
2025-09-12 18:50:17,578 - mcp_tools - INFO - 🔍 단순 RAG 검색 실행: '4MATIC 사륜구동 시스템 관련 자료' (limit: 5)
2025-09-12 18:50:17,579 - kars_db - INFO - 🔍 검색 시작: '4MATIC 사륜구동 시스템 관련 자료' (limit: 5)
2025-09-12 18:50:17,635 - weaviate_db - INFO - 🔍 검색 완료: 5개 결과 (쿼리: '4MATIC 사륜구동 시스템 관련 자료'
2025-09-12 18:50:17,635 - kars_db - INFO - ✅ 검색 완료: 5개 결과 반환
📊 RAG 검색 결과:
  - 성공 여부: True
  - 총 결과 수: 5개
  - 검색 방식: N/A

📄 검색된 문서들:
  1. 문서 ID: dadccea7-c2be-4cfe-b694-9407897e6042
     파일명: 2020 03 31 WVX222 MY20 S-Class (ver.15).pdf
     내용 미리보기:   
 
 
 
 
 
Mercedes-Benz Korea Ltd. 
9 Fl., Seoul Square Building, 
416, Hangang-daero, Jung-Gu, 
Seoul 100-714, Korea 
Phone +82 2 6456-2500 
Fax   +82 2 6456-2501 
www.mercedes-benz.co.kr 
  
 
 ...

  2. 문서 ID: 09f47ac9-a4f0-4e73-aab4-147ed30a7033
     파일명: 2020 03 31 WVX222 MY20 S-Class (ver.15).pdf
     내용 미리보기:   
 
 
 
 
 
Mercedes-Benz Korea Ltd. 
9 Fl., Seoul Square Building, 
416, Hangang-daero, Jung-Gu, 
Seoul 100-714, Korea 
Phone +82 2 6456-2500 
Fax   +82 2 6456-2501 
www.mercedes-benz.co.kr 
  
 
 ...

  3. 문서 ID: 66835a14-be70-40c1-9306-1b37464c8d4a
     파일명: 2020 03 31 WVX222 MY20 S-Class (ver.15).pdf
     내용 미리보기:   
 
 
 
 
 
Mercedes-Benz Korea Ltd. 
9 Fl., Seoul Square Building, 
416, Hangang-daero, Jung-Gu, 
Seoul 100-714, Korea 
Phone +82 2 6456-2500 
Fax   +82 2 6456-2501 
www.mercedes-benz.co.kr 
  
 
 ...

  4. 문서 ID: 26aec033-3016-4d83-a5b3-a3dd04478d7f
     파일명: 2019_10_29_WVX222_MY20_S-Class_(ver.1).pdf
     내용 미리보기:   
 
 
 
 
 
Mercedes-Benz Korea Ltd. 
9 Fl., Seoul Square Building, 
416, Hangang-daero, Jung-Gu, 
Seoul 100-714, Korea 
Phone +82 2 6456-2500 
Fax   +82 2 6456-2501 
www.mercedes-benz.co.kr 
  
 
 ...

  5. 문서 ID: 89f5d419-3caa-48b7-a67c-731c1de0005a
     파일명: 2020 03 31 WVX222 MY20 S-Class (ver.15).pdf
     내용 미리보기:   
 
 
 
 
 
Mercedes-Benz Korea Ltd. 
9 Fl., Seoul Square Building, 
416, Hangang-daero, Jung-Gu, 
Seoul 100-714, Korea 
Phone +82 2 6456-2500 
Fax   +82 2 6456-2501 
www.mercedes-benz.co.kr 
  
 
 ...


================================================================================

테스트 케이스 19: SOCAR와의 카셰어링 협력 관련 자료
------------------------------------------------------------
2025-09-12 18:50:17,636 - mcp_tools - INFO - 🔍 필터 추출 시작: 'SOCAR와의 카셰어링 협력 관련 자료'
2025-09-12 18:50:19,144 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:50:19,145 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:50:19,146 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:50:19,221 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:50:19,221 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:50:19,281 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:50:19,281 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:50:19,345 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:50:19,346 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:50:19,439 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:50:19,439 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:50:19,439 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
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
2025-09-12 18:50:19,440 - mcp_tools - INFO - 🔍 단순 RAG 검색 실행: 'SOCAR와의 카셰어링 협력 관련 자료' (limit: 5)
2025-09-12 18:50:19,440 - kars_db - INFO - 🔍 검색 시작: 'SOCAR와의 카셰어링 협력 관련 자료' (limit: 5)
2025-09-12 18:50:19,484 - weaviate_db - INFO - 🔍 검색 완료: 5개 결과 (쿼리: 'SOCAR와의 카셰어링 협력 관련 자료'
2025-09-12 18:50:19,484 - kars_db - INFO - ✅ 검색 완료: 5개 결과 반환
📊 RAG 검색 결과:
  - 성공 여부: True
  - 총 결과 수: 5개
  - 검색 방식: N/A

📄 검색된 문서들:
  1. 문서 ID: 46b2a513-9392-4a8a-88a3-7c00f24fcfae
     파일명: 2024 08 12 Issue Report_Cheongna Thermal Incident_v12_F.pptx
     내용 미리보기: 


Issue Reportincident in Cheongna, Korea
Mercedes-Benz Korea Communications  
August 12, 2024
Summary of Representative Article – Battery Manufacturer Information
6
[Editorial] Information on EV ba...

  2. 문서 ID: 3774fab8-b8e6-4138-a5c3-e8cbf9310ad3
     파일명: 2024 08 13 Issue Report_Cheongna Thermal Incident_v13 (1).pptx
     내용 미리보기: Summary of Representative Article – Evacuation Status
19
Residents of Cheongna apartment complex are focusing on restoration work(Yonhap News, 2024/08/10)
Nearly 10 days have passed since the EV ther...

  3. 문서 ID: b2678df2-3e9b-4c02-9140-d3ecf1055d50
     파일명: 2024 08 14 Issue Report_Cheongna Thermal Incident_v14.pptx
     내용 미리보기: Summary of Representative Article – Support from SOCAR
19
SOCAR to provide 100 support vehicles to residents affected by recent EV thermal incident in Cheongna(Money Today, 2024/08/12)
Car sharing pl...

  4. 문서 ID: 812cfd8c-c12d-4ddc-b134-154024f0f710
     파일명: 2024 08 19 Issue Report_Cheongna Thermal Incident_v17.pptx
     내용 미리보기: Summary of Representative Article – Hyundai & Kia Hold Inspection
19
Hyundai Motor and Kia hold complimentary inspection amid concerns over EV thermal incidents (Yonhap News, 2024/08/13)
Hyundai Moto...

  5. 문서 ID: f3ee6fb4-bece-4d4f-ac91-5cdc33fafce7
     파일명: 2024 08 19 Issue Report_Cheongna Thermal Incident_v17.pptx
     내용 미리보기: Summary of Representative Article – Hyundai & Kia Hold Inspection
19
Hyundai Motor and Kia hold complimentary inspection amid concerns over EV thermal incidents (Yonhap News, 2024/08/13)
Hyundai Moto...


================================================================================

테스트 케이스 20: SOCAR, 몽클레르, 버질 아블로 협력 관련 모든 자료
------------------------------------------------------------
2025-09-12 18:50:19,484 - mcp_tools - INFO - 🔍 필터 추출 시작: 'SOCAR, 몽클레르, 버질 아블로 협력 관련 모든 자료'
2025-09-12 18:50:20,994 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:50:20,995 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:50:20,996 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:50:21,077 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:50:21,078 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:50:21,157 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:50:21,157 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:50:21,222 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:50:21,223 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:50:21,288 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:50:21,289 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:50:21,289 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
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
2025-09-12 18:50:21,289 - mcp_tools - INFO - 🔍 단순 RAG 검색 실행: 'SOCAR, 몽클레르, 버질 아블로 협력 관련 모든 자료' (limit: 5)
2025-09-12 18:50:21,289 - kars_db - INFO - 🔍 검색 시작: 'SOCAR, 몽클레르, 버질 아블로 협력 관련 모든 자료' (limit: 5)
2025-09-12 18:50:21,338 - weaviate_db - INFO - 🔍 검색 완료: 5개 결과 (쿼리: 'SOCAR, 몽클레르, 버질 아블로 협력 관련 모든 자료'
2025-09-12 18:50:21,338 - kars_db - INFO - ✅ 검색 완료: 5개 결과 반환
📊 RAG 검색 결과:
  - 성공 여부: True
  - 총 결과 수: 5개
  - 검색 방식: N/A

📄 검색된 문서들:
  1. 문서 ID: 92eab4c9-4855-42d4-9ad6-74a06aaacd5f
     파일명: Press Kit_2023 서울모빌리티쇼_메르세데스-벤츠 코리아_0318.doc
     내용 미리보기: 





Page 3






C O N T E N T S


I. 메르세데스-벤츠의 럭셔리 & 전동화 & 지속가능성 전략                                        p. 2  -  3


II. 메르세데스-벤츠 코리아 출품 모델                                                ...

  2. 문서 ID: c8ba16d9-ec57-44af-bcc5-1a99595f07d2
     파일명: Press Kit_2023 서울모빌리티쇼_메르세데스-벤츠 코리아_0316.doc
     내용 미리보기: 





Page 1






C O N T E N T S


I. 메르세데스-벤츠의 럭셔리 & 전동화 & 지속가능성 전략                                        p. 2  -  3


II. 메르세데스-벤츠 코리아 출품 모델                                                ...

  3. 문서 ID: 585a0165-ccb4-4515-9b63-046ac3b768fa
     파일명: Press Kit_2023 서울모빌리티쇼_메르세데스-벤츠 코리아_0318.doc EJ comment.doc
     내용 미리보기: 





Page 11






C O N T E N T S


I. 메르세데스-벤츠의 럭셔리 & 전동화 & 지속가능성 전략                                        p. 2  -  3


II. 메르세데스-벤츠 코리아 출품 모델                                               ...

  4. 문서 ID: dca883e0-8312-46ef-97ac-88b5b9f1536e
     파일명: Press Kit_2023 서울모빌리티쇼_메르세데스-벤츠 코리아_0324.docx
     내용 미리보기: 

C O N T E N T S


I. 메르세데스-벤츠의 럭셔리 & 전동화 & 지속가능성 전략                                        p. 2  -  3


II. 메르세데스-벤츠 코리아 출품 모델                                                                       ...

  5. 문서 ID: c99ad5bf-c56c-45fc-8ffd-39ce902031ad
     파일명: Press Kit_2023 서울모빌리티쇼_메르세데스-벤츠 코리아_0315-1.doc
     내용 미리보기: 





Page 11






C O N T E N T S


I. 메르세데스-벤츠의 럭셔리 & 전동화 & 지속가능성 전략                                        p. 2  -  4


II. 메르세데스-벤츠 코리아 출품 모델                                               ...


================================================================================

테스트 케이스 21: 전기차 관련 기술 중 MBUX, 4MATIC, 하이브리드 언급된 문서들
------------------------------------------------------------
2025-09-12 18:50:21,339 - mcp_tools - INFO - 🔍 필터 추출 시작: '전기차 관련 기술 중 MBUX, 4MATIC, 하이브리드 언급된 문서들'
2025-09-12 18:50:22,848 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:50:22,850 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:50:22,850 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:50:22,927 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:50:22,928 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:50:22,995 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:50:22,995 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:50:23,070 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:50:23,070 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:50:23,144 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:50:23,145 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:50:23,145 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
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
2025-09-12 18:50:23,145 - mcp_tools - INFO - 🔍 단순 RAG 검색 실행: '전기차 관련 기술 중 MBUX, 4MATIC, 하이브리드 언급된 문서들' (limit: 5)
2025-09-12 18:50:23,145 - kars_db - INFO - 🔍 검색 시작: '전기차 관련 기술 중 MBUX, 4MATIC, 하이브리드 언급된 문서들' (limit: 5)
2025-09-12 18:50:23,186 - weaviate_db - INFO - 🔍 검색 완료: 5개 결과 (쿼리: '전기차 관련 기술 중 MBUX, 4MATIC, 하이브리드 언급된 문서들'
2025-09-12 18:50:23,186 - kars_db - INFO - ✅ 검색 완료: 5개 결과 반환
📊 RAG 검색 결과:
  - 성공 여부: True
  - 총 결과 수: 5개
  - 검색 방식: N/A

📄 검색된 문서들:
  1. 문서 ID: bcd860ce-2d11-462a-95d3-970ec7623f14
     파일명: [PRGATE] 메르세데스-벤츠 코리아 모니터링 가이드.docx
     내용 미리보기: 벤츠 모니터링 가이드
선택 기준은 [Daily Monitoring Categorization] 파일 참조

1. 국문 워드파일 작성 방법

Brand & Product News (자사)
- 커버리지 배열 순서: 지면 게재 커버리지 → 시승기 → 기획 기사 → 보도자료 → 국내 기사 → 글로벌 기사 → 부정 기사
*단, 전일 행사 진행했거나 자료 배포한 경...

  2. 문서 ID: 2a88afbf-03d4-4178-9c31-1d2895b98cae
     파일명: 2023 06 09 Brand Committee COM_Summary, competitor.pptx
     내용 미리보기: Summary of PR Activities 










Development and dissemination of 10 press releases



Dailies
/Online
Auto
TV
Weeklies
Magazine
Total
Impression
(Ad Value)
Press Release
CSR
Feb. 27
10th GIVE ‘N ...

  3. 문서 ID: 14f6907e-bfcc-4c72-b445-346a8bb35c04
     파일명: KPR  7월 협찬 증빙 기사 송부.msg
     내용 미리보기: From:이 승연(Yonnie Lee)
Sent:Fri 7/29/2022
To:Hwang, Yun-Ju (191); Kim, Hyunji (191)
Cc:MBK
Bcc:
Subject:[KPR] 7월 협찬 증빙 기사 송부
Attachments:MBK_7월 애드버토리얼 증빙_220729.xlsx; [에너지 경제]메르세데스-벤츠_2030년까지 全차종 전기차 ...

  4. 문서 ID: e7a2335c-a501-4359-b0f1-f6349c1b8621
     파일명: Press Release-메르세데스-벤츠 코리아, 메르세데스-AMG의 첫번째 순수 전기차 ‘더 뉴 메르세데스-AMG EQS 53 4MATIC+’ 출시_draft.docx
     내용 미리보기: 메르세데스-벤츠 코리아, 
메르세데스-AMG의 첫번째 순수 전기차 ‘더 뉴 메르세데스-AMG EQS 53 4MATIC+’ 출시

- 메르세데스-AMG 가 선보이는 최초의 고성능 순수 전기차 ‘더 뉴 메르세데스-AMG EQS 53 4MATIC+’ 국내 출시
- 2개의 전기 모터를 탑재한 사륜구동 모델로 AMG만의 강력한 주행 성능을 지원
- AMG 개성을 ...

  5. 문서 ID: 8010a334-5d38-408c-aa2f-ad604ac6f190
     파일명: Press Release-메르세데스-벤츠 코리아 메르세데스-AMG의 첫번째 순수 전기차 더 뉴 메르세데스-AMG EQS 53 4MATIC+ 출시_v2.docx
     내용 미리보기: 메르세데스-벤츠 코리아, 
메르세데스-AMG의 첫번째 순수 전기차 ‘더 뉴 메르세데스-AMG EQS 53 4MATIC+’ 출시

- 메르세데스-AMG 가 선보이는 최초의 고성능 순수 전기차 ‘더 뉴 메르세데스-AMG EQS 53 4MATIC+’ 국내 출시
- 2개의 전기 모터를 탑재한 사륜구동 모델로 AMG만의 강력한 주행 성능을 지원
- AMG 개성을 ...


================================================================================

테스트 케이스 22: SOCAR와의 카셰어링 서비스 협약 체결 과정
------------------------------------------------------------
2025-09-12 18:50:23,187 - mcp_tools - INFO - 🔍 필터 추출 시작: 'SOCAR와의 카셰어링 서비스 협약 체결 과정'
2025-09-12 18:50:24,697 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:50:24,699 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:50:24,699 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:50:24,784 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:50:24,784 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:50:24,859 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:50:24,859 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:50:24,933 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:50:24,933 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:50:24,999 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:50:24,999 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:50:24,999 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
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
2025-09-12 18:50:24,999 - mcp_tools - INFO - 🔍 단순 RAG 검색 실행: 'SOCAR와의 카셰어링 서비스 협약 체결 과정' (limit: 5)
2025-09-12 18:50:24,999 - kars_db - INFO - 🔍 검색 시작: 'SOCAR와의 카셰어링 서비스 협약 체결 과정' (limit: 5)
2025-09-12 18:50:25,038 - weaviate_db - INFO - 🔍 검색 완료: 5개 결과 (쿼리: 'SOCAR와의 카셰어링 서비스 협약 체결 과정'
2025-09-12 18:50:25,038 - kars_db - INFO - ✅ 검색 완료: 5개 결과 반환
📊 RAG 검색 결과:
  - 성공 여부: True
  - 총 결과 수: 5개
  - 검색 방식: N/A

📄 검색된 문서들:
  1. 문서 ID: 46b2a513-9392-4a8a-88a3-7c00f24fcfae
     파일명: 2024 08 12 Issue Report_Cheongna Thermal Incident_v12_F.pptx
     내용 미리보기: 


Issue Reportincident in Cheongna, Korea
Mercedes-Benz Korea Communications  
August 12, 2024
Summary of Representative Article – Battery Manufacturer Information
6
[Editorial] Information on EV ba...

  2. 문서 ID: b2678df2-3e9b-4c02-9140-d3ecf1055d50
     파일명: 2024 08 14 Issue Report_Cheongna Thermal Incident_v14.pptx
     내용 미리보기: Summary of Representative Article – Support from SOCAR
19
SOCAR to provide 100 support vehicles to residents affected by recent EV thermal incident in Cheongna(Money Today, 2024/08/12)
Car sharing pl...

  3. 문서 ID: 1eb91ecc-36e7-43ee-94de-047fb00a3df8
     파일명: V2_Press Release-Mercedes-Benz Korea signs MoU with Socar to bring the larg.._ (003).doc
     내용 미리보기: 

Page 2
Mercedes-Benz Korea partners up with SOCAR for bringing the largest supply of electric vehicles to the car-sharing industry

- Mercedes-Benz Korea and SOCAR signed a car-sharing service a...

  4. 문서 ID: 812cfd8c-c12d-4ddc-b134-154024f0f710
     파일명: 2024 08 19 Issue Report_Cheongna Thermal Incident_v17.pptx
     내용 미리보기: Summary of Representative Article – Hyundai & Kia Hold Inspection
19
Hyundai Motor and Kia hold complimentary inspection amid concerns over EV thermal incidents (Yonhap News, 2024/08/13)
Hyundai Moto...

  5. 문서 ID: 8e5ca30d-824a-4410-bd4e-8a22a8395ff4
     파일명: Press Release  Mercedes-Benz Korea partners up with SOCAR for bringing the largest supply of electric vehicles to the car-sharing industry.msg
     내용 미리보기: From:정은하
Sent:Mon 6/01/2020
To:Dear Journalist
Cc:
Bcc:
Subject:[Press Release] Mercedes-Benz Korea partners up with SOCAR for bringing the largest supply of electric vehicles to the car-sharing indu...


================================================================================

테스트 케이스 23: EQC 모델의 국내 시장 출시 및 홍보 활동
------------------------------------------------------------
2025-09-12 18:50:25,039 - mcp_tools - INFO - 🔍 필터 추출 시작: 'EQC 모델의 국내 시장 출시 및 홍보 활동'
2025-09-12 18:50:26,551 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:50:26,552 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:50:26,553 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:50:26,627 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:50:26,628 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:50:26,705 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:50:26,706 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:50:26,783 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:50:26,784 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:50:26,850 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:50:26,851 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:50:26,851 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
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
2025-09-12 18:50:26,851 - mcp_tools - INFO - 🔍 단순 RAG 검색 실행: 'EQC 모델의 국내 시장 출시 및 홍보 활동' (limit: 5)
2025-09-12 18:50:26,851 - kars_db - INFO - 🔍 검색 시작: 'EQC 모델의 국내 시장 출시 및 홍보 활동' (limit: 5)
2025-09-12 18:50:26,884 - weaviate_db - INFO - 🔍 검색 완료: 5개 결과 (쿼리: 'EQC 모델의 국내 시장 출시 및 홍보 활동'
2025-09-12 18:50:26,884 - kars_db - INFO - ✅ 검색 완료: 5개 결과 반환
📊 RAG 검색 결과:
  - 성공 여부: True
  - 총 결과 수: 5개
  - 검색 방식: N/A

📄 검색된 문서들:
  1. 문서 ID: b5004cc8-74d4-46cd-86a8-a0e0077aca7b
     파일명: Dealer Award EQ Session Template Consolidated V2.pptx
     내용 미리보기: 


Agenda


Charging
MBK 충전 인프라 확대 요청(MBK Charging Infra Enhancement request)

Mme어플리케이션 충전 활용 요청
(Mme App utilized Charging Solution request)



충전 관련 딜러사 요청사항


Dealer request on Network & Charging...

  2. 문서 ID: e592e179-2f43-4477-af39-ee1722d318c5
     파일명: 20191217 eMC Meeting.pdf
     내용 미리보기: Rese t the sli de bac k to i ts 
Chan ge the sli de lay out 
via menu ba r: 
Alte rna tin g be tween whi te an d blac k 
sli de lay outs via menu ba r: 
Dec eMC meeting
Dec, 201917
th
Dec eMC meeting...

  3. 문서 ID: 1b403fc7-ffd1-4ead-b070-1436c19fb9a0
     파일명: Dealer Award EQ Session Template Consolidated.pptx
     내용 미리보기: 


Agenda


Charging
MBK 충전 인프라 확대 요청(MBK Charging Infra Enhancement request)

Mme어플리케이션 충전 활용 요청
(Mme App utilized Charging Solution request)



충전 관련 딜러사 요청사항


Dealer request on Network & Charging...

  4. 문서 ID: 590ed758-8b59-474c-be19-4e9c3e4062a2
     파일명: 2023 0719 Monthly EQ STECO Meeting.pdf
     내용 미리보기: Rese t the sli de bac k to i ts 
Chan ge the sli de lay out 
via menu ba r: 
Alte rna tin g be tween whi te an d blac k 
sli de lay outs via menu ba r: 
Internal
Monthly EQ STECOMeeting
19
th
July, 2...

  5. 문서 ID: ed18f143-36bd-4e3c-9cbf-3be8567b9d4e
     파일명: 2023 Dealer Conference_Business Update_draft_v1.pptx
     내용 미리보기: 


홀세일 예상 수치
리테일 예상 수치
We are planning optimal supply to maintain optimal stock level. 
남은하반기에도 적정 재고 수준이 유지 될 수 있도록 균형 잡힌 차량 공급을 계획하고 있습니다. 
딜러 재고 예상 수치

Target Stock Reach: 1 month
Q1
Q2
Q3
Q4

시장상...


================================================================================

테스트 케이스 24: 메르세데스-벤츠의 전동화 전략 및 기술 로드맵
------------------------------------------------------------
2025-09-12 18:50:26,884 - mcp_tools - INFO - 🔍 필터 추출 시작: '메르세데스-벤츠의 전동화 전략 및 기술 로드맵'
2025-09-12 18:50:28,398 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:50:28,400 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:50:28,400 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:50:28,497 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:50:28,498 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:50:28,545 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:50:28,546 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:50:28,624 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:50:28,624 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:50:28,680 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:50:28,681 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:50:28,681 - mcp_tools - INFO - ✅ 필터 추출 완료: similarity 검색, 필터: custodian=None ori_file_name=None s_created_date=None sent_date=None from_email=None to_email=None cc=None bcc=None last_author=None extension=None
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
2025-09-12 18:50:28,681 - mcp_tools - INFO - 🔍 단순 RAG 검색 실행: '메르세데스-벤츠의 전동화 전략 및 기술 로드맵' (limit: 5)
2025-09-12 18:50:28,681 - kars_db - INFO - 🔍 검색 시작: '메르세데스-벤츠의 전동화 전략 및 기술 로드맵' (limit: 5)
2025-09-12 18:50:28,717 - weaviate_db - INFO - 🔍 검색 완료: 5개 결과 (쿼리: '메르세데스-벤츠의 전동화 전략 및 기술 로드맵'
2025-09-12 18:50:28,717 - kars_db - INFO - ✅ 검색 완료: 5개 결과 반환
📊 RAG 검색 결과:
  - 성공 여부: True
  - 총 결과 수: 5개
  - 검색 방식: N/A

📄 검색된 문서들:
  1. 문서 ID: 648e4ef1-5023-45f7-9f8e-24956cfeca5d
     파일명: Press Kit_2023 서울모빌리티쇼_메르세데스-벤츠 코리아_0315-1.doc
     내용 미리보기: 





Page 11






C O N T E N T S


I. 메르세데스-벤츠의 럭셔리 & 전동화 & 지속가능성 전략                                        p. 2  -  4


II. 메르세데스-벤츠 코리아 출품 모델                                               ...

  2. 문서 ID: f35de869-05ce-4f9e-99ba-a7b11fdae671
     파일명: Press Kit_KAIDA Presskit_230508.docx
     내용 미리보기: 

C O N T E N T S


I. 메르세데스-벤츠 코리아 소개  p. 2  -  3
회사 소개
전략
차량 라인업
고객 만족도를 높이기 위한 노력
네트워크 및 고객 지원 시설
한국 사회와의 상생을 위한 기술 혁신 노력
지속적인 사회공헌활동

II. 메르세데스-벤츠 브랜드 소개         p. 4 - 22
브랜드 역사
헤일로 브랜드(Halo Brand) 소개

...

  3. 문서 ID: 13f9fd3c-acc1-44e2-9a0d-ae5dc9e06aca
     파일명: Press Kit_2023 서울모빌리티쇼_메르세데스-벤츠 코리아_0316.doc
     내용 미리보기: 





Page 1






C O N T E N T S


I. 메르세데스-벤츠의 럭셔리 & 전동화 & 지속가능성 전략                                        p. 2  -  3


II. 메르세데스-벤츠 코리아 출품 모델                                                ...

  4. 문서 ID: d5581f73-2d87-40bf-96a6-c9ad992646a3
     파일명: Press Kit_2023 서울모빌리티쇼_메르세데스-벤츠 코리아_0315.doc
     내용 미리보기: 





Page 1






C O N T E N T S


I. 메르세데스-벤츠의 럭셔리 & 전동화 & 지속가능성 전략                                        p. 2  -  3


II. 메르세데스-벤츠 코리아 출품 모델                                                ...

  5. 문서 ID: 5f17a797-4420-4e27-b50c-6ed4a4cb159d
     파일명: 애드버토리얼 자료-전기 모빌리티 시대 청사진을 제시하는 메르세데스-벤츠의 전기 구동화 로드맵.docx
     내용 미리보기: 전기 모빌리티 시대 청사진을 제시하는 
메르세데스-벤츠의 전기 구동화 로드맵

2022.08.23

메르세데스-벤츠는 지난 2021년 7월 제품 포트폴리오 전략과 투자 계획을 포함한 새로운 전동화 전략을 발표했다. 메르세데스-벤츠는 전동화 전략을 ‘전기차 중심(EV-first)’에서 ‘전기차 전용(EV-only)’으로 전환함과 동시에 소프트웨어가 주도하는...


================================================================================

✅ 테스트 완료!
/raid1/workspace/kars-agent/weaviate-mcp/.venv/lib/python3.12/site-packages/weaviate/warnings.py:302: ResourceWarning: Con004: The connection to Weaviate was not closed properly. This can lead to memory leaks.
            Please make sure to close the connection using `client.close()`.
  warnings.warn(
/raid1/workspace/kars-agent/weaviate-mcp/tmp_sungwon_chae/test_extract_value_tool_modified.py:326: ResourceWarning: unclosed <socket.socket fd=9, family=2, type=1, proto=6, laddr=('10.10.150.195', 33488), raddr=('10.10.150.195', 8080)>
  await test_extract_filter()
ResourceWarning: Enable tracemalloc to get the object allocation traceback

====================================================================================================

🔍 이름 매칭 기능 테스트 시작

2025-09-12 18:50:28,751 - mcp_tools - INFO - Weaviate MCP 도구 초기화 완료
👤 1단계: 데이터베이스의 unique한 이름 값들 조회
------------------------------------------------------------
2025-09-12 18:50:28,751 - kars_db - INFO - 🚀 RAG 벡터 데이터베이스 초기화 시작
2025-09-12 18:50:28,751 - simple_manager - INFO - Weaviate URL: http://10.10.150.195:8080
2025-09-12 18:50:28,751 - simple_manager - INFO - OpenAI Base URL: http://10.10.190.1:8125
2025-09-12 18:50:28,751 - kars_db - INFO - ✅ VectorDB 매니저 초기화 완료
2025-09-12 18:50:28,779 - httpx - INFO - HTTP Request: GET http://10.10.190.1:8125/v1/models "HTTP/1.1 200 OK"
2025-09-12 18:50:28,779 - weaviate_db - INFO - ✅ vLLM 서버에서 모델명 가져옴: /data/models_ckpt/bge-m3
2025-09-12 18:50:28,791 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8125/v1/embeddings "HTTP/1.1 200 OK"
2025-09-12 18:50:28,792 - weaviate_db - INFO - ✅ 샘플 임베딩 생성 성공 (차원: 1024)
2025-09-12 18:50:28,834 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/.well-known/openid-configuration "HTTP/1.1 404 Not Found"
2025-09-12 18:50:28,859 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/meta "HTTP/1.1 200 OK"
2025-09-12 18:50:30,891 - weaviate_db - INFO - ✅ Weaviate 클라이언트 연결 성공: http://10.10.150.195:8080
2025-09-12 18:50:30,891 - weaviate_db - INFO - 📡 OpenAI Base URL (Python용): http://10.10.190.1:8125/v1
2025-09-12 18:50:30,892 - weaviate_db - INFO - 📡 OpenAI Base URL (Weaviate용): http://10.10.190.1:8125
2025-09-12 18:50:30,892 - weaviate_db - INFO - 🔧 동적 모델명: /data/models_ckpt/bge-m3
2025-09-12 18:50:30,892 - simple_manager - INFO - DB 연결 초기화 완료
2025-09-12 18:50:30,895 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema "HTTP/1.1 200 OK"
2025-09-12 18:50:30,900 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema/DocumentChunk "HTTP/1.1 200 OK"
2025-09-12 18:50:30,904 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema/EnronDocument "HTTP/1.1 200 OK"
2025-09-12 18:50:30,905 - weaviate_db - INFO - 스키마 조회 완료: 2개 클래스
2025-09-12 18:50:30,905 - simple_manager - WARNING - 클래스 매핑 파일이 없습니다. 기본 규칙을 사용합니다.
2025-09-12 18:50:30,905 - simple_manager - INFO - 기존 클래스 등록: chunk_db -> DocumentChunk
2025-09-12 18:50:30,905 - simple_manager - INFO - 기존 클래스 등록: enron_db -> EnronDocument
2025-09-12 18:50:30,905 - simple_manager - INFO - 총 2개 DB에 클래스 등록 완료
2025-09-12 18:50:30,905 - simple_manager - INFO -   chunk_db: ['DocumentChunk']
2025-09-12 18:50:30,905 - simple_manager - INFO -   enron_db: ['EnronDocument']
2025-09-12 18:50:30,909 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema "HTTP/1.1 200 OK"
2025-09-12 18:50:30,913 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema/DocumentChunk "HTTP/1.1 200 OK"
2025-09-12 18:50:30,916 - httpx - INFO - HTTP Request: GET http://10.10.150.195:8080/v1/schema/EnronDocument "HTTP/1.1 200 OK"
2025-09-12 18:50:30,917 - weaviate_db - INFO - 스키마 조회 완료: 2개 클래스
2025-09-12 18:50:30,917 - kars_db - INFO - 📊 사용 가능한 클래스들: ['DocumentChunk', 'EnronDocument']
2025-09-12 18:50:30,917 - kars_db - INFO - ✅ 사용할 클래스명: DocumentChunk
2025-09-12 18:50:30,918 - mcp_tools - INFO - ✅ RAG 데이터베이스 초기화 성공: kars_test
2025-09-12 18:50:30,918 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:50:30,918 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:50:30,992 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:50:30,992 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:50:31,073 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:50:31,074 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:50:31,150 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:50:31,150 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:50:31,223 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:50:31,223 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
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

🧪 테스트 케이스 1: MBG 발신자 이름으로 검색
   입력: 'Jeong, Yeeun (191)'
--------------------------------------------------
2025-09-12 18:50:31,223 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:50:31,224 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:50:31,296 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:50:31,297 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:50:31,377 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:50:31,377 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:50:31,442 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:50:31,442 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:50:31,512 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:50:31,513 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:50:40,591 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:50:40,593 - mcp_tools - INFO - ✅ 이메일 유사도 매칭 완료: 'Jeong, Yeeun (191)' → 5개 매치
✅ 매칭 성공!
  - 총 후보 수: 17개
  - 매치 결과: 5개
  - 검색 필드 타입: all

🎯 매치 결과:
  1. Jeong, Yeeun (191) on behalf of korea_com (191-NPM)
     - 유사도 점수: 100.0
     - 매칭 타입: exact
     - 매칭 이유: 이름이 완전히 일치합니다.
  2. Jeong, Yeeun (691)
     - 유사도 점수: 90.0
     - 매칭 타입: name_similar
     - 매칭 이유: 이름이 일치하지만, 뒤에 있는 (691)은 쿼리의 (191)과 다릅니다. 이는 이름 유사성에 해당합니다.
  3. Song, Jieun (191)
     - 유사도 점수: 30.0
     - 매칭 타입: partial
     - 매칭 이유: 이름의 일부가 유사합니다. 'Jieun'은 'Yeeun'과 유사한 발음입니다.
  4. Song, Jieun (691)
     - 유사도 점수: 30.0
     - 매칭 타입: partial
     - 매칭 이유: 이름의 일부가 유사합니다. 'Jieun'은 'Yeeun'과 유사한 발음입니다.
  5. Ju, Hyeyeon (191-Extern-MBK)
     - 유사도 점수: 30.0
     - 매칭 타입: partial
     - 매칭 이유: 이름의 일부가 유사합니다. 'Hyeyeon'은 'Yeeun'과 부분적으로 유사한 발음입니다.


🧪 테스트 케이스 2: MBG 발신자 이름으로 검색
   입력: 'Park, Sep (191)'
--------------------------------------------------
2025-09-12 18:50:40,593 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:50:40,593 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:50:40,675 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:50:40,675 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:50:40,746 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:50:40,746 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:50:40,814 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:50:40,814 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:50:40,887 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:50:40,887 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:50:48,987 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:50:48,989 - mcp_tools - INFO - ✅ 이메일 유사도 매칭 완료: 'Park, Sep (191)' → 5개 매치
✅ 매칭 성공!
  - 총 후보 수: 17개
  - 매치 결과: 5개
  - 검색 필드 타입: all

🎯 매치 결과:
  1. Park, Sep (191) on behalf of korea_com (191-NPM)
     - 유사도 점수: 100.0
     - 매칭 타입: exact
     - 매칭 이유: 이름이 완전히 일치합니다.
  2. Park, Jaekyung (191)
     - 유사도 점수: 90.0
     - 매칭 타입: name_similar
     - 매칭 이유: 성은 일치하지만 이름이 다릅니다. 그러나 같은 성을 가진 경우 이름 유사성으로 90점으로 평가합니다.
  3. Jeong, Yeeun (191)
     - 유사도 점수: 30.0
     - 매칭 타입: partial
     - 매칭 이유: 이름이 아예 다르지만, (191)이라는 공통 번호가 있습니다.
  4. Shim, Ellen (191)
     - 유사도 점수: 30.0
     - 매칭 타입: partial
     - 매칭 이유: 이름이 아예 다르지만, (191)이라는 공통 번호가 있습니다.
  5. Song, Jieun (191)
     - 유사도 점수: 30.0
     - 매칭 타입: partial
     - 매칭 이유: 이름이 아예 다르지만, (191)이라는 공통 번호가 있습니다.


🧪 테스트 케이스 3: MBG 보관자 이름으로 검색
   입력: '세진 김'
--------------------------------------------------
2025-09-12 18:50:48,989 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:50:48,990 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:50:49,106 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:50:49,106 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:50:49,153 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:50:49,153 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:50:49,227 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:50:49,227 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:50:49,297 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:50:49,297 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:50:58,568 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:50:58,569 - mcp_tools - INFO - ✅ 이메일 유사도 매칭 완료: '세진 김' → 5개 매치
✅ 매칭 성공!
  - 총 후보 수: 17개
  - 매치 결과: 5개
  - 검색 필드 타입: all

🎯 매치 결과:
  1. 세진 김
     - 유사도 점수: 100.0
     - 매칭 타입: exact
     - 매칭 이유: 이름이 완전히 일치합니다.
  2. Kim, Ji-Hyun (191)
     - 유사도 점수: 30.0
     - 매칭 타입: partial
     - 매칭 이유: 이름의 일부가 일치합니다. 'Kim'은 '김'과 일치하지만, 'Ji-Hyun'은 '세진'과 일치하지 않습니다.
  3. Shim, Ellen (191)
     - 유사도 점수: 30.0
     - 매칭 타입: partial
     - 매칭 이유: 이름의 일부가 유사합니다. 'Shim'은 '김'과 발음이 비슷하지만, 'Ellen'은 '세진'과 일치하지 않습니다.
  4. Joo, Jaeyool (191)
     - 유사도 점수: 30.0
     - 매칭 타입: partial
     - 매칭 이유: 이름의 일부가 일치합니다. 'Joo'는 '김'과 관련이 없지만, 'Jaeyool'은 '세진'과 일부가 유사할 수 있습니다.
  5. Song, Jieun (191)
     - 유사도 점수: 30.0
     - 매칭 타입: partial
     - 매칭 이유: 이름의 일부가 일치합니다. 'Song'은 '김'과 관련이 없지만, 'Jieun'은 '세진'과 일부가 유사할 수 있습니다.


🧪 테스트 케이스 4: MBG 최종 작성자 이름으로 검색
   입력: 'Song, Jieun (191)'
--------------------------------------------------
2025-09-12 18:50:58,570 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:50:58,570 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:50:58,644 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:50:58,645 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:50:58,724 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:50:58,724 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:50:58,791 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:50:58,791 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:50:58,867 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:50:58,868 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:51:05,645 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:51:05,647 - mcp_tools - INFO - ✅ 이메일 유사도 매칭 완료: 'Song, Jieun (191)' → 5개 매치
✅ 매칭 성공!
  - 총 후보 수: 17개
  - 매치 결과: 5개
  - 검색 필드 타입: all

🎯 매치 결과:
  1. Song, Jieun (191)
     - 유사도 점수: 100.0
     - 매칭 타입: exact
     - 매칭 이유: 이름이 완전히 일치합니다.
  2. Song, Jieun (691)
     - 유사도 점수: 90.0
     - 매칭 타입: name_similar
     - 매칭 이유: 이름이 완전히 일치하지만, 뒤에 있는 숫자가 다릅니다.
  3. Shim, Ellen (191)
     - 유사도 점수: 30.0
     - 매칭 타입: partial
     - 매칭 이유: 이름의 일부가 유사합니다.
  4. Ju, Hyeyeon (191-Extern-MBK)
     - 유사도 점수: 30.0
     - 매칭 타입: partial
     - 매칭 이유: 이름의 일부가 유사합니다.
  5. Joo, Jaeyool (191)
     - 유사도 점수: 30.0
     - 매칭 타입: partial
     - 매칭 이유: 이름의 일부가 유사합니다.


🧪 테스트 케이스 5: MBG 외부 작성자 이름으로 검색
   입력: 'Ju, Hyeyeon (191-Extern-MBK)'
--------------------------------------------------
2025-09-12 18:51:05,648 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:51:05,648 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:51:05,724 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:51:05,725 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:51:05,802 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:51:05,802 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:51:05,880 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:51:05,880 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:51:05,954 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:51:05,954 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:51:15,943 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:51:15,945 - mcp_tools - INFO - ✅ 이메일 유사도 매칭 완료: 'Ju, Hyeyeon (191-Extern-MBK)' → 5개 매치
✅ 매칭 성공!
  - 총 후보 수: 17개
  - 매치 결과: 5개
  - 검색 필드 타입: all

🎯 매치 결과:
  1. Ju, Hyeyeon (191-Extern-MBK)
     - 유사도 점수: 100.0
     - 매칭 타입: exact
     - 매칭 이유: 이름과 이메일 주소가 완전히 일치합니다.
  2. Joo, Jaeyool (191)
     - 유사도 점수: 90.0
     - 매칭 타입: name_similar
     - 매칭 이유: 이름의 철자가 유사하며, 'Ju'와 'Joo'는 발음이 유사하고, 'Hyeyeon'과 'Jaeyool'은 한글 이름으로서 유사한 형태를 띱니다.
  3. Kim, Ji-Hyun (191)
     - 유사도 점수: 90.0
     - 매칭 타입: name_similar
     - 매칭 이유: 이름의 철자가 유사하며, 'Hyeyeon'과 'Ji-Hyun'은 한글 이름으로서 유사한 형태를 띱니다.
  4. Jeong, Yeeun (191)
     - 유사도 점수: 90.0
     - 매칭 타입: name_similar
     - 매칭 이유: 이름의 철자가 유사하며, 'Hyeyeon'과 'Yeeun'은 한글 이름으로서 유사한 형태를 띱니다.
  5. Song, Jieun (191)
     - 유사도 점수: 90.0
     - 매칭 타입: name_similar
     - 매칭 이유: 이름의 철자가 유사하며, 'Hyeyeon'과 'Jieun'은 한글 이름으로서 유사한 형태를 띱니다.


🧪 테스트 케이스 6: MBG 작성자 이름으로 검색
   입력: 'Kim, Ji-Hyun (191)'
--------------------------------------------------
2025-09-12 18:51:15,945 - mcp_tools - INFO - 🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.
2025-09-12 18:51:15,946 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=from_email, limit=50000
2025-09-12 18:51:16,021 - kars_db - INFO - ✅ Unique 값 조회 완료: from_email 필드에서 3개 unique 값 발견
2025-09-12 18:51:16,022 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=to_email, limit=50000
2025-09-12 18:51:16,095 - kars_db - INFO - ✅ Unique 값 조회 완료: to_email 필드에서 1개 unique 값 발견
2025-09-12 18:51:16,095 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=custodian, limit=50000
2025-09-12 18:51:16,173 - kars_db - INFO - ✅ Unique 값 조회 완료: custodian 필드에서 1개 unique 값 발견
2025-09-12 18:51:16,174 - kars_db - INFO - 🔍 Unique 값 조회 시작: field=last_author, limit=50000
2025-09-12 18:51:16,244 - kars_db - INFO - ✅ Unique 값 조회 완료: last_author 필드에서 14개 unique 값 발견
2025-09-12 18:51:16,245 - mcp_tools - INFO - ✅ Unique 이름들 조회 완료: from_email 3개, to_email 1개, custodian 1, total_last_author:  14
2025-09-12 18:51:25,583 - httpx - INFO - HTTP Request: POST http://10.10.190.1:8124/v1/chat/completions "HTTP/1.1 200 OK"
2025-09-12 18:51:25,584 - mcp_tools - INFO - ✅ 이메일 유사도 매칭 완료: 'Kim, Ji-Hyun (191)' → 5개 매치
✅ 매칭 성공!
  - 총 후보 수: 17개
  - 매치 결과: 5개
  - 검색 필드 타입: all

🎯 매치 결과:
  1. Kim, Ji-Hyun (191)
     - 유사도 점수: 100.0
     - 매칭 타입: exact
     - 매칭 이유: 이름이 완전히 일치합니다.
  2. Shim, Ellen (191)
     - 유사도 점수: 30.0
     - 매칭 타입: partial
     - 매칭 이유: 이름의 일부가 유사합니다. 'Ji-Hyun'과 'Ellen'은 모두 여성 이름일 수 있지만, 정확한 일치는 아닙니다.
  3. Song, Jieun (191)
     - 유사도 점수: 30.0
     - 매칭 타입: partial
     - 매칭 이유: 이름의 일부가 유사합니다. 'Ji-Hyun'과 'Jieun'은 모두 여성 이름일 수 있지만, 정확한 일치는 아닙니다.
  4. Ju, Hyeyeon (191-Extern-MBK)
     - 유사도 점수: 30.0
     - 매칭 타입: partial
     - 매칭 이유: 이름의 일부가 유사합니다. 'Ji-Hyun'과 'Hyeyeon'은 모두 여성 이름일 수 있지만, 정확한 일치는 아닙니다.
  5. Joo, Jaeyool (191)
     - 유사도 점수: 30.0
     - 매칭 타입: partial
     - 매칭 이유: 이름의 일부가 유사합니다. 'Ji-Hyun'과 'Jaeyool'은 모두 여성 이름일 수 있지만, 정확한 일치는 아닙니다.

✅ 이름 매칭 테스트 완료!
/raid1/workspace/kars-agent/weaviate-mcp/tmp_sungwon_chae/test_extract_value_tool_modified.py:331: ResourceWarning: unclosed <socket.socket fd=10, family=2, type=1, proto=6, laddr=('10.10.150.195', 55824), raddr=('10.10.150.195', 8080)>
  await test_name_matching()
ResourceWarning: Enable tracemalloc to get the object allocation traceback

🎉 모든 테스트 완료!
(.venv) min.choi10@wss-195:/raid1/workspace/kars-agent/weaviate-mcp/tmp_sungwon_chae$ 
