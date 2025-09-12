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
            messages=[{"role": "user", "content": "hi"}],
            max_tokens=10
        )
        print("Test Query Response: ", response)
        print("✅ OpenAI 클라이언트 설정 완료")
    except Exception as e:
        print(f"❌ OpenAI 클라이언트 설정 실패: {e}")
        return

    print("\n🔍 extract_filter_from_query 도구 테스트 시작 (MBG 실제 데이터 기반)")
    print("\n📋 테스트 목적:")
    print("  1. Filter 자동 추출 검증")
    print("  2. 벡터DB에서 관련 문서 검색 확인")
    print("  3. 실제 MBG 데이터 기반 GT 검증")
    print("  4. 유사도 기반 검색 성능 확인")
    
    print("\n📋 FilterExtractionResult 필드:")
    print("  - custodian: 보관자")
    print("  - ori_file_name: 원본 파일명")
    print("  - s_created_date: 생성일")
    print("  - sent_date: 발송일")
    print("  - from_name: 발신자 이름")
    print("  - to_name: 수신자 이름")
    print("  - cc: 참조자 이름")
    print("  - bcc: 숨은참조자 이름")
    print("  - last_author: 최종 작성자")
    print("  - extension: 파일 확장자")

    # MBG 실제 데이터 기반 테스트 쿼리들
    test_queries = [
        # Filter 기반 검색 (정확한 매칭)
        "Jeong, Yeeun (191) on behalf of korea_com (191-NPM)가 발신한 메시지를 모두 찾아줘",
        "Park, Sep (191) on behalf of korea_com (191-NPM)가 발신한 메시지를 모두 찾아줘",
        
        # Similarity 기반 검색 (유사도 검색)
        "세진 김이 보관한 문서들을 모두 찾아줘",
        "Song, Jieun (191)가 최종 작성한 문서들을 모두 찾아줘",
        "Kim, Ji-Hyun (191)가 최종 작성한 문서들을 모두 찾아줘",
        "Joo, Jaeyool (191)가 최종 작성한 문서들을 모두 찾아줘",
        "Shim, Ellen (191)가 최종 작성한 문서들을 모두 찾아줘",
        "Park, Jaekyung (191)가 최종 작성한 문서들을 모두 찾아줘",
        "Jeong, Yeeun (691)가 최종 작성한 문서들을 모두 찾아줘",
        "Song, Jieun (691)가 최종 작성한 문서들을 모두 찾아줘",
        "Ju, Hyeyeon (191-Extern-MBK)가 최종 작성한 문서들을 모두 찾아줘",
        "Microsoft® Word 2016가 최종 작성한 문서들을 모두 찾아줘",
        "Microsoft® Word Microsoft 365용이 최종 작성한 문서들을 모두 찾아줘",
        "Microsoft® Word for Microsoft 365가 최종 작성한 문서들을 모두 찾아줘",
        
        # 복합 필터 테스트
        "세진 김이 보관하고 jpg 확장자인 문서들을 모두 찾아줘",
        "Song, Jieun (191)가 최종 작성하고 docx 확장자인 문서들을 모두 찾아줘",
        "Kim, Ji-Hyun (191)가 최종 작성하고 pdf 확장자인 문서들을 모두 찾아줘",
        
        # RAG 검색 테스트
        "4MATIC 사륜구동 시스템 관련 자료",
        "SOCAR와의 카셰어링 협력 관련 자료",
        "SOCAR, 몽클레르, 버질 아블로 협력 관련 모든 자료",
        "전기차 관련 기술 중 MBUX, 4MATIC, 하이브리드 언급된 문서들",
        "SOCAR와의 카셰어링 서비스 협약 체결 과정",
        "EQC 모델의 국내 시장 출시 및 홍보 활동",
        "메르세데스-벤츠의 전동화 전략 및 기술 로드맵"
    ]

    print(f"\n📊 총 {len(test_queries)}개 테스트 케이스 실행 예정")

    # 각 테스트 케이스 실행
    for i, query in enumerate(test_queries, 1):
        print(f"\n테스트 케이스 {i}: {query}")
        print("-" * 60)
        
        try:
            # 필터 추출 및 검색 실행
            result = await tools.extract_filter_from_query(query)
            
            # result가 문자열인지 확인
            if isinstance(result, str):
                if result == "success":
                    print("✅ 필터 추출 성공!")
                    print("  - 검색이 완료되었습니다.")
                elif result == "error":
                    print("❌ 필터 추출 실패!")
                    print("  - 오류가 발생했습니다.")
                else:
                    print(f"⚠️ 예상치 못한 결과: {result}")
            else:
                # 딕셔너리인 경우
                if result.get("search_type"):
                    print("✅ 필터 추출 성공!")
                    print(f"📊 추출된 필터:")
                    filters = result.get("filters", {})
                    for key, value in filters.items():
                        print(f"  - {key}: {value}")
                    
                    print(f"🔍 검색 방식: {result.get('search_type')}")
                    print(f"💭 판단 근거: {result.get('reasoning', 'N/A')}")
                    
                    # 검색 결과가 있는 경우
                    if "search_results" in result:
                        search_results = result["search_results"]
                        print(f"📋 검색에 사용할 필터: {result.get('filters', {})}")
                        
                        if search_results.get("success"):
                            print(f"📊 검색 결과:")
                            print(f"  - 성공 여부: {search_results.get('success')}")
                            print(f"  - 총 결과 수: {search_results.get('total_results', 0)}개")
                            print(f"  - 검색 방식: {search_results.get('search_type', 'N/A')}")
                            print(f"  - 사용된 필터: {search_results.get('filters', {})}")
                            
                            documents = search_results.get("documents", [])
                            if documents:
                                print(f"\n📄 검색된 문서들:")
                                for j, doc in enumerate(documents, 1):
                                    print(f"  {j}. 문서 ID: {doc.get('id', 'N/A')}")
                                    print(f"     파일명: {doc.get('ori_file_name', 'N/A')}")
                                    print(f"     보관자: {doc.get('custodian', 'N/A')}")
                                    print(f"     생성일: {doc.get('s_created_date', 'N/A')}")
                                    print(f"     발송일: {doc.get('sent_date', 'N/A')}")
                                    print(f"     발신자: {doc.get('from_email', 'N/A')}")
                                    print(f"     수신자: {doc.get('to_email', 'N/A')}")
                                    print(f"     확장자: {doc.get('extension', 'N/A')}")
                                    print(f"     내용 미리보기: {doc.get('content', 'N/A')[:100]}...")
                                    print(f"     최종 작성자: {doc.get('last_author', 'N/A')}")
                                    print()
                            else:
                                print("  📭 검색 결과가 없습니다.")
                        else:
                            print(f"❌ 검색 실패: {search_results.get('error', '알 수 없는 오류')}")
                    else:
                        print("  📭 검색할 필터가 없어 단순 RAG 검색을 수행합니다.")
                else:
                    print(f"❌ 필터 추출 실패: {result.get('error', '알 수 없는 오류')}")
            
        except Exception as e:
            print(f"❌ 오류 발생: {e}")
        
        print("\n" + "=" * 80 + "\n")

    print("✅ 테스트 완료!")


