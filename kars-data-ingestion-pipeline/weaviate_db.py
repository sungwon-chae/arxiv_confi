import logging
import os
from typing import Dict, Any, List, Optional
from pathlib import Path
from datetime import datetime
import re
import weaviate
from weaviate.classes.config import Property, DataType, Configure, VectorDistances
from weaviate.classes.query import Filter, MetadataQuery
from openai import OpenAI
from dotenv import load_dotenv
from base import VectorDB, VectorDBConfig

# 환경변수 로드
env_path = Path(__file__).parent / 'config.env'
load_dotenv(env_path)

logger = logging.getLogger(__name__)

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
        logger.warning(f"날짜 형식 파싱 실패: {date_str}, 기본값 사용")
        return "1970-01-01T00:00:00Z"
        
    except Exception as e:
        logger.warning(f"날짜 변환 오류: {e}, 기본값 사용")
        return "1970-01-01T00:00:00Z"

class WeaviateDB(VectorDB):
    """Weaviate 벡터 데이터베이스 구현체 (test_openai_vectorizer.py 방식 완전 적용)"""
    
    def __init__(self, config: VectorDBConfig):
        super().__init__(config)
        self.client = None
        self.openai_client = None
        self.dynamic_model_name = None
        
    async def initialize(self):
        """초기화 (test_openai_vectorizer.py 방식 그대로)"""
        try:
            # 1. 먼저 OpenAI 클라이언트 초기화 및 모델명 동적 가져오기
            openai_api_key = self.config.connection_params.get('openai_api_key', os.getenv('OPENAI_API_KEY', 'token-abc123'))
            openai_base_url_with_v1 = self.config.connection_params.get('openai_base_url', os.getenv('OPENAI_BASE_URL', 'http://localhost:8125'))
            
            # /v1 suffix가 있으면 제거하고 다시 추가 (일관성 보장)
            if openai_base_url_with_v1.endswith('/v1'):
                openai_base_url_with_v1 = openai_base_url_with_v1[:-3]
            openai_base_url_with_v1 += '/v1'
            
            self.openai_client = OpenAI(
                api_key=openai_api_key,
                base_url=openai_base_url_with_v1
            )
            
            # vLLM 서버에서 모델명 동적 가져오기 (test_openai_vectorizer.py 방식)
            try:
                models = self.openai_client.models.list()
                if models.data:
                    self.dynamic_model_name = models.data[0].id
                    logger.info(f"✅ vLLM 서버에서 모델명 가져옴: {self.dynamic_model_name}")
                else:
                    self.dynamic_model_name = self.config.embedding_model
                    logger.warning(f"⚠️ vLLM 서버에서 모델 목록이 비어있음. 기본값 사용: {self.dynamic_model_name}")
            except Exception as e:
                logger.warning(f"⚠️ vLLM 서버에서 모델명 가져오기 실패: {e}")
                self.dynamic_model_name = self.config.embedding_model

            # 2. 샘플 임베딩 생성 확인 (test_openai_vectorizer.py 방식)
            try:
                sample_text = "벡터 데이터베이스 연결 테스트"
                response = self.openai_client.embeddings.create(
                    input=[sample_text],
                    model=self.dynamic_model_name,
                )
                embedding = response.data[0].embedding
                logger.info(f"✅ 샘플 임베딩 생성 성공 (차원: {len(embedding)})")
            except Exception as e:
                logger.error(f"❌ 샘플 임베딩 생성 실패: {e}")
                raise

            # 3. Weaviate 클라이언트 연결
            url = self.config.connection_params.get('url', os.getenv('WEAVIATE_URL', 'http://localhost:8084'))
            
            # URL에서 호스트와 포트 추출
            if '://' in url:
                protocol, host_port = url.split('://', 1)
                if ':' in host_port:
                    host, port = host_port.split(':', 1)
                    port = int(port)
                else:
                    host = host_port
                    port = int(os.getenv('WEAVIATE_PORT', '8084'))
            else:
                host = os.getenv('WEAVIATE_HOST', 'localhost')
                port = int(os.getenv('WEAVIATE_PORT', '8084'))
            
            # OpenAI 헤더 설정 (test_openai_vectorizer.py 방식 - /v1 제거)
            # Weaviate 컨테이너에서 호스트의 vLLM 서버에 접근하기 위해 host.docker.internal 사용
            openai_base_url_for_weaviate = openai_base_url_with_v1.replace('localhost', 'host.docker.internal').replace('/v1', '')
            headers = {
                "X-OpenAI-Api-Key": openai_api_key, 
                "X-OpenAI-BaseURL": openai_base_url_for_weaviate  # Weaviate expects URL without /v1
            }
            
            # gRPC 포트 환경변수에서 가져오기
            grpc_port = int(os.getenv('WEAVIATE_GRPC_PORT', '50051'))
            
            # 원격 서버 연결을 위해 connect_to_local 대신 weaviate.connect_to_custom 사용
            if host == 'localhost' or host == '127.0.0.1':
                self.client = weaviate.connect_to_local(
                    host=host,
                    port=port,
                    grpc_port=grpc_port,
                    headers=headers
                )
            else:
                # 원격 서버 연결
                self.client = weaviate.connect_to_custom(
                    http_host=host,
                    http_port=port,
                    http_secure=False,
                    grpc_host=host,
                    grpc_port=grpc_port,
                    grpc_secure=False,
                    headers=headers
                )
            
            logger.info(f"✅ Weaviate 클라이언트 연결 성공: {url}")
            logger.info(f"📡 OpenAI Base URL (Python용): {openai_base_url_with_v1}")
            logger.info(f"📡 OpenAI Base URL (Weaviate용): {headers['X-OpenAI-BaseURL']}")
            logger.info(f"🔧 동적 모델명: {self.dynamic_model_name}")
            
        except Exception as e:
            logger.error(f"❌ Weaviate 초기화 실패: {e}")
            raise

    async def create_schema(self, schema_definition: Dict[str, Any]) -> bool:
        """스키마 생성 (동적 모델명 사용, test_openai_vectorizer.py 방식)"""
        try:
            class_name = schema_definition.get("class", "Document")
            
            # 기존 컬렉션 삭제
            if self.client.collections.exists(class_name):
                self.client.collections.delete(class_name)
                logger.info(f"🗑️ 기존 컬렉션 삭제: {class_name}")
            
            # 속성 정의
            properties = []
            for prop in schema_definition.get("properties", []):
                prop_name = prop["name"]
                prop_type = prop.get("dataType", ["text"])[0].upper()
                
                # 데이터 타입 매핑
                if prop_type == "TEXT":
                    data_type = DataType.TEXT
                elif prop_type == "INT":
                    data_type = DataType.INT
                elif prop_type == "NUMBER":
                    data_type = DataType.NUMBER
                elif prop_type == "BOOLEAN":
                    data_type = DataType.BOOL
                elif prop_type == "DATE":
                    data_type = DataType.DATE
                else:
                    data_type = DataType.TEXT
                
                properties.append(Property(name=prop_name, data_type=data_type))
            
            # 벡터라이저 설정에서 동적 모델명 사용 (test_openai_vectorizer.py 방식)
            # Weaviate 컨테이너에서 호스트의 vLLM 서버에 접근하기 위해 host.docker.internal 사용
            openai_base_url_raw = self.config.connection_params.get('openai_base_url', os.getenv('OPENAI_BASE_URL', 'http://localhost:8125'))
            # Docker 내부에서 사용할 URL (컨테이너에서 호스트 접근용)
            openai_base_url_for_weaviate = os.getenv('OPENAI_BASE_URL_DOCKER', openai_base_url_raw.replace('localhost', 'host.docker.internal'))
            if openai_base_url_for_weaviate.endswith('/v1'):
                openai_base_url_for_weaviate = openai_base_url_for_weaviate[:-3]
            
            vectorizer = Configure.Vectorizer.text2vec_openai(
                model=self.dynamic_model_name,  # 동적 모델명 사용
                base_url=openai_base_url_for_weaviate  # /v1 제거된 URL 사용
            )
            
            # 컬렉션 생성 (test_openai_vectorizer.py 방식)
            collection = self.client.collections.create(
                name=class_name,
                properties=properties,
                vectorizer_config=vectorizer,
                vector_index_config=Configure.VectorIndex.hnsw(
                    distance_metric=VectorDistances.COSINE
                )
            )
            
            logger.info(f"✅ 스키마 생성 성공: {class_name} (모델: {self.dynamic_model_name})")
            return True
            
        except Exception as e:
            logger.error(f"❌ 스키마 생성 실패: {e}")
            return False

    async def get_schema(self) -> Dict[str, Any]:
        """Weaviate 스키마 조회"""
        try:
            # Weaviate v4 client를 사용해서 스키마 조회
            schema_data = {"classes": []}
            
            # 모든 컬렉션 조회
            for collection_name in self.client.collections.list_all():
                try:
                    collection = self.client.collections.get(collection_name)
                    collection_config = collection.config.get()
                    
                    # 클래스 정보 구성
                    class_info = {
                        "class": collection_name,
                        "vectorizer": collection_config.vectorizer_config.vectorizer.value if collection_config.vectorizer_config else None,
                        "properties": []
                    }
                    
                    # 속성 정보 추가
                    if hasattr(collection_config, 'properties') and collection_config.properties:
                        if hasattr(collection_config.properties, 'items'):
                            # Dict-like properties
                            for prop_name, prop_config in collection_config.properties.items():
                                prop_info = {
                                    "name": prop_name,
                                    "dataType": [prop_config.data_type.value] if prop_config.data_type else ["text"]
                                }
                                class_info["properties"].append(prop_info)
                        elif isinstance(collection_config.properties, list):
                            # List-like properties
                            for prop_config in collection_config.properties:
                                if hasattr(prop_config, 'name'):
                                    prop_info = {
                                        "name": prop_config.name,
                                        "dataType": [prop_config.data_type.value] if hasattr(prop_config, 'data_type') and prop_config.data_type else ["text"]
                                    }
                                    class_info["properties"].append(prop_info)
                    
                    schema_data["classes"].append(class_info)
                    
                except Exception as e:
                    logger.warning(f"컬렉션 {collection_name} 정보 조회 실패: {e}")
                    continue
            
            logger.info(f"스키마 조회 완료: {len(schema_data['classes'])}개 클래스")
            return schema_data
            
        except Exception as e:
            logger.error(f"스키마 조회 실패: {e}")
            return {"classes": []}

    async def insert_documents(self, documents: List[Dict[str, Any]], class_name: str = None, 
                              vectorize_fields: List[str] = None) -> List[str]:
        """문서 삽입 (스키마 기반 자동 벡터화 + 선택적 필드 벡터화)"""
        if not class_name:
            class_name = self.config.default_class
        
        try:
            collection = self.client.collections.get(class_name)
            inserted_ids = []
            
            # 벡터화 필드 로깅
            if vectorize_fields:
                logger.info(f"📝 수동 벡터화 필드 지정: {vectorize_fields}")
            else:
                logger.info(f"📝 스키마 기반 자동 벡터화 사용 (moduleConfig 기반)")
            
            # 배치 삽입
            with collection.batch.dynamic() as batch:
                for i, doc in enumerate(documents):
                    try:
                        # 날짜 필드 정규화
                        normalized_doc = self._normalize_document_dates(doc)
                        
                        # 벡터화 필드가 명시적으로 지정된 경우 처리
                        if vectorize_fields:
                            # 명시된 필드들만 벡터화용 텍스트 생성
                            vectorize_text = self._create_vectorize_text(normalized_doc, vectorize_fields)
                            logger.debug(f"문서 {i+1} 벡터화 텍스트: {vectorize_text[:100]}...")
                            
                            # 수동 임베딩 생성
                            try:
                                response = self.openai_client.embeddings.create(
                                    input=[vectorize_text],
                                    model=self.dynamic_model_name,
                                )
                                vector = response.data[0].embedding
                                logger.debug(f"문서 {i+1} 임베딩 생성 성공 (차원: {len(vector)})")
                            except Exception as e:
                                logger.warning(f"문서 {i+1} 임베딩 생성 실패: {e}, 자동 벡터화로 대체")
                                vector = None
                        else:
                            # 스키마 기반 자동 벡터화 (기존 방식)
                            vector = None
                        
                        # 문서 삽입
                        uuid = batch.add_object(properties=normalized_doc, vector=vector)
                        if uuid:
                            inserted_ids.append(str(uuid))
                            
                    except Exception as e:
                        logger.error(f"문서 {i+1} 삽입 실패: {e}")
                        continue
            
            logger.info(f"✅ {len(inserted_ids)}개 문서 삽입 완료: {class_name}")
            if vectorize_fields:
                logger.info(f"📊 벡터화 필드: {vectorize_fields}")
            
            return inserted_ids
            
        except Exception as e:
            logger.error(f"❌ 문서 삽입 실패: {e}")
            return []
    
    def _create_vectorize_text(self, doc: Dict[str, Any], vectorize_fields: List[str]) -> str:
        """지정된 필드들로부터 벡터화용 텍스트 생성"""
        texts = []
        
        for field in vectorize_fields:
            if field in doc:
                value = doc[field]
                if isinstance(value, str):
                    texts.append(value)
                elif isinstance(value, (list, tuple)):
                    texts.extend([str(item) for item in value])
                else:
                    texts.append(str(value))
        
        combined_text = " ".join(texts).strip()
        return combined_text if combined_text else "빈 문서"
    
    def _normalize_document_dates(self, doc: Dict[str, Any]) -> Dict[str, Any]:
        """문서의 날짜 필드를 RFC3339 형식으로 정규화"""
        normalized_doc = doc.copy()
        
        # 날짜 필드로 추정되는 필드명 패턴
        date_field_patterns = [
            'date', 'time', 'created', 'updated', 'published', 'modified',
            'sent', 'received', 'sort_date', 'publish_date', 'create_date'
        ]
        
        for field_name, value in normalized_doc.items():
            # 필드명이 날짜 관련 패턴을 포함하는지 확인
            is_date_field = any(pattern in field_name.lower() for pattern in date_field_patterns)
            
            if is_date_field and isinstance(value, str) and value.strip():
                try:
                    normalized_doc[field_name] = normalize_date_to_rfc3339(value)
                    logger.debug(f"날짜 필드 '{field_name}' 정규화: {value} -> {normalized_doc[field_name]}")
                except Exception as e:
                    logger.warning(f"날짜 필드 '{field_name}' 정규화 실패: {e}")
                    # 정규화 실패 시 기본값 사용
                    normalized_doc[field_name] = "1970-01-01T00:00:00Z"
        
        return normalized_doc

    async def search(self, query: str, class_name: str = None, limit: int = 5, 
                    filters: Optional[Dict[str, Any]] = None, hybrid: bool = False) -> List[Dict[str, Any]]:
        """검색 (스키마 기반 지능적 필터링 지원)"""
        if not class_name:
            class_name = self.config.default_class
        
        try:
            collection = self.client.collections.get(class_name)
            
            # 필터 처리 - 스키마 정보를 활용한 지능적 필터링
            filter_obj = None
            if filters:
                filter_obj = await self._build_smart_filter(filters, class_name)
            
            # 검색 실행 (test_openai_vectorizer.py 방식)
            if hybrid:
                # 하이브리드 검색
                response = collection.query.hybrid(
                    query=query,
                    filters=filter_obj,
                    limit=limit,
                    return_metadata=MetadataQuery(distance=True, score=True)
                )
            else:
                # 벡터 검색
                response = collection.query.near_text(
                    query=query,
                    filters=filter_obj,
                    limit=limit,
                    return_metadata=MetadataQuery(distance=True)
                )
            
            # 결과 변환 (test_openai_vectorizer.py 방식)
            results = []
            for obj in response.objects:
                result = {
                    "id": str(obj.uuid),
                    "properties": obj.properties,
                    "distance": getattr(obj.metadata, 'distance', 0.0),
                    "score": getattr(obj.metadata, 'score', 0.0)
                }
                results.append(result)
            
            logger.info(f"🔍 검색 완료: {len(results)}개 결과 (쿼리: '{query}'")
            if filter_obj:
                logger.info(f"📊 필터 적용됨: {filters}")
            return results
            
        except Exception as e:
            logger.error(f"❌ 검색 실패: {e}")
            return []
    
    async def _build_smart_filter(self, filters: Dict[str, Any], class_name: str) -> Optional[object]:
        """스키마 정보를 활용한 지능적 필터 구성"""
        try:
            # 스키마 정보 조회
            schema_data = await self.get_schema()
            class_schema = None
            
            # 해당 클래스의 스키마 찾기
            for class_info in schema_data.get('classes', []):
                if class_info['class'] == class_name:
                    class_schema = class_info
                    break
            
            if not class_schema:
                logger.warning(f"클래스 '{class_name}' 스키마를 찾을 수 없음")
                return self._build_basic_filter(filters)
            
            # 스키마 기반 필터 구성
            filter_conditions = []
            
            for field_name, filter_value in filters.items():
                # 스키마에서 해당 필드 정보 찾기
                field_info = self._find_field_in_schema(field_name, class_schema)
                
                if field_info:
                    field_filter = self._create_field_filter(field_name, filter_value, field_info)
                    if field_filter:
                        filter_conditions.append(field_filter)
                else:
                    logger.warning(f"필드 '{field_name}'이 스키마에 없음, 기본 필터 적용")
                    # 스키마에 없는 필드도 기본 방식으로 처리
                    basic_filter = self._create_basic_field_filter(field_name, filter_value)
                    if basic_filter:
                        filter_conditions.append(basic_filter)
            
            # 여러 조건을 AND로 결합
            if len(filter_conditions) == 1:
                return filter_conditions[0]
            elif len(filter_conditions) > 1:
                combined_filter = filter_conditions[0]
                for condition in filter_conditions[1:]:
                    combined_filter = combined_filter & condition
                return combined_filter
            
            return None
            
        except Exception as e:
            logger.error(f"스키마 기반 필터 구성 실패: {e}")
            return self._build_basic_filter(filters)
    
    def _find_field_in_schema(self, field_name: str, class_schema: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """스키마에서 필드 정보 찾기"""
        for prop in class_schema.get('properties', []):
            if prop['name'] == field_name:
                return prop
        return None
    
    def _create_field_filter(self, field_name: str, filter_value: Any, field_info: Dict[str, Any]) -> Optional[object]:
        """필드 타입에 맞는 필터 생성"""
        try:
            data_type = field_info.get('dataType', ['text'])[0].lower()
            
            if isinstance(filter_value, dict):
                # 연산자 기반 필터 (gt, lt, eq, gte, lte, between)
                if "between" in filter_value:
                    return self._create_between_filter(field_name, filter_value["between"], data_type)
                elif "after" in filter_value or "gt" in filter_value:
                    value = filter_value.get("after", filter_value.get("gt"))
                    return self._create_comparison_filter(field_name, value, "gt", data_type)
                elif "before" in filter_value or "lt" in filter_value:
                    value = filter_value.get("before", filter_value.get("lt"))
                    return self._create_comparison_filter(field_name, value, "lt", data_type)
                elif "gte" in filter_value:
                    return self._create_comparison_filter(field_name, filter_value["gte"], "gte", data_type)
                elif "lte" in filter_value:
                    return self._create_comparison_filter(field_name, filter_value["lte"], "lte", data_type)
                elif "eq" in filter_value:
                    return self._create_comparison_filter(field_name, filter_value["eq"], "eq", data_type)
                elif "contains" in filter_value:
                    return Filter.by_property(field_name).contains_any([filter_value["contains"]])
            else:
                # 직접 값 비교
                return self._create_comparison_filter(field_name, filter_value, "eq", data_type)
            
            return None
            
        except Exception as e:
            logger.error(f"필드 '{field_name}' 필터 생성 실패: {e}")
            return None
    
    def _create_comparison_filter(self, field_name: str, value: Any, operator: str, data_type: str) -> Optional[object]:
        """비교 연산자 필터 생성"""
        try:
            # 날짜 타입 처리
            if data_type == "date" or self._is_date_field(field_name):
                if isinstance(value, str):
                    value = normalize_date_to_rfc3339(value)
            
            # 연산자별 필터 생성
            if operator == "gt" or operator == "after":
                return Filter.by_property(field_name).greater_than(value)
            elif operator == "gte":
                return Filter.by_property(field_name).greater_or_equal(value)
            elif operator == "lt" or operator == "before":
                return Filter.by_property(field_name).less_than(value)
            elif operator == "lte":
                return Filter.by_property(field_name).less_or_equal(value)
            elif operator == "eq":
                return Filter.by_property(field_name).equal(value)
            
            return None
            
        except Exception as e:
            logger.error(f"비교 필터 생성 실패 ({field_name} {operator} {value}): {e}")
            return None
    
    def _create_between_filter(self, field_name: str, between_value: Any, data_type: str) -> Optional[object]:
        """범위 필터 생성 (between)"""
        try:
            if isinstance(between_value, str):
                # "2024-01-01,2024-12-31" 형태 파싱
                parts = between_value.split(',')
                if len(parts) != 2:
                    logger.error(f"between 값 형식 오류: {between_value}")
                    return None
                start_value, end_value = parts[0].strip(), parts[1].strip()
            elif isinstance(between_value, list) and len(between_value) == 2:
                start_value, end_value = between_value
            else:
                logger.error(f"between 값 타입 오류: {between_value}")
                return None
            
            # 날짜 타입 처리
            if data_type == "date" or self._is_date_field(field_name):
                start_value = normalize_date_to_rfc3339(str(start_value))
                end_value = normalize_date_to_rfc3339(str(end_value))
            
            # 범위 필터: start_value <= field <= end_value
            return (Filter.by_property(field_name).greater_or_equal(start_value) & 
                   Filter.by_property(field_name).less_or_equal(end_value))
            
        except Exception as e:
            logger.error(f"범위 필터 생성 실패: {e}")
            return None
    
    def _is_date_field(self, field_name: str) -> bool:
        """필드명이 날짜 관련인지 확인"""
        date_patterns = [
            'date', 'time', 'created', 'updated', 'published', 'modified',
            'sent', 'received', 'sort_date', 'publish_date', 'create_date'
        ]
        return any(pattern in field_name.lower() for pattern in date_patterns)
    
    def _create_basic_field_filter(self, field_name: str, filter_value: Any) -> Optional[object]:
        """기본 필드 필터 생성 (스키마 정보 없을 때)"""
        try:
            if isinstance(filter_value, dict):
                if "gt" in filter_value:
                    return Filter.by_property(field_name).greater_than(filter_value["gt"])
                elif "lt" in filter_value:
                    return Filter.by_property(field_name).less_than(filter_value["lt"])
                elif "eq" in filter_value:
                    return Filter.by_property(field_name).equal(filter_value["eq"])
            else:
                return Filter.by_property(field_name).equal(filter_value)
            return None
        except Exception as e:
            logger.error(f"기본 필터 생성 실패: {e}")
            return None
    
    def _build_basic_filter(self, filters: Dict[str, Any]) -> Optional[object]:
        """기본 필터 구성 (기존 방식)"""
        filter_obj = None
        for field, value in filters.items():
            current_filter = self._create_basic_field_filter(field, value)
            if current_filter:
                if filter_obj is None:
                    filter_obj = current_filter
                else:
                    filter_obj = filter_obj & current_filter
        return filter_obj

    async def get_document_by_id(self, doc_id: str, class_name: str = None) -> Optional[Dict[str, Any]]:
        """ID로 문서 조회 (test_openai_vectorizer.py 방식)"""
        if not class_name:
            class_name = self.config.default_class
        
        try:
            collection = self.client.collections.get(class_name)
            
            # UUID로 문서 조회 (test_openai_vectorizer.py 방식)
            retrieved_obj = collection.query.fetch_object_by_id(doc_id)
            
            if retrieved_obj:
                document = {
                    "id": str(retrieved_obj.uuid),
                    "properties": retrieved_obj.properties,
                    "class_name": class_name
                }
                logger.info(f"📄 문서 조회 성공: {doc_id}")
                return document
            else:
                logger.warning(f"⚠️ 문서 조회 실패: {doc_id} (존재하지 않음)")
                return None
            
        except Exception as e:
            logger.error(f"❌ 문서 조회 실패: {e}")
            return None

    def close(self):
        """연결 종료 (test_openai_vectorizer.py 방식)"""
        try:
            if self.client:
                self.client.close()
                logger.info("✅ Weaviate 클라이언트 연결 종료")
        except Exception as e:
            logger.warning(f"⚠️ 클라이언트 종료 중 오류: {e}") 