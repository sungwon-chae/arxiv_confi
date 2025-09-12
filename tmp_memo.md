#!/usr/bin/env python3
"""
extract_filter_from_query 도구 테스트 스크립트 (수정된 버전)
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
            messages=[{"role": "user", "content": "hi!"}],
            max_tokens=10
        )
        print("Test Query Response: ", response)
        print("✅ OpenAI 클라이언트 설정 완료")
    except Exception as e:
        print(f"❌ OpenAI 클라이언트 설정 실패: {e}")
        return

    print("🔍 extract_filter_from_query 도구 테스트 시작 (MBG 실제 데이터 기반)")
    print("\n📋 테스트 목적:")
    print("  1. Filter 자동 추출 검증")
    print("  2. 벡터DB에서 관련 문서 검색 확인")
    print("  3. 실제 MBG 데이터 기반 GT 검증")
    print("  4. 유사도 기반 검색 성능 확인")

    # 실제 데이터 기반 테스트 쿼리들
    test_queries = [
        # A. 필터 기반 검색 테스트 (실제 존재하는 데이터)
        "Jeong, Yeeun (191) on behalf of korea_com (191-NPM)가 발신한 메시지를 모두 찾아줘",
        "Park, Sep (191) on behalf of korea_com (191-NPM)가 발신한 메시지를 모두 찾아줘",
        "세진 김이 보관한 문서들을 모두 찾아줘",
        "Song, Jieun (191)가 최종 작성한 문서들을 모두 찾아줘",
        "Ju, Hyeyeon (191-Extern-MBK)가 최종 작성한 문서들을 모두 찾아줘",
        "Kim, Ji-Hyun (191)가 최종 작성한 문서들을 모두 찾아줘",
        "msg 확장자 파일들을 모두 찾아줘",
        "pdf 확장자 파일들을 모두 찾아줘",
        "csv 확장자 파일들을 모두 찾아줘",
        
        # B. RAG 벡터 검색 테스트
        "EQC 전기차 관련 모든 자료",
        "MBUX 시스템 관련 기술 자료",
        "4MATIC 사륜구동 시스템 관련 자료",
        "SOCAR와의 카셰어링 협력 관련 자료",
        "SOCAR, 몽클레르, 버질 아블로 협력 관련 모든 자료",
        "전기차 관련 기술 중 MBUX, 4MATIC, 하이브리드 언급된 문서들",
        "SOCAR와의 카셰어링 서비스 협약 체결 과정",
        "EQC 모델의 국내 시장 출시 및 홍보 활동",
        "메르세데스-벤츠의 전동화 전략 및 기술 로드맵",
    ]

    for i, query in enumerate(test_queries, 1):
        print(f"\n테스트 케이스 {i}: {query}")
        print("-" * 60)
        
        try:
            # 필터 추출 및 검색 실행
            result = await tools.extract_filter_from_query(query)
            
            # result가 문자열인지 확인
            if isinstance(result, str):
                if result == "success":
                    print("✅ 필터 추출 및 검색 성공!")
                    print("  - 검색이 완료되었습니다.")
                elif result == "error":
                    print("❌ 필터 추출 또는 검색 실패!")
                    print("  - 오류가 발생했습니다.")
                else:
                    print(f"⚠️ 예상치 못한 결과: {result}")
            else:
                # 딕셔너리인 경우 (기존 로직)
                if result.get("success"):
                    print(f"✅ 필터 추출 성공!")
                    print(f"  - 검색 방식: {result.get('search_type', 'N/A')}")
                    print(f"  - 판단 근거: {result.get('reasoning', 'N/A')}")
                    
                    # 추출된 필터 출력
                    if result.get("filters"):
                        print(f"\n📊 추출된 필터:")
                        for field, value in result["filters"].items():
                            if value is not None:
                                print(f"  - {field}: {value}")
                    
                    # 검색 결과 출력
                    if result.get('search_result'):
                        search_data = result['search_result']
                        print(f"\n📊 검색 결과:")
                        print(f"  - 성공 여부: {search_data.get('success', False)}")
                        print(f"  - 총 결과 수: {len(search_data.get('documents', []))}개")
                        
                        # 문서들 출력
                        if search_data.get('documents'):
                            print(f"\n📄 검색된 문서들:")
                            for j, doc in enumerate(search_data['documents'], 1):
                                print(f"  {j}. 문서 ID: {doc.get('id', 'N/A')}")
                                print(f"     파일명: {doc.get('ori_file_name', 'N/A')}")
                                print(f"     내용 미리보기: {doc.get('content', 'N/A')[:200]}...")
                                print()
                        else:
                            print("  📭 검색 결과가 없습니다.")
                    else:
                        print("  📭 검색할 필터가 없어 단순 RAG 검색을 수행합니다.")
                else:
                    print(f"❌ 필터 추출 실패: {result.get('error', '알 수 없는 오류')}")
                
        except Exception as e:
            print(f"❌ 오류 발생: {e}")
        
        print("\n" + "=" * 80 + "\n")

    print("✅ 테스트 완료!")


async def test_filter_based_search():
    """필터 기반 검색 테스트 (수정된 버전)"""
    try:
        # 도구 인스턴스 생성
        tools = WeaviateMCPTools()
        
        print(" 필터 기반 검색 테스트 시작 (MBG 실제 데이터 기반)")
        
        # 1. 데이터베이스의 unique한 이름 값들 조회
        print("\n👤 1단계: 데이터베이스의 unique한 이름 값들 조회")
        print("-" * 60)
        
        unique_names_result = await tools.get_unique_names()
        
        if unique_names_result['success']:
            print("✅ Unique 이름 조회 성공!")
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
        
        # 2. 필터 기반 검색 테스트 (실제 MBG 데이터 기반)
        print(" 2단계: 필터 기반 검색 테스트 (MBG 실제 데이터 기반)")
        print("-" * 60)
        
        # 실제 존재하는 데이터 기반 테스트 쿼리들
        test_queries = [
            # A. 발신자 필터 테스트 (실제 존재하는 값들)
            "Jeong, Yeeun (191) on behalf of korea_com (191-NPM)가 발신한 메시지를 모두 찾아줘",
            "Park, Sep (191) on behalf of korea_com (191-NPM)가 발신한 메시지를 모두 찾아줘",
            
            # B. 보관자 필터 테스트 (실제 존재하는 값)
            "세진 김이 보관한 문서들을 모두 찾아줘",
            
            # C. 최종 작성자 필터 테스트 (실제 존재하는 값들)
            "Song, Jieun (191)가 최종 작성한 문서들을 모두 찾아줘",
            "Ju, Hyeyeon (191-Extern-MBK)가 최종 작성한 문서들을 모두 찾아줘",
            "Kim, Ji-Hyun (191)가 최종 작성한 문서들을 모두 찾아줘",
            "Joo, Jaeyool (191)가 최종 작성한 문서들을 모두 찾아줘",
            "Park, Jaekyung (191)가 최종 작성한 문서들을 모두 찾아줘",
            "Shim, Ellen (191)가 최종 작성한 문서들을 모두 찾아줘",
            
            # D. 파일 확장자 필터 테스트
            "msg 확장자 파일들을 모두 찾아줘",
            "pdf 확장자 파일들을 모두 찾아줘",
            "csv 확장자 파일들을 모두 찾아줘",
            
            # E. 복합 필터 테스트
            "세진 김이 보관한 msg 파일들을 모두 찾아줘",
            "Song, Jieun (191)가 최종 작성한 pdf 파일들을 모두 찾아줘",
            "Ju, Hyeyeon (191-Extern-MBK)가 최종 작성한 msg 파일들을 모두 찾아줘",
        ]
        
        for i, query in enumerate(test_queries, 1):
            print(f"\n🧪 테스트 케이스 {i}: {query}")
            print("-" * 50)
            
            try:
                # 필터 추출 및 검색 실행
                result = await tools.extract_filter_from_query(query)
                
                # result가 문자열인지 확인
                if isinstance(result, str):
                    if result == "success":
                        print("✅ 필터 추출 및 검색 성공!")
                        print("  - 검색이 완료되었습니다.")
                    elif result == "error":
                        print("❌ 필터 추출 또는 검색 실패!")
                        print("  - 오류가 발생했습니다.")
                    else:
                        print(f"⚠️ 예상치 못한 결과: {result}")
                else:
                    # 딕셔너리인 경우 (기존 로직)
                    if result.get("success"):
                        print(f"✅ 필터 추출 성공!")
                        print(f"  - 검색 방식: {result.get('search_type', 'N/A')}")
                        print(f"  - 판단 근거: {result.get('reasoning', 'N/A')}")
                        
                        # 추출된 필터 출력
                        if result.get("filters"):
                            print(f"\n📊 추출된 필터:")
                            for field, value in result["filters"].items():
                                if value is not None:
                                    print(f"  - {field}: {value}")
                        
                        # 필터 딕셔너리 생성 (None이 아닌 값만)
                        search_filters = {}
                        if result.get("filters"):
                            search_filters = {k: v for k, v in result["filters"].items() if v is not None}
                        
                        if search_filters:
                            print(f"\n 검색에 사용할 필터: {search_filters}")
                            
                            # 문서 검색 실행
                            search_result = await tools.get_document_with_filter(
                                class_name="DocumentChunk",
                                limit=5,
                                filters=search_filters 
                            )
                            
                            print(f"\n📊 검색 결과:")
                            print(f"  - 성공 여부: {search_result.get('success', False)}")
                            print(f"  - 총 결과 수: {len(search_result.get('documents', []))}개")
                            print(f"  - 검색 방식: 필터 검색")
                            print(f"  - 사용된 필터: {search_filters}")
                            
                            # 결과 상세 출력
                            if search_result.get('success') and search_result.get('documents'):
                                print(f"\n📄 검색된 문서들:")
                                for j, doc in enumerate(search_result['documents'], 1):
                                    print(f"  {j}. 문서 ID: {doc.get('id', 'N/A')}")
                                    properties = doc.get('properties', {})
                                    print(f"     파일명: {properties.get('ori_file_name', 'N/A')}")
                                    print(f"     보관자: {properties.get('custodian', 'N/A')}")
                                    print(f"     생성일: {properties.get('s_created_date', 'N/A')}")
                                    print(f"     발송일: {properties.get('sent_date', 'N/A')}")
                                    print(f"     발신자: {properties.get('from_name', 'N/A')}")
                                    print(f"     수신자: {properties.get('to_name', 'N/A')}")
                                    print(f"     확장자: {properties.get('extension', 'N/A')}")
                                    print(f"     내용 미리보기: {properties.get('content', 'N/A')[:200]}...")
                                    print(f"     최종 작성자: {properties.get('last_author', 'N/A')}")
                                    print()
                            else:
                                print("  📭 검색 결과가 없습니다.")
                        else:
                            print("  📭 검색할 필터가 없습니다.")
                    else:
                        print(f"❌ 필터 추출 실패: {result.get('error', '알 수 없는 오류')}")
                        
            except Exception as e:
                print(f"❌ 오류 발생: {e}")
            
            print()
        
        print("✅ 필터 기반 검색 테스트 완료!")
        
    except Exception as e:
        print(f"❌ 전체 테스트 중 오류 발생: {e}")


async def main():
    """메인 테스트 함수"""
    print("�� Weaviate MCP 도구 테스트 시작 (수정된 버전)\n")
    
    # 1. 기존 필터 추출 테스트
    await test_extract_filter()
    
    print("\n" + "=" * 100 + "\n")
    
    # 2. 새로운 필터 기반 검색 테스트
    await test_filter_based_search()
    
    print("\n🎉 모든 테스트 완료!")


if __name__ == "__main__":
    asyncio.run(main()) 
