"""
하이브리드 RAG 프로세서
KnowledgeGraphBuilder의 결과를 LightRAG 형식으로 변환하고 통합 처리
"""

import logging
import json
import asyncio
from typing import Dict, Any, List, Optional, Tuple, Set
from pathlib import Path
from datetime import datetime
from dataclasses import dataclass, asdict
import hashlib

# LightRAG 관련 imports
try:
    from lightrag import LightRAG
    from lightrag.llm import gpt_4o_mini_complete
    from lightrag.utils import EmbeddingFunc
    LIGHTRAG_AVAILABLE = True
except ImportError:
    LIGHTRAG_AVAILABLE = False
    logging.warning("LightRAG not available. Install with: pip install lightrag")

# 기존 모듈 imports
import sys
sys.path.append(str(Path(__file__).parent.parent))
from processors.multimodal_processor import MultimodalDocumentProcessor
from processors.knowledge_graph_builder import (
    KnowledgeGraphBuilder, 
    Entity, 
    Relationship, 
    KnowledgeGraph,
    EntityType,
    RelationType
)
from processors.lightrag_adapter import WeaviateVectorAdapter, LightRAGIntegration
from weaviate_db import WeaviateDB
from base import VectorDBConfig

logger = logging.getLogger(__name__)

@dataclass
class HybridProcessingResult:
    """하이브리드 처리 결과"""
    success: bool
    file_path: str
    multimodal_elements: List[Dict[str, Any]]
    entities: List[Entity]
    relationships: List[Relationship]
    lightrag_entities: List[Dict[str, Any]]
    weaviate_chunks: List[str]
    processing_time: float
    metadata: Dict[str, Any]

