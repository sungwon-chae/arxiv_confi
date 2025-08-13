#!/usr/bin/env python3
"""
CSV 파일 헤더를 기반으로 동적 스키마 JSON 파일 생성
다양한 CSV 파일에 대응 가능한 일반화된 스키마 생성기
"""

import csv
import json
import os
import argparse
from pathlib import Path


def generate_schema_from_csv(csv_path, class_name=None, db_name=None, output_path=None, vectorize_fields=None):
    """CSV 파일 헤더를 기반으로 스키마 생성하고 JSON 파일로 저장"""
    print("📊 CSV 헤더 분석 중...")
    
    # CSV 파일 헤더 읽기
    with open(csv_path, 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        headers = csv_reader.fieldnames
    
    print(f"📋 발견된 헤더: {headers}")
    
    # 클래스명과 DB명 자동 생성
    if class_name is None:
        csv_name = Path(csv_path).stem.replace('_schema', '').replace('_', '').title()
        class_name = f"{csv_name}Document"
    
    if db_name is None:
        csv_name = Path(csv_path).stem.replace('_schema', '')
        db_name = f"{csv_name}_db"
    
    print(f"🏷️ 클래스명: {class_name}")
    print(f"🏷️ DB명: {db_name}")
    
    # 데이터 타입 매핑 (확장된 패턴)
    type_mapping = {
        'date': ['date'],
        'time': ['date'],
        'created': ['date'],
        'modified': ['date'],
        'updated': ['date'],
        'size': ['number'],
        'number': ['number'],
        'count': ['number'],
        'amount': ['number'],
        'price': ['number'],
        'score': ['number'],
        'rating': ['number'],
        'id': ['text'],
        'uuid': ['text'],
        'hash': ['text'],
        'email': ['text'],
        'mail': ['text'],
        'file': ['text'],
        'path': ['text'],
        'url': ['text'],
        'uri': ['text'],
        'phone': ['text'],
        'address': ['text'],
        'location': ['text'],
        'category': ['text'],
        'type': ['text'],
        'status': ['text'],
        'state': ['text']
    }
    
    # 벡터화할 필드 결정
    if vectorize_fields is None:
        # 기본적으로 텍스트 내용이 들어갈 만한 필드들을 벡터화
        default_vectorize_patterns = ['content', 'text', 'description', 'summary', 'body', 'message']
        vectorize_fields = []
    
    # 스키마 속성 생성
    properties = []
    vectorizer_config = {}
    
    for header in headers:
        # 헤더를 소문자로 변환하고 공백을 언더스코어로 치환
        field_name = header.lower().replace(' ', '_').replace('-', '_')
        
        # 데이터 타입 결정
        data_type = ['text']  # 기본값
        for keyword, type_val in type_mapping.items():
            if keyword in field_name.lower():
                data_type = type_val
                break
        
        # 속성 정의
        property_def = {
            "name": field_name,
            "dataType": data_type,
            "description": header
        }
        properties.append(property_def)
        
        # 벡터화 설정
        should_vectorize = False
        if vectorize_fields:
            # 명시적으로 지정된 필드들
            should_vectorize = field_name in vectorize_fields
        else:
            # 기본 패턴 매칭
            should_vectorize = any(pattern in field_name.lower() for pattern in ['content', 'text', 'description', 'summary', 'body', 'message'])
        
        vectorizer_config[field_name] = {"skip": not should_vectorize}
    
    # content 필드가 없으면 추가 (텍스트 파일에서 읽을 내용용)
    if 'content' not in [p['name'] for p in properties]:
        properties.append({
            "name": "content",
            "dataType": ["text"],
            "description": "Document Content"
        })
        vectorizer_config['content'] = {"skip": False}
    
    # 완전한 스키마 생성
    schema = {
        "class": class_name,
        "vectorizer": "text2vec-openai",
        "properties": properties,
        "moduleConfig": {
            "text2vec-openai": {
                "model": "/data/models_ckpt/bge-m3",
                "type": "text",
                "vectorizeClassName": False,
                "vectorizePropertyName": False,
                "properties": vectorizer_config
            }
        }
    }
    
    print(f"✅ {len(properties)}개 속성을 가진 스키마 생성 완료")
    
    # JSON 파일로 저장
    if output_path is None:
        schema_name = Path(csv_path).stem.replace('_schema', '') + '_schema.json'
        output_path = Path(csv_path).parent / schema_name
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(schema, f, ensure_ascii=False, indent=2)
    
    print(f"📄 스키마 파일 저장: {output_path}")
    return schema, db_name


def main():
    """메인 실행 함수"""
    parser = argparse.ArgumentParser(description="CSV 파일 헤더를 기반으로 동적 스키마 생성")
    parser.add_argument("csv_path", help="CSV 파일 경로")
    parser.add_argument("--class-name", help="Weaviate 클래스명 (기본값: CSV파일명+Document)")
    parser.add_argument("--db-name", help="데이터베이스명 (기본값: CSV파일명_db)")
    parser.add_argument("--output", help="출력 JSON 파일 경로")
    parser.add_argument("--vectorize", nargs='+', help="벡터화할 필드명 목록")
    
    args = parser.parse_args()
    
    print("🏗️ 동적 스키마 생성기")
    print("=" * 50)
    
    # CSV 파일 경로 확인
    csv_path = Path(args.csv_path)
    if not csv_path.exists():
        print(f"❌ CSV 파일이 존재하지 않습니다: {csv_path}")
        return
    
    # 스키마 생성
    schema, db_name = generate_schema_from_csv(
        csv_path=csv_path,
        class_name=args.class_name,
        db_name=args.db_name,
        output_path=args.output,
        vectorize_fields=args.vectorize
    )
    
    # 생성된 스키마 정보 출력
    print("\n📊 생성된 스키마 정보:")
    print(f"   클래스명: {schema['class']}")
    print(f"   DB명: {db_name}")
    print(f"   벡터라이저: {schema['vectorizer']}")
    print(f"   속성 수: {len(schema['properties'])}")
    
    print("\n📋 속성 목록:")
    vectorized_count = 0
    for i, prop in enumerate(schema['properties'], 1):
        data_type = prop['dataType'][0]
        is_vectorized = not schema['moduleConfig']['text2vec-openai']['properties'][prop['name']]['skip']
        vectorized = "✅" if is_vectorized else "❌"
        if is_vectorized:
            vectorized_count += 1
        print(f"   {i:2d}. {prop['name']:<20} ({data_type:<8}) {vectorized} - {prop['description']}")
    
    print(f"\n📈 벡터화 필드 수: {vectorized_count}/{len(schema['properties'])}")
    print("\n✅ 스키마 생성 완료!")


def generate_precedent_schema(output_path=None):
    """판례 데이터를 위한 스키마 생성"""
    print("📊 판례 스키마 생성 중...")
    
    # 판례 스키마 정의
    schema = {
        "class": "Precedent",
        "vectorizer": "text2vec-openai",
        "properties": [
            {"name": "text", "dataType": ["text"], "description": "판례 내용"},
            {"name": "documentId", "dataType": ["int"], "description": "문서 ID"},
            {"name": "documentName", "dataType": ["text"], "description": "사건명"},
            {"name": "documentType", "dataType": ["text"], "description": "사건 유형"},
            {"name": "source", "dataType": ["text"], "description": "출처"}
        ],
        "moduleConfig": {
            "text2vec-openai": {
                "model": "/data/models_ckpt/bge-m3",
                "type": "text",
                "vectorizeClassName": False,
                "vectorizePropertyName": False,
                "properties": {
                    "text": {"skip": False},
                    "documentId": {"skip": True},
                    "documentName": {"skip": True},
                    "documentType": {"skip": True},
                    "source": {"skip": True}
                }
            }
        }
    }
    
    # JSON 파일로 저장
    if output_path is None:
        output_path = Path(__file__).parent / "../schema_examples/precedent_schema.json"
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(schema, f, ensure_ascii=False, indent=4)
    
    print(f"📄 판례 스키마 파일 저장: {output_path}")
    return schema


if __name__ == "__main__":
    main()