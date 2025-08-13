from abc import ABC, abstractmethod
from typing import Dict, List, Any, Optional
from dataclasses import dataclass


@dataclass 
class VectorDBConfig:
    """벡터 DB 설정을 나타내는 데이터 클래스"""
    db_type: str  # 'weaviate', 'chroma', 'pinecone', etc.
    connection_params: Dict[str, Any]
    embedding_model: str
    default_class: Optional[str] = None


class VectorSearchResult:
    """검색 결과를 나타내는 클래스"""
    
    def __init__(self, id: str, properties: Dict[str, Any], distance: float = 0.0, score: float = 0.0):
        self.id = id
        self.properties = properties
        self.distance = distance
        self.score = score
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "properties": self.properties,
            "distance": self.distance,
            "score": self.score
        }


class VectorDB(ABC):
    """모든 벡터 DB 구현체가 상속받아야 하는 추상 기본 클래스"""
    
    def __init__(self, config: VectorDBConfig):
        self.config = config
        
    @abstractmethod
    async def initialize(self) -> None:
        """DB 연결 초기화"""
        pass
    
    @abstractmethod
    async def create_schema(self, schema_definition: Dict[str, Any]) -> bool:
        """스키마 생성"""
        pass
    
    @abstractmethod
    async def insert_documents(
        self, 
        documents: List[Dict[str, Any]], 
        class_name: str = None
    ) -> List[str]:
        """문서 삽입"""
        pass
    
    @abstractmethod
    async def search(
        self,
        query: str,
        class_name: str = None,
        limit: int = 5,
        filters: Optional[Dict[str, Any]] = None,
        hybrid: bool = False
    ) -> List[Dict[str, Any]]:
        """벡터 검색 수행"""
        pass
    
    @abstractmethod
    async def get_document_by_id(self, doc_id: str, class_name: str = None) -> Optional[Dict[str, Any]]:
        """ID로 문서 조회"""
        pass
    
    def close(self):
        """연결 종료"""
        pass 