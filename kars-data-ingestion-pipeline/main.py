#!/usr/bin/env python3
"""
Data Ingestion Pipeline - 고도화된 데이터 처리 시스템
processors 기반의 통합 파이프라인 CLI
"""

import asyncio
import argparse
import logging
import sys
from pathlib import Path
from typing import List, Optional
import json

from pipeline_engine import DataIngestionPipeline, PipelineConfig

# 로깅 설정
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

def setup_argument_parser():
    """CLI 인수 파서 설정"""
    parser = argparse.ArgumentParser(
        description="고도화된 데이터 인제스션 파이프라인",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
사용 예시:
  # CSV 파일 고급 처리
  python main.py process-csv data.csv --text-dir texts/ --build-kg
  
  # 멀티모달 문서 처리
  python main.py process-documents *.pdf --extract-tables --build-kg
  
  # 지식 그래프만 구축
  python main.py build-kg processed_data/ --output kg.json
  
  # 기존 방식 호환 (간단한 CSV 처리)
  python main.py csv-legacy data.csv --text-dir texts/
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='사용 가능한 명령들')
    
    # CSV 고급 처리
    csv_parser = subparsers.add_parser('process-csv', help='CSV 파일 고급 처리')
    csv_parser.add_argument('csv_path', help='CSV 파일 경로')
    csv_parser.add_argument('--text-dir', help='외부 텍스트 파일 디렉토리')
    csv_parser.add_argument('--text-path-field', help='텍스트 파일 경로 필드명')
    csv_parser.add_argument('--content-field', default='content', help='콘텐츠 필드명')
    csv_parser.add_argument('--class-name', help='Weaviate 클래스명')
    csv_parser.add_argument('--db-name', help='데이터베이스명')
    csv_parser.add_argument('--vectorize', nargs='+', help='벡터화할 필드들')
    csv_parser.add_argument('--build-kg', action='store_true', help='지식 그래프 구축')
    csv_parser.add_argument('--chunk-strategy', choices=['semantic', 'sentence', 'fixed'], 
                           default='semantic', help='청킹 전략')
    csv_parser.add_argument('--output-dir', help='출력 디렉토리')
    
    # 멀티모달 문서 처리  
    docs_parser = subparsers.add_parser('process-documents', help='멀티모달 문서 처리')
    docs_parser.add_argument('file_paths', nargs='+', help='처리할 문서 파일들')
    docs_parser.add_argument('--batch-size', type=int, default=10, help='배치 크기')
    docs_parser.add_argument('--no-images', action='store_true', help='이미지 추출 비활성화')
    docs_parser.add_argument('--no-tables', action='store_true', help='테이블 추출 비활성화')
    docs_parser.add_argument('--build-kg', action='store_true', help='지식 그래프 구축')
    docs_parser.add_argument('--db-name', help='데이터베이스명')
    docs_parser.add_argument('--output-dir', help='출력 디렉토리')
    docs_parser.add_argument('--output-format', choices=['structured_json', 'markdown', 'elements'],
                           default='structured_json', help='출력 형식')
    
    # 지식 그래프 독립 구축
    kg_parser = subparsers.add_parser('build-kg', help='지식 그래프 독립 구축')
    kg_parser.add_argument('data_path', help='처리된 데이터 경로 (디렉토리 또는 JSON 파일)')
    kg_parser.add_argument('--output', required=True, help='지식 그래프 출력 파일')
    kg_parser.add_argument('--min-confidence', type=float, default=0.5, help='최소 엔티티 신뢰도')
    kg_parser.add_argument('--similarity-threshold', type=float, default=0.8, help='유사도 임계값')
    
    # 기존 방식 호환 (legacy)
    legacy_parser = subparsers.add_parser('csv-legacy', help='기존 방식 CSV 처리 (호환성)')
    legacy_parser.add_argument('csv_path', help='CSV 파일 경로')
    legacy_parser.add_argument('--text-dir', help='외부 텍스트 파일 디렉토리')
    legacy_parser.add_argument('--text-path-field', help='텍스트 파일 경로 필드명')
    legacy_parser.add_argument('--class-name', help='Weaviate 클래스명')
    legacy_parser.add_argument('--db-name', help='데이터베이스명')
    legacy_parser.add_argument('--vectorize', nargs='+', help='벡터화할 필드들')
    legacy_parser.add_argument('--no-verification', action='store_true', help='인제스션 검증 테스트 건너뛰기')
    
    return parser