async def test_name_matching():
    """이름 매칭 기능을 테스트합니다."""
    
    print("\n" + "=" * 80)
    print("🔍 이름 매칭 기능 테스트 시작")
    
    # 도구 인스턴스 생성
    tools = WeaviateMCPTools()
    
    print("\n👤 1단계: 데이터베이스의 unique한 이름 값들 조회")
    print("-" * 60)
    
    try:
        # unique한 이름들 조회
        unique_names = await tools.get_unique_names()
        
        if unique_names.get("success"):
            print("✅ Unique 이름 조회 성공!")
            print(f"  - from_email 개수: {len(unique_names.get('from_email', []))}개")
            print(f"  - to_email 개수: {len(unique_names.get('to_email', []))}개")
            print(f"  - custodian 개수: {len(unique_names.get('custodian', []))}개")
            print(f"  - last_author 개수: {len(unique_names.get('last_author', []))}개")
            
            print(f"\n📤 from_email 샘플 (처음 10개):")
            for i, name in enumerate(unique_names.get('from_email', [])[:10], 1):
                print(f"  {i}. {name}")
            
            print(f"\n📥 to_email 샘플 (처음 10개):")
            for i, name in enumerate(unique_names.get('to_email', [])[:10], 1):
                print(f"  {i}. {name}")
            
            print(f"\n👤 custodian 샘플 (처음 10개):")
            for i, name in enumerate(unique_names.get('custodian', [])[:10], 1):
                print(f"  {i}. {name}")
            
            print(f"\n✍️ last_author 샘플 (처음 10개):")
            for i, name in enumerate(unique_names.get('last_author', [])[:10], 1):
                print(f"  {i}. {name}")
        else:
            print(f"❌ Unique 이름 조회 실패: {unique_names.get('error', '알 수 없는 오류')}")
            return
            
    except Exception as e:
        print(f"❌ 오류 발생: {e}")
        return
    
    print("\n" + "=" * 80)
    print("\n🔍 2단계: 이름 유사도 매칭 테스트")
    print("-" * 60)
    
    # 이름 매칭 테스트 케이스들
    test_names = [
        "Jeong, Yeeun (191)",
        "Park, Sep (191)",
        "세진 김",
        "Song, Jieun (191)",
        "Ju, Hyeyeon (191-Extern-MBK)",
        "Kim, Ji-Hyun (191)"
    ]
    
    for i, test_name in enumerate(test_names, 1):
        print(f"\n🧪 테스트 케이스 {i}: MBG {'발신자' if i <= 2 else '보관자' if i == 3 else '최종 작성자' if i <= 5 else '작성자'} 이름으로 검색")
        print(f"   입력: '{test_name}'")
        print("-" * 50)
        
        try:
            # 이름 매칭 실행
            match_result = await tools.find_similar_name(test_name)
            
            if match_result.get("success"):
                print("✅ 매칭 성공!")
                print(f"  - 총 후보 수: {len(match_result.get('candidates', []))}개")
                print(f"  - 매치 결과: {len(match_result.get('matches', []))}개")
                print(f"  - 검색 필드 타입: {match_result.get('search_type', 'N/A')}")
                
                matches = match_result.get("matches", [])
                if matches:
                    print(f"\n🎯 매치 결과:")
                    for j, match in enumerate(matches, 1):
                        print(f"  {j}. {match.get('name', 'N/A')}")
                        print(f"     - 유사도 점수: {match.get('similarity_score', 0)}")
                        print(f"     - 매칭 타입: {match.get('match_type', 'N/A')}")
                        print(f"     - 매칭 이유: {match.get('reason', 'N/A')}")
                        print()
                else:
                    print("  📭 매치 결과가 없습니다.")
            else:
                print(f"❌ 매칭 실패: {match_result.get('error', '알 수 없는 오류')}")
                
        except Exception as e:
            print(f"❌ 오류 발생: {e}")
    
    print("✅ 이름 매칭 테스트 완료!")


async def main():
    """메인 함수"""
    print("🚀 Weaviate MCP 도구 테스트 시작")
    
    # 1단계: extract_filter_from_query 테스트
    await test_extract_filter()
    
    # 2단계: 이름 매칭 테스트
    await test_name_matching()
    
    print("\n🎉 모든 테스트 완료!")


if __name__ == "__main__":
    asyncio.run(main())
