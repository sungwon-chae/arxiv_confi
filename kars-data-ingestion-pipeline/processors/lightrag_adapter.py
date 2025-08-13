"""
LightRAG 어댑터 모듈
Weaviate를 LightRAG의 벡터 스토리지로 사용하기 위한 어댑터
"""

import logging
import json
import numpy as np
from typing import Dict, Any, List, Optional, Tuple, Union
from pathlib import Path
import asyncio
from datetime import datetime
from abc import ABC, abstractmethod

# LightRAG의 벡터 스토리지 인터페이스
try:
    from lightrag.storage import BaseVectorStorage
    LIGHTRAG_AVAILABLE = True
except ImportError:
    LIGHTRAG_AVAILABLE = False
    # LightRAG가 없어도 작동하도록 기본 인터페이스 정의
    class BaseVectorStorage(ABC):
        @abstractmethod
        async def upsert(self, data: dict) -> dict:
            pass
        
        @abstractmethod
        async def query(self, query: str, top_k: int = 5) -> List[dict]:
            pass

# 기존 Weaviate DB import
import sys
sys.path.append(str(Path(__file__).parent.parent))
from weaviate_db import WeaviateDB
from base import VectorDBConfig

logger = logging.getLogger(__name__)

class WeaviateVectorAdapter(BaseVectorStorage):
    """
    Weaviate를 LightRAG 벡터 스토리지로 사용하기 위한 어댑터
    
    LightRAG의 BaseVectorStorage 인터페이스를 구현하여
    기존 WeaviateDB를 LightRAG에서 사용할 수 있게 함
    """
    
    def __init__(self, 
                 weaviate_db: Optional[WeaviateDB] = None,
                 config: Optional[VectorDBConfig] = None,
                 collection_name: str = "LightRAGVectors"):
        """
        Args:
            weaviate_db: 기존 WeaviateDB 인스턴스 (없으면 새로 생성)
            config: VectorDBConfig 설정 (weaviate_db가 없을 때 사용)
            collection_name: LightRAG 전용 컬렉션 이름
        """
        self.collection_name = collection_name
        self.initialized = False
        
        if weaviate_db:
            self.weaviate_db = weaviate_db
        else:
            if not config:
                # 기본 설정 사용
                config = VectorDBConfig(
                    db_type="weaviate",
                    connection_params={
                        "url": "http://localhost:8084",
                        "timeout": 30
                    },
                    embedding_model="BAAI/bge-m3",
                    embedding_dimension=1024,
                    default_class=collection_name
                )
            self.weaviate_db = WeaviateDB(config)
        
        # LightRAG 벡터 스토리지 스키마 정의
        self.schema = {
            "class": collection_name,
            "properties": [
                {"name": "entity_name", "dataType": ["text"]},
                {"name": "entity_type", "dataType": ["text"]},
                {"name": "description", "dataType": ["text"]},
                {"name": "source_id", "dataType": ["text"]},
                {"name": "chunk_id", "dataType": ["text"]},
                {"name": "metadata", "dataType": ["text"]},  # JSON string
                {"name": "created_at", "dataType": ["date"]},
                {"name": "confidence", "dataType": ["number"]}
            ]
        }
    
    async def initialize(self):
        """어댑터 초기화"""
        if not self.initialized:
            try:
                # Weaviate DB 초기화
                await self.weaviate_db.initialize()
                
                # LightRAG 전용 스키마 생성
                await self.weaviate_db.create_schema(self.schema)
                
                self.initialized = True
                logger.info(f"✅ WeaviateVectorAdapter 초기화 완료: {self.collection_name}")
                
            except Exception as e:
                logger.error(f"❌ WeaviateVectorAdapter 초기화 실패: {e}")
                raise
    
    async def upsert(self, data: dict) -> dict:
        """
        LightRAG 형식의 데이터를 Weaviate에 저장
        
        Args:
            data: {
                "id": str,
                "entity_name": str,
                "entity_type": str,
                "description": str,
                "embedding": List[float],  # 이미 생성된 임베딩
                "metadata": dict
            }
            
        Returns:
            {"status": "success", "id": str}
        """
        if not self.initialized:
            await self.initialize()
        
        try:
            # LightRAG 데이터를 Weaviate 형식으로 변환
            weaviate_doc = {
                "entity_name": data.get("entity_name", ""),
                "entity_type": data.get("entity_type", "UNKNOWN"),
                "description": data.get("description", ""),
                "source_id": data.get("source_id", ""),
                "chunk_id": data.get("id", ""),
                "metadata": json.dumps(data.get("metadata", {})),
                "created_at": datetime.now().isoformat() + "Z",
                "confidence": data.get("confidence", 1.0)
            }
            
            # 임베딩이 제공된 경우 직접 사용
            vector = data.get("embedding")
            
            # Weaviate에 저장
            if vector:
                # 벡터와 함께 저장 (수동 벡터화)
                result = await self._insert_with_vector(weaviate_doc, vector)
            else:
                # 자동 벡터화
                result = await self.weaviate_db.insert_documents(
                    [weaviate_doc], 
                    class_name=self.collection_name
                )
            
            return {
                "status": "success",
                "id": result[0] if result else data.get("id")
            }
            
        except Exception as e:
            logger.error(f"Upsert 실패: {e}")
            return {"status": "error", "message": str(e)}
    
    async def _insert_with_vector(self, doc: dict, vector: List[float]) -> List[str]:
        """벡터와 함께 문서 삽입"""
        try:
            collection = self.weaviate_db.client.collections.get(self.collection_name)
            
            # 직접 벡터 삽입
            with collection.batch.dynamic() as batch:
                uuid = batch.add_object(
                    properties=doc,
                    vector=vector
                )
            
            return [str(uuid)] if uuid else []
            
        except Exception as e:
            logger.error(f"벡터 삽입 실패: {e}")
            return []
    
    async def query(self, 
                   query: str = None,
                   vector: List[float] = None,
                   filter_dict: Dict[str, Any] = None,
                   top_k: int = 5) -> List[dict]:
        """
        LightRAG 형식의 쿼리 실행
        
        Args:
            query: 텍스트 쿼리 (vector와 함께 사용 불가)
            vector: 벡터 쿼리 (query와 함께 사용 불가)
            filter_dict: 필터 조건
            top_k: 반환할 결과 수
            
        Returns:
            List[{
                "id": str,
                "entity_name": str,
                "entity_type": str,
                "description": str,
                "score": float,
                "metadata": dict
            }]
        """
        if not self.initialized:
            await self.initialize()
        
        try:
            # 필터 구성
            weaviate_filters = None
            if filter_dict:
                weaviate_filters = self._build_weaviate_filter(filter_dict)
            
            # 쿼리 실행
            if query:
                # 텍스트 기반 검색
                results = await self.weaviate_db.search(
                    query=query,
                    class_name=self.collection_name,
                    limit=top_k,
                    filters=weaviate_filters
                )
            elif vector:
                # 벡터 기반 검색
                results = await self._search_by_vector(
                    vector=vector,
                    top_k=top_k,
                    filters=weaviate_filters
                )
            else:
                # 필터만으로 검색
                results = await self._search_by_filter(
                    filters=weaviate_filters,
                    limit=top_k
                )
            
            # LightRAG 형식으로 변환
            lightrag_results = []
            for result in results:
                props = result.get("properties", {})
                
                lightrag_result = {
                    "id": props.get("chunk_id", result.get("id")),
                    "entity_name": props.get("entity_name", ""),
                    "entity_type": props.get("entity_type", ""),
                    "description": props.get("description", ""),
                    "score": 1.0 - result.get("distance", 0.0),  # 거리를 점수로 변환
                    "metadata": json.loads(props.get("metadata", "{}"))
                }
                lightrag_results.append(lightrag_result)
            
            return lightrag_results
            
        except Exception as e:
            logger.error(f"Query 실패: {e}")
            return []
    
    async def _search_by_vector(self, 
                               vector: List[float], 
                               top_k: int,
                               filters: Any = None) -> List[dict]:
        """벡터로 직접 검색"""
        try:
            collection = self.weaviate_db.client.collections.get(self.collection_name)
            
            # 벡터 검색
            response = collection.query.near_vector(
                near_vector=vector,
                limit=top_k,
                where=filters,
                return_metadata=["distance"]
            )
            
            results = []
            for obj in response.objects:
                results.append({
                    "id": str(obj.uuid),
                    "properties": obj.properties,
                    "distance": obj.metadata.distance
                })
            
            return results
            
        except Exception as e:
            logger.error(f"벡터 검색 실패: {e}")
            return []
    
    async def _search_by_filter(self, 
                               filters: Any,
                               limit: int) -> List[dict]:
        """필터만으로 검색"""
        try:
            collection = self.weaviate_db.client.collections.get(self.collection_name)
            
            # 필터 검색
            response = collection.query.fetch_objects(
                where=filters,
                limit=limit
            )
            
            results = []
            for obj in response.objects:
                results.append({
                    "id": str(obj.uuid),
                    "properties": obj.properties,
                    "distance": 0.0  # 필터 검색은 거리 없음
                })
            
            return results
            
        except Exception as e:
            logger.error(f"필터 검색 실패: {e}")
            return []
    
    def _build_weaviate_filter(self, filter_dict: Dict[str, Any]) -> Any:
        """LightRAG 필터를 Weaviate 필터로 변환"""
        from weaviate.classes.query import Filter
        
        filters = []
        
        for field, value in filter_dict.items():
            if field == "entity_type":
                filters.append(Filter.by_property("entity_type").equal(value))
            elif field == "entity_name":
                filters.append(Filter.by_property("entity_name").equal(value))
            elif field == "source_id":
                filters.append(Filter.by_property("source_id").equal(value))
            elif field == "confidence_min":
                filters.append(Filter.by_property("confidence").greater_or_equal(value))
        
        if len(filters) == 1:
            return filters[0]
        elif len(filters) > 1:
            # 모든 조건을 AND로 결합
            combined = filters[0]
            for f in filters[1:]:
                combined = combined & f
            return combined
        
        return None
    
    async def delete(self, ids: List[str]) -> dict:
        """LightRAG 데이터 삭제"""
        try:
            collection = self.weaviate_db.client.collections.get(self.collection_name)
            
            deleted_count = 0
            for chunk_id in ids:
                # chunk_id로 찾아서 삭제
                filter_obj = Filter.by_property("chunk_id").equal(chunk_id)
                result = collection.query.fetch_objects(where=filter_obj, limit=1)
                
                if result.objects:
                    collection.data.delete_by_id(result.objects[0].uuid)
                    deleted_count += 1
            
            return {
                "status": "success",
                "deleted_count": deleted_count
            }
            
        except Exception as e:
            logger.error(f"Delete 실패: {e}")
            return {"status": "error", "message": str(e)}
    
    async def get_all(self, limit: int = 1000) -> List[dict]:
        """모든 데이터 조회 (디버깅/관리용)"""
        return await self.query(filter_dict={}, top_k=limit)
    
    def close(self):
        """연결 종료"""
        if hasattr(self, 'weaviate_db'):
            self.weaviate_db.close()

