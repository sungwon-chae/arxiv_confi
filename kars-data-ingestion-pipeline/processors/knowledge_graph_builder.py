"""
지식 그래프 구축 모듈
문서들 사이의 관계와 엔티티를 추출하여 지식 그래프를 구축
"""

import logging
import json
import re
from typing import Dict, Any, List, Optional, Tuple, Set, Union
from pathlib import Path
from datetime import datetime
from dataclasses import dataclass, asdict
from collections import defaultdict, Counter
from enum import Enum

# 엔티티 추출 및 관계 분석
try:
    import spacy
    from spacy import displacy
    SPACY_AVAILABLE = True
    
    # 한국어 모델 로드 시도
    try:
        nlp_ko = spacy.load("ko_core_news_sm")
    except OSError:
        try:
            nlp_ko = spacy.load("ko_core_news_md")
        except OSError:
            nlp_ko = None
            logging.warning("한국어 spaCy 모델을 찾을 수 없습니다. pip install ko_core_news_sm 실행하세요.")
    
    # 영어 모델 로드 시도
    try:
        nlp_en = spacy.load("en_core_web_sm")
    except OSError:
        try:
            nlp_en = spacy.load("en_core_web_md")
        except OSError:
            nlp_en = None
            logging.warning("영어 spaCy 모델을 찾을 수 없습니다. pip install en_core_web_sm 실행하세요.")
            
except ImportError:
    SPACY_AVAILABLE = False
    nlp_ko = None
    nlp_en = None
    logging.warning("spaCy not available, using fallback entity extraction")

# 그래프 분석
try:
    import networkx as nx
    NETWORKX_AVAILABLE = True
except ImportError:
    NETWORKX_AVAILABLE = False
    logging.warning("NetworkX not available, graph analysis disabled")

logger = logging.getLogger(__name__)

class EntityType(Enum):
    """엔티티 타입"""
    PERSON = "PERSON"
    ORGANIZATION = "ORG"
    LOCATION = "GPE"
    DATE = "DATE"
    MONEY = "MONEY"
    PERCENT = "PERCENT"
    PRODUCT = "PRODUCT"
    EVENT = "EVENT"
    LAW = "LAW"
    LANGUAGE = "LANGUAGE"
    UNKNOWN = "UNKNOWN"

class RelationType(Enum):
    """관계 타입"""
    WORKS_AT = "WORKS_AT"
    LOCATED_IN = "LOCATED_IN"
    PART_OF = "PART_OF"
    MENTIONS = "MENTIONS"
    RELATED_TO = "RELATED_TO"
    OCCURS_ON = "OCCURS_ON"
    INVOLVES = "INVOLVES"
    SIMILAR_TO = "SIMILAR_TO"
    UNKNOWN = "UNKNOWN"

@dataclass
class Entity:
    """지식 그래프 엔티티"""
    id: str
    name: str
    entity_type: EntityType
    confidence: float
    metadata: Dict[str, Any]
    mentions: List[Dict[str, Any]]  # 언급된 위치와 컨텍스트
    
@dataclass
class Relationship:
    """엔티티 간 관계"""
    id: str
    source_entity_id: str
    target_entity_id: str
    relation_type: RelationType
    confidence: float
    evidence: List[str]  # 관계를 뒷받침하는 텍스트
    metadata: Dict[str, Any]

@dataclass
class KnowledgeGraph:
    """지식 그래프"""
    entities: Dict[str, Entity]
    relationships: Dict[str, Relationship]
    document_sources: List[str]
    created_at: str
    metadata: Dict[str, Any]