class HybridRAGProcessor:
    """
    멀티모달 문서 처리 + 지식 그래프 구축 + LightRAG 통합
    """
    
    def __init__(self,
                 weaviate_db: WeaviateDB,
                 lightrag_working_dir: str = "./lightrag_data",
                 use_lightrag: bool = True,
                 llm_model: str = "gpt-4o-mini",
                 embedding_model: str = "text-embedding-3-small"):
        """
        Args:
            weaviate_db: 기존 Weaviate DB 인스턴스
            lightrag_working_dir: LightRAG 작업 디렉토리
            use_lightrag: LightRAG 사용 여부
            llm_model: LLM 모델명
            embedding_model: 임베딩 모델명
        """
        self.weaviate_db = weaviate_db
        self.use_lightrag = use_lightrag and LIGHTRAG_AVAILABLE
        
        # 기존 프로세서들
        self.multimodal_processor = MultimodalDocumentProcessor()
        self.kg_builder = KnowledgeGraphBuilder()
        
        # LightRAG 통합
        if self.use_lightrag:
            self.lightrag_integration = LightRAGIntegration(weaviate_db)
            self.vector_adapter = self.lightrag_integration.vector_adapter
            
            # LightRAG 인스턴스 생성
            self._init_lightrag(lightrag_working_dir, llm_model, embedding_model)
        else:
            self.lightrag_integration = None
            self.vector_adapter = None
            self.rag = None
            
        self.initialized = False
    
    def _init_lightrag(self, working_dir: str, llm_model: str, embedding_model: str):
        """LightRAG 인스턴스 초기화"""
        try:
            # LightRAG 설정
            self.rag = LightRAG(
                working_dir=working_dir,
                llm_model_func=self._create_llm_func(llm_model),
                embedding_func=self._create_embedding_func(embedding_model),
                # 커스텀 벡터 스토리지 사용
                vector_storage=self.vector_adapter,
                graph_storage="NetworkXStorage",  # 로컬 그래프 스토리지
                chunk_size=1200,
                chunk_overlap=200,
                enable_llm_cache=True
            )
            logger.info("✅ LightRAG 인스턴스 생성 완료")
        except Exception as e:
            logger.error(f"❌ LightRAG 초기화 실패: {e}")
            self.use_lightrag = False
            self.rag = None
    
    def _create_llm_func(self, model_name: str):
        """LightRAG용 LLM 함수 생성"""
        def llm_func(prompt, **kwargs):
            try:
                # 기존 OpenAI 클라이언트 사용
                response = self.weaviate_db.openai_client.chat.completions.create(
                    model=model_name,
                    messages=[
                        {"role": "system", "content": kwargs.get("system_prompt", "")},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=kwargs.get("temperature", 0.7),
                    max_tokens=kwargs.get("max_tokens", 1000)
                )
                return response.choices[0].message.content
            except Exception as e:
                logger.error(f"LLM 호출 실패: {e}")
                return ""
        
        return llm_func
    
    def _create_embedding_func(self, model_name: str):
        """LightRAG용 임베딩 함수 생성"""
        embedding_dim = 1536 if "text-embedding-3" in model_name else 1024
        
        def embed_func(texts: List[str]) -> List[List[float]]:
            try:
                response = self.weaviate_db.openai_client.embeddings.create(
                    input=texts,
                    model=model_name
                )
                return [data.embedding for data in response.data]
            except Exception as e:
                logger.error(f"임베딩 생성 실패: {e}")
                return [[0.0] * embedding_dim for _ in texts]
        
        return EmbeddingFunc(
            embedding_dim=embedding_dim,
            max_token_size=8192,
            func=embed_func
        )
    
    async def initialize(self):
        """하이브리드 시스템 초기화"""
        if not self.initialized:
            try:
                # Weaviate 초기화는 이미 완료됨
                
                # LightRAG 관련 초기화
                if self.use_lightrag:
                    await self.lightrag_integration.initialize()
                    if self.rag:
                        # LightRAG 스토리지 초기화
                        await self.rag.ainiitialize_storages()
                
                self.initialized = True
                logger.info("✅ HybridRAGProcessor 초기화 완료")
                
            except Exception as e:
                logger.error(f"❌ 초기화 실패: {e}")
                raise
    
    async def process_document(self, 
                             file_path: Union[str, Path],
                             extract_options: Optional[Dict[str, bool]] = None) -> HybridProcessingResult:
        """
        문서를 하이브리드 방식으로 처리
        
        1. 멀티모달 문서 파싱 (MinerU/magic-pdf)
        2. 지식 그래프 구축 (엔티티/관계 추출)
        3. LightRAG 인덱싱 (그래프 기반)
        4. Weaviate 벡터 저장 (상세 컨텍스트)
        """
        if not self.initialized:
            await self.initialize()
        
        start_time = datetime.now()
        file_path = Path(file_path)
        
        try:
            logger.info(f"📄 하이브리드 처리 시작: {file_path}")
            
            # 1. 멀티모달 문서 처리
            logger.info("1️⃣ 멀티모달 문서 처리 중...")
            doc_data = await self.multimodal_processor.process_document(
                file_path, 
                extract_options, 
                output_format="structured_json"
            )
            
            if not doc_data.get("success", False):
                raise Exception(f"문서 처리 실패: {doc_data.get('error')}")
            
            # 2. 지식 그래프 구축
            logger.info("2️⃣ 지식 그래프 구축 중...")
            kg = self.kg_builder.build_knowledge_graph([doc_data])
            
            # 3. LightRAG 형식으로 변환 및 인덱싱
            lightrag_entities = []
            if self.use_lightrag and self.rag:
                logger.info("3️⃣ LightRAG 인덱싱 중...")
                lightrag_entities = await self._index_to_lightrag(kg, doc_data)
            
            # 4. Weaviate에 상세 청크 저장
            logger.info("4️⃣ Weaviate 벡터 저장 중...")
            chunks = self.multimodal_processor.extract_for_vectorization(doc_data)
            chunk_ids = await self._save_chunks_to_weaviate(chunks, kg)
            
            # 처리 시간 계산
            processing_time = (datetime.now() - start_time).total_seconds()
            
            # 결과 생성
            result = HybridProcessingResult(
                success=True,
                file_path=str(file_path),
                multimodal_elements=doc_data.get("elements", []),
                entities=list(kg.entities.values()),
                relationships=list(kg.relationships.values()),
                lightrag_entities=lightrag_entities,
                weaviate_chunks=chunk_ids,
                processing_time=processing_time,
                metadata={
                    "total_elements": doc_data.get("total_elements", 0),
                    "element_statistics": doc_data.get("element_statistics", {}),
                    "total_entities": len(kg.entities),
                    "total_relationships": len(kg.relationships),
                    "total_chunks": len(chunk_ids),
                    "lightrag_indexed": len(lightrag_entities)
                }
            )
            
            logger.info(f"✅ 하이브리드 처리 완료: {processing_time:.2f}초")
            return result
            
        except Exception as e:
            logger.error(f"❌ 하이브리드 처리 실패: {e}")
            return HybridProcessingResult(
                success=False,
                file_path=str(file_path),
                multimodal_elements=[],
                entities=[],
                relationships=[],
                lightrag_entities=[],
                weaviate_chunks=[],
                processing_time=(datetime.now() - start_time).total_seconds(),
                metadata={"error": str(e)}
            )
    
    async def _index_to_lightrag(self, 
                               kg: KnowledgeGraph, 
                               doc_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """지식 그래프를 LightRAG 형식으로 변환하여 인덱싱"""
        indexed_entities = []
        
        try:
            # 문서 전체를 LightRAG에 추가 (자동 엔티티/관계 추출)
            if self.rag:
                # 전체 텍스트 수집
                full_text = self._collect_text_from_elements(doc_data.get("elements", []))
                
                if full_text:
                    # LightRAG의 insert로 자동 처리
                    await self.rag.ainsert(full_text)
                    logger.info("LightRAG 자동 엔티티/관계 추출 완료")
            
            # 추가로 우리가 추출한 엔티티들을 명시적으로 저장
            for entity_id, entity in kg.entities.items():
                # 엔티티 설명 생성
                description = self._generate_entity_description(entity, kg)
                
                # LightRAG 벡터 스토리지에 저장
                lightrag_entity = {
                    "id": entity_id,
                    "entity_name": entity.name,
                    "entity_type": entity.entity_type.value,
                    "description": description,
                    "source_id": doc_data.get("file_path", "unknown"),
                    "confidence": entity.confidence,
                    "metadata": {
                        **entity.metadata,
                        "mentions_count": len(entity.mentions),
                        "source_element_types": list(set(
                            m.get("element_type", "unknown") for m in entity.mentions
                        ))
                    }
                }
                
                # 벡터 어댑터를 통해 저장
                result = await self.vector_adapter.upsert(lightrag_entity)
                if result.get("status") == "success":
                    indexed_entities.append(lightrag_entity)
            
            # 관계 정보도 저장 (관계를 특별한 엔티티로 저장)
            for rel_id, rel in kg.relationships.items():
                source_entity = kg.entities.get(rel.source_entity_id)
                target_entity = kg.entities.get(rel.target_entity_id)
                
                if source_entity and target_entity:
                    rel_description = (
                        f"{source_entity.name} {rel.relation_type.value} {target_entity.name}. "
                        f"Evidence: {'; '.join(rel.evidence[:3])}"
                    )
                    
                    lightrag_rel = {
                        "id": rel_id,
                        "entity_name": f"{source_entity.name}-{target_entity.name}",
                        "entity_type": f"RELATIONSHIP_{rel.relation_type.value}",
                        "description": rel_description,
                        "source_id": doc_data.get("file_path", "unknown"),
                        "confidence": rel.confidence,
                        "metadata": {
                            "source_entity": source_entity.name,
                            "target_entity": target_entity.name,
                            "relation_type": rel.relation_type.value,
                            **rel.metadata
                        }
                    }
                    
                    result = await self.vector_adapter.upsert(lightrag_rel)
                    if result.get("status") == "success":
                        indexed_entities.append(lightrag_rel)
            
        except Exception as e:
            logger.error(f"LightRAG 인덱싱 실패: {e}")
        
        return indexed_entities
    
    def _generate_entity_description(self, entity: Entity, kg: KnowledgeGraph) -> str:
        """엔티티에 대한 설명 생성"""
        description_parts = []
        
        # 기본 정보
        description_parts.append(f"{entity.name} is a {entity.entity_type.value}")
        
        # 멘션 컨텍스트
        if entity.mentions:
            contexts = [m.get("context", "") for m in entity.mentions[:3]]
            if contexts:
                description_parts.append(f"mentioned in contexts: {'; '.join(contexts)}")
        
        # 관계 정보
        related_entities = []
        for rel in kg.relationships.values():
            if rel.source_entity_id == entity.id:
                target = kg.entities.get(rel.target_entity_id)
                if target:
                    related_entities.append(f"{rel.relation_type.value} {target.name}")
            elif rel.target_entity_id == entity.id:
                source = kg.entities.get(rel.source_entity_id)
                if source:
                    related_entities.append(f"is {rel.relation_type.value} by {source.name}")
        
        if related_entities:
            description_parts.append(f"relationships: {', '.join(related_entities[:5])}")
        
        return ". ".join(description_parts)
    
    def _collect_text_from_elements(self, elements: List[Dict[str, Any]]) -> str:
        """멀티모달 요소들에서 텍스트 수집"""
        texts = []
        
        for elem in elements:
            if elem.get("type") == "text":
                texts.append(elem.get("content", ""))
            elif elem.get("type") == "table":
                # 테이블을 텍스트로 변환
                content = elem.get("content", {})
                if isinstance(content, dict) and "rows" in content:
                    table_text = "\n".join([
                        " | ".join(str(cell) for cell in row)
                        for row in content["rows"]
                    ])
                    texts.append(f"Table:\n{table_text}")
            elif elem.get("type") == "image":
                # OCR 텍스트 추가
                ocr_text = elem.get("metadata", {}).get("ocr_text", "")
                if ocr_text:
                    texts.append(f"Image text: {ocr_text}")
        
        return "\n\n".join(texts)
    
    async def _save_chunks_to_weaviate(self, 
                                     chunks: List[Dict[str, Any]], 
                                     kg: KnowledgeGraph) -> List[str]:
        """청크를 Weaviate에 저장하고 엔티티 정보로 보강"""
        enhanced_chunks = []
        
        for chunk in chunks:
            # 청크와 관련된 엔티티 찾기
            related_entities = self._find_entities_in_chunk(chunk["content"], kg)
            
            # 메타데이터에 엔티티 정보 추가
            chunk["metadata"]["entities"] = [
                {
                    "name": entity.name,
                    "type": entity.entity_type.value,
                    "confidence": entity.confidence
                }
                for entity in related_entities
            ]
            chunk["metadata"]["entity_count"] = len(related_entities)
            
            # 엔티티 이름들을 벡터화 텍스트에 추가 (검색 성능 향상)
            if related_entities:
                entity_names = [e.name for e in related_entities]
                chunk["vectorize_text"] = f"{chunk['content']}\nEntities: {', '.join(entity_names)}"
            
            enhanced_chunks.append(chunk)
        
        # Weaviate에 저장
        chunk_ids = await self.weaviate_db.insert_documents(
            enhanced_chunks,
            vectorize_fields=["content", "vectorize_text"] if "vectorize_text" in enhanced_chunks[0] else ["content"]
        )
        
        return chunk_ids
    
    def _find_entities_in_chunk(self, chunk_text: str, kg: KnowledgeGraph) -> List[Entity]:
        """청크 텍스트에서 언급된 엔티티 찾기"""
        found_entities = []
        chunk_lower = chunk_text.lower()
        
        for entity in kg.entities.values():
            # 엔티티 이름이 청크에 포함되어 있는지 확인
            if entity.name.lower() in chunk_lower:
                found_entities.append(entity)
                continue
            
            # 엔티티의 멘션들 확인
            for mention in entity.mentions:
                mention_text = mention.get("text", "").lower()
                if mention_text and mention_text in chunk_lower:
                    found_entities.append(entity)
                    break
        
        return found_entities
    
    async def hybrid_search(self,
                          query: str,
                          search_mode: str = "hybrid",
                          top_k: int = 10,
                          filters: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        하이브리드 검색 실행
        
        Args:
            query: 검색 쿼리
            search_mode: "hybrid", "graph_only", "vector_only"
            top_k: 반환할 결과 수
            filters: 추가 필터 조건
            
        Returns:
            검색 결과
        """
        if not self.initialized:
            await self.initialize()
        
        results = {
            "query": query,
            "mode": search_mode,
            "graph_results": [],
            "vector_results": [],
            "combined_results": [],
            "metadata": {}
        }
        
        try:
            # 1. LightRAG 그래프 검색
            if search_mode in ["hybrid", "graph_only"] and self.use_lightrag and self.rag:
                logger.info("🔍 LightRAG 그래프 검색 중...")
                graph_response = await self.rag.aquery(
                    query=query,
                    param={"top_k": top_k * 2}  # 더 많이 가져와서 필터링
                )
                
                # 그래프 검색 결과 파싱
                results["graph_results"] = self._parse_lightrag_response(graph_response)
            
            # 2. Weaviate 벡터 검색
            if search_mode in ["hybrid", "vector_only"]:
                logger.info("🔍 Weaviate 벡터 검색 중...")
                
                # 그래프 검색에서 찾은 엔티티로 필터 구성
                entity_filter = None
                if results["graph_results"] and search_mode == "hybrid":
                    entity_names = [r["entity_name"] for r in results["graph_results"][:5]]
                    entity_filter = {"entities": {"contains": entity_names}}
                
                # 필터 병합
                combined_filters = {**(filters or {}), **(entity_filter or {})}
                
                # Weaviate 검색
                vector_results = await self.weaviate_db.search(
                    query=query,
                    limit=top_k,
                    filters=combined_filters if combined_filters else None,
                    hybrid=True  # 하이브리드 검색 (BM25 + 벡터)
                )
                
                results["vector_results"] = vector_results
            
            # 3. 결과 통합 및 순위 재조정
            if search_mode == "hybrid":
                results["combined_results"] = self._combine_results(
                    results["graph_results"],
                    results["vector_results"],
                    top_k
                )
            
            # 메타데이터 추가
            results["metadata"] = {
                "total_graph_results": len(results["graph_results"]),
                "total_vector_results": len(results["vector_results"]),
                "total_combined_results": len(results["combined_results"]),
                "timestamp": datetime.now().isoformat()
            }
            
        except Exception as e:
            logger.error(f"하이브리드 검색 실패: {e}")
            results["metadata"]["error"] = str(e)
        
        return results
    
    def _parse_lightrag_response(self, response: str) -> List[Dict[str, Any]]:
        """LightRAG 응답을 파싱하여 구조화"""
        # LightRAG는 텍스트 응답을 반환하므로 파싱 필요
        # 실제 구현은 LightRAG의 응답 형식에 따라 조정
        parsed_results = []
        
        # 간단한 파싱 예시
        if response:
            # 엔티티와 관계 추출 (실제로는 더 정교한 파싱 필요)
            lines = response.split('\n')
            for line in lines:
                if '->' in line or 'relates to' in line:
                    # 관계 정보 파싱
                    parsed_results.append({
                        "type": "relationship",
                        "content": line.strip(),
                        "confidence": 0.8
                    })
        
        return parsed_results
    
    def _combine_results(self, 
                        graph_results: List[Dict[str, Any]], 
                        vector_results: List[Dict[str, Any]], 
                        top_k: int) -> List[Dict[str, Any]]:
        """그래프와 벡터 검색 결과를 통합하여 순위 재조정"""
        combined = []
        seen_ids = set()
        
        # 점수 정규화 및 가중치 적용
        graph_weight = 0.6  # 그래프 검색 가중치
        vector_weight = 0.4  # 벡터 검색 가중치
        
        # 그래프 결과 추가
        for result in graph_results:
            result_id = result.get("id", str(hash(result.get("content", ""))))
            if result_id not in seen_ids:
                combined.append({
                    **result,
                    "source": "graph",
                    "combined_score": result.get("score", 0.5) * graph_weight
                })
                seen_ids.add(result_id)
        
        # 벡터 결과 추가
        for result in vector_results:
            result_id = result.get("id")
            if result_id not in seen_ids:
                combined.append({
                    **result,
                    "source": "vector",
                    "combined_score": result.get("score", 0.5) * vector_weight
                })
                seen_ids.add(result_id)
            else:
                # 이미 있는 결과라면 점수 업데이트
                for item in combined:
                    if item.get("id") == result_id:
                        item["combined_score"] += result.get("score", 0.5) * vector_weight
                        item["source"] = "both"
                        break
        
        # 통합 점수로 정렬
        combined.sort(key=lambda x: x["combined_score"], reverse=True)
        
        return combined[:top_k]
    
    def close(self):
        """리소스 정리"""
        if self.vector_adapter:
            self.vector_adapter.close()

# 사용 예시
async def example_usage():
    """HybridRAGProcessor 사용 예시"""
    
    # Weaviate DB 설정
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
    
    weaviate_db = WeaviateDB(config)
    await weaviate_db.initialize()
    
    # 하이브리드 프로세서 생성
    processor = HybridRAGProcessor(
        weaviate_db=weaviate_db,
        use_lightrag=True
    )
    await processor.initialize()
    
    # 문서 처리
    result = await processor.process_document(
        "path/to/document.pdf",
        extract_options={
            "extract_text": True,
            "extract_images": True,
            "extract_tables": True
        }
    )
    
    if result.success:
        print(f"✅ 처리 완료!")
        print(f"- 멀티모달 요소: {len(result.multimodal_elements)}개")
        print(f"- 추출된 엔티티: {len(result.entities)}개")
        print(f"- 추출된 관계: {len(result.relationships)}개")
        print(f"- LightRAG 인덱싱: {len(result.lightrag_entities)}개")
        print(f"- Weaviate 청크: {len(result.weaviate_chunks)}개")
        print(f"- 처리 시간: {result.processing_time:.2f}초")
    
    # 하이브리드 검색
    search_results = await processor.hybrid_search(
        query="Find information about machine learning models",
        search_mode="hybrid",
        top_k=5
    )
    
    print(f"\n🔍 검색 결과:")
    print(f"- 그래프 결과: {len(search_results['graph_results'])}개")
    print(f"- 벡터 결과: {len(search_results['vector_results'])}개")
    print(f"- 통합 결과: {len(search_results['combined_results'])}개")
    
    processor.close()
    weaviate_db.close()

if __name__ == "__main__":
    asyncio.run(example_usage())