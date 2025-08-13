#!/usr/bin/env python3
"""
동적 데이터베이스 설정 및 CSV 데이터 삽입 스크립트
다양한 CSV 파일에 대응 가능한 일반화된 데이터베이스 설정 도구
"""

import asyncio
import csv
import os
import sys
import argparse
from pathlib import Path
from datetime import datetime
import re

# 현재 스크립트 디렉토리를 Python 패스에 추가
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from simple_manager import MultipleVectorDBManager
from scripts.generate_schema import generate_schema_from_csv


def normalize_date_to_rfc3339(date_str: str) -> str:
    """날짜 문자열을 RFC3339 형식으로 변환"""
    if not date_str or date_str.strip() == "":
        return "1970-01-01T00:00:00Z"  # 기본값
    
    try:
        # 이미 RFC3339 형식인지 확인
        if re.match(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z?', date_str):
            if not date_str.endswith('Z'):
                date_str += 'Z'
            return date_str
        
        # 다양한 날짜 형식 파싱 시도
        formats = [
            "%Y-%m-%d %H:%M",      # 2000-07-10 23:47
            "%Y-%m-%d %H:%M:%S",   # 2000-07-10 23:47:00
            "%Y-%m-%d",            # 2000-07-10
            "%m/%d/%Y",            # 07/10/2000
            "%m/%d/%Y %H:%M",      # 07/10/2000 23:47
            "%d/%m/%Y",            # 10/07/2000
            "%Y%m%d",              # 20000710
        ]
        
        for fmt in formats:
            try:
                dt = datetime.strptime(date_str, fmt)
                return dt.strftime("%Y-%m-%dT%H:%M:%SZ")
            except ValueError:
                continue
        
        # 파싱 실패 시 기본값 반환
        print(f"   ⚠️ 날짜 형식 파싱 실패: {date_str}, 기본값 사용")
        return "1970-01-01T00:00:00Z"
        
    except Exception as e:
        print(f"   ⚠️ 날짜 변환 오류: {e}, 기본값 사용")
        return "1970-01-01T00:00:00Z"


async def create_database_schema(manager, csv_path, class_name=None, db_name=None, vectorize_fields=None):
    """CSV 기반 데이터베이스 스키마 생성"""
    print("=" * 60)
    print("🏗️ 데이터베이스 스키마 생성")
    print("=" * 60)
    
    if not csv_path.exists():
        print(f"❌ CSV 파일이 존재하지 않습니다: {csv_path}")
        return False, None, None
    
    # CSV 헤더 기반 스키마 생성
    schema, db_name = generate_schema_from_csv(
        csv_path=csv_path,
        class_name=class_name,
        db_name=db_name,
        vectorize_fields=vectorize_fields
    )
    
    print(f"📄 {schema['class']} 스키마 생성 중...")
    success = await manager.create_schema_from_definition(db_name, schema)
    
    if success:
        print(f"✅ {schema['class']} 스키마 생성 성공")
        return True, schema, db_name
    else:
        print(f"❌ {schema['class']} 스키마 생성 실패")
        return False, None, None


async def load_csv_data(manager, csv_path, db_name, schema, text_dir=None, text_field_mapping=None):
    """CSV 데이터 로딩"""
    print("\n" + "=" * 60)
    print("📊 CSV 데이터 로딩")
    print("=" * 60)
    
    # 파일 존재 확인
    if not csv_path.exists():
        print(f"❌ CSV 파일이 존재하지 않습니다: {csv_path}")
        return False
    
    print(f"📁 CSV 파일: {csv_path}")
    if text_dir:
        print(f"📁 텍스트 디렉토리: {text_dir}")
    
    documents = []
    
    try:
        # CSV 파일 읽기
        print("\n1️⃣ CSV 파일 읽기 및 데이터 변환...")
        
        with open(csv_path, 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            
            for row_num, row in enumerate(csv_reader, 1):
                print(f"   📄 처리 중: {row_num}번째 문서")
                
                # 동적 문서 객체 생성
                document = {}
                
                # 모든 CSV 필드를 문서에 매핑
                for header, value in row.items():
                    field_name = header.lower().replace(' ', '_').replace('-', '_')
                    
                    # 데이터 타입별 처리
                    if field_name.endswith('_date') or 'date' in field_name:
                        # 날짜 필드는 RFC3339 형식으로 변환
                        document[field_name] = normalize_date_to_rfc3339(value)
                    elif field_name.endswith('_size') or 'size' in field_name or 'number' in field_name:
                        # 숫자 필드 처리
                        try:
                            document[field_name] = float(value) if value else 0.0
                        except ValueError:
                            document[field_name] = 0.0
                    else:
                        # 텍스트 필드
                        document[field_name] = value if value else ""
                
                # 외부 텍스트 파일에서 내용 읽기 (선택사항)
                content = ""
                if text_dir and text_field_mapping:
                    # 텍스트 파일 경로 필드가 지정된 경우
                    text_path_field = text_field_mapping.get('path_field')
                    if text_path_field and text_path_field in row:
                        text_file_path = text_dir / Path(row[text_path_field]).name
                        
                        if text_file_path.exists():
                            try:
                                with open(text_file_path, 'r', encoding='utf-8') as text_file:
                                    content = text_file.read()
                            except Exception as e:
                                print(f"   ⚠️ 텍스트 파일 읽기 실패 ({text_file_path}): {e}")
                                content = f"텍스트 파일 읽기 실패: {e}"
                        else:
                            print(f"   ⚠️ 텍스트 파일이 존재하지 않음: {text_file_path}")
                            content = "텍스트 파일이 존재하지 않음"
                
                # content 필드 추가/덮어쓰기
                content_field = text_field_mapping.get('content_field', 'content') if text_field_mapping else 'content'
                if content or content_field not in document:
                    document[content_field] = content if content else document.get(content_field, "")
                
                documents.append(document)
        
        print(f"📊 총 {len(documents)}개 문서 로드 완료")
        
        # 데이터베이스에 삽입
        print("\n2️⃣ 데이터베이스에 문서 삽입...")
        
        result = await manager.load_data(db_name, "", documents)
        
        if result.get("success"):
            print(f"✅ {result.get('inserted_count', 0)}개 문서 삽입 성공")
            return True
        else:
            print(f"❌ 문서 삽입 실패: {result.get('error', 'Unknown error')}")
            return False
            
    except Exception as e:
        print(f"❌ CSV 처리 중 오류 발생: {e}")
        import traceback
        traceback.print_exc()
        return False


async def test_database_ingestion(manager, db_name):
    """데이터베이스 인제스션 검증 테스트"""
    print("\n" + "=" * 60)
    print(f"📊 {db_name} 데이터 인제스션 검증")
    print("=" * 60)
    
    if db_name not in manager.list_databases():
        print(f"⚠️ {db_name}가 활성화되지 않음")
        return False
    
    try:
        # 데이터베이스 연결 확인
        print("1️⃣ 데이터베이스 연결 확인...")
        await manager._ensure_db_connection()
        if not manager.db_instance or not manager.initialized:
            print("❌ 데이터베이스 연결 실패")
            return False
        print("✅ 데이터베이스 연결 성공")
        
        # 스키마 존재 확인
        print("2️⃣ 스키마 존재 확인...")
        schemas = manager.list_schemas()
        if not schemas:
            print("❌ 스키마가 존재하지 않음")
            return False
        print(f"✅ 스키마 확인: {len(schemas)}개 스키마 존재")
        
        # 데이터 존재 확인 - 간단한 집계 쿼리 사용
        print("3️⃣ 인제스션된 데이터 확인...")
        
        # Weaviate 집계 쿼리로 총 객체 수 확인
        try:
            # 단순히 데이터가 존재하는지만 확인하는 기본 쿼리
            results = await manager.search([db_name], "*", limit=1)
            
            if ("results" in results and 
                db_name in results["results"] and 
                "results" in results["results"][db_name]):
                
                db_results = results["results"][db_name]["results"]
                print(f"✅ 데이터 존재 확인: 최소 {len(db_results)}개 문서 발견")
                
                # 첫 번째 문서의 기본 정보만 출력 (인제스션 검증용)
                if db_results:
                    first_doc = db_results[0]
                    if hasattr(first_doc, 'to_dict'):
                        doc_dict = first_doc.to_dict()
                    else:
                        doc_dict = first_doc
                    
                    properties = doc_dict.get('properties', {})
                    print(f"   📄 샘플 문서 ID: {doc_dict.get('id', 'N/A')}")
                    print(f"   📝 속성 수: {len(properties)}개")
                    
                    # 속성 이름들만 출력 (값은 검증 불필요)
                    if properties:
                        prop_names = list(properties.keys())[:5]  # 처음 5개만
                        print(f"   🏷️ 주요 속성: {', '.join(prop_names)}")
                
                return True
            else:
                print("❌ 인제스션된 데이터가 없음")
                return False
                
        except Exception as e:
            print(f"❌ 데이터 확인 실패: {e}")
            return False
            
    except Exception as e:
        print(f"❌ 인제스션 검증 중 오류 발생: {e}")
        return False


def main():
    """메인 실행 함수"""
    parser = argparse.ArgumentParser(description="CSV 기반 동적 데이터베이스 설정 및 데이터 삽입")
    parser.add_argument("csv_path", help="CSV 파일 경로")
    parser.add_argument("--class-name", help="Weaviate 클래스명 (기본값: CSV파일명+Document)")
    parser.add_argument("--db-name", help="데이터베이스명 (기본값: CSV파일명_db)")
    parser.add_argument("--text-dir", help="외부 텍스트 파일 디렉토리")
    parser.add_argument("--text-path-field", help="텍스트 파일 경로가 저장된 CSV 필드명")
    parser.add_argument("--content-field", default="content", help="텍스트 내용을 저장할 필드명 (기본값: content)")
    parser.add_argument("--vectorize", nargs='+', help="벡터화할 필드명 목록")
    parser.add_argument("--no-verification", action='store_true', help="인제스션 검증 테스트 건너뛰기")
    
    args = parser.parse_args()
    
    async def run_setup():
        print("🚀 동적 데이터베이스 설정 스크립트 시작")
        print("=" * 60)
        
        manager = None
        
        try:
            # 1. VectorDB 매니저 초기화
            print("1️⃣ VectorDB 매니저 초기화...")
            manager = MultipleVectorDBManager()
            print("✅ 매니저 초기화 완료")
            
            # 2. 스키마 생성
            print("\n2️⃣ 스키마 생성...")
            csv_path = Path(args.csv_path)
            
            schema_success, schema, db_name = await create_database_schema(
                manager=manager,
                csv_path=csv_path,
                class_name=args.class_name,
                db_name=args.db_name,
                vectorize_fields=args.vectorize
            )
            
            if not schema_success:
                print("❌ 스키마 생성 실패로 스크립트 종료")
                return
            
            # 3. 데이터 로딩
            print("\n3️⃣ 데이터 로딩...")
            
            # 텍스트 파일 매핑 설정
            text_field_mapping = None
            if args.text_dir and args.text_path_field:
                text_field_mapping = {
                    'path_field': args.text_path_field,
                    'content_field': args.content_field
                }
            
            text_dir = Path(args.text_dir) if args.text_dir else None
            
            data_success = await load_csv_data(
                manager=manager,
                csv_path=csv_path,
                db_name=db_name,
                schema=schema,
                text_dir=text_dir,
                text_field_mapping=text_field_mapping
            )
            
            if not data_success:
                print("❌ 데이터 로딩 실패")
                return
            
            # 4. 인제스션 검증 테스트 (선택사항)
            if not args.no_verification:
                print("\n4️⃣ 인제스션 검증...")
                ingestion_success = await test_database_ingestion(manager, db_name)
                if not ingestion_success:
                    print("⚠️ 인제스션 검증에서 문제가 발견되었습니다")
            
            # 5. 최종 상태 확인
            print("\n" + "=" * 60)
            print("✅ 데이터베이스 설정 완료!")
            print("=" * 60)
            
            print(f"📊 최종 상태:")
            print(f"   클래스명: {schema['class']}")
            print(f"   DB명: {db_name}")
            print(f"   활성 DB 수: {len(manager.list_databases())}")
            print(f"   활성 DB 목록: {manager.list_databases()}")
            print(f"   사용 가능한 스키마: {len(manager.list_schemas())}개")
            
        except Exception as e:
            print(f"❌ 스크립트 실행 중 오류 발생: {e}")
            import traceback
            traceback.print_exc()
        
        finally:
            # 정리
            if manager:
                manager.close()
                print("\n🔌 VectorDB 연결 종료")
    
    asyncio.run(run_setup())


if __name__ == "__main__":
    main()