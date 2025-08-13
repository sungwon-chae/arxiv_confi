#!/usr/bin/env python3
"""
통합 데이터 인제스션 파이프라인 엔진
processors 기반의 고도화된 데이터 처리 시스템
"""

import asyncio
import logging
import json
import csv
from typing import Dict, Any, List, Optional, Union
from pathlib import Path
from datetime import datetime
import tempfile
from dataclasses import dataclass

# 내부 모듈
from simple_manager import MultipleVectorDBManager
from processors.multimodal_processor import MultimodalDocumentProcessor
from processors.knowledge_graph_builder import KnowledgeGraphBuilder

logger = logging.getLogger(__name__)

@dataclass
class PipelineConfig:
    """파이프라인 설정"""
    # 데이터베이스 설정
    db_name: Optional[str] = None
    class_name: Optional[str] = None
    vectorize_fields: Optional[List[str]] = None
    
    # 텍스트 처리 설정
    chunk_strategy: str = "semantic"
    chunk_size: int = 1000
    chunk_overlap: int = 200
    
    # 멀티모달 처리 설정
    extract_images: bool = True
    extract_tables: bool = True
    preserve_layout: bool = True
    
    # 지식 그래프 설정
    build_knowledge_graph: bool = False
    min_entity_confidence: float = 0.5
    similarity_threshold: float = 0.8
    
    # 출력 설정
    output_format: str = "structured_json"
    save_intermediate: bool = False
    output_dir: Optional[Path] = None