async def cmd_process_csv(args):
    """CSV 고급 처리 명령"""
    logger.info(f"CSV 고급 처리 시작: {args.csv_path}")
    
    config = PipelineConfig(
        db_name=args.db_name,
        class_name=args.class_name,
        vectorize_fields=args.vectorize,
        chunk_strategy=args.chunk_strategy,
        build_knowledge_graph=args.build_kg,
        output_dir=Path(args.output_dir) if args.output_dir else None
    )
    
    pipeline = DataIngestionPipeline(config)
    
    try:
        result = await pipeline.process_csv_enhanced(
            csv_path=args.csv_path,
            text_dir=args.text_dir,
            text_path_field=args.text_path_field,
            content_field=args.content_field
        )
        
        if result["success"]:
            logger.info("✅ CSV 처리 완료!")
            logger.info(f"📊 데이터베이스: {result['database_name']}")
            logger.info(f"📄 총 문서 수: {result['total_documents']}")
            
            if result.get("knowledge_graph_stats"):
                kg_stats = result["knowledge_graph_stats"]
                logger.info(f"🧠 지식 그래프: {kg_stats['basic_stats']['total_entities']}개 엔티티, "
                           f"{kg_stats['basic_stats']['total_relationships']}개 관계")
        else:
            logger.error(f"❌ CSV 처리 실패: {result.get('error')}")
            return 1
            
    finally:
        pipeline.close()
    
    return 0

async def cmd_process_documents(args):
    """멀티모달 문서 처리 명령"""
    # 파일 경로 확장 (glob 패턴 지원)
    file_paths = []
    for pattern in args.file_paths:
        if '*' in pattern or '?' in pattern:
            from glob import glob
            file_paths.extend(glob(pattern))
        else:
            file_paths.append(pattern)
    
    logger.info(f"멀티모달 문서 처리 시작: {len(file_paths)}개 파일")
    
    config = PipelineConfig(
        db_name=args.db_name,
        extract_images=not args.no_images,
        extract_tables=not args.no_tables,
        build_knowledge_graph=args.build_kg,
        output_format=args.output_format,
        output_dir=Path(args.output_dir) if args.output_dir else None
    )
    
    pipeline = DataIngestionPipeline(config)
    
    try:
        result = await pipeline.process_documents_multimodal(
            file_paths=file_paths,
            batch_size=args.batch_size
        )
        
        if result["success"]:
            logger.info("✅ 문서 처리 완료!")
            logger.info(f"📊 성공: {result['successful_files']}/{result['total_files']} 파일")
            logger.info(f"📄 총 요소: {result['processing_stats']['total_elements']}개")
            
            if result["failed_files"] > 0:
                logger.warning(f"⚠️ 실패한 파일: {result['failed_files']}개")
            
            if result.get("knowledge_graph"):
                kg_stats = result["knowledge_graph"]["stats"]
                logger.info(f"🧠 지식 그래프: {kg_stats['basic_stats']['total_entities']}개 엔티티")
        else:
            logger.error("❌ 문서 처리 실패")
            return 1
            
    finally:
        pipeline.close()
    
    return 0

async def cmd_build_kg(args):
    """지식 그래프 독립 구축 명령"""
    logger.info(f"지식 그래프 구축 시작: {args.data_path}")
    
    # 데이터 로드
    data_path = Path(args.data_path)
    processed_documents = []
    
    if data_path.is_file() and data_path.suffix == '.json':
        # JSON 파일에서 로드
        with open(data_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, list):
                processed_documents = data
            elif isinstance(data, dict) and 'processed_documents' in data:
                processed_documents = data['processed_documents']
    elif data_path.is_dir():
        # 디렉토리에서 JSON 파일들 로드
        for json_file in data_path.glob('*.json'):
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                processed_documents.append(data)
    else:
        logger.error(f"❌ 지원하지 않는 데이터 형식: {data_path}")
        return 1
    
    if not processed_documents:
        logger.error("❌ 처리할 문서 데이터가 없습니다")
        return 1
    
    config = PipelineConfig(
        min_entity_confidence=args.min_confidence,
        similarity_threshold=args.similarity_threshold,
        build_knowledge_graph=True
    )
    
    pipeline = DataIngestionPipeline(config)
    
    try:
        result = await pipeline.build_knowledge_graph_standalone(
            processed_documents=processed_documents,
            output_path=args.output
        )
        
        if result["success"]:
            logger.info("✅ 지식 그래프 구축 완료!")
            logger.info(f"📁 저장 경로: {args.output}")
            
            stats = result["stats"]
            logger.info(f"🧠 엔티티: {stats['basic_stats']['total_entities']}개")
            logger.info(f"🔗 관계: {stats['basic_stats']['total_relationships']}개")
        else:
            logger.error(f"❌ 지식 그래프 구축 실패: {result.get('error')}")
            return 1
            
    finally:
        pipeline.close()
    
    return 0

