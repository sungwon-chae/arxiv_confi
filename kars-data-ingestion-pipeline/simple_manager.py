import os
import json
import logging
from typing import Dict, Any, List, Optional
from pathlib import Path
from dotenv import load_dotenv

from base import VectorDBConfig, VectorSearchResult
from weaviate_db import WeaviateDB

# 환경변수 로드
env_path = Path(__file__).parent / 'config.env'
load_dotenv(env_path)

logger = logging.getLogger(__name__)

class MultipleVectorDBManager:
    """다중 스키마 지원 벡터 DB 매니저 - mcp_tools 전용 (최적화됨)"""
    
    def __init__(self):
        self.db_instance = None
        self.active_collections = {}  # {db_name: [class_name1, class_name2, ...]}
        self.initialized = False
        
        # 환경 변수에서 설정 로드 (config.env 파일에서 로드됨)
        self.weaviate_url = os.getenv('WEAVIATE_URL', 'http://localhost:8084')
        self.openai_api_key = os.getenv('OPENAI_API_KEY', 'token-abc123')
        self.openai_base_url = os.getenv('OPENAI_BASE_URL', 'http://localhost:8125')
        
        logger.info(f"Weaviate URL: {self.weaviate_url}")
        logger.info(f"OpenAI Base URL: {self.openai_base_url}")
    
    async def _ensure_db_connection(self):
        """DB 연결 보장"""
        if not self.db_instance or not self.initialized:
            config = VectorDBConfig(
                db_type="weaviate",
                connection_params={
                    "url": self.weaviate_url,
                    "openai_api_key": self.openai_api_key,
                    "openai_base_url": self.openai_base_url
                },
                embedding_model=os.getenv('EMBEDDING_MODEL', '/data/models_ckpt/bge-m3'),  # vLLM에서 동적으로 가져옴
                default_class=os.getenv('DEFAULT_CLASS', 'Document')
            )
            
            self.db_instance = WeaviateDB(config)
            await self.db_instance.initialize()
            self.initialized = True
            logger.info("DB 연결 초기화 완료")
            
            # 기존 클래스들을 자동으로 감지하여 active_collections에 등록
            await self._load_existing_classes()
    
    def _load_class_mapping(self) -> Dict[str, List[str]]:
        """클래스명 매핑 설정 로드 (db_name -> [class_names])"""
        try:
            mapping_path = os.path.join(os.path.dirname(__file__), 'schema_examples', 'class_mapping.json')
            if os.path.exists(mapping_path):
                with open(mapping_path, 'r', encoding='utf-8') as f:
                    mapping_config = json.load(f)
                    return mapping_config.get('mappings', {})
            else:
                logger.warning("클래스 매핑 파일이 없습니다. 기본 규칙을 사용합니다.")
                return {}
        except Exception as e:
            logger.error(f"클래스 매핑 로드 실패: {e}")
            return {}

    async def _load_existing_classes(self):
        """Weaviate에서 기존 클래스들을 감지하여 active_collections에 등록"""
        try:
            # Weaviate 스키마 조회
            schema_data = await self.db_instance.get_schema()
            if not schema_data or 'classes' not in schema_data:
                logger.info("기존 클래스 없음")
                return
            
            # 클래스명 매핑 규칙 로드 (db_name -> [class_names])
            db_to_classes_mapping = self._load_class_mapping()
            
            # 역매핑을 위한 딕셔너리 생성 (class_name -> db_name)
            class_to_db_mapping = {}
            for db_name, class_names in db_to_classes_mapping.items():
                for class_name in class_names:
                    class_to_db_mapping[class_name] = db_name
            
            for class_info in schema_data['classes']:
                class_name = class_info['class']
                
                # 매핑 규칙에 따라 db_name 결정
                if class_name in class_to_db_mapping:
                    db_name = class_to_db_mapping[class_name]
                else:
                    # 기본 규칙: ClassName -> classname_db
                    db_name = class_name.lower().replace('document', '') + '_db'
                
                # active_collections에 추가 (리스트 형태로)
                if db_name not in self.active_collections:
                    self.active_collections[db_name] = []
                
                if class_name not in self.active_collections[db_name]:
                    self.active_collections[db_name].append(class_name)
                    logger.info(f"기존 클래스 등록: {db_name} -> {class_name}")
            
            logger.info(f"총 {len(self.active_collections)}개 DB에 클래스 등록 완료")
            for db_name, class_names in self.active_collections.items():
                logger.info(f"  {db_name}: {class_names}")
            
        except Exception as e:
            logger.error(f"기존 클래스 로드 실패: {e}")
    
    async def create_schema(self, db_name: str, schema_file: str) -> bool:
        """스키마 생성"""
        try:
            await self._ensure_db_connection()
            
            # 스키마 파일 로드
            schema_path = os.path.join(os.path.dirname(__file__), 'schema_examples', schema_file)
            if not os.path.exists(schema_path):
                logger.error(f"스키마 파일 찾을 수 없음: {schema_file}")
                return False
            
            with open(schema_path, 'r', encoding='utf-8') as f:
                schema_definition = json.load(f)
            
            class_name = schema_definition.get("class", "Document")
            
            logger.info(f"스키마 생성 시작: {db_name} -> {class_name}")
            
            # 스키마 생성
            success = await self.db_instance.create_schema(schema_definition)
            if success:
                if db_name not in self.active_collections:
                    self.active_collections[db_name] = []
                if class_name not in self.active_collections[db_name]:
                    self.active_collections[db_name].append(class_name)
                logger.info(f"스키마 생성 완료: {db_name} -> {class_name}")
                return True
            else:
                logger.error(f"스키마 생성 실패: {db_name}")
                return False
                
        except Exception as e:
            logger.error(f"스키마 생성 중 오류: {e}")
            return False

    async def create_schema_from_definition(self, db_name: str, schema_definition: Dict[str, Any]) -> bool:
        """스키마 정의로부터 직접 스키마 생성 (새로운 스키마 처리용)"""
        try:
            await self._ensure_db_connection()
            
            class_name = schema_definition.get("class", "Document")
            
            logger.info(f"동적 스키마 생성 시작: {db_name} -> {class_name}")
            
            # 스키마 생성
            success = await self.db_instance.create_schema(schema_definition)
            if success:
                if db_name not in self.active_collections:
                    self.active_collections[db_name] = []
                if class_name not in self.active_collections[db_name]:
                    self.active_collections[db_name].append(class_name)
                logger.info(f"동적 스키마 생성 완료: {db_name} -> {class_name}")
                return True
            else:
                logger.error(f"동적 스키마 생성 실패: {db_name}")
                return False
                
        except Exception as e:
            logger.error(f"동적 스키마 생성 중 오류: {e}")
            return False

    async def create_schema_from_json(self, db_name: str, schema_json: str) -> bool:
        """JSON 문자열로부터 스키마 생성"""
        try:
            schema_definition = json.loads(schema_json)
            return await self.create_schema_from_definition(db_name, schema_definition)
        except json.JSONDecodeError as e:
            logger.error(f"JSON 파싱 실패: {e}")
            return False
        except Exception as e:
            logger.error(f"JSON 스키마 생성 실패: {e}")
            return False

    def validate_schema_definition(self, schema_definition: Dict[str, Any]) -> Dict[str, Any]:
        """스키마 정의 유효성 검사 및 정규화"""
        result = {"valid": True, "errors": [], "normalized": None}
        
        try:
            # 필수 필드 검사
            if "class" not in schema_definition:
                result["errors"].append("'class' 필드가 필요합니다")
            
            if "properties" not in schema_definition:
                result["errors"].append("'properties' 필드가 필요합니다")
            
            if result["errors"]:
                result["valid"] = False
                return result
            
            # 스키마 정규화
            normalized = {
                "class": schema_definition["class"],
                "vectorizer": schema_definition.get("vectorizer", "text2vec-openai"),
                "properties": [],
                "moduleConfig": schema_definition.get("moduleConfig", self._get_default_module_config(schema_definition["properties"]))
            }
            
            # 속성 정규화
            for prop in schema_definition["properties"]:
                if not isinstance(prop, dict) or "name" not in prop:
                    result["errors"].append(f"속성 정의가 잘못되었습니다: {prop}")
                    continue
                
                normalized_prop = {
                    "name": prop["name"],
                    "dataType": prop.get("dataType", ["text"]),
                    "description": prop.get("description", "")
                }
                normalized["properties"].append(normalized_prop)
            
            if result["errors"]:
                result["valid"] = False
            else:
                result["normalized"] = normalized
            
        except Exception as e:
            result["valid"] = False
            result["errors"].append(f"스키마 검증 중 오류: {str(e)}")
        
        return result

    def _get_default_module_config(self, properties: List[Dict[str, Any]]) -> Dict[str, Any]:
        """기본 모듈 설정 생성 (vectorize 필드 기반 또는 content/text 필드 우선)"""
        config = {
            "text2vec-openai": {
                "model": os.getenv('EMBEDDING_MODEL', '/data/models_ckpt/bge-m3'),
                "type": "text",
                "vectorizeClassName": False,
                "vectorizePropertyName": False,
                "properties": {}
            }
        }
        
        # 1. vectorize 필드가 있는 경우 그것을 우선 사용
        has_vectorize_field = any(prop.get("vectorize") is not None for prop in properties)
        
        if has_vectorize_field:
            for prop in properties:
                prop_name = prop.get("name", "")
                vectorize = prop.get("vectorize", False)
                
                # text 타입 필드만 skip 설정 적용
                if prop.get("dataType", ["text"])[0] == "text":
                    config["text2vec-openai"]["properties"][prop_name] = {"skip": not vectorize}
        else:
            # 2. vectorize 필드가 없는 경우 기본 로직 사용 (content > text 순서)
            for prop in properties:
                prop_name = prop.get("name", "")
                
                # 우선순위: content > text > 기타 skip
                if prop_name == "content":
                    config["text2vec-openai"]["properties"][prop_name] = {"skip": False}
                elif prop_name == "text":
                    # content 필드가 있으면 text는 skip, 없으면 text 사용
                    has_content = any(p.get("name") == "content" for p in properties)
                    config["text2vec-openai"]["properties"][prop_name] = {"skip": has_content}
                else:
                    # text 타입 필드만 skip 설정 (다른 타입은 자동으로 스킵됨)
                    if prop.get("dataType", ["text"])[0] == "text":
                        config["text2vec-openai"]["properties"][prop_name] = {"skip": True}
        
        return config

    def _detect_vectorize_fields(self, documents: List[Dict[str, Any]]) -> List[str]:
        """문서에서 벡터화할 필드 자동 감지"""
        if not documents:
            return []
        
        # 우선순위: content > text > title > 기타 긴 텍스트 필드
        priority_fields = ["content", "text", "title", "description", "summary"]
        
        sample_doc = documents[0]
        detected_fields = []
        
        # 우선순위 필드 검사
        for field in priority_fields:
            if field in sample_doc:
                value = sample_doc[field]
                if isinstance(value, str) and len(value.strip()) > 10:  # 의미있는 텍스트
                    detected_fields.append(field)
                    break  # 첫 번째 우선순위 필드만 사용
        
        # 우선순위 필드가 없으면 긴 텍스트 필드 찾기
        if not detected_fields:
            for field, value in sample_doc.items():
                if isinstance(value, str) and len(value.strip()) > 50:  # 긴 텍스트
                    detected_fields.append(field)
                    break
        
        # 기본값으로 None 반환 (스키마 기반 자동 벡터화 사용)
        return detected_fields if detected_fields else None

    async def load_data(self, db_name: str, schema_file: str, documents: List[Dict[str, Any]] = None, 
                       vectorize_fields: List[str] = None) -> Dict[str, Any]:
        """데이터 로딩 (테스트용 더미 데이터 또는 실제 데이터)"""
        try:
            if db_name not in self.active_collections:
                logger.error(f"활성화된 컬렉션 없음: {db_name}")
                return {"success": False, "message": "컬렉션이 활성화되지 않음"}
            
            # 첫 번째 클래스 사용 (기본적으로 단일 클래스 가정)
            class_names = self.active_collections[db_name]
            if not class_names:
                logger.error(f"DB {db_name}에 활성화된 클래스가 없음")
                return {"success": False, "message": "활성화된 클래스가 없음"}
            
            class_name = class_names[0]  # 첫 번째 클래스 사용
            
            # 실제 데이터가 제공되지 않으면 더미 데이터 생성
            if not documents:
                documents = self._generate_dummy_data(db_name, schema_file)
            
            # 벡터화 필드가 지정되지 않은 경우 자동 감지
            if vectorize_fields is None:
                vectorize_fields = self._detect_vectorize_fields(documents)
            
            inserted_ids = await self.db_instance.insert_documents(
                documents, class_name, vectorize_fields
            )
            
            return {
                "success": True,
                "message": f"{len(inserted_ids)}개 문서 삽입 완료",
                "inserted_count": len(inserted_ids),
                "inserted_ids": inserted_ids,
                "vectorize_fields": vectorize_fields
            }
            
        except Exception as e:
            logger.error(f"데이터 로딩 실패: {e}")
            return {"success": False, "message": str(e)}

    def _generate_dummy_data(self, db_name: str, schema_file: str) -> List[Dict[str, Any]]:
        """스키마별 더미 데이터 생성 (실제 데이터가 없는 스키마용)"""
        if "news" in schema_file.lower():
            return [
                {
                    "text": "인공지능 기술의 급속한 발전으로 다양한 산업 분야에서 혁신이 일어나고 있다. 특히 법률 분야에서도 AI를 활용한 판례 검색과 문서 분석이 활발히 도입되고 있어 업무 효율성이 크게 향상되고 있다.",
                    "content": "인공지능 기술의 급속한 발전으로 다양한 산업 분야에서 혁신이 일어나고 있다. 특히 법률 분야에서도 AI를 활용한 판례 검색과 문서 분석이 활발히 도입되고 있어 업무 효율성이 크게 향상되고 있다.",
                    "title": "AI 기술 혁신, 법률 분야까지 확산",
                    "author": "김기자",
                    "category": "기술",
                    "publishDate": "2024-01-15",
                    "source": "테크뉴스",
                    "tags": ["AI", "인공지능", "법률", "혁신"]
                },
                {
                    "text": "최근 대법원이 발표한 새로운 판례에 따르면, 디지털 증거의 증명력에 대한 기준이 더욱 명확해졌다. 이는 사이버 범죄 수사와 재판에서 중요한 의미를 갖는다고 법조계는 평가하고 있다.",
                    "content": "최근 대법원이 발표한 새로운 판례에 따르면, 디지털 증거의 증명력에 대한 기준이 더욱 명확해졌다. 이는 사이버 범죄 수사와 재판에서 중요한 의미를 갖는다고 법조계는 평가하고 있다.",
                    "title": "대법원, 디지털 증거 증명력 기준 명확화",
                    "author": "박기자",
                    "category": "법률",
                    "publishDate": "2024-01-14",
                    "source": "법률신문",
                    "tags": ["대법원", "판례", "디지털증거", "사이버범죄"]
                },
                {
                    "text": "전국 법무법인들이 AI 기반 리걸테크 도구 도입을 가속화하고 있다. 문서 검토, 계약서 분석, 판례 검색 등의 업무에서 AI가 활용되면서 변호사들의 업무 방식이 크게 변화하고 있다.",
                    "content": "전국 법무법인들이 AI 기반 리걸테크 도구 도입을 가속화하고 있다. 문서 검토, 계약서 분석, 판례 검색 등의 업무에서 AI가 활용되면서 변호사들의 업무 방식이 크게 변화하고 있다.",
                    "title": "법무법인, AI 리걸테크 도입 가속화",
                    "author": "이기자",
                    "category": "법률",
                    "publishDate": "2024-01-13",
                    "source": "리걸타임즈",
                    "tags": ["리걸테크", "AI", "법무법인", "변호사"]
                }
            ]
        else:
            return [
                {
                    "text": f"{db_name}에 대한 샘플 문서 내용입니다.",
                    "content": f"{db_name}에 대한 샘플 문서 내용입니다.",
                    "documentId": 9999,
                    "documentName": f"{db_name} 샘플 문서",
                    "documentType": "일반문서",
                    "source": "시스템"
                }
            ]

    def _get_default_class_name(self, db_name: str) -> str:
        """DB 이름을 기반으로 기본 클래스명 생성 (enron_db -> EnronDocument)"""
        # enron_db -> EnronDocument
        parts = db_name.split('_')
        class_name = ''.join(part.capitalize() for part in parts if part != 'db')
        return f"{class_name}Document"
    
    def _get_class_names_for_db(self, db_name: str, class_names: Optional[Dict[str, List[str]]] = None) -> List[str]:
        """DB에 대한 클래스명 리스트 반환"""
        if class_names and db_name in class_names:
            return class_names[db_name]
        
        # active_collections에서 확인
        if db_name in self.active_collections:
            active_class = self.active_collections[db_name]
            if isinstance(active_class, list):
                return active_class
            else:
                return [active_class]
        
        # 기본 클래스명 생성
        return [self._get_default_class_name(db_name)]

    async def search(self, db_names: List[str], query: str, limit: int = 5, 
                    filters: Optional[Dict[str, Any]] = None, hybrid: bool = True,
                    class_names: Optional[Dict[str, List[str]]] = None) -> Dict[str, Any]:
        """다중 DB 검색"""
        try:
            await self._ensure_db_connection()
            
            results = {}
            
            for db_name in db_names:
                # DB별 클래스명 리스트 가져오기
                db_class_names = self._get_class_names_for_db(db_name, class_names)
                
                all_results = []
                errors = []
                
                # 각 클래스별로 검색 수행
                for class_name in db_class_names:
                    try:
                        search_results = await self.db_instance.search(
                            query=query,
                            class_name=class_name,
                            limit=limit,
                            filters=filters,
                            hybrid=hybrid
                        )
                        
                        # 결과를 VectorSearchResult 객체로 변환하고 클래스명 추가
                        for result in search_results:
                            if isinstance(result, dict):
                                vector_result = VectorSearchResult(
                                    id=result.get('id', ''),
                                    properties=result.get('properties', {}),
                                    distance=result.get('distance', 0.0),
                                    score=result.get('score', 0.0)
                                )
                                # 클래스명 정보 추가
                                vector_result.properties['_class_name'] = class_name
                                all_results.append(vector_result)
                            else:
                                # 기존 result 객체에 클래스명 추가
                                if hasattr(result, 'properties'):
                                    result.properties['_class_name'] = class_name
                                all_results.append(result)
                        
                    except Exception as e:
                        logger.error(f"DB '{db_name}', 클래스 '{class_name}' 검색 실패: {e}")
                        errors.append(f"클래스 '{class_name}': {str(e)}")
                
                # 결과 통합 - 점수/거리 기준으로 정렬
                if all_results:
                    # 하이브리드 검색인 경우 score 기준, 아니면 distance 기준으로 정렬
                    if hybrid:
                        all_results.sort(key=lambda x: getattr(x, 'score', 0.0), reverse=True)
                    else:
                        all_results.sort(key=lambda x: getattr(x, 'distance', float('inf')))
                    
                    # limit 적용
                    all_results = all_results[:limit]
                
                # 결과 저장
                if all_results:
                    results[db_name] = {
                        "results": all_results,
                        "total": len(all_results),
                        "searched_classes": db_class_names
                    }
                    if errors:
                        results[db_name]["partial_errors"] = errors
                else:
                    results[db_name] = {
                        "error": f"모든 클래스 검색 실패: {'; '.join(errors)}" if errors else "검색 결과 없음",
                        "results": [],
                        "searched_classes": db_class_names
                    }
            
            return {
                "query": query,
                "results": results,
                "total_databases": len(db_names)
            }
            
        except Exception as e:
            logger.error(f"다중 DB 검색 실패: {e}")
            return {
                "query": query,
                "error": str(e),
                "results": {}
            }

    async def get_document_by_id(self, db_name: str, doc_id: str, class_name: str = None) -> Dict[str, Any]:
        """ID로 문서 조회"""
        try:
            await self._ensure_db_connection()
            
            if db_name not in self.active_collections and not class_name:
                return {
                    "database": db_name,
                    "doc_id": doc_id,
                    "error": f"DB '{db_name}'이 활성화되지 않음",
                    "document": None
                }
            
            target_class = class_name or self.active_collections[db_name]
            
            document = await self.db_instance.get_document_by_id(doc_id, target_class)
            
            return {
                "database": db_name,
                "doc_id": doc_id,
                "class_name": target_class,
                "document": document
            }
            
        except Exception as e:
            logger.error(f"문서 조회 실패: {e}")
            return {
                "database": db_name,
                "doc_id": doc_id,
                "error": str(e),
                "document": None
            }

    def list_databases(self) -> List[str]:
        """활성화된 데이터베이스 목록"""
        # 메모리의 active_collections와 실제 Weaviate 서버의 클래스들을 모두 확인
        databases = set(self.active_collections.keys())
        
        # Weaviate 서버에서 실제 존재하는 클래스들도 추가
        try:
            if self.db_instance and hasattr(self.db_instance, 'client'):
                # Weaviate v4 클라이언트에서 컬렉션 목록 조회
                collections = self.db_instance.client.collections.list_all()
                for collection_name in collections:
                    # 컬렉션명을 db_name으로 변환 (역매핑)
                    db_name = self._class_to_db_name(collection_name)
                    databases.add(db_name)
                    # active_collections에도 추가 (동기화)
                    if db_name not in self.active_collections:
                        self.active_collections[db_name] = []
                    if collection_name not in self.active_collections[db_name]:
                        self.active_collections[db_name].append(collection_name)
        except Exception as e:
            logger.warning(f"Weaviate 서버에서 컬렉션 목록 조회 실패: {e}")
        
        return list(databases)
    
    def _class_to_db_name(self, class_name: str) -> str:
        """클래스명을 db_name으로 변환"""
        # 매핑 파일에서 규칙 로드 (db_name -> [class_names])
        db_to_classes_mapping = self._load_class_mapping()
        
        # 역매핑으로 class_name -> db_name 찾기
        for db_name, class_names in db_to_classes_mapping.items():
            if class_name in class_names:
                return db_name
        
        # 없으면 클래스명을 기반으로 db_name 생성
        # 예: MyDocument -> my_db
        db_name = class_name.replace('Document', '').lower()
        if not db_name.endswith('_db'):
            db_name += '_db'
        return db_name

    def list_schemas(self) -> List[str]:
        """사용 가능한 스키마 파일 목록"""
        try:
            schema_dir = os.path.join(os.path.dirname(__file__), 'schema_examples')
            if os.path.exists(schema_dir):
                return [f for f in os.listdir(schema_dir) if f.endswith('.json')]
            return []
        except Exception as e:
            logger.error(f"스키마 목록 조회 실패: {e}")
            return []

    def is_initialized(self) -> bool:
        """초기화 상태 확인"""
        return self.initialized and self.db_instance is not None

    def close(self):
        """연결 종료"""
        if self.db_instance:
            self.db_instance.close()
            logger.info("vectordb 연결 종료")
        
        self.initialized = False
        self.active_collections.clear()

# 싱글톤 인스턴스
_manager_instance = None

async def initialize_manager() -> MultipleVectorDBManager:
    """매니저 인스턴스 초기화 및 반환 (비동기 싱글톤)"""
    global _manager_instance
    if _manager_instance is None:
        _manager_instance = MultipleVectorDBManager()
        await _manager_instance._ensure_db_connection()
    return _manager_instance

def get_manager() -> MultipleVectorDBManager:
    """매니저 인스턴스 반환 (동기 싱글톤 - 이미 초기화된 경우에만 사용)"""
    global _manager_instance
    if _manager_instance is None:
        _manager_instance = MultipleVectorDBManager()
    return _manager_instance 