# LightRAG 통합 헬퍼 클래스
class LightRAGIntegration:
    """
    LightRAG와 기존 시스템을 통합하는 헬퍼 클래스
    """
    
    def __init__(self, weaviate_db: WeaviateDB):
        self.weaviate_db = weaviate_db
        self.vector_adapter = WeaviateVectorAdapter(weaviate_db)
        self.initialized = False
    
    async def initialize(self):
        """통합 시스템 초기화"""
        if not self.initialized:
            await self.vector_adapter.initialize()
            self.initialized = True
            logger.info("✅ LightRAG 통합 시스템 초기화 완료")
    
    def get_lightrag_config(self) -> dict:
        """LightRAG 초기화를 위한 설정 반환"""
        return {
            "vector_storage": self.vector_adapter,
            "vector_storage_type": "custom",
            "embedding_func": self._create_embedding_func(),
            "llm_model_func": self._create_llm_func()
        }
    
    def _create_embedding_func(self):
        """LightRAG용 임베딩 함수 생성"""
        async def embed_texts(texts: List[str]) -> List[List[float]]:
            # 기존 Weaviate의 임베딩 기능 활용
            embeddings = []
            for text in texts:
                try:
                    response = self.weaviate_db.openai_client.embeddings.create(
                        input=[text],
                        model=self.weaviate_db.dynamic_model_name
                    )
                    embeddings.append(response.data[0].embedding)
                except Exception as e:
                    logger.error(f"임베딩 생성 실패: {e}")
                    # 더미 임베딩 반환
                    embeddings.append([0.0] * 1024)
            return embeddings
        
        return embed_texts
    
    def _create_llm_func(self):
        """LightRAG용 LLM 함수 생성"""
        async def llm_complete(prompt: str, **kwargs) -> str:
            try:
                # 기존 시스템의 LLM 설정 사용
                response = self.weaviate_db.openai_client.completions.create(
                    model=self.weaviate_db.dynamic_model_name,
                    prompt=prompt,
                    max_tokens=kwargs.get("max_tokens", 1000)
                )
                return response.choices[0].text
            except Exception as e:
                logger.error(f"LLM 완성 실패: {e}")
                return ""
        
        return llm_complete

# 사용 예시
async def example_usage():
    """WeaviateVectorAdapter 사용 예시"""
    
    # 기존 Weaviate DB 설정
    config = VectorDBConfig(
        db_type="weaviate",
        connection_params={
            "url": "http://localhost:8084",
            "openai_api_key": "your-key",
            "openai_base_url": "http://localhost:8125"
        },
        embedding_model="BAAI/bge-m3",
        default_class="Documents"
    )
    
    # 어댑터 생성
    adapter = WeaviateVectorAdapter(config=config)
    await adapter.initialize()
    
    # 데이터 삽입
    result = await adapter.upsert({
        "id": "entity_001",
        "entity_name": "Apple Inc.",
        "entity_type": "ORGANIZATION",
        "description": "Technology company that designs and manufactures consumer electronics",
        "metadata": {
            "source": "wikipedia",
            "confidence": 0.95
        }
    })
    print(f"삽입 결과: {result}")
    
    # 쿼리
    results = await adapter.query(
        query="technology companies",
        top_k=5
    )
    print(f"검색 결과: {results}")
    
    adapter.close()

if __name__ == "__main__":
    asyncio.run(example_usage())