class DataIngestionPipeline:
    """통합 데이터 인제스션 파이프라인"""
    
    def __init__(self, config: Optional[PipelineConfig] = None):
        self.config = config or PipelineConfig()
        
        # 프로세서 초기화
        self.multimodal_processor = MultimodalDocumentProcessor()
        
        self.kg_builder = KnowledgeGraphBuilder(
            min_entity_confidence=self.config.min_entity_confidence,
            similarity_threshold=self.config.similarity_threshold
        ) if self.config.build_knowledge_graph else None
        
        self.db_manager = None
        
        logger.info("데이터 인제스션 파이프라인 초기화 완료")
    
    def _simple_text_analysis(self, text: str) -> Dict[str, Any]:
        """간단한 텍스트 분석 (text_processor 대체)"""
        if not text:
            return {"success": False}
        
        # 기본 통계
        words = text.split()
        word_count = len(words)
        
        # 언어 감지 (간단한 휴리스틱)
        korean_chars = sum(1 for char in text if '가' <= char <= '힣')
        total_chars = len(text.replace(' ', ''))
        language = "ko" if korean_chars > total_chars * 0.3 else "en"
        
        # 간단한 키워드 추출 (단어 빈도 기반)
        word_freq = {}
        for word in words:
            if len(word) > 3:  # 3글자 이상 단어만
                word_freq[word] = word_freq.get(word, 0) + 1
        
        key_phrases = sorted(word_freq.keys(), key=lambda x: word_freq[x], reverse=True)[:10]
        
        return {
            "success": True,
            "text_type": "document",
            "statistics": {
                "language": language,
                "word_count": word_count
            },
            "key_phrases": key_phrases
        }
    
    async def initialize_database(self):
        """데이터베이스 매니저 초기화"""
        if not self.db_manager:
            self.db_manager = MultipleVectorDBManager()
            logger.info("데이터베이스 매니저 초기화 완료")
    
    async def process_csv_enhanced(self, 
                                 csv_path: Union[str, Path],
                                 text_dir: Optional[Union[str, Path]] = None,
                                 text_path_field: Optional[str] = None,
                                 content_field: str = "content") -> Dict[str, Any]:
        """
        고도화된 CSV 처리 (기존 setup_database.py 기능 + 고급 처리)
        
        Args:
            csv_path: CSV 파일 경로
            text_dir: 외부 텍스트 파일 디렉토리
            text_path_field: 텍스트 파일 경로 필드명
            content_field: 콘텐츠 필드명
            
        Returns:
            처리 결과
        """
        csv_path = Path(csv_path)
        text_dir = Path(text_dir) if text_dir else None
        
        logger.info(f"고도화된 CSV 처리 시작: {csv_path}")
        
        await self.initialize_database()
        
        # 1. CSV 메타데이터 분석 및 스키마 생성
        schema_result = await self._generate_enhanced_schema(csv_path)
        if not schema_result["success"]:
            return schema_result
        
        schema = schema_result["schema"]
        db_name = schema_result["db_name"]
        
        # 2. 스키마로 데이터베이스 생성
        schema_success = await self.db_manager.create_schema_from_definition(db_name, schema)
        if not schema_success:
            return {"success": False, "error": "스키마 생성 실패"}
        
        # 3. 고도화된 데이터 처리 및 삽입
        processing_result = await self._process_csv_data_enhanced(
            csv_path, db_name, text_dir, text_path_field, content_field
        )
        
        # 4. 지식 그래프 구축 (옵션)
        if self.config.build_knowledge_graph and self.kg_builder:
            kg_result = await self._build_knowledge_graph_from_processed_data(
                processing_result.get("processed_documents", [])
            )
            processing_result["knowledge_graph"] = kg_result
        
        return {
            "success": True,
            "timestamp": datetime.now().isoformat(),
            "database_name": db_name,
            "schema": schema,
            "processing_stats": processing_result.get("stats", {}),
            "total_documents": processing_result.get("total_documents", 0),
            "knowledge_graph_stats": processing_result.get("knowledge_graph", {}).get("stats")
        }
    
    async def process_documents_multimodal(self, 
                                         file_paths: List[Union[str, Path]],
                                         batch_size: int = 10) -> Dict[str, Any]:
        """
        멀티모달 문서 일괄 처리
        
        Args:
            file_paths: 처리할 문서 파일 경로들
            batch_size: 배치 크기
            
        Returns:
            처리 결과
        """
        logger.info(f"멀티모달 문서 처리 시작: {len(file_paths)}개 파일")
        
        await self.initialize_database()
        
        processed_documents = []
        failed_documents = []
        
        # 배치 단위로 문서 처리
        for i in range(0, len(file_paths), batch_size):
            batch = file_paths[i:i + batch_size]
            batch_results = await self._process_document_batch(batch)
            
            for file_path, result in batch_results.items():
                if result.get("success", False):
                    processed_documents.append(result)
                else:
                    failed_documents.append({"file_path": file_path, "error": result.get("error")})
        
        # 벡터 DB에 저장
        if processed_documents:
            db_result = await self._store_processed_documents(processed_documents)
        else:
            db_result = {"success": False, "error": "처리된 문서가 없습니다"}
        
        # 지식 그래프 구축 (옵션)
        kg_result = None
        if self.config.build_knowledge_graph and self.kg_builder and processed_documents:
            kg_result = await self._build_knowledge_graph_from_processed_data(processed_documents)
        
        return {
            "success": True,
            "timestamp": datetime.now().isoformat(),
            "total_files": len(file_paths),
            "successful_files": len(processed_documents),
            "failed_files": len(failed_documents),
            "failed_documents": failed_documents,
            "database_result": db_result,
            "knowledge_graph": kg_result,
            "processing_stats": {
                "total_elements": sum(doc.get("total_elements", 0) for doc in processed_documents),
                "total_text_elements": sum(doc.get("element_statistics", {}).get("text", 0) for doc in processed_documents),
                "total_image_elements": sum(doc.get("element_statistics", {}).get("image", 0) for doc in processed_documents),
                "total_table_elements": sum(doc.get("element_statistics", {}).get("table", 0) for doc in processed_documents)
            }
        }
    
    async def build_knowledge_graph_standalone(self, 
                                             processed_documents: List[Dict[str, Any]],
                                             output_path: Optional[Union[str, Path]] = None) -> Dict[str, Any]:
        """
        독립적인 지식 그래프 구축
        
        Args:
            processed_documents: 처리된 문서 데이터들
            output_path: 지식 그래프 저장 경로
            
        Returns:
            지식 그래프 구축 결과
        """
        if not self.kg_builder:
            self.kg_builder = KnowledgeGraphBuilder(
                min_entity_confidence=self.config.min_entity_confidence,
                similarity_threshold=self.config.similarity_threshold
            )
        
        logger.info(f"독립적인 지식 그래프 구축 시작: {len(processed_documents)}개 문서")
        
        try:
            kg = self.kg_builder.build_knowledge_graph(processed_documents)
            stats = self.kg_builder.analyze_graph_statistics(kg)
            
            if output_path:
                self.kg_builder.save_knowledge_graph(kg, output_path)
            
            return {
                "success": True,
                "knowledge_graph_path": str(output_path) if output_path else None,
                "stats": stats,
                "timestamp": datetime.now().isoformat()
            }
            
        except Exception as e:
            logger.error(f"지식 그래프 구축 실패: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    async def _generate_enhanced_schema(self, csv_path: Path) -> Dict[str, Any]:
        """고도화된 스키마 생성"""
        try:
            # 기존 generate_schema 로직을 개선
            from scripts.generate_schema import generate_schema_from_csv
            
            schema, db_name = generate_schema_from_csv(
                csv_path=csv_path,
                class_name=self.config.class_name,
                db_name=self.config.db_name,
                vectorize_fields=self.config.vectorize_fields
            )
            
            return {
                "success": True,
                "schema": schema,
                "db_name": db_name
            }
            
        except Exception as e:
            logger.error(f"스키마 생성 실패: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    async def _process_csv_data_enhanced(self, 
                                       csv_path: Path, 
                                       db_name: str,
                                       text_dir: Optional[Path],
                                       text_path_field: Optional[str],
                                       content_field: str) -> Dict[str, Any]:
        """고도화된 CSV 데이터 처리"""
        documents = []
        processed_documents = []
        stats = {"total_rows": 0, "processed_rows": 0, "failed_rows": 0}
        
        try:
            with open(csv_path, 'r', encoding='utf-8') as file:
                csv_reader = csv.DictReader(file)
                
                for row_num, row in enumerate(csv_reader, 1):
                    stats["total_rows"] = row_num
                    
                    try:
                        # 기본 문서 데이터 생성
                        document = self._create_document_from_csv_row(row, text_dir, text_path_field, content_field)
                        
                        # 간단한 텍스트 분석
                        if document.get(content_field):
                            text_analysis = self._simple_text_analysis(document[content_field])
                            
                            if text_analysis.get("success"):
                                # 텍스트 분석 결과를 문서에 추가
                                document.update({
                                    "text_type": text_analysis.get("text_type"),
                                    "language": text_analysis.get("statistics", {}).get("language"),
                                    "word_count": text_analysis.get("statistics", {}).get("word_count"),
                                    "key_phrases": text_analysis.get("key_phrases", [])[:5]  # 상위 5개만
                                })
                                
                                processed_documents.append(text_analysis)
                        
                        documents.append(document)
                        stats["processed_rows"] += 1
                        
                    except Exception as e:
                        logger.warning(f"행 {row_num} 처리 실패: {e}")
                        stats["failed_rows"] += 1
                        continue
            
            # 데이터베이스에 삽입
            if documents:
                result = await self.db_manager.load_data(db_name, "", documents)
                
                return {
                    "success": result.get("success", False),
                    "stats": stats,
                    "total_documents": len(documents),
                    "processed_documents": processed_documents,
                    "inserted_count": result.get("inserted_count", 0)
                }
            else:
                return {
                    "success": False,
                    "error": "처리할 문서가 없습니다",
                    "stats": stats
                }
                
        except Exception as e:
            logger.error(f"CSV 데이터 처리 실패: {e}")
            return {
                "success": False,
                "error": str(e),
                "stats": stats
            }
    
    def _create_document_from_csv_row(self, 
                                    row: Dict[str, str], 
                                    text_dir: Optional[Path],
                                    text_path_field: Optional[str],
                                    content_field: str) -> Dict[str, Any]:
        """CSV 행에서 문서 객체 생성 (기존 setup_database.py 로직)"""
        document = {}
        
        # 모든 CSV 필드를 문서에 매핑
        for header, value in row.items():
            field_name = header.lower().replace(' ', '_').replace('-', '_')
            
            # 데이터 타입별 처리
            if field_name.endswith('_date') or 'date' in field_name:
                from scripts.setup_database import normalize_date_to_rfc3339
                document[field_name] = normalize_date_to_rfc3339(value)
            elif field_name.endswith('_size') or 'size' in field_name or 'number' in field_name:
                try:
                    document[field_name] = float(value) if value else 0.0
                except ValueError:
                    document[field_name] = 0.0
            else:
                document[field_name] = value if value else ""
        
        # 외부 텍스트 파일에서 내용 읽기
        content = ""
        if text_dir and text_path_field and text_path_field in row:
            text_file_path = text_dir / Path(row[text_path_field]).name
            
            if text_file_path.exists():
                try:
                    with open(text_file_path, 'r', encoding='utf-8') as text_file:
                        content = text_file.read()
                except Exception as e:
                    logger.warning(f"텍스트 파일 읽기 실패 ({text_file_path}): {e}")
                    content = f"텍스트 파일 읽기 실패: {e}"
        
        # content 필드 설정
        if content or content_field not in document:
            document[content_field] = content if content else document.get(content_field, "")
        
        return document
    
    async def _process_document_batch(self, file_paths: List[Union[str, Path]]) -> Dict[str, Dict[str, Any]]:
        """문서 배치 처리"""
        results = {}
        
        # 병렬 처리
        tasks = []
        for file_path in file_paths:
            task = self._process_single_document(file_path)
            tasks.append((str(file_path), task))
        
        # 결과 수집
        for file_path, task in tasks:
            try:
                result = await task
                results[file_path] = result
            except Exception as e:
                logger.error(f"문서 처리 실패 ({file_path}): {e}")
                results[file_path] = {"success": False, "error": str(e)}
        
        return results
    
    async def _process_single_document(self, file_path: Union[str, Path]) -> Dict[str, Any]:
        """단일 문서 처리"""
        extract_options = {
            "extract_text": True,
            "extract_images": self.config.extract_images,
            "extract_tables": self.config.extract_tables,
            "preserve_layout": self.config.preserve_layout
        }
        
        return await self.multimodal_processor.process_document(
            file_path, extract_options, self.config.output_format
        )
    
    async def _store_processed_documents(self, processed_documents: List[Dict[str, Any]]) -> Dict[str, Any]:
        """처리된 문서들을 벡터 DB에 저장"""
        try:
            # 벡터화용 청크 추출
            all_chunks = []
            
            for doc in processed_documents:
                chunks = self.multimodal_processor.extract_for_vectorization(doc)
                all_chunks.extend(chunks)
            
            if not all_chunks:
                return {"success": False, "error": "벡터화할 데이터가 없습니다"}
            
            # 데이터베이스명 결정
            db_name = self.config.db_name or "multimodal_documents"
            
            # 간단한 스키마 생성 (필요시)
            schema = {
                "class": "MultimodalDocument",
                "properties": [
                    {"name": "content", "dataType": ["text"], "vectorizePropertyName": True},
                    {"name": "source_file", "dataType": ["text"]},
                    {"name": "element_type", "dataType": ["text"]},
                    {"name": "page_number", "dataType": ["int"]},
                    {"name": "processing_timestamp", "dataType": ["date"]}
                ],
                "vectorizer": "text2vec-openai"
            }
            
            # 스키마 생성
            await self.db_manager.create_schema_from_definition(db_name, schema)
            
            # 데이터 삽입
            documents = []
            for chunk in all_chunks:
                doc = {
                    "content": chunk["content"],
                    **chunk["metadata"]
                }
                documents.append(doc)
            
            result = await self.db_manager.load_data(db_name, "", documents)
            
            return {
                "success": result.get("success", False),
                "database_name": db_name,
                "inserted_count": result.get("inserted_count", 0),
                "total_chunks": len(all_chunks)
            }
            
        except Exception as e:
            logger.error(f"문서 저장 실패: {e}")
            return {"success": False, "error": str(e)}
    
    async def _build_knowledge_graph_from_processed_data(self, processed_documents: List[Dict[str, Any]]) -> Dict[str, Any]:
        """처리된 데이터에서 지식 그래프 구축"""
        try:
            if not self.kg_builder:
                return {"success": False, "error": "지식 그래프 빌더가 초기화되지 않았습니다"}
            
            kg = self.kg_builder.build_knowledge_graph(processed_documents)
            stats = self.kg_builder.analyze_graph_statistics(kg)
            
            # 저장 (옵션)
            if self.config.output_dir:
                kg_path = self.config.output_dir / "knowledge_graph.json"
                self.kg_builder.save_knowledge_graph(kg, kg_path)
                
                return {
                    "success": True,
                    "knowledge_graph_path": str(kg_path),
                    "stats": stats
                }
            else:
                return {
                    "success": True,
                    "stats": stats
                }
                
        except Exception as e:
            logger.error(f"지식 그래프 구축 실패: {e}")
            return {"success": False, "error": str(e)}
    
    def close(self):
        """리소스 정리"""
        if self.db_manager:
            self.db_manager.close()
            logger.info("데이터베이스 연결 종료")

# 편의 함수들
async def process_csv_simple(csv_path: Union[str, Path], 
                           text_dir: Optional[Union[str, Path]] = None,
                           **kwargs) -> Dict[str, Any]:
    """간단한 CSV 처리 함수"""
    config = PipelineConfig(**kwargs)
    pipeline = DataIngestionPipeline(config)
    
    try:
        return await pipeline.process_csv_enhanced(csv_path, text_dir)
    finally:
        pipeline.close()

async def process_documents_simple(file_paths: List[Union[str, Path]], 
                                 **kwargs) -> Dict[str, Any]:
    """간단한 문서 처리 함수"""
    config = PipelineConfig(**kwargs)
    pipeline = DataIngestionPipeline(config)
    
    try:
        return await pipeline.process_documents_multimodal(file_paths)
    finally:
        pipeline.close()