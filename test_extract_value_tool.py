#!/usr/bin/env python3
"""
extract_filter_from_query 도구 테스트 스크립트
"""

import asyncio
import sys
import os
from pathlib import Path

# 현재 디렉토리를 Python 경로에 추가
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

from mcp_tools import WeaviateMCPTools


async def test_extract_filter():
    """extract_filter_from_query 도구를 테스트합니다."""

    # 도구 인스턴스 생성
    tools = WeaviateMCPTools()
    
    # OpenAI 클라이언트 설정 (테스트용)
    try:
        from openai import OpenAI
        base_url="http://10.10.190.1:8124/v1"
        api_key="token-abc123"
        client = OpenAI(base_url=base_url, api_key=api_key)
        response = client.chat.completions.create(
                model="/data/models_ckpt/Qwen3-32B",
                messages=[
                    {"role": "user", "content": "hi!"}
                ]
            )
        print("Test Query Response: ", response)
        print("✅ OpenAI 클라이언트 설정 완료")
    except ImportError:
        print("❌ openai 패키지가 설치되지 않았습니다. 'pip install openai'로 설치해주세요.")
        return
    except Exception as e:
        print(f"❌ OpenAI 클라이언트 설정 실패: {e}")
        return
    
    # 테스트 케이스들 (실제 MBG 데이터 기반)
    test_queries = [
        # A. Filter 기반 검색 테스트 (High Priority)
        "2020년 6월에 작성된 모든 문서들",
        "Dimitris Psillakis가 작성한 모든 문서를 찾아주세요",
        "Lee Sang-kuk이 언급된 모든 이메일을 찾아주세요",
        "SOCAR 관련 모든 문서들",
        "메르세데스-벤츠 코리아 홍보팀이 작성한 문서들",
        
        # B. RAG 기반 검색 테스트 (High Priority)
        "EQC 전기차 관련 모든 자료",
        "SOCAR와의 카셰어링 협력 관련 자료",
        "MBUX 시스템 관련 기술 자료",
        "4MATIC 사륜구동 시스템 관련 자료",
        
        # C. 하이브리드 검색 테스트 (Medium Priority)
        "2020년에 작성된 EQC 관련 문서들",
        "Dimitris Psillakis가 언급한 전기차 전략",
        "SOCAR 협력 관련 2020년 6월 문서",
        "메르세데스-벤츠 코리아 홍보팀의 EQC 관련 자료",
        
        # D. 고급 검색 테스트 (Medium Priority)
        "2020년 6월에 Dimitris Psillakis가 작성한 SOCAR 협력 관련 문서",
        "EQC와 EQE 모델 관련 2020년 이후 작성된 모든 문서",
        "SOCAR, 몽클레르, 버질 아블로 협력 관련 모든 자료",
        "전기차 관련 기술 중 MBUX, 4MATIC, 하이브리드 언급된 문서들",
        
        # E. 특수 검색 테스트 (Low Priority)
        "메르세데스-벤츠 코리아의 2020년 전기차 시장 진출 전략",
        "SOCAR와의 카셰어링 서비스 협약 체결 과정",
        "EQC 모델의 국내 시장 출시 및 홍보 활동",
        "메르세데스-벤츠의 전동화 전략 및 기술 로드맵"
    ]
    
    print("🔍 extract_filter_from_query 도구 테스트 시작 (MBG 실제 데이터 기반)\n")
    print("📋 테스트 목적:")
    print("  1. Filter 자동 추출 검증")
    print("  2. 벡터DB에서 관련 문서 검색 확인")  
    print("  3. 실제 MBG 데이터 기반 GT 검증")
    print("  4. 유사도 기반 검색 성능 확인\n")
    print("📋 FilterExtractionResult 필드:")
    print("  - custodian: 보관자")
    print("  - ori_file_name: 원본 파일명")
    print("  - s_created_date: 생성일")
    print("  - sent_date: 발송일")
    print("  - from_name: 발신자 이름")
    print("  - to_name: 수신자 이름")
    print("  - cc: 참조자 이름")
    print("  - bcc: 숨은참조자 이름")
    print("  - last_author: 최종 작성자")
    print("  - extension: 파일 확장자\n")
    
    for i, query in enumerate(test_queries, 1):
        print(f"테스트 케이스 {i}: {query}")
        print("-" * 60)
        
        try:
            # 도구 실행
            result = await tools.extract_filter_from_query(query)
            
            # 결과 출력
            print(f"📊 추출된 필터:")
            if result["filters"]:
                for field, value in result["filters"].items():
                    if value is not None:
                        print(f"  - {field}: {value}")
                    else:
                        print(f"  - {field}: None")
            else:
                print("  필터 없음")
            
            print(f"🔍 검색 방식: {result['search_type']}")
            print(f"💭 판단 근거: {result['reasoning']}")

    
            # 필터 딕셔너리 생성 (None이 아닌 값만)
            search_filters = {}
            if result["filters"]:
                search_filters = {k: v for k, v in result["filters"].items() if v is not None}
            
            if search_filters:
                print(f"📋 검색에 사용할 필터: {search_filters}")
                
                # 문서 검색 실행
                search_result = await tools.get_document_with_filter(
                    class_name="DocumentChunk",  # 기본 클래스명
                    limit=5,
                    filters=search_filters 
                )
                
                print(f"📊 검색 결과:")
                print(f"  - 성공 여부: {search_result.get('success', False)}")
                print(f"  - 총 결과 수: {search_result.get('total_results', 0)}개")
                print(f"  - 검색 방식: {search_result.get('search_type', 'N/A')}")
                print(f"  - 사용된 필터: {search_result.get('search_type', 'N/A')}")
                
                # 결과 상세 출력
                if search_result.get('success') and search_result.get('results'):
                    print(f"\n📄 검색된 문서들:")
                    for j, doc in enumerate(search_result['results'], 1):
                        print(f"  {j}. 문서 ID: {doc.get('id', 'N/A')}")
                        properties = doc.get('properties', {})
                        print(f"     파일명: {properties.get('file_name', 'N/A')}")
                        print(f"     보관자: {properties.get('custodian', 'N/A')}")
                        print(f"     생성일: {properties.get('created_date', 'N/A')}")
                        print(f"     발송일: {properties.get('sent_date', 'N/A')}")
                        print(f"     발신자: {properties.get('from_email', 'N/A')}")
                        print(f"     수신자: {properties.get('to_email', 'N/A')}")
                        print(f"     확장자: {properties.get('file_type', 'N/A')}")
                        print(f"     내용 미리보기: {properties.get('chunk', 'N/A')[:100] if properties.get('chunk') else 'N/A'}...")
                        print(f"     최종 작성자: {properties.get('last_author', 'N/A')}")
                        print()
                else:
                    print("  📭 검색 결과가 없습니다.")
            else:
                print("  📭 검색할 필터가 없어 단순 RAG 검색을 수행합니다.")
                
                # 단순 RAG 검색
                rag_result = await tools.search_documents(
                    query=query,
                    filters=None,
                    sort_by_date=False,
                    limit=5
                )
                
                print(f"📊 RAG 검색 결과:")
                print(f"  - 성공 여부: {rag_result.get('success', False)}")
                print(f"  - 총 결과 수: {rag_result.get('total_results', 0)}개")
                print(f"  - 검색 방식: {rag_result.get('search_type', 'N/A')}")
                
                if rag_result.get('success') and rag_result.get('results'):
                    print(f"\n📄 검색된 문서들:")
                    for j, doc in enumerate(rag_result['results'], 1):
                        print(f"  {j}. 문서 ID: {doc.get('id', 'N/A')}")
                        properties = doc.get('properties', {})
                        print(f"     파일명: {properties.get('ori_file_name', 'N/A')}")
                        print(f"     내용 미리보기: {properties.get('chunk', 'N/A')[:100] if properties.get('chunk') else 'N/A'}...")
                        print()

            
        except Exception as e:
            print(f"❌ 오류 발생: {e}")
        
        print("\n" + "=" * 80 + "\n")
    
    print("✅ 테스트 완료!")


