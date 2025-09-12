#!/usr/bin/env python3
"""
벡터DB 데이터 구조 및 내용 조회 스크립트
실제 데이터를 확인해서 테스트 쿼리 작성에 활용
"""

import asyncio
import sys
import os
from pathlib import Path

# 현재 디렉토리를 Python 경로에 추가
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

from mcp_tools import WeaviateMCPTools


async def explore_database():
    """데이터베이스 구조 및 내용을 탐색합니다."""
    
    print("�� 벡터DB 데이터 구조 및 내용 탐색 시작\n")
    
    # 도구 인스턴스 생성
    tools = WeaviateMCPTools()
    
    # 1. 스키마 정보 조회
    print("📋 1단계: 데이터베이스 스키마 정보")
    print("-" * 60)
    
    try:
        # 스키마 조회 (간접적으로)
        unique_names_result = await tools.get_unique_names()
        
        if unique_names_result['success']:
            print("✅ 데이터베이스 연결 성공!")
            print(f"  - from_email 개수: {unique_names_result['total_from_emails']}개")
            print(f"  - to_email 개수: {unique_names_result['total_to_emails']}개")
            print(f"  - custodian 개수: {unique_names_result['total_custodian']}개")
            print(f"  - last_author 개수: {unique_names_result['total_last_author']}개")
        else:
            print(f"❌ 데이터베이스 연결 실패: {unique_names_result['error']}")
            return
            
    except Exception as e:
        print(f"❌ 스키마 조회 중 오류: {e}")
        return
    
    # 2. 실제 데이터 샘플 조회
    print("\n�� 2단계: 실제 데이터 샘플 조회")
    print("-" * 60)
    
    # 다양한 필터로 샘플 데이터 조회
    sample_queries = [
        # 기본 조회
        "모든 문서를 5개만 보여줘",
        
        # 발신자별 조회
        "Jeong, Yeeun이 발신한 문서들을 보여줘",
        "Park, Sep이 발신한 문서들을 보여줘",
        
        # 보관자별 조회
        "세진 김이 보관한 문서들을 보여줘",
        
        # 파일 타입별 조회
        "msg 파일들을 보여줘",
        "pdf 파일들을 보여줘",
        "csv 파일들을 보여줘",
        
        # 작성자별 조회
        "Song, Jieun이 작성한 문서들을 보여줘",
        "Ju, Hyeyeon이 작성한 문서들을 보여줘",
    ]
    
    for i, query in enumerate(sample_queries, 1):
        print(f"\n🔍 샘플 조회 {i}: {query}")
        print("-" * 40)
        
        try:
            result = await tools.extract_filter_from_query(query)
            
            if isinstance(result, str):
                if result == "success":
                    print("✅ 조회 성공!")
                elif result == "error":
                    print("❌ 조회 실패!")
                else:
                    print(f"⚠️ 예상치 못한 결과: {result}")
            else:
                # 딕셔너리인 경우 상세 정보 출력
                if result.get("success"):
                    print(f"✅ 조회 성공!")
                    print(f"  - 검색 방식: {result.get('search_type', 'N/A')}")
                    
                    # 추출된 필터 출력
                    if result.get("filters"):
                        print(f"  - 추출된 필터:")
                        for field, value in result["filters"].items():
                            if value is not None:
                                print(f"    * {field}: {value}")
                    
                    # 검색 결과 출력
                    if result.get('search_result'):
                        search_data = result['search_result']
                        documents = search_data.get('documents', [])
                        print(f"  - 검색된 문서 수: {len(documents)}개")
                        
                        # 첫 번째 문서의 상세 정보 출력
                        if documents:
                            first_doc = documents[0]
                            print(f"\n  📄 첫 번째 문서 상세 정보:")
                            print(f"    - 문서 ID: {first_doc.get('id', 'N/A')}")
                            print(f"    - 파일명: {first_doc.get('ori_file_name', 'N/A')}")
                            print(f"    - 보관자: {first_doc.get('custodian', 'N/A')}")
                            print(f"    - 생성일: {first_doc.get('s_created_date', 'N/A')}")
                            print(f"    - 발송일: {first_doc.get('sent_date', 'N/A')}")
                            print(f"    - 발신자: {first_doc.get('from_name', 'N/A')}")
                            print(f"    - 수신자: {first_doc.get('to_name', 'N/A')}")
                            print(f"    - 확장자: {first_doc.get('extension', 'N/A')}")
                            print(f"    - 최종 작성자: {first_doc.get('last_author', 'N/A')}")
                            print(f"    - 내용 미리보기: {first_doc.get('content', 'N/A')[:150]}...")
                else:
                    print(f"❌ 조회 실패: {result.get('error', '알 수 없는 오류')}")
                    
        except Exception as e:
            print(f"❌ 조회 중 오류: {e}")
        
        print()
    
    # 3. 필드별 고유값 상세 조회
    print("\n📋 3단계: 필드별 고유값 상세 조회")
    print("-" * 60)
    
    if unique_names_result['success']:
        names = unique_names_result['names']
        
        # from_email 상세 조회
        if names.get('from_emails'):
            print(f"\n📤 from_email 전체 목록 ({len(names['from_emails'])}개):")
            for i, email in enumerate(names['from_emails'], 1):
                print(f"  {i}. {email}")
        
        # to_email 상세 조회
        if names.get('to_emails'):
            print(f"\n📥 to_email 전체 목록 ({len(names['to_emails'])}개):")
            for i, email in enumerate(names['to_emails'], 1):
                print(f"  {i}. {email}")
        
        # custodian 상세 조회
        if names.get('custodian'):
            print(f"\n👤 custodian 전체 목록 ({len(names['custodian'])}개):")
            for i, custodian in enumerate(names['custodian'], 1):
                print(f"  {i}. {custodian}")
        
        # last_author 상세 조회
        if names.get('last_author'):
            print(f"\n✍️ last_author 전체 목록 ({len(names['last_author'])}개):")
            for i, author in enumerate(names['last_author'], 1):
                print(f"  {i}. {author}")
    
    # 4. 테스트 쿼리 제안
    print("\n�� 4단계: 추천 테스트 쿼리")
    print("-" * 60)
    
    print("실제 데이터를 바탕으로 한 추천 테스트 쿼리들:")
    print("\n�� 필터 기반 검색 쿼리:")
    print("  1. 'Jeong, Yeeun (191) on behalf of korea_com (191-NPM)가 발신한 메시지를 모두 찾아줘'")
    print("  2. 'Park, Sep (191) on behalf of korea_com (191-NPM)가 발신한 메시지를 모두 찾아줘'")
    print("  3. '세진 김이 보관한 문서들을 모두 찾아줘'")
    print("  4. 'Song, Jieun (191)가 최종 작성한 문서들을 모두 찾아줘'")
    print("  5. 'msg 확장자 파일들을 모두 찾아줘'")
    print("  6. 'pdf 확장자 파일들을 모두 찾아줘'")
    print("  7. 'csv 확장자 파일들을 모두 찾아줘'")
    
    print("\n🔍 복합 필터 검색 쿼리:")
    print("  8. '세진 김이 보관한 msg 파일들을 모두 찾아줘'")
    print("  9. 'Song, Jieun (191)가 최종 작성한 pdf 파일들을 모두 찾아줘'")
    
    print("\n🔍 RAG 벡터 검색 쿼리:")
    print("  10. 'EQC 전기차 관련 모든 자료'")
    print("  11. 'MBUX 시스템 관련 기술 자료'")
    print("  12. 'SOCAR와의 카셰어링 협력 관련 자료'")
    
    print("\n✅ 데이터 탐색 완료!")
    print("\n💡 이제 위의 추천 쿼리들을 바탕으로 테스트 쿼리를 작성하세요!")


async def main():
    """메인 함수"""
    await explore_database()


if __name__ == "__main__":
    asyncio.run(main()) 