class KnowledgeGraphBuilder:
    """지식 그래프 구축기"""
    
    def __init__(self,
                 language: str = "auto",
                 similarity_threshold: float = 0.8,
                 min_entity_confidence: float = 0.5):
        self.language = language
        self.similarity_threshold = similarity_threshold
        self.min_entity_confidence = min_entity_confidence
        
        # spaCy 모델 설정
        self.nlp_models = {}
        if SPACY_AVAILABLE:
            if nlp_ko:
                self.nlp_models['ko'] = nlp_ko
            if nlp_en:
                self.nlp_models['en'] = nlp_en
        
        # 한국어 특화 패턴들
        self.korean_patterns = {
            'person': [
                r'([가-힣]{2,4})\s*(대표|사장|이사|부장|과장|팀장|교수|박사|연구원)',
                r'([가-힣]{2,4})\s*(씨|님|선생님)',
                r'([가-힣]{2,4})\s*(의원|판사|검사|변호사)'
            ],
            'organization': [
                r'([가-힣\w\s]+)\s*(주식회사|유한회사|재단법인|사단법인|협회|위원회)',
                r'([가-힣\w\s]+)\s*(대학교|대학|고등학교|중학교|초등학교)',
                r'([가-힣\w\s]+)\s*(부|청|원|처|실|과|팀)'
            ],
            'location': [
                r'([가-힣]+시|[가-힣]+구|[가-힣]+동|[가-힣]+읍|[가-힣]+면)',
                r'([가-힣]+도|[가-힣]+시|[가-힣]+군)'
            ]
        }
        
        # 관계 추출 패턴들
        self.relation_patterns = {
            RelationType.WORKS_AT: [
                r'(.+?)(?:는|이|께서)\s*(.+?)(?:에서|에|의)\s*(?:근무|일|직장)',
                r'(.+?)\s*(.+?)\s*(?:사원|직원|임원|대표)'
            ],
            RelationType.LOCATED_IN: [
                r'(.+?)(?:는|이)\s*(.+?)(?:에|에서)\s*(?:위치|소재|있)',
                r'(.+?)\s*(.+?)\s*(?:지역|지방|소재지)'
            ],
            RelationType.PART_OF: [
                r'(.+?)(?:는|이)\s*(.+?)(?:의|에)\s*(?:소속|부분|일부)',
                r'(.+?)\s*(.+?)\s*(?:산하|하위|소속)'
            ]
        }
        
    def extract_entities(self, text: str, source_info: Dict[str, Any]) -> List[Entity]:
        """
        텍스트에서 엔티티 추출
        
        Args:
            text: 분석할 텍스트
            source_info: 소스 문서 정보
            
        Returns:
            추출된 엔티티 리스트
        """
        entities = []
        
        if not text:
            return entities
        
        # 언어 감지
        detected_lang = self._detect_language(text)
        
        # spaCy 기반 엔티티 추출
        if SPACY_AVAILABLE and detected_lang in self.nlp_models:
            spacy_entities = self._extract_entities_spacy(text, detected_lang, source_info)
            entities.extend(spacy_entities)
        
        # 패턴 기반 엔티티 추출 (한국어)
        if detected_lang == 'ko':
            pattern_entities = self._extract_entities_patterns(text, source_info)
            entities.extend(pattern_entities)
        
        # 엔티티 중복 제거 및 병합
        entities = self._merge_similar_entities(entities)
        
        # 신뢰도 필터링
        entities = [e for e in entities if e.confidence >= self.min_entity_confidence]
        
        return entities
    
    def _detect_language(self, text: str) -> str:
        """언어 감지"""
        if self.language != "auto":
            return self.language
        
        # 간단한 언어 감지 (한글 비율 기반)
        korean_chars = len(re.findall(r'[가-힣]', text))
        total_chars = len(re.findall(r'[가-힣a-zA-Z]', text))
        
        if total_chars == 0:
            return 'en'
        
        korean_ratio = korean_chars / total_chars
        return 'ko' if korean_ratio > 0.3 else 'en'
    
    def _extract_entities_spacy(self, text: str, language: str, source_info: Dict[str, Any]) -> List[Entity]:
        """spaCy를 사용한 엔티티 추출"""
        entities = []
        
        if language not in self.nlp_models:
            return entities
        
        nlp = self.nlp_models[language]
        doc = nlp(text)
        
        for ent in doc.ents:
            # spaCy 엔티티 타입을 내부 타입으로 매핑
            entity_type = self._map_spacy_entity_type(ent.label_)
            
            # 엔티티 ID 생성
            entity_id = self._generate_entity_id(ent.text, entity_type)
            
            # 언급 정보
            mention = {
                "text": ent.text,
                "start": ent.start_char,
                "end": ent.end_char,
                "context": text[max(0, ent.start_char-50):ent.end_char+50],
                "source_file": source_info.get("file_path", "unknown"),
                "confidence": 0.8  # spaCy 기본 신뢰도
            }
            
            entity = Entity(
                id=entity_id,
                name=ent.text.strip(),
                entity_type=entity_type,
                confidence=0.8,
                metadata={
                    "spacy_label": ent.label_,
                    "language": language,
                    "extraction_method": "spacy"
                },
                mentions=[mention]
            )
            
            entities.append(entity)
        
        return entities
    
    def _extract_entities_patterns(self, text: str, source_info: Dict[str, Any]) -> List[Entity]:
        """패턴 기반 엔티티 추출 (한국어 특화)"""
        entities = []
        
        for entity_type, patterns in self.korean_patterns.items():
            for pattern in patterns:
                matches = re.finditer(pattern, text)
                
                for match in matches:
                    entity_text = match.group(1).strip()
                    
                    if len(entity_text) < 2:  # 너무 짧은 엔티티 제외
                        continue
                    
                    # 엔티티 타입 매핑
                    if entity_type == 'person':
                        ent_type = EntityType.PERSON
                    elif entity_type == 'organization':
                        ent_type = EntityType.ORGANIZATION
                    elif entity_type == 'location':
                        ent_type = EntityType.LOCATION
                    else:
                        ent_type = EntityType.UNKNOWN
                    
                    entity_id = self._generate_entity_id(entity_text, ent_type)
                    
                    mention = {
                        "text": match.group(0),
                        "entity_text": entity_text,
                        "start": match.start(),
                        "end": match.end(),
                        "context": text[max(0, match.start()-50):match.end()+50],
                        "source_file": source_info.get("file_path", "unknown"),
                        "confidence": 0.7
                    }
                    
                    entity = Entity(
                        id=entity_id,
                        name=entity_text,
                        entity_type=ent_type,
                        confidence=0.7,
                        metadata={
                            "pattern": pattern,
                            "language": "ko",
                            "extraction_method": "pattern"
                        },
                        mentions=[mention]
                    )
                    
                    entities.append(entity)
        
        return entities
    
    def _map_spacy_entity_type(self, spacy_label: str) -> EntityType:
        """spaCy 엔티티 레이블을 내부 타입으로 매핑"""
        mapping = {
            'PERSON': EntityType.PERSON,
            'PER': EntityType.PERSON,
            'ORG': EntityType.ORGANIZATION,
            'GPE': EntityType.LOCATION,
            'LOC': EntityType.LOCATION,
            'DATE': EntityType.DATE,
            'TIME': EntityType.DATE,
            'MONEY': EntityType.MONEY,
            'PERCENT': EntityType.PERCENT,
            'PRODUCT': EntityType.PRODUCT,
            'EVENT': EntityType.EVENT,
            'LAW': EntityType.LAW,
            'LANGUAGE': EntityType.LANGUAGE
        }
        
        return mapping.get(spacy_label, EntityType.UNKNOWN)
    
    def _generate_entity_id(self, entity_text: str, entity_type: EntityType) -> str:
        """엔티티 ID 생성"""
        clean_text = re.sub(r'[^\w가-힣]', '_', entity_text.lower())
        return f"{entity_type.value}_{clean_text}_{hash(entity_text) % 10000:04d}"
    
    def _merge_similar_entities(self, entities: List[Entity]) -> List[Entity]:
        """유사한 엔티티들 병합"""
        if not entities:
            return entities
        
        merged_entities = []
        entity_groups = defaultdict(list)
        
        # 엔티티를 타입별로 그룹화
        for entity in entities:
            key = (entity.entity_type, entity.name.lower().strip())
            entity_groups[key].append(entity)
        
        for (entity_type, name), group in entity_groups.items():
            if len(group) == 1:
                merged_entities.append(group[0])
            else:
                # 여러 개의 유사한 엔티티를 하나로 병합
                merged_entity = self._merge_entity_group(group)
                merged_entities.append(merged_entity)
        
        return merged_entities
    
    def _merge_entity_group(self, entities: List[Entity]) -> Entity:
        """엔티티 그룹을 하나로 병합"""
        # 가장 긴 이름을 사용
        best_entity = max(entities, key=lambda e: len(e.name))
        
        # 모든 언급을 수집
        all_mentions = []
        for entity in entities:
            all_mentions.extend(entity.mentions)
        
        # 신뢰도는 평균값 사용
        avg_confidence = sum(e.confidence for e in entities) / len(entities)
        
        # 메타데이터 병합
        merged_metadata = {}
        for entity in entities:
            merged_metadata.update(entity.metadata)
        merged_metadata['merged_from'] = len(entities)
        
        return Entity(
            id=best_entity.id,
            name=best_entity.name,
            entity_type=best_entity.entity_type,
            confidence=avg_confidence,
            metadata=merged_metadata,
            mentions=all_mentions
        )
    
    def extract_relationships(self, text: str, entities: List[Entity], source_info: Dict[str, Any]) -> List[Relationship]:
        """
        엔티티 간 관계 추출
        
        Args:
            text: 분석할 텍스트
            entities: 추출된 엔티티들
            source_info: 소스 문서 정보
            
        Returns:
            추출된 관계 리스트
        """
        relationships = []
        
        if len(entities) < 2:
            return relationships
        
        # 패턴 기반 관계 추출
        pattern_relations = self._extract_relationships_patterns(text, entities, source_info)
        relationships.extend(pattern_relations)
        
        # 동시 출현 기반 관계 추출
        cooccurrence_relations = self._extract_relationships_cooccurrence(text, entities, source_info)
        relationships.extend(cooccurrence_relations)
        
        # 중복 관계 제거
        relationships = self._deduplicate_relationships(relationships)
        
        return relationships
    
    def _extract_relationships_patterns(self, text: str, entities: List[Entity], source_info: Dict[str, Any]) -> List[Relationship]:
        """패턴 기반 관계 추출"""
        relationships = []
        
        for relation_type, patterns in self.relation_patterns.items():
            for pattern in patterns:
                matches = re.finditer(pattern, text)
                
                for match in matches:
                    # 매치된 텍스트에서 엔티티 찾기
                    source_text = match.group(1).strip()
                    target_text = match.group(2).strip()
                    
                    source_entity = self._find_entity_by_text(source_text, entities)
                    target_entity = self._find_entity_by_text(target_text, entities)
                    
                    if source_entity and target_entity and source_entity.id != target_entity.id:
                        relation_id = f"{relation_type.value}_{source_entity.id}_{target_entity.id}"
                        
                        relationship = Relationship(
                            id=relation_id,
                            source_entity_id=source_entity.id,
                            target_entity_id=target_entity.id,
                            relation_type=relation_type,
                            confidence=0.7,
                            evidence=[match.group(0)],
                            metadata={
                                "pattern": pattern,
                                "source_file": source_info.get("file_path", "unknown"),
                                "extraction_method": "pattern"
                            }
                        )
                        
                        relationships.append(relationship)
        
        return relationships
    
    def _extract_relationships_cooccurrence(self, text: str, entities: List[Entity], source_info: Dict[str, Any]) -> List[Relationship]:
        """동시 출현 기반 관계 추출"""
        relationships = []
        
        # 문장 단위로 텍스트 분할
        sentences = re.split(r'[.!?]\s+', text)
        
        for sentence in sentences:
            if len(sentence.strip()) < 10:
                continue
            
            # 이 문장에 언급된 엔티티들 찾기
            sentence_entities = []
            for entity in entities:
                for mention in entity.mentions:
                    if mention['text'].lower() in sentence.lower():
                        sentence_entities.append(entity)
                        break
            
            # 같은 문장에 등장하는 엔티티들 간의 관계 생성
            for i, entity1 in enumerate(sentence_entities):
                for entity2 in sentence_entities[i+1:]:
                    if entity1.id != entity2.id:
                        relation_id = f"MENTIONS_{entity1.id}_{entity2.id}"
                        
                        relationship = Relationship(
                            id=relation_id,
                            source_entity_id=entity1.id,
                            target_entity_id=entity2.id,
                            relation_type=RelationType.MENTIONS,
                            confidence=0.5,
                            evidence=[sentence.strip()],
                            metadata={
                                "source_file": source_info.get("file_path", "unknown"),
                                "extraction_method": "cooccurrence"
                            }
                        )
                        
                        relationships.append(relationship)
        
        return relationships
    
    def _find_entity_by_text(self, text: str, entities: List[Entity]) -> Optional[Entity]:
        """텍스트로 엔티티 찾기"""
        text = text.strip().lower()
        
        for entity in entities:
            if entity.name.lower() == text:
                return entity
            
            # 부분 매치 확인
            for mention in entity.mentions:
                if mention.get('entity_text', mention['text']).lower() == text:
                    return entity
        
        return None
    
    def _deduplicate_relationships(self, relationships: List[Relationship]) -> List[Relationship]:
        """중복 관계 제거"""
        unique_relations = {}
        
        for relation in relationships:
            # 양방향 관계를 고려한 키 생성
            key1 = (relation.source_entity_id, relation.target_entity_id, relation.relation_type)
            key2 = (relation.target_entity_id, relation.source_entity_id, relation.relation_type)
            
            if key1 not in unique_relations and key2 not in unique_relations:
                unique_relations[key1] = relation
            else:
                # 기존 관계의 증거에 추가
                existing_key = key1 if key1 in unique_relations else key2
                existing_relation = unique_relations[existing_key]
                existing_relation.evidence.extend(relation.evidence)
                existing_relation.confidence = max(existing_relation.confidence, relation.confidence)
        
        return list(unique_relations.values())
    
    def build_knowledge_graph(self, processed_documents: List[Dict[str, Any]]) -> KnowledgeGraph:
        """
        처리된 문서들로부터 지식 그래프 구축 (멀티모달 지원)
        
        Args:
            processed_documents: 처리된 문서 데이터 리스트
            
        Returns:
            구축된 지식 그래프
        """
        all_entities = []
        all_relationships = []
        document_sources = []
        
        logger.info(f"지식 그래프 구축 시작: {len(processed_documents)}개 문서")
        
        for doc in processed_documents:
            if not doc.get('success', False):
                continue
            
            document_sources.append(doc.get('file_path', 'unknown'))
            
            source_info = {
                "file_path": doc.get('file_path', 'unknown'),
                "processing_timestamp": doc.get('timestamp')
            }
            
            # 멀티모달 요소별 엔티티 추출
            doc_entities = []
            
            # 구조화된 JSON 형식의 경우 (멀티모달)
            if 'elements' in doc:
                for element in doc['elements']:
                    element_entities = self._extract_entities_from_element(element, source_info)
                    doc_entities.extend(element_entities)
                
                # 요소 간 관계도 활용
                element_relationships = self._extract_cross_modal_relationships(doc['elements'], doc_entities, source_info)
                all_relationships.extend(element_relationships)
            
            # 텍스트 전체 처리 (fallback)
            else:
                full_text = ""
                
                # 청크 형식의 경우
                if 'chunks' in doc:
                    for chunk in doc['chunks']:
                        full_text += chunk.get('content', '') + "\n\n"
                
                # 마크다운 형식의 경우
                elif 'markdown_content' in doc:
                    full_text = doc['markdown_content']
                
                if full_text.strip():
                    # 엔티티 추출
                    entities = self.extract_entities(full_text, source_info)
                    doc_entities.extend(entities)
            
            all_entities.extend(doc_entities)
            
            # 문서 내 관계 추출
            if doc_entities:
                # 텍스트 수집 (관계 추출용)
                combined_text = self._collect_text_from_document(doc)
                if combined_text:
                    relationships = self.extract_relationships(combined_text, doc_entities, source_info)
                    all_relationships.extend(relationships)
        
        # 글로벌 엔티티 병합
        merged_entities = self._merge_global_entities(all_entities)
        
        # 관계 정리 (병합된 엔티티 ID로 업데이트)
        updated_relationships = self._update_relationships_with_merged_entities(
            all_relationships, merged_entities
        )
        
        # 지식 그래프 생성
        entities_dict = {entity.id: entity for entity in merged_entities}
        relationships_dict = {rel.id: rel for rel in updated_relationships}
        
        knowledge_graph = KnowledgeGraph(
            entities=entities_dict,
            relationships=relationships_dict,
            document_sources=document_sources,
            created_at=datetime.now().isoformat(),
            metadata={
                "total_entities": len(entities_dict),
                "total_relationships": len(relationships_dict),
                "total_documents": len(document_sources),
                "builder_version": "1.0"
            }
        )
        
        logger.info(f"지식 그래프 구축 완료: {len(entities_dict)}개 엔티티, {len(relationships_dict)}개 관계")
        
        return knowledge_graph
    
    def _merge_global_entities(self, entities: List[Entity]) -> List[Entity]:
        """전역 엔티티 병합 (문서 간 중복 엔티티 처리)"""
        entity_groups = defaultdict(list)
        
        # 엔티티를 이름과 타입으로 그룹화
        for entity in entities:
            # 정규화된 이름 생성
            normalized_name = self._normalize_entity_name(entity.name)
            key = (entity.entity_type, normalized_name)
            entity_groups[key].append(entity)
        
        merged_entities = []
        
        for (entity_type, normalized_name), group in entity_groups.items():
            if len(group) == 1:
                merged_entities.append(group[0])
            else:
                # 유사도 기반 클러스터링
                clusters = self._cluster_similar_entities(group)
                for cluster in clusters:
                    merged_entity = self._merge_entity_group(cluster)
                    merged_entities.append(merged_entity)
        
        return merged_entities
    
    def _normalize_entity_name(self, name: str) -> str:
        """엔티티 이름 정규화"""
        # 공백, 특수문자 정리
        normalized = re.sub(r'\s+', ' ', name.strip())
        normalized = re.sub(r'[^\w가-힣\s]', '', normalized)
        return normalized.lower()
    
    def _cluster_similar_entities(self, entities: List[Entity]) -> List[List[Entity]]:
        """유사한 엔티티들을 클러스터링"""
        if len(entities) <= 1:
            return [entities]
        
        clusters = []
        processed = set()
        
        for i, entity1 in enumerate(entities):
            if i in processed:
                continue
            
            cluster = [entity1]
            processed.add(i)
            
            for j, entity2 in enumerate(entities):
                if j in processed or i == j:
                    continue
                
                # 문자열 유사도 계산
                similarity = self._calculate_string_similarity(entity1.name, entity2.name)
                
                if similarity >= self.similarity_threshold:
                    cluster.append(entity2)
                    processed.add(j)
            
            clusters.append(cluster)
        
        return clusters
    
    def _calculate_string_similarity(self, str1: str, str2: str) -> float:
        """두 문자열 간의 유사도 계산 (Jaccard similarity)"""
        str1 = str1.lower().strip()
        str2 = str2.lower().strip()
        
        if str1 == str2:
            return 1.0
        
        # 문자 단위 집합으로 변환
        set1 = set(str1)
        set2 = set(str2)
        
        intersection = len(set1.intersection(set2))
        union = len(set1.union(set2))
        
        return intersection / union if union > 0 else 0.0
    
    def _update_relationships_with_merged_entities(self, relationships: List[Relationship], entities: List[Entity]) -> List[Relationship]:
        """병합된 엔티티 ID로 관계 업데이트"""
        # 엔티티 이름 -> ID 매핑 생성
        name_to_id = {}
        for entity in entities:
            name_to_id[entity.name.lower().strip()] = entity.id
            
            # 모든 언급된 텍스트도 매핑에 추가
            for mention in entity.mentions:
                name_to_id[mention['text'].lower().strip()] = entity.id
                if 'entity_text' in mention:
                    name_to_id[mention['entity_text'].lower().strip()] = entity.id
        
        updated_relationships = []
        
        for rel in relationships:
            # 새로운 관계 ID 생성
            new_rel_id = f"{rel.relation_type.value}_{rel.source_entity_id}_{rel.target_entity_id}"
            
            # 중복 관계 확인
            duplicate_found = False
            for existing_rel in updated_relationships:
                if (existing_rel.source_entity_id == rel.source_entity_id and 
                    existing_rel.target_entity_id == rel.target_entity_id and
                    existing_rel.relation_type == rel.relation_type):
                    # 증거 추가
                    existing_rel.evidence.extend(rel.evidence)
                    existing_rel.confidence = max(existing_rel.confidence, rel.confidence)
                    duplicate_found = True
                    break
            
            if not duplicate_found:
                rel.id = new_rel_id
                updated_relationships.append(rel)
        
        return updated_relationships
    
    def _extract_entities_from_element(self, element: Dict[str, Any], source_info: Dict[str, Any]) -> List[Entity]:
        """멀티모달 요소에서 엔티티 추출"""
        entities = []
        
        element_type = element.get('type', 'unknown')
        content = element.get('content', '')
        metadata = element.get('metadata', {})
        
        if element_type == 'text':
            # 텍스트 엔티티 추출
            text_entities = self.extract_entities(content, source_info)
            # 요소 타입 정보 추가
            for entity in text_entities:
                entity.metadata['source_element_type'] = 'text'
                entity.metadata['text_type'] = metadata.get('text_type', 'paragraph')
            entities.extend(text_entities)
            
        elif element_type == 'table':
            # 테이블에서 엔티티 추출
            table_entities = self._extract_entities_from_table(element, source_info)
            entities.extend(table_entities)
            
        elif element_type == 'image':
            # 이미지 OCR 텍스트에서 엔티티 추출
            ocr_text = metadata.get('ocr_text', '')
            if ocr_text:
                ocr_entities = self.extract_entities(ocr_text, source_info)
                for entity in ocr_entities:
                    entity.metadata['source_element_type'] = 'image'
                    entity.metadata['extracted_via'] = 'ocr'
                    entity.confidence *= 0.8  # OCR 결과는 신뢰도 조정
                entities.extend(ocr_entities)
                
        elif element_type == 'equation':
            # 수식에서 변수명이나 함수명 추출
            equation_entities = self._extract_entities_from_equation(element, source_info)
            entities.extend(equation_entities)
        
        # 페이지 정보 추가
        page_number = element.get('page_number')
        if page_number:
            for entity in entities:
                entity.metadata['page_number'] = page_number
        
        return entities
    
    def _extract_entities_from_table(self, table_element: Dict[str, Any], source_info: Dict[str, Any]) -> List[Entity]:
        """테이블에서 엔티티 추출"""
        entities = []
        
        content = table_element.get('content', {})
        if not isinstance(content, dict):
            return entities
        
        rows = content.get('rows', [])
        headers = content.get('headers', [])
        
        # 헤더를 기준으로 컬럼 타입 추측
        column_types = self._infer_column_types(headers, rows)
        
        # 각 행에서 엔티티 추출
        for row_idx, row in enumerate(rows):
            for col_idx, cell in enumerate(row):
                if not cell or not str(cell).strip():
                    continue
                
                cell_text = str(cell).strip()
                col_type = column_types.get(col_idx, 'unknown')
                
                # 컬럼 타입에 따른 엔티티 타입 결정
                if col_type == 'person':
                    entity_type = EntityType.PERSON
                elif col_type == 'organization':
                    entity_type = EntityType.ORGANIZATION
                elif col_type == 'location':
                    entity_type = EntityType.LOCATION
                elif col_type == 'date':
                    entity_type = EntityType.DATE
                elif col_type == 'money':
                    entity_type = EntityType.MONEY
                else:
                    # 패턴 매칭으로 타입 추측
                    entity_type = self._guess_entity_type(cell_text)
                
                if entity_type != EntityType.UNKNOWN:
                    entity_id = self._generate_entity_id(cell_text, entity_type)
                    
                    entity = Entity(
                        id=entity_id,
                        name=cell_text,
                        entity_type=entity_type,
                        confidence=0.7,  # 테이블 데이터는 기본 신뢰도 0.7
                        metadata={
                            "source_element_type": "table",
                            "row_index": row_idx,
                            "column_index": col_idx,
                            "column_header": headers[col_idx] if col_idx < len(headers) else None,
                            "extraction_method": "table_parsing"
                        },
                        mentions=[{
                            "text": cell_text,
                            "source_file": source_info.get("file_path", "unknown"),
                            "element_type": "table_cell",
                            "confidence": 0.7
                        }]
                    )
                    entities.append(entity)
        
        return entities
    
    def _infer_column_types(self, headers: List[str], rows: List[List[Any]]) -> Dict[int, str]:
        """테이블 컬럼의 엔티티 타입 추측"""
        column_types = {}
        
        # 헤더 기반 추측
        for idx, header in enumerate(headers):
            header_lower = header.lower()
            if any(term in header_lower for term in ['name', '이름', '성명', '담당자']):
                column_types[idx] = 'person'
            elif any(term in header_lower for term in ['company', '회사', '기관', '조직', '부서']):
                column_types[idx] = 'organization'
            elif any(term in header_lower for term in ['location', '위치', '주소', '지역']):
                column_types[idx] = 'location'
            elif any(term in header_lower for term in ['date', '날짜', '일시', '기간']):
                column_types[idx] = 'date'
            elif any(term in header_lower for term in ['amount', '금액', '가격', 'price']):
                column_types[idx] = 'money'
        
        # 데이터 샘플링을 통한 추측 (헤더가 없거나 불명확한 경우)
        sample_size = min(5, len(rows))
        for col_idx in range(len(rows[0]) if rows else 0):
            if col_idx in column_types:
                continue
            
            # 샘플 데이터 분석
            samples = [rows[i][col_idx] for i in range(sample_size) if col_idx < len(rows[i])]
            guessed_type = self._guess_column_type_from_samples(samples)
            if guessed_type != 'unknown':
                column_types[col_idx] = guessed_type
        
        return column_types
    
    def _guess_column_type_from_samples(self, samples: List[Any]) -> str:
        """샘플 데이터로부터 컬럼 타입 추측"""
        type_votes = defaultdict(int)
        
        for sample in samples:
            if not sample:
                continue
            
            sample_str = str(sample).strip()
            entity_type = self._guess_entity_type(sample_str)
            
            if entity_type == EntityType.PERSON:
                type_votes['person'] += 1
            elif entity_type == EntityType.ORGANIZATION:
                type_votes['organization'] += 1
            elif entity_type == EntityType.LOCATION:
                type_votes['location'] += 1
            elif entity_type == EntityType.DATE:
                type_votes['date'] += 1
            elif entity_type == EntityType.MONEY:
                type_votes['money'] += 1
        
        if type_votes:
            return max(type_votes.items(), key=lambda x: x[1])[0]
        return 'unknown'
    
    def _guess_entity_type(self, text: str) -> EntityType:
        """텍스트로부터 엔티티 타입 추측"""
        # 날짜 패턴
        if re.search(r'\d{4}[-/]\d{1,2}[-/]\d{1,2}|\d{1,2}[-/]\d{1,2}[-/]\d{4}', text):
            return EntityType.DATE
        
        # 금액 패턴
        if re.search(r'[\$￦₩]\s*[\d,]+|[\d,]+\s*(?:원|달러|엔|위안)', text):
            return EntityType.MONEY
        
        # 퍼센트 패턴
        if re.search(r'\d+\.?\d*\s*%', text):
            return EntityType.PERCENT
        
        # 이메일 패턴 (조직/개인)
        if '@' in text:
            domain = text.split('@')[1].lower()
            if any(corp in domain for corp in ['company', 'corp', 'org', 'gov']):
                return EntityType.ORGANIZATION
            else:
                return EntityType.PERSON
        
        # 한국어 이름 패턴
        if re.match(r'^[가-힣]{2,4}$', text):
            return EntityType.PERSON
        
        # 영어 이름 패턴
        if re.match(r'^[A-Z][a-z]+\s+[A-Z][a-z]+$', text):
            return EntityType.PERSON
        
        return EntityType.UNKNOWN
    
    def _extract_entities_from_equation(self, equation_element: Dict[str, Any], source_info: Dict[str, Any]) -> List[Entity]:
        """수식에서 변수나 함수명 추출"""
        entities = []
        
        content = equation_element.get('content', {})
        if isinstance(content, dict):
            latex = content.get('latex', '')
            text = content.get('text', '')
        else:
            latex = str(content)
            text = str(content)
        
        # 변수명 추출 (단순 패턴)
        variables = re.findall(r'[a-zA-Z]_?\{?[a-zA-Z0-9]*\}?', latex or text)
        
        for var in set(variables):
            if len(var) > 1 or var.isupper():  # 단일 소문자는 일반 변수로 간주
                entity = Entity(
                    id=self._generate_entity_id(var, EntityType.UNKNOWN),
                    name=var,
                    entity_type=EntityType.UNKNOWN,
                    confidence=0.6,
                    metadata={
                        "source_element_type": "equation",
                        "entity_subtype": "mathematical_symbol",
                        "extraction_method": "pattern_matching"
                    },
                    mentions=[{
                        "text": var,
                        "source_file": source_info.get("file_path", "unknown"),
                        "element_type": "equation",
                        "confidence": 0.6
                    }]
                )
                entities.append(entity)
        
        return entities
    
    def _extract_cross_modal_relationships(self, elements: List[Dict[str, Any]], 
                                         entities: List[Entity], 
                                         source_info: Dict[str, Any]) -> List[Relationship]:
        """멀티모달 요소 간 관계 추출"""
        relationships = []
        
        # 요소별 엔티티 매핑
        element_entity_map = defaultdict(list)
        for entity in entities:
            source_type = entity.metadata.get('source_element_type')
            if source_type:
                element_entity_map[source_type].append(entity)
        
        # 이미지-텍스트 관계
        if 'image' in element_entity_map and 'text' in element_entity_map:
            for img_entity in element_entity_map['image']:
                for text_entity in element_entity_map['text']:
                    # 같은 페이지에 있고 이름이 유사한 경우
                    if (img_entity.metadata.get('page_number') == text_entity.metadata.get('page_number') and
                        self._calculate_string_similarity(img_entity.name, text_entity.name) > 0.7):
                        
                        relationship = Relationship(
                            id=f"CROSS_MODAL_{img_entity.id}_{text_entity.id}",
                            source_entity_id=img_entity.id,
                            target_entity_id=text_entity.id,
                            relation_type=RelationType.SIMILAR_TO,
                            confidence=0.8,
                            evidence=[f"이미지와 텍스트에서 동일한 엔티티 '{img_entity.name}' 발견"],
                            metadata={
                                "relationship_subtype": "cross_modal_match",
                                "source_file": source_info.get("file_path", "unknown")
                            }
                        )
                        relationships.append(relationship)
        
        # 테이블-텍스트 관계
        if 'table' in element_entity_map and 'text' in element_entity_map:
            for table_entity in element_entity_map['table']:
                for text_entity in element_entity_map['text']:
                    # 텍스트가 헤딩이고 테이블 엔티티를 언급하는 경우
                    if (text_entity.metadata.get('text_type') == 'heading' and
                        table_entity.name.lower() in text_entity.name.lower()):
                        
                        relationship = Relationship(
                            id=f"TABLE_MENTIONED_{text_entity.id}_{table_entity.id}",
                            source_entity_id=text_entity.id,
                            target_entity_id=table_entity.id,
                            relation_type=RelationType.MENTIONS,
                            confidence=0.7,
                            evidence=[f"제목에서 테이블 엔티티 '{table_entity.name}' 언급"],
                            metadata={
                                "relationship_subtype": "heading_mentions_table_entity",
                                "source_file": source_info.get("file_path", "unknown")
                            }
                        )
                        relationships.append(relationship)
        
        return relationships
    
    def _collect_text_from_document(self, doc: Dict[str, Any]) -> str:
        """문서에서 모든 텍스트 수집"""
        texts = []
        
        if 'elements' in doc:
            for element in doc['elements']:
                if element.get('type') == 'text':
                    texts.append(element.get('content', ''))
                elif element.get('type') == 'table':
                    # 테이블을 텍스트로 변환
                    content = element.get('content', {})
                    if isinstance(content, dict) and 'rows' in content:
                        for row in content['rows']:
                            texts.append(' '.join(str(cell) for cell in row))
                elif element.get('type') == 'image':
                    # OCR 텍스트 추가
                    ocr_text = element.get('metadata', {}).get('ocr_text', '')
                    if ocr_text:
                        texts.append(ocr_text)
        
        elif 'chunks' in doc:
            for chunk in doc['chunks']:
                texts.append(chunk.get('content', ''))
        
        elif 'markdown_content' in doc:
            texts.append(doc['markdown_content'])
        
        return '\n\n'.join(texts)
    
    def save_knowledge_graph(self, kg: KnowledgeGraph, output_path: Union[str, Path]):
        """지식 그래프를 JSON 파일로 저장"""
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # 직렬화 가능한 형태로 변환
        serializable_kg = {
            "entities": {eid: asdict(entity) for eid, entity in kg.entities.items()},
            "relationships": {rid: asdict(rel) for rid, rel in kg.relationships.items()},
            "document_sources": kg.document_sources,
            "created_at": kg.created_at,
            "metadata": kg.metadata
        }
        
        # Enum 값들을 문자열로 변환
        for entity_data in serializable_kg["entities"].values():
            entity_data["entity_type"] = entity_data["entity_type"].value if hasattr(entity_data["entity_type"], 'value') else entity_data["entity_type"]
        
        for rel_data in serializable_kg["relationships"].values():
            rel_data["relation_type"] = rel_data["relation_type"].value if hasattr(rel_data["relation_type"], 'value') else rel_data["relation_type"]
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(serializable_kg, f, ensure_ascii=False, indent=2)
        
        logger.info(f"지식 그래프 저장 완료: {output_path}")
    
    def load_knowledge_graph(self, input_path: Union[str, Path]) -> KnowledgeGraph:
        """JSON 파일에서 지식 그래프 로드"""
        input_path = Path(input_path)
        
        if not input_path.exists():
            raise FileNotFoundError(f"지식 그래프 파일을 찾을 수 없습니다: {input_path}")
        
        with open(input_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # 엔티티 복원
        entities = {}
        for eid, entity_data in data["entities"].items():
            entity_data["entity_type"] = EntityType(entity_data["entity_type"])
            entities[eid] = Entity(**entity_data)
        
        # 관계 복원
        relationships = {}
        for rid, rel_data in data["relationships"].items():
            rel_data["relation_type"] = RelationType(rel_data["relation_type"])
            relationships[rid] = Relationship(**rel_data)
        
        return KnowledgeGraph(
            entities=entities,
            relationships=relationships,
            document_sources=data["document_sources"],
            created_at=data["created_at"],
            metadata=data["metadata"]
        )
    
    def analyze_graph_statistics(self, kg: KnowledgeGraph) -> Dict[str, Any]:
        """지식 그래프 통계 분석 (멀티모달 지원)"""
        stats = {
            "basic_stats": {
                "total_entities": len(kg.entities),
                "total_relationships": len(kg.relationships),
                "total_documents": len(kg.document_sources)
            },
            "entity_type_distribution": Counter(),
            "relationship_type_distribution": Counter(),
            "most_connected_entities": [],
            "entity_mention_stats": {},
            "multimodal_stats": {
                "entity_source_distribution": Counter(),
                "cross_modal_relationships": 0,
                "ocr_extracted_entities": 0,
                "table_extracted_entities": 0,
                "equation_extracted_entities": 0
            }
        }
        
        # 엔티티 타입 분포
        for entity in kg.entities.values():
            stats["entity_type_distribution"][entity.entity_type.value] += 1
            
            # 멀티모달 소스 분포
            source_type = entity.metadata.get('source_element_type', 'unknown')
            stats["multimodal_stats"]["entity_source_distribution"][source_type] += 1
            
            # 특수 추출 방법 통계
            if entity.metadata.get('extracted_via') == 'ocr':
                stats["multimodal_stats"]["ocr_extracted_entities"] += 1
            elif source_type == 'table':
                stats["multimodal_stats"]["table_extracted_entities"] += 1
            elif source_type == 'equation':
                stats["multimodal_stats"]["equation_extracted_entities"] += 1
        
        # 관계 타입 분포
        for rel in kg.relationships.values():
            stats["relationship_type_distribution"][rel.relation_type.value] += 1
            
            # Cross-modal 관계 카운트
            if rel.metadata.get('relationship_subtype') == 'cross_modal_match':
                stats["multimodal_stats"]["cross_modal_relationships"] += 1
        
        # 엔티티 연결도 분석
        entity_connections = defaultdict(int)
        for rel in kg.relationships.values():
            entity_connections[rel.source_entity_id] += 1
            entity_connections[rel.target_entity_id] += 1
        
        # 가장 연결된 엔티티들
        most_connected = sorted(entity_connections.items(), key=lambda x: x[1], reverse=True)[:10]
        for entity_id, connection_count in most_connected:
            entity = kg.entities.get(entity_id)
            if entity:
                stats["most_connected_entities"].append({
                    "entity_id": entity_id,
                    "entity_name": entity.name,
                    "entity_type": entity.entity_type.value,
                    "source_type": entity.metadata.get('source_element_type', 'unknown'),
                    "connection_count": connection_count
                })
        
        # 엔티티 언급 통계
        for entity in kg.entities.values():
            mention_stats = {
                "total_mentions": len(entity.mentions),
                "sources": list(set(m.get("source_file", "unknown") for m in entity.mentions)),
                "avg_confidence": sum(m.get("confidence", 0) for m in entity.mentions) / len(entity.mentions) if entity.mentions else 0,
                "element_types": list(set(m.get("element_type", "unknown") for m in entity.mentions))
            }
            
            # 페이지 정보 추가
            pages = [entity.metadata.get('page_number')] if entity.metadata.get('page_number') else []
            for mention in entity.mentions:
                if 'page_number' in mention:
                    pages.append(mention['page_number'])
            if pages:
                mention_stats['pages'] = list(set(pages))
            
            stats["entity_mention_stats"][entity.id] = mention_stats
        
        # 멀티모달 요약 통계
        stats["multimodal_summary"] = {
            "text_based_entities": stats["multimodal_stats"]["entity_source_distribution"].get('text', 0),
            "table_based_entities": stats["multimodal_stats"]["table_extracted_entities"],
            "image_based_entities": stats["multimodal_stats"]["ocr_extracted_entities"],
            "equation_based_entities": stats["multimodal_stats"]["equation_extracted_entities"],
            "cross_modal_integration_rate": (
                stats["multimodal_stats"]["cross_modal_relationships"] / 
                len(kg.relationships) * 100 if kg.relationships else 0
            )
        }
        
        return stats

# 편의 함수들
def build_knowledge_graph_from_documents(processed_documents: List[Dict[str, Any]], 
                                       output_path: Optional[Union[str, Path]] = None) -> KnowledgeGraph:
    """문서들로부터 지식 그래프 구축하는 편의 함수"""
    builder = KnowledgeGraphBuilder()
    kg = builder.build_knowledge_graph(processed_documents)
    
    if output_path:
        builder.save_knowledge_graph(kg, output_path)
    
    return kg

def analyze_knowledge_graph(kg_path: Union[str, Path]) -> Dict[str, Any]:
    """지식 그래프 분석하는 편의 함수"""
    builder = KnowledgeGraphBuilder()
    kg = builder.load_knowledge_graph(kg_path)
    return builder.analyze_graph_statistics(kg)