async def test_name_matching():
    """새로 추가된 이름 매칭 기능을 테스트합니다."""
    
    print("🔍 이름 매칭 기능 테스트 시작\n")
    
    # 도구 인스턴스 생성
    tools = WeaviateMCPTools()
    
    try:
        # 1. 데이터베이스에서 unique한 이름 값들 조회
        print("👤 1단계: 데이터베이스의 unique한 이름 값들 조회")
        print("-" * 60)
        
        unique_names_result = await tools.get_unique_names()
        
        if unique_names_result["success"]:
            print(f"✅ Unique 이름 조회 성공!")
            print(f"  - from_email 개수: {unique_names_result['total_from_emails']}개")
            print(f"  - to_email 개수: {unique_names_result['total_to_emails']}개")
            print(f"  - custodian 개수: {unique_names_result['total_custodian']}개")
            print(f"  - last_author 개수: {unique_names_result['total_last_author']}개")
            
            # 샘플 이름 출력 (처음 10개)
            if unique_names_result['names']['from_emails']:
                print(f"\n📤 from_email 샘플 (처음 10개):")
                for i, name in enumerate(unique_names_result['names']['from_emails'][:10], 1):
                    print(f"  {i}. {name}")
            
            if unique_names_result['names']['to_emails']:
                print(f"\n📥 to_email 샘플 (처음 10개):")
                for i, name in enumerate(unique_names_result['names']['to_emails'][:10], 1):
                    print(f"  {i}. {name}")
            
            if unique_names_result['names']['custodian']:
                print(f"\n👤 custodian 샘플 (처음 10개):")
                for i, name in enumerate(unique_names_result['names']['custodian'][:10], 1):
                    print(f"  {i}. {name}")
            
            if unique_names_result['names']['last_author']:
                print(f"\n✍️ last_author 샘플 (처음 10개):")
                for i, name in enumerate(unique_names_result['names']['last_author'][:10], 1):
                    print(f"  {i}. {name}")
        else:
            print(f"❌ Unique 이름 조회 실패: {unique_names_result['error']}")
            return
        
        print("\n" + "=" * 80 + "\n")
        
        # 2. 이름 유사도 매칭 테스트
        print("🔍 2단계: 이름 유사도 매칭 테스트")
        print("-" * 60)
        
        # 테스트 케이스들
        test_cases = [
            {
                "input": "조효원",
                "description": "한글 이름으로 검색",
                "field_type": "all"
            },
            {
                "input": "hyowon cho",
                "description": "영어 이름으로 검색",
                "field_type": "all"
            },
            {
                "input": "효원 조",
                "description": "이름 순서가 바뀐 경우",
                "field_type": "all"
            },
            {
                "input": "hyowon cho (KC)",
                "description": "약어/별칭이 포함된 경우",
                "field_type": "all"
            },
            {
                "input": "김철수",
                "description": "일반적인 한글 이름",
                "field_type": "all"
            },
            {
                "input": "Park Young-hee",
                "description": "영어 이름 (하이픈 포함)",
                "field_type": "all"
            }
        ]
        
        for i, test_case in enumerate(test_cases, 1):
            print(f"\n🧪 테스트 케이스 {i}: {test_case['description']}")
            print(f"   입력: '{test_case['input']}'")
            print("-" * 50)
            
            try:
                # 이름 유사도 매칭 실행
                result = await tools.find_similar_name(
                    query_input=test_case['input'],
                    field_type=test_case['field_type'],
                    limit=5
                )
                
                if result["success"]:
                    print(f"✅ 매칭 성공!")
                    print(f"  - 총 후보 수: {result['total_candidates']}개")
                    print(f"  - 매치 결과: {len(result['matches'])}개")
                    print(f"  - 검색 필드 타입: {result.get('email_type', 'N/A')}")
                    
                    if result['matches']:
                        print(f"\n🎯 매치 결과:")
                        for j, match in enumerate(result['matches'], 1):
                            print(f"  {j}. {match.get('email', match.get('name', 'N/A'))}")
                            print(f"     - 유사도 점수: {match.get('similarity_score', 'N/A')}")
                            print(f"     - 매칭 타입: {match.get('match_type', 'N/A')}")
                            print(f"     - 매칭 이유: {match.get('reasoning', 'N/A')}")
                    else:
                        print("  📭 매치 결과가 없습니다.")
                else:
                    print(f"❌ 매칭 실패: {result['error']}")
                    
            except Exception as e:
                print(f"❌ 오류 발생: {e}")
            
            print()
        
        print("✅ 이름 매칭 테스트 완료!")
        
    except Exception as e:
        print(f"❌ 전체 테스트 중 오류 발생: {e}")


async def main():
    """메인 테스트 함수"""
    print("🚀 Weaviate MCP 도구 테스트 시작\n")
    
    # 1. 기존 필터 추출 테스트 ### 각주 처리해뒀었음
    await test_extract_filter()
    
    print("\n" + "=" * 100 + "\n")
    
    # 2. 새로운 이름 매칭 테스트
    await test_name_matching()
    
    print("\n🎉 모든 테스트 완료!")


if __name__ == "__main__":
    asyncio.run(main())
