#!/usr/bin/env python3
"""
데이터 인제스션 파이프라인 테스트
CSV 데이터 로딩, 스키마 생성, 벡터 DB 적재 검증에 초점을 맞춘 테스트
"""

import asyncio
import csv
import json
import logging
import os
import tempfile
from pathlib import Path
from typing import Dict, List, Any
import pytest

from simple_manager import MultipleVectorDBManager
from scripts.generate_schema import generate_schema_from_csv
from scripts.setup_database import (
    create_database_schema, 
    load_csv_data, 
    test_database_ingestion,
    normalize_date_to_rfc3339
)
from pipeline_engine import DataIngestionPipeline, PipelineConfig

# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class IngestionTestSuite:
    """데이터 인제스션 테스트 스위트"""
    
    def __init__(self):
        self.test_data_dir = Path("test_data")
        self.test_data_dir.mkdir(exist_ok=True)
        self.manager = None
        
    async def setup_manager(self):
        """VectorDB 매니저 초기화"""
        self.manager = MultipleVectorDBManager()
        return self.manager
        
    async def cleanup_manager(self):
        """VectorDB 매니저 정리"""
        if self.manager:
            self.manager.close()
            self.manager = None
    
    def create_test_csv(self, filename: str, data: List[Dict[str, Any]]) -> Path:
        """테스트용 CSV 파일 생성"""
        csv_path = self.test_data_dir / filename
        
        if data:
            with open(csv_path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)
        
        return csv_path
    
    def create_test_text_files(self, text_data: Dict[str, str]) -> Path:
        """테스트용 텍스트 파일들 생성"""
        text_dir = self.test_data_dir / "texts"
        text_dir.mkdir(exist_ok=True)
        
        for filename, content in text_data.items():
            with open(text_dir / filename, 'w', encoding='utf-8') as f:
                f.write(content)
        
        return text_dir
    
    async def test_csv_schema_generation(self):
        """CSV 기반 스키마 생성 테스트"""
        logger.info("=== CSV 스키마 생성 테스트 ===")
        
        # 테스트 데이터 생성
        test_data = [
            {
                "id": "doc_001",
                "title": "테스트 문서 1",
                "content": "이것은 테스트 문서입니다.",
                "created_date": "2024-01-01T00:00:00Z",
                "category": "테스트",
                "size": "1024"
            },
            {
                "id": "doc_002", 
                "title": "테스트 문서 2",
                "content": "두 번째 테스트 문서입니다.",
                "created_date": "2024-01-02T00:00:00Z",
                "category": "샘플",
                "size": "2048"
            }
        ]
        
        csv_path = self.create_test_csv("test_schema.csv", test_data)
        
        try:
            # 스키마 생성 테스트
            schema, db_name = generate_schema_from_csv(
                csv_path=csv_path,
                class_name="TestDocument",
                db_name="test_schema_db",
                vectorize_fields=["title", "content"]
            )
            
            # 스키마 검증
            assert schema is not None, "스키마가 생성되지 않음"
            assert schema["class"] == "TestDocument", f"클래스명 불일치: {schema['class']}"
            assert len(schema["properties"]) > 0, "속성이 정의되지 않음"
            
            # 벡터화 필드 확인
            vectorized_props = [p for p in schema["properties"] if p.get("vectorizePropertyName", False)]
            assert len(vectorized_props) >= 2, f"벡터화 필드 부족: {len(vectorized_props)}"
            
            logger.info(f"✅ 스키마 생성 성공: {schema['class']}, {len(schema['properties'])}개 속성")
            return True
            
        except Exception as e:
            logger.error(f"❌ 스키마 생성 실패: {e}")
            return False
        finally:
            # 정리
            if csv_path.exists():
                csv_path.unlink()
    
    async def test_csv_data_loading(self):
        """CSV 데이터 로딩 테스트"""
        logger.info("=== CSV 데이터 로딩 테스트 ===")
        
        await self.setup_manager()
        
        try:
            # 테스트 데이터 생성
            test_data = [
                {
                    "id": "load_001",
                    "title": "로딩 테스트 1",
                    "content": "데이터 로딩을 위한 테스트 문서입니다.",
                    "created_date": "2024-01-01 10:00",
                    "category": "로딩테스트",
                    "priority": "1"
                },
                {
                    "id": "load_002",
                    "title": "로딩 테스트 2", 
                    "content": "두 번째 로딩 테스트 문서입니다.",
                    "created_date": "2024-01-02 11:00",
                    "category": "로딩테스트",
                    "priority": "2"
                }
            ]
            
            csv_path = self.create_test_csv("test_loading.csv", test_data)
            
            # 스키마 생성
            schema_success, schema, db_name = await create_database_schema(
                self.manager, csv_path, "LoadingTest", "test_loading_db", ["title", "content"]
            )
            
            assert schema_success, "스키마 생성 실패"
            
            # 데이터 로딩
            loading_success = await load_csv_data(
                self.manager, csv_path, db_name, schema
            )
            
            assert loading_success, "데이터 로딩 실패"
            
            # 인제스션 검증
            verification_success = await test_database_ingestion(self.manager, db_name)
            assert verification_success, "인제스션 검증 실패"
            
            logger.info("✅ CSV 데이터 로딩 및 검증 성공")
            return True
            
        except Exception as e:
            logger.error(f"❌ CSV 데이터 로딩 실패: {e}")
            return False
        finally:
            await self.cleanup_manager()
            # 정리
            for file in self.test_data_dir.glob("test_loading.*"):
                if file.exists():
                    file.unlink()
    
    async def test_enron_data_ingestion(self):
        """실제 Enron 데이터를 사용한 외부 텍스트 연동 테스트"""
        logger.info("=== 실제 Enron 데이터 인제스션 테스트 ===")
        
        await self.setup_manager()
        
        try:
            # 실제 Enron 스키마와 텍스트 파일 사용
            enron_csv_path = Path("config/schemas/enron_schema.csv")
            dummy_texts_dir = Path("dummy_texts")
            
            # 파일 존재 확인
            if not enron_csv_path.exists():
                logger.warning(f"Enron CSV 파일이 없습니다: {enron_csv_path}")
                return True  # 테스트 스킵
            
            if not dummy_texts_dir.exists():
                logger.warning(f"Dummy texts 디렉토리가 없습니다: {dummy_texts_dir}")
                return True  # 테스트 스킵
            
            logger.info(f"📁 Enron CSV: {enron_csv_path}")
            logger.info(f"📁 텍스트 디렉토리: {dummy_texts_dir}")
            
            # 스키마 생성 (실제 Enron 데이터 구조 사용)
            schema_success, schema, db_name = await create_database_schema(
                self.manager, 
                enron_csv_path, 
                "EnronDocument", 
                "enron_test_db", 
                ["Email Subject", "content"]  # 제목과 내용을 벡터화
            )
            
            assert schema_success, "Enron 스키마 생성 실패"
            logger.info(f"✅ Enron 스키마 생성 성공: {schema['class']}")
            
            # 외부 텍스트와 함께 데이터 로딩
            text_field_mapping = {
                'path_field': 'Text Precedence',  # CSV의 텍스트 파일 경로 컬럼
                'content_field': 'content'
            }
            
            loading_success = await load_csv_data(
                self.manager, enron_csv_path, db_name, schema, dummy_texts_dir, text_field_mapping
            )
            
            assert loading_success, "Enron 데이터 로딩 실패"
            
            # 인제스션 검증
            verification_success = await test_database_ingestion(self.manager, db_name)
            assert verification_success, "Enron 데이터 인제스션 검증 실패"
            
            # 추가 검증: 실제 텍스트 내용이 로딩되었는지 확인
            try:
                # 간단한 검색으로 텍스트 내용 포함 여부 확인
                results = await self.manager.search([db_name], "한국 LNG", limit=1)
                
                if ("results" in results and 
                    db_name in results["results"] and 
                    "results" in results["results"][db_name]):
                    
                    db_results = results["results"][db_name]["results"]
                    if db_results:
                        first_result = db_results[0]
                        if hasattr(first_result, 'to_dict'):
                            result_dict = first_result.to_dict()
                        else:
                            result_dict = first_result
                        
                        properties = result_dict.get('properties', {})
                        content = properties.get('content', '')
                        
                        if content and len(content) > 50:  # 의미있는 텍스트 내용이 있는지
                            logger.info(f"✅ 외부 텍스트 내용 확인: {len(content)}자")
                        else:
                            logger.warning("⚠️ 외부 텍스트 내용이 비어있음")
                            
            except Exception as e:
                logger.warning(f"텍스트 내용 검증 중 오류: {e}")
            
            logger.info("✅ 실제 Enron 데이터 인제스션 테스트 성공")
            return True
            
        except Exception as e:
            logger.error(f"❌ Enron 데이터 인제스션 테스트 실패: {e}")
            return False
        finally:
            await self.cleanup_manager()
    
    async def test_date_normalization(self):
        """날짜 정규화 테스트"""
        logger.info("=== 날짜 정규화 테스트 ===")
        
        test_cases = [
            ("2024-01-01T00:00:00Z", "2024-01-01T00:00:00Z"),  # 이미 RFC3339
            ("2024-01-01 10:30", "2024-01-01T10:30:00Z"),      # 시간 포함
            ("2024-01-01", "2024-01-01T00:00:00Z"),            # 날짜만
            ("01/15/2024", "2024-01-15T00:00:00Z"),            # MM/DD/YYYY
            ("", "1970-01-01T00:00:00Z"),                      # 빈 값
            ("잘못된날짜", "1970-01-01T00:00:00Z")              # 잘못된 형식
        ]
        
        try:
            for input_date, expected in test_cases:
                result = normalize_date_to_rfc3339(input_date)
                assert result == expected, f"날짜 정규화 실패: {input_date} -> {result} (예상: {expected})"
            
            logger.info("✅ 날짜 정규화 테스트 성공")
            return True
            
        except Exception as e:
            logger.error(f"❌ 날짜 정규화 테스트 실패: {e}")
            return False
    
    async def test_pipeline_csv_processing(self):
        """파이프라인 엔진을 통한 CSV 처리 테스트"""
        logger.info("=== 파이프라인 CSV 처리 테스트 ===")
        
        try:
            # 테스트 데이터 생성
            test_data = [
                {
                    "document_id": "pipe_001",
                    "title": "파이프라인 테스트 문서 1",
                    "description": "파이프라인 엔진을 통한 처리 테스트입니다.",
                    "created_at": "2024-01-01T10:00:00Z",
                    "status": "active",
                    "importance": "3"
                },
                {
                    "document_id": "pipe_002",
                    "title": "파이프라인 테스트 문서 2",
                    "description": "고급 처리 기능을 테스트합니다.",
                    "created_at": "2024-01-02T11:00:00Z", 
                    "status": "active",
                    "importance": "5"
                }
            ]
            
            csv_path = self.create_test_csv("test_pipeline.csv", test_data)
            
            # 파이프라인 설정
            config = PipelineConfig(
                db_name="test_pipeline_db",
                class_name="PipelineTest",
                vectorize_fields=["title", "description"],
                build_knowledge_graph=False  # 간단한 테스트
            )
            
            pipeline = DataIngestionPipeline(config)
            
            try:
                result = await pipeline.process_csv_enhanced(
                    csv_path=str(csv_path),
                    text_dir=None,
                    text_path_field=None,
                    content_field="description"
                )
                
                assert result["success"], f"파이프라인 처리 실패: {result.get('error')}"
                assert result["total_documents"] == 2, f"문서 수 불일치: {result['total_documents']}"
                
                logger.info("✅ 파이프라인 CSV 처리 테스트 성공")
                return True
                
            finally:
                pipeline.close()
                
        except Exception as e:
            logger.error(f"❌ 파이프라인 CSV 처리 테스트 실패: {e}")
            return False
        finally:
            # 정리
            for file in self.test_data_dir.glob("test_pipeline.*"):
                if file.exists():
                    file.unlink()
    
    async def run_all_tests(self) -> Dict[str, bool]:
        """모든 인제스션 테스트 실행"""
        logger.info("🚀 데이터 인제스션 테스트 스위트 시작")
        logger.info("=" * 60)
        
        test_results = {}
        
        tests = [
            ("CSV 스키마 생성", self.test_csv_schema_generation),
            ("CSV 데이터 로딩", self.test_csv_data_loading), 
            ("실제 Enron 데이터 인제스션", self.test_enron_data_ingestion),
            ("날짜 정규화", self.test_date_normalization),
            ("파이프라인 CSV 처리", self.test_pipeline_csv_processing)
        ]
        
        for test_name, test_func in tests:
            try:
                logger.info(f"\n▶️ {test_name} 테스트 시작...")
                result = await test_func()
                test_results[test_name] = result
                
                if result:
                    logger.info(f"✅ {test_name} 테스트 성공")
                else:
                    logger.error(f"❌ {test_name} 테스트 실패")
                    
            except Exception as e:
                logger.error(f"❌ {test_name} 테스트 중 예외 발생: {e}")
                test_results[test_name] = False
        
        # 결과 요약
        logger.info("\n" + "=" * 60)
        logger.info("📊 테스트 결과 요약")
        logger.info("=" * 60)
        
        passed = sum(1 for result in test_results.values() if result)
        total = len(test_results)
        
        for test_name, result in test_results.items():
            status = "✅ PASS" if result else "❌ FAIL"
            logger.info(f"{status} {test_name}")
        
        logger.info(f"\n🎯 총 {passed}/{total}개 테스트 통과")
        
        if passed == total:
            logger.info("🎉 모든 인제스션 테스트 성공!")
        else:
            logger.warning(f"⚠️ {total - passed}개 테스트 실패")
        
        return test_results
    
    def cleanup_test_data(self):
        """테스트 데이터 정리"""
        if self.test_data_dir.exists():
            for file in self.test_data_dir.rglob("*"):
                if file.is_file():
                    file.unlink()
            
            # 빈 디렉토리 제거
            for dir_path in sorted(self.test_data_dir.rglob("*"), reverse=True):
                if dir_path.is_dir() and not any(dir_path.iterdir()):
                    dir_path.rmdir()


async def main():
    """메인 테스트 실행 함수"""
    test_suite = IngestionTestSuite()
    
    try:
        results = await test_suite.run_all_tests()
        
        # 실패한 테스트가 있으면 종료 코드 1 반환
        failed_tests = [name for name, result in results.items() if not result]
        
        if failed_tests:
            logger.error(f"실패한 테스트: {', '.join(failed_tests)}")
            return 1
        else:
            logger.info("모든 테스트 성공!")
            return 0
            
    finally:
        test_suite.cleanup_test_data()


if __name__ == "__main__":
    exit_code = asyncio.run(main())
    exit(exit_code)