async def cmd_csv_legacy(args):
    """기존 방식 CSV 처리 (호환성)"""
    logger.info(f"기존 방식 CSV 처리: {args.csv_path}")
    
    # 기존 스크립트의 async 함수를 직접 호출
    try:
        from simple_manager import MultipleVectorDBManager
        from scripts.generate_schema import generate_schema_from_csv
        from scripts.setup_database import (
            create_database_schema, load_csv_data, test_database_ingestion,
            normalize_date_to_rfc3339
        )
        from pathlib import Path
        
        logger.info("🚀 기존 방식 데이터베이스 설정 스크립트 시작")
        
        manager = None
        
        try:
            # 1. VectorDB 매니저 초기화
            logger.info("1️⃣ VectorDB 매니저 초기화...")
            manager = MultipleVectorDBManager()
            logger.info("✅ 매니저 초기화 완료")
            
            # 2. 스키마 생성
            logger.info("2️⃣ 스키마 생성...")
            csv_path = Path(args.csv_path)
            
            schema_success, schema, db_name = await create_database_schema(
                manager=manager,
                csv_path=csv_path,
                class_name=args.class_name,
                db_name=args.db_name,
                vectorize_fields=args.vectorize
            )
            
            if not schema_success:
                logger.error("❌ 스키마 생성 실패로 스크립트 종료")
                return 1
            
            # 3. 데이터 로딩
            logger.info("3️⃣ 데이터 로딩...")
            
            # 텍스트 파일 매핑 설정
            text_field_mapping = None
            if args.text_dir and args.text_path_field:
                text_field_mapping = {
                    'path_field': args.text_path_field,
                    'content_field': 'content'
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
                logger.error("❌ 데이터 로딩 실패")
                return 1
            
            # 4. 인제스션 검증 테스트 (선택사항)
            if not args.no_verification:
                logger.info("4️⃣ 인제스션 검증...")
                await test_database_ingestion(manager, db_name)
            
            # 5. 최종 상태 확인
            logger.info("✅ 데이터베이스 설정 완료!")
            logger.info(f"📊 최종 상태:")
            logger.info(f"   클래스명: {schema['class']}")
            logger.info(f"   DB명: {db_name}")
            logger.info(f"   활성 DB 수: {len(manager.list_databases())}")
            logger.info(f"   활성 DB 목록: {manager.list_databases()}")
            logger.info(f"   사용 가능한 스키마: {len(manager.list_schemas())}개")
            
            return 0
            
        except Exception as e:
            logger.error(f"❌ 스크립트 실행 중 오류 발생: {e}")
            import traceback
            traceback.print_exc()
            return 1
        
        finally:
            # 정리
            if manager:
                manager.close()
                logger.info("🔌 VectorDB 연결 종료")
                
    except ImportError as e:
        logger.error(f"❌ 필요한 모듈을 import할 수 없습니다: {e}")
        return 1

async def main():
    """메인 함수"""
    parser = setup_argument_parser()
    
    if len(sys.argv) == 1:
        parser.print_help()
        return 0
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return 0
    
    try:
        if args.command == 'process-csv':
            return await cmd_process_csv(args)
        elif args.command == 'process-documents':
            return await cmd_process_documents(args)
        elif args.command == 'build-kg':
            return await cmd_build_kg(args)
        elif args.command == 'csv-legacy':
            return await cmd_csv_legacy(args)
        else:
            logger.error(f"알 수 없는 명령: {args.command}")
            return 1
            
    except KeyboardInterrupt:
        logger.info("사용자에 의해 중단되었습니다")
        return 130
    except Exception as e:
        logger.error(f"예상치 못한 오류: {e}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    exit_code = asyncio.run(main())
