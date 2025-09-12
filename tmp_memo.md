"""
Weaviate MCP 도구 클래스

kars_db.py의 RAGVectorDB를 활용하여 문서 검색 기능을 제공합니다.
"""

import asyncio
import json
import logging
import os
import sys
from pathlib import Path
from typing import Dict, List, Any, Optional, Union
from datetime import datetime
from openai import OpenAI
from kars_db import RAGVectorDB
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# 이름 수정 기능 사용 여부
USE_NAME_REVISION = os.getenv("USE_NAME_REVISION", "true").lower() == "true"


class FilterExtractionResult(BaseModel):
    custodian: Optional[str] = Field(None, description="보관자")
    ori_file_name: Optional[str] = Field(None, description="원본 파일명")
    s_created_date: Optional[Union[str, Dict[str, Any]]] = Field(None, description="생성일")
    # s_modified_date: Optional[str] = Field(None, description="수정일")
    sent_date: Optional[Union[str, Dict[str, Any]]] = Field(None, description="발송일")
    from_email: Optional[str] = Field(None, description="발신자 이메일")
    to_email: Optional[str] = Field(None, description="수신자 이메일")
    cc: Optional[str] = Field(None, description="참조 이메일")
    bcc: Optional[str] = Field(None, description="숨은참조 이메일")
    last_author: Optional[str] = Field(None, description="최종 작성자")
    extension: Optional[str] = Field(None, description="파일 확장자")
    


class WeaviateMCPTools:
    """Weaviate MCP 도구 클래스"""
    
    def __init__(self):
        """초기화"""
        self.rag_db: Optional[RAGVectorDB] = None
        self.initialized = False
        self.default_db_name = os.getenv("WEAVIATE_DB_NAME", "kars_test")
        base_url="http://10.10.190.1:8124/v1"
        api_key="token-abc123"
        self.client = OpenAI(base_url=base_url, api_key=api_key)
        
        
        # 데이터베이스 필드 매핑 정의 (FilterExtractionResult에 맞게 조정)
        self.db_fields = {
            "custodian": "보관자",
            "ori_file_name": "원본 파일명",
            "s_created_date": "생성일",
            "sent_date": "발송일",
            "from_email": "발신자 이메일",
            "to_email": "수신자 이메일",
            "cc": "참조 이메일",
            "bcc": "숨은참조 이메일",
            "last_author": "최종 작성자",
            "extension": "파일 확장자"
        }
        

        logger.info("Weaviate MCP 도구 초기화 완료")
    
    async def initialize_rag_db(self, db_name: str = None) -> bool:
        """RAG 데이터베이스 초기화"""

        try:
            db_name = db_name or self.default_db_name
            self.rag_db = RAGVectorDB(db_name)
            success = await self.rag_db.initialize()
            
            if success:
                self.initialized = True
                logger.info(f"✅ RAG 데이터베이스 초기화 성공: {db_name}")
                return True
            else:
                logger.error(f"❌ RAG 데이터베이스 초기화 실패: {db_name}")
                return False
                
        except Exception as e:
            logger.error(f"❌ RAG 데이터베이스 초기화 중 오류: {e}")
            return False
    
    async def search_documents(self, query: str, filters: Optional[Dict[str, Any]] = None, 
                             sort_by_date: bool = False, limit: int = 5, 
                             db_name: str = None) -> Dict[str, Any]:
        """
        쿼리로 관련 문서를 검색합니다.
        
        Args:
            query: 검색할 쿼리 문자열
            filters: 메타데이터 필터 딕셔너리 (None이면 단순 RAG 검색)
            sort_by_date: 날짜 순으로 정렬할지 여부 (기본값: False)
            limit: 반환할 최대 결과 수 (기본값: 5)
            db_name: 사용할 데이터베이스 이름 (기본값: 환경변수 또는 kars_test)
        
        Returns:
            검색 결과를 포함한 딕셔너리
        """
        try:
            # 데이터베이스가 초기화되지 않았거나 다른 DB를 사용하려는 경우 재초기화
            if not self.initialized or (db_name and db_name != self.default_db_name):
                if not await self.initialize_rag_db(db_name):
                    return {
                        "success": False,
                        "error": "데이터베이스 초기화에 실패했습니다.",
                        "results": []
                    }
            
            if not self.rag_db:
                return {
                    "success": False,
                    "error": "RAG 데이터베이스가 초기화되지 않았습니다.",
                    "results": []
                }
            
            # 필터가 모두 None이거나 비어있는 경우 단순 RAG 검색
            if not filters or all(v is None for v in filters.values()):
                logger.info(f"🔍 단순 RAG 검색 실행: '{query}' (limit: {limit})")
                results = await self.rag_db.search_chunks(query, limit=limit)
            else:
                # 필터가 있는 경우 필터와 함께 검색
                logger.info(f"🔍 필터 검색 실행: '{query}' (필터: {filters}, limit: {limit})")
                results = await self.rag_db.search_with_metadata_filter(query, filters, limit=limit)
            
            if results:
                # 결과 포맷팅
                formatted_results = []
                for result in results:
                    formatted_result = {
                        "id": result.get("id", ""),
                        "score": result.get("score", 0.0),
                        "content": result.get("properties", {}).get("chunk", ""),
                        "properties": result.get("properties", {})
                    }
                    formatted_results.append(formatted_result)
                
                # 날짜 순으로 정렬 (sort_by_date가 True인 경우)
                if sort_by_date:
                    formatted_results.sort(key=lambda x: self._parse_date_for_sorting(
                        x["properties"].get("sent_date") or 
                        x["properties"].get("s_created_date")
                    ))
                
                return {
                    "success": True,
                    "query": query,
                    "filters": filters,
                    "sort_by_date": sort_by_date,
                    "total_results": len(formatted_results),
                    "results": formatted_results,
                    "search_timestamp": datetime.now().isoformat()
                }
            else:
                return {
                    "success": True,
                    "query": query,
                    "filters": filters,
                    "sort_by_date": sort_by_date,
                    "total_results": 0,
                    "results": [],
                    "message": "검색 결과가 없습니다.",
                    "search_timestamp": datetime.now().isoformat()
                }
                
        except Exception as e:
            logger.error(f"문서 검색 중 오류 발생: {e}")
            return {
                "success": False,
                "error": f"검색 중 오류가 발생했습니다: {str(e)}",
                "results": []
            }
    
    async def get_document_with_filter(self, class_name: str, limit: int, 
                                     filters: Optional[Dict[str, Any]] = None,
                                     db_name: str = None, sort_by_date=True) -> Dict[str, Any]:
        """
        특정 클래스에서 필터를 적용하여 문서를 검색합니다.
        
        Args:
            class_name: 검색할 클래스 이름 (필수)
            limit: 반환할 최대 결과 수 (필수)
            filters: 메타데이터 필터 딕셔너리 (선택사항, None이면 모든 문서 반환)
            db_name: 사용할 데이터베이스 이름 (선택사항)
        
        Returns:
            검색 결과를 포함한 딕셔너리
        """
        try:
            # 데이터베이스가 초기화되지 않았거나 다른 DB를 사용하려는 경우 재초기화
            if not self.initialized or (db_name and db_name != self.default_db_name):
                if not await self.initialize_rag_db(db_name):
                    return {
                        "success": False,
                        "error": "데이터베이스 초기화에 실패했습니다.",
                        "results": []
                    }
            
            if not self.rag_db:
                return {
                    "success": False,
                    "error": "RAG 데이터베이스가 초기화되지 않았습니다.",
                    "results": []
                }
            
            # 필터 검색 실행
            logger.info(f"🔍 필터 검색 실행: class_name={class_name}, limit={limit}, filters={filters}")
            results = await self.rag_db.get_document_with_filter(class_name, limit, filters)
            
            if results:
                # 결과 포맷팅
                formatted_results = []
                for result in results:
                    formatted_result = {
                        "id": result.get("id", ""),
                        "score": result.get("score", 1.0),
                        "content": result.get("properties", {}).get("chunk", ""),
                        "properties": result.get("properties", {})
                    }
                    formatted_results.append(formatted_result)
                
                if sort_by_date:
                    formatted_results.sort(key=lambda x: self._parse_date_for_sorting(
                        x["properties"].get("s_created_date") or 
                        x["properties"].get("created_date")
                    ))
                
                
                return {
                    "success": True,
                    "class_name": class_name,
                    "filters": filters,
                    "total_results": len(formatted_results),
                    "results": formatted_results,
                    "search_timestamp": datetime.now().isoformat()
                }
            else:
                
                return {
                    "success": True,
                    "class_name": class_name,
                    "filters": filters,
                    "total_results": 0,
                    "results": [],
                    "message": "검색 결과가 없습니다.",
                    "search_timestamp": datetime.now().isoformat()
                }
                
        except Exception as e:
            logger.error(f"필터 검색 중 오류 발생: {e}")
            return {
                "success": False,
                "error": f"필터 검색 중 오류가 발생했습니다: {str(e)}",
                "results": []
            }
    
    async def extract_filter_from_query(self, query: str) -> Dict[str, Any]:
        """
        질의에서 데이터베이스 필드와 매핑되는 정보를 추출하고 검색 방식을 결정합니다.
        
        Args:
            query: 사용자 질의 문자열
            
        Returns:
            {
                "filters": Dict[str, Any],  # 추출된 필터 정보 (None이면 매핑되지 않음)
                "search_type": str,  # "similarity" 또는 "filter"
                "reasoning": str     # 판단 근거
            }
        """
        try:
            logger.info(f"🔍 필터 추출 시작: '{query}'")
            
            # LLM을 사용하여 필터 추출을 위한 프롬프트 생성
            prompt = self._create_filter_extraction_prompt(query)
            
            # LLM 호출 
            extracted_filters = await self._extract_filters_with_llm(prompt)
            
            # 검색 방식 결정
            search_type, reasoning = self._determine_search_type(query, extracted_filters)
            
            result = {
                "filters": extracted_filters.model_dump() if extracted_filters else None,
                "search_type": search_type,
                "reasoning": reasoning,
                "query": query,
            }
            
            logger.info(f"✅ 필터 추출 완료: {search_type} 검색, 필터: {extracted_filters}")
            return result
            
        except Exception as e:
            logger.error(f"필터 추출 중 오류 발생: {e}")
            return {
                "filters": None,
                "search_type": "similarity",
                "reasoning": f"오류 발생으로 인해 기본 유사도 검색을 사용합니다: {str(e)}",
                "query": query,
            }
    
    def _create_filter_extraction_prompt(self, query: str) -> str:
        """필터 추출을 위한 프롬프트를 생성합니다."""
        prompt = f"""
당신은 사용자 질의에서 데이터베이스 필드 정보를 정확하게 추출하는 전문가입니다.

사용자 질의: {query}

사용 가능한 데이터베이스 필드:
{self._format_db_fields()}

추출 규칙:
1. 질의에서 명확하게 언급된 정보만 추출
2. 날짜는 Weaviate 필터 연산자로 변환하여 추출:
   - "2024년 1월" → {{"gte": "2024-01-01T00:00:00Z", "lt": "2024-02-01T00:00:00Z"}}
   - "2024년 1월 15일" → {{"gte": "2024-01-15T00:00:00Z", "lt": "2024-01-16T00:00:00Z"}}
   - "2024년 이후" → {{"gte": "2024-01-01T00:00:00Z"}}
   - "2024년 이전" → {{"lt": "2024-01-01T00:00:00Z"}}
   - "2024년" → {{"gte": "2024-01-01T00:00:00Z", "lt": "2025-01-01T00:00:00Z"}}
3. 이메일 주소는 정확히 추출
4. 파일명, 폴더명은 정확히 추출
5. 보관자(custodian) 정보가 명시된 경우 정확히 추출
6. 매핑되지 않는 정보는 null로 설정
7. 반드시 JSON 형식으로만 응답

다음 JSON 형식으로 응답하세요:
{{
    "custodian": null,
    "ori_file_name": null,
    "s_created_date": null,
    "sent_date": null,
    "from_email": null,
    "to_email": null,
    "cc": null,
    "bcc": null,
    "last_author": null,
    "extension": null
}}

예시:
- 질의: "2024년 1월에 생성된 문서를 찾아주세요" → {{"s_created_date": {{"gte": "2024-01-01T00:00:00Z", "lt": "2024-02-01T00:00:00Z"}}, ...}}
- 질의: "2024년 이후 생성된 문서" → {{"s_created_date": {{"gte": "2024-01-01T00:00:00Z"}}, ...}}
- 질의: "2024년 1월 15일에 생성된 문서" → {{"s_created_date": {{"gte": "2024-01-15T00:00:00Z", "lt": "2024-01-16T00:00:00Z"}}, ...}}
- 질의: "user@example.com이 보낸 이메일" → {{"from_email": "user@example.com", ...}}
- 질의: "황재섭이 보낸 이메일" → {{"from_email": "황재섭", ...}}
- 질의: "이민우가 받은 이메일" → {{"to_email": "이민우", ...}}
- 질의: "보관자: 김철수, 파일: report.pdf" → {{"custodian": "김철수", "ori_file_name": "report.pdf", ...}}
"""
        return prompt
    
    def _format_db_fields(self) -> str:
        """데이터베이스 필드를 포맷팅합니다."""
        formatted = []
        for field, description in self.db_fields.items():
            formatted.append(f"- {field}: {description}")
        return "\n".join(formatted)
    
    async def _extract_filters_with_llm(self, prompt: str) -> FilterExtractionResult:
        """LLM을 사용하여 필터를 추출합니다."""
        try:
            # OpenAI API 호출
            response = self.client.chat.completions.create(
                model="/data/models_ckpt/Qwen3-32B",
                messages=[
                    {"role": "system", "content": "다음 JSON 스키마에 맞춰 정보를 추출하세요. 반드시 유효한 JSON 형식으로 응답해야 합니다."},
                    {"role": "user", "content": f"다음 텍스트에서 정보를 추출하여 JSON 형식으로 응답하세요: {prompt}"}
                ],
                response_format={"type": "json_object"},
                temperature=0.1
            )
            
            # 응답에서 JSON 추출
            content = response.choices[0].message.content

            # JSON 파싱하여 FilterExtractionResult 객체 생성
            parsed_data = json.loads(content)
            result = FilterExtractionResult(**parsed_data)
            
            # USE_NAME_REVISION이 True인 경우 이름 관련 필드에 대해 유사도 매칭 수행
            if USE_NAME_REVISION:
                result = await self._apply_name_revision(result, prompt)
            
            return result
            
        except Exception as e:
            logger.error(f"LLM 필터 추출 중 오류: {e}")
            return self._get_empty_filters()
    
    async def _apply_name_revision(self, filters: FilterExtractionResult, original_prompt: str) -> FilterExtractionResult:
        """이름 관련 필드에 대해 유사도 매칭을 적용하여 더 정확한 값을 찾습니다."""
        try:
            # 이름 관련 필드들
            name_fields = {
                "from_email": "from",
                "to_email": "to", 
                "custodian": "custodian",
                "last_author": "last_author"
            }
            
            # 데이터베이스에서 unique한 값들을 한 번만 가져옴
            unique_names_result = await self.get_unique_names()
            if not unique_names_result["success"]:
                logger.warning("⚠️ Unique 이름 조회 실패로 이름 수정을 건너뜁니다.")
                return filters
            
            for field_name, field_type in name_fields.items():
                current_value = getattr(filters, field_name)
                if current_value and isinstance(current_value, str) and current_value.strip():
                    # 먼저 정확한 매칭이 있는지 확인 (이미 가져온 데이터 사용)
                    exact_match = self._check_exact_match_with_data(current_value, field_type, unique_names_result)
                    if exact_match:
                        logger.info(f"✅ {field_name} 필드 정확한 매칭 발견: '{current_value}'")
                        continue
                    
                    # 정확한 매칭이 없을 때만 유사도 매칭 수행 (이미 가져온 데이터 사용)
                    similar_result = await self._find_name_matches_with_existing_data(
                        query_input=current_value,
                        field_type=field_type,
                        unique_names_result=unique_names_result,
                        limit=3
                    )
                    
                    if similar_result["success"] and similar_result["matches"]:
                        # 가장 유사한 매치를 선택
                        best_match = similar_result["matches"][0]
                        if best_match["similarity_score"] > 0.7:  # 유사도 임계값
                            setattr(filters, field_name, best_match["name"])
                            logger.info(f"✅ {field_name} 필드 수정: '{current_value}' → '{best_match['name']}' (유사도: {best_match['similarity_score']:.2f})")
                        else:
                            logger.info(f"⚠️ {field_name} 필드 유사도 부족: '{current_value}' (최고 유사도: {best_match['similarity_score']:.2f})")
                    else:
                        logger.info(f"ℹ️ {field_name} 필드에 대한 유사한 이름을 찾을 수 없음: '{current_value}'")
            
            return filters
            
        except Exception as e:
            logger.error(f"이름 수정 적용 중 오류: {e}")
            return filters
    
    async def _check_exact_match(self, value: str, field_type: str) -> bool:
        """정확한 매칭이 있는지 확인합니다."""
        try:
            # 데이터베이스에서 unique한 값들을 가져옴
            unique_names_result = await self.get_unique_names()
            if not unique_names_result["success"]:
                return False
            
            # 필드 타입에 따라 검색 대상 결정
            search_names = []
            if field_type == "from":
                search_names = unique_names_result["names"]["from_emails"]
            elif field_type == "to":
                search_names = unique_names_result["names"]["to_emails"]
            elif field_type == "custodian":
                search_names = unique_names_result["names"]["custodian"]
            elif field_type == "last_author":
                search_names = unique_names_result["names"]["last_author"]
            
            # 정확한 매칭 확인 (대소문자 무시)
            return value.lower().strip() in [name.lower().strip() for name in search_names]
            
        except Exception as e:
            logger.error(f"정확한 매칭 확인 중 오류: {e}")
            return False
    
    def _check_exact_match_with_data(self, value: str, field_type: str, unique_names_result: Dict[str, Any]) -> bool:
        """이미 가져온 데이터를 사용하여 정확한 매칭이 있는지 확인합니다."""
        try:
            # 필드 타입에 따라 검색 대상 결정
            search_names = []
            if field_type == "from":
                search_names = unique_names_result["names"]["from_emails"]
            elif field_type == "to":
                search_names = unique_names_result["names"]["to_emails"]
            elif field_type == "custodian":
                search_names = unique_names_result["names"]["custodian"]
            elif field_type == "last_author":
                search_names = unique_names_result["names"]["last_author"]
            
            # 정확한 매칭 확인 (대소문자 무시)
            return value.lower().strip() in [name.lower().strip() for name in search_names]
            
        except Exception as e:
            logger.error(f"정확한 매칭 확인 중 오류: {e}")
            return False
    
    async def _find_name_matches_with_existing_data(self, query_input: str, field_type: str, 
                                                   unique_names_result: Dict[str, Any], limit: int) -> Dict[str, Any]:
        """이미 가져온 데이터를 사용하여 이름 유사도 매칭을 수행합니다."""
        try:
            # 이메일 타입에 따라 검색 대상 결정
            search_names = []
            if field_type == "from" or field_type == "all":
                search_names.extend(unique_names_result["names"]["from_emails"])
            if field_type == "to" or field_type == "all":
                search_names.extend(unique_names_result["names"]["to_emails"])
            if field_type == "custodian" or field_type == "all":
                search_names.extend(unique_names_result["names"]["custodian"])
            if field_type == "last_author" or field_type == "all":
                search_names.extend(unique_names_result["names"]["last_author"])
            
            # 중복 제거
            search_names = list(set(search_names))
            
            if not search_names:
                return {
                    "success": True,
                    "query_input": query_input,
                    "field_type": field_type,
                    "message": "데이터베이스에 이메일 정보가 없습니다.",
                    "matches": [],
                    "timestamp": datetime.now().isoformat()
                }
            
            # LLM을 사용하여 유사도 매칭 수행
            matches = await self._find_name_matches_with_llm(query_input, search_names, limit)
            
            result = {
                "success": True,
                "query_input": query_input,
                "email_type": field_type,
                "total_candidates": len(search_names),
                "matches": matches,
                "timestamp": datetime.now().isoformat()
            }
            
            return result
            
        except Exception as e:
            logger.error(f"이름 유사도 매칭 중 오류 발생: {e}")
            return {
                "success": False,
                "error": f"이름 유사도 매칭 중 오류가 발생했습니다: {str(e)}",
                "matches": []
            }
    
    def _get_empty_filters(self) -> FilterExtractionResult:
        """빈 필터 Pydantic 모델을 반환합니다."""
        return FilterExtractionResult(
            custodian=None,
            ori_file_name=None,
            s_created_date=None,
            sent_date=None,
            from_email=None,
            to_email=None,
            cc=None,
            bcc=None,
            last_author=None,
            extension=None
        )
        
        
    
    def _determine_search_type(self, query: str, filters: FilterExtractionResult) -> tuple[str, str]:
        """검색 방식을 결정합니다."""
        try:
            # 쿼리에서 유사한 문서 검색을 나타내는 키워드 확인
            similarity_keywords = [
                "~에 관한", "~에 대한", "~와 유사한", "비슷한", "같은", "유사한", 
                "관련된", "연관된", "참고할", "참고용", "참고 자료", "참고 문서",
                "~와 같은", "~와 비슷한", "~와 관련된", "~와 연관된"
            ]
            
            # 쿼리에 유사성 키워드가 포함되어 있는지 확인
            has_similarity_keyword = any(keyword in query for keyword in similarity_keywords)
            
            # 필터가 모두 None이거나 비어있는 경우
            if not filters or all(v is None for v in filters.model_dump().values()):
                if has_similarity_keyword:
                    return "similarity", "질의에서 유사한 문서 검색 키워드를 발견하여 유사도 기반 검색을 사용합니다."
                return "similarity", "질의에서 구체적인 필터 정보를 찾을 수 없어 유사도 기반 검색을 사용합니다."
            
            # 유효한 필터가 있는지 확인
            valid_filters = {k: v for k, v in filters.model_dump().items() if v is not None}
            
            if not valid_filters:
                if has_similarity_keyword:
                    return "similarity", "질의에서 유사한 문서 검색 키워드를 발견하여 유사도 기반 검색을 사용합니다."
                return "similarity", "질의에서 유효한 필터 정보를 찾을 수 없어 유사도 기반 검색을 사용합니다."
            
            # 유사성 키워드가 있으면 similarity 검색 우선
            if has_similarity_keyword:
                return "similarity", "질의에서 유사한 문서 검색 키워드를 발견하여 유사도 기반 검색을 사용합니다."
            
            # 특정 조건들이 모두 만족되는 경우 필터 검색 사용
            if len(valid_filters) >= 2:
                return "filter", f"질의에서 {len(valid_filters)}개의 구체적인 필터 정보를 찾았습니다: {list(valid_filters.keys())}. 조건 필터링을 사용합니다."
            
            # 단일 필터인 경우 질의의 복잡성에 따라 결정
            if len(valid_filters) == 1:
                field, value = list(valid_filters.items())[0]
                
                # 이메일이나 파일명 등 구체적인 식별자가 있는 경우
                if field in ["from_email", "to_email", "ori_file_name"]:
                    return "filter", f"질의에서 구체적인 식별자 '{field}: {value}'를 찾았습니다. 조건 필터링을 사용합니다."
                
                # 날짜 필드인 경우
                elif field in ["s_created_date", "sent_date"]:
                    return "filter", f"질의에서 구체적인 날짜 정보 '{field}: {value}'를 찾았습니다. 조건 필터링을 사용합니다."
                
                # 기타 필드인 경우
                else:
                    return "similarity", f"질의에서 구체적인 필터 정보를 찾았지만 단일 필터이므로 유사도 기반 검색을 사용합니다."
            
            return "similarity", "기본적으로 유사도 기반 검색을 사용합니다."
            
        except Exception as e:
            logger.error(f"검색 방식 결정 중 오류: {e}")
            return "similarity", f"오류 발생으로 인해 기본 유사도 검색을 사용합니다: {str(e)}"
    
    def _parse_date_for_sorting(self, date_input) -> str:
        """정렬을 위한 날짜 입력을 파싱합니다."""

        # datetime 객체인 경우
        if isinstance(date_input, datetime):
            return date_input.strftime("%Y-%m-%dT%H:%M:%SZ")
        
        # 문자열인 경우
        if isinstance(date_input, str):
            # RFC3339 형식이 아닌 경우 기본값 반환
            if not date_input.endswith('Z') and 'T' in date_input:
                try:
                    # ISO 형식을 RFC3339로 변환
                    dt = datetime.fromisoformat(date_input.replace('Z', '+00:00'))
                    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")
                except:
                    pass
            
            return date_input
        
    
    async def cleanup(self):
        """리소스 정리"""
        try:
            if self.rag_db:
                self.rag_db.close()
                self.rag_db = None
            
            self.initialized = False
            logger.info("Weaviate MCP 도구 정리 완료")
            
        except Exception as e:
            logger.error(f"리소스 정리 중 오류 발생: {e}")
    
    def get_tool_descriptions(self) -> List[Dict[str, str]]:
        """사용 가능한 도구들의 설명을 반환합니다."""
        tools = [
            {
                "name": "search_documents",
                "description": "쿼리로 관련 문서를 검색합니다. 필터가 제공되면 메타데이터 필터와 함께 검색하고, 필터가 없으면 단순 RAG 검색을 수행합니다.",
                "parameters": {
                    "query": "검색할 쿼리 문자열 (필수)",
                    "filters": "메타데이터 필터 딕셔너리 (선택사항, None이면 단순 RAG 검색)",
                    "sort_by_date": "날짜 순으로 정렬할지 여부 (기본값: false)",
                    "limit": "반환할 최대 결과 수 (기본값: 5)",
                    "db_name": "사용할 데이터베이스 이름 (선택사항)"
                }
            },
            {
                "name": "get_document_with_filter",
                "description": "특정 클래스에서 필터를 적용하여 문서를 검색합니다. 쿼리 없이 필터만으로 검색할 때 사용합니다.",
                "parameters": {
                    "class_name": "검색할 클래스 이름 (필수)",
                    "limit": "반환할 최대 결과 수 (필수)",
                    "filters": "메타데이터 필터 딕셔너리 (선택사항, None이면 모든 문서 반환)",
                    "db_name": "사용할 데이터베이스 이름 (선택사항)"
                }
            },
            {
                "name": "extract_filter_from_query",
                "description": "질의에서 데이터베이스 필드와 매핑되는 정보를 추출하고 검색 방식을 결정합니다.",
                "parameters": {
                    "query": "사용자 질의 문자열 (필수)"
                }
            },
            {
                "name": "get_unique_names",
                "description": "데이터베이스에서 이름이 있을 가능성이 있는 필드의 모든 unique한 값들을 가져옵니다.",
                "parameters": {
                    "db_name": "사용할 데이터베이스 이름 (선택사항)"
                }
            },
            {
                "name": "find_similar_name",
                "description": "쿼리에서 추출한 이메일 값 또는 이름과 가장 비슷한 데이터베이스의 이메일을 찾습니다. LLM이 유사도를 판단하여 가장 적합한 매치를 찾아냅니다. 한글/영어 이름, 이메일 주소, 부분 정보 등 다양한 형태의 입력을 지원합니다.",
                "parameters": {
                    "query_input": "쿼리에서 추출한 이메일 값 또는 이름 (예: '조효원', 'hyyoka@gmail.com', 'hyyoka') (필수)",
                    "field_type": "from, to, all 중 선택 (기본값: all)",
                    "db_name": "사용할 데이터베이스 이름 (선택사항)",
                    "limit": "반환할 최대 결과 수 (기본값: 5)"
                }
            }
        ]
        
        return tools

    async def get_unique_names(self, db_name: str = None) -> Dict[str, Any]:
        """
        데이터베이스에서 이름이 있을 가능성이 있는 필드의 모든 unique한 값들을 가져옵니다.
        
        Args:
            db_name: 사용할 데이터베이스 이름 (선택사항)
            
        Returns:
            unique한 이메일 값들을 포함한 딕셔너리
        """
        try:
            # 데이터베이스가 초기화되지 않았거나 다른 DB를 사용하려는 경우 재초기화
            if not self.initialized or (db_name and db_name != self.default_db_name):
                if not await self.initialize_rag_db(db_name):
                    return {
                        "success": False,
                        "error": "데이터베이스 초기화에 실패했습니다.",
                        "names": {"from_emails": [], "to_emails": [],  "custodian": [], "last_author": []}
                    }
            
            if not self.rag_db:
                return {
                    "success": False,
                    "error": "RAG 데이터베이스가 초기화되지 않았습니다.",
                     "names": {"from_emails": [], "to_emails": [],  "custodian": [], "last_author": []}
                }
                
      
            logger.info("🔍 데이터베이스에서 unique한 이메일 값들을 조회합니다.")
            
            # from_email과 to_email의 unique한 값들을 가져오기 위한 쿼리
            from_emails = await self.rag_db.get_unique_values("from_email")
            to_emails = await self.rag_db.get_unique_values("to_email")
            custodian = await self.rag_db.get_unique_values("custodian")
            last_author = await self.rag_db.get_unique_values("last_author")
            
            
            
            # 결과 정리 및 중복 제거
            unique_from_emails = list(set([email for email in from_emails if email]))
            unique_to_emails = list(set([email for email in to_emails if email]))
            unique_custodian = list(set([name for name in custodian if name]))
            unique_last_author = list(set([name for name in last_author if name]))
            
            # 정렬
            unique_from_emails.sort()
            unique_to_emails.sort()
            unique_custodian.sort()
            unique_last_author.sort()
            
            result = {
                "success": True,
                "total_from_emails": len(unique_from_emails),
                "total_to_emails": len(unique_to_emails),
                "total_custodian": len(unique_custodian),
                "total_last_author": len(unique_last_author),
                "names": {
                    "from_emails": unique_from_emails,
                    "to_emails": unique_to_emails,
                    "custodian": unique_custodian,
                    "last_author": unique_last_author
                },
                "timestamp": datetime.now().isoformat()
            }
            
            logger.info(f"✅ Unique 이름들 조회 완료: from_email {len(unique_from_emails)}개, to_email {len(unique_to_emails)}개, custodian {len(unique_custodian)}, total_last_author:  {len(unique_last_author)}")
            return result
            
        except Exception as e:
            logger.error(f"Unique 이름 조회 중 오류 발생: {e}")
            return {
                "success": False,
                "error": f"Unique 이름 조회 중 오류가 발생했습니다: {str(e)}",
                "names": {"from_emails": [], "to_emails": [],  "custodian": [], "last_author": []}
            }
    
    async def find_similar_name(self, query_input: str, field_type: str = "all", 
                                db_name: str = None, limit: int = 5) -> Dict[str, Any]:
        """
        쿼리에서 추출한 이메일 값 또는 이름과 가장 비슷한 데이터베이스의 이메일을 찾습니다.
        LLM이 유사도를 판단하여 가장 적합한 매치를 찾아냅니다.
        
        Args:
            query_input: 쿼리에서 추출한 이메일 값 또는 이름 (예: "조효원", "hyyoka@gmail.com", "hyyoka")
            email_type: "from", "to", "both" 중 선택 (기본값: "all")
            db_name: 사용할 데이터베이스 이름 (선택사항)
            limit: 반환할 최대 결과 수 (기본값: 5)
            
        Returns:
            유사한 이메일 매치 결과를 포함한 딕셔너리
        """
        try:
            if not query_input:
                return {
                    "success": False,
                    "error": "쿼리 입력 값이 제공되지 않았습니다.",
                    "matches": []
                }
            
            # 데이터베이스에서 unique한 이메일 값들을 가져옴
            unique_emails_result = await self.get_unique_names(db_name)
            if not unique_emails_result["success"]:
                return unique_emails_result
            
            # 이메일 타입에 따라 검색 대상 결정
            search_names = []
            if field_type == "from" or field_type == "all":
                search_names.extend(unique_emails_result["names"]["from_emails"])
            if field_type == "to" or field_type == "all":
                search_names.extend(unique_emails_result["names"]["to_emails"])
            if field_type == "custodian" or field_type == "all":
                search_names.extend(unique_emails_result["names"]["custodian"])
            if field_type == "last_author" or field_type == "all":
                search_names.extend(unique_emails_result["names"]["last_author"])
            
            # 중복 제거
            search_names = list(set(search_names))
            
            if not search_names:
                return {
                    "success": True,
                    "query_input": query_input,
                    "field_type": field_type,
                    "message": "데이터베이스에 이메일 정보가 없습니다.",
                    "matches": [],
                    "timestamp": datetime.now().isoformat()
                }
            
            # LLM을 사용하여 유사도 매칭 수행
            matches = await self._find_name_matches_with_llm(query_input, search_names, limit)
            
            result = {
                "success": True,
                "query_input": query_input,
                "email_type": field_type,
                "total_candidates": len(search_names),
                "matches": matches,
                "timestamp": datetime.now().isoformat()
            }
            
            logger.info(f"✅ 이메일 유사도 매칭 완료: '{query_input}' → {len(matches)}개 매치")
            return result
            
        except Exception as e:
            logger.error(f"이메일 유사도 매칭 중 오류 발생: {e}")
            return {
                "success": False,
                "error": f"이메일 유사도 매칭 중 오류가 발생했습니다: {str(e)}",
                "matches": []
            }
    
    async def _find_name_matches_with_llm(self, query_input: str, candidate_names: List[str], 
                                          limit: int) -> List[Dict[str, Any]]:
        """LLM을 사용하여 이름 유사도 매칭을 수행합니다."""
        try:
            # LLM을 위한 프롬프트 생성
            prompt = self._create_name_matching_prompt(query_input, candidate_names, limit)
            
            # LLM 호출
            response = self.client.chat.completions.create(
                model="/data/models_ckpt/Qwen3-32B",
                messages=[
                    {"role": "system", "content": "당신은 이메일 주소와 이름의 유사도를 판단하는 전문가입니다. 주어진 입력과 가장 유사한 후보들을 선택하세요."},
                    {"role": "user", "content": prompt}
                ],
                response_format={"type": "json_object"},
                temperature=0.1
            )
            
            # 응답에서 JSON 추출
            content = response.choices[0].message.content
            parsed_data = json.loads(content)
            
            # 결과 포맷팅
            matches = []
            for match in parsed_data.get("matches", []):
                matches.append({
                    "name": match.get("name", ""),
                    "similarity_score": match.get("similarity_score", 0.0),
                    "reasoning": match.get("reasoning", ""),
                    "match_type": match.get("match_type", "unknown")
                })
            
            # 유사도 점수 순으로 정렬
            matches.sort(key=lambda x: x["similarity_score"], reverse=True)
            
            return matches[:limit]
            
        except Exception as e:
            logger.error(f"LLM 이메일 매칭 중 오류: {e}")
            # LLM 실패 시 간단한 문자열 유사도 기반 매칭으로 폴백
            return self._fallback_name_matching(query_input, candidate_names, limit)
    
    def _create_name_matching_prompt(self, query_input: str, candidate_names: List[str], 
                                     limit: int) -> str:
        """이메일 매칭을 위한 프롬프트를 생성합니다."""
        prompt = f"""
당신은 이메일 주소와 이름의 유사도를 판단하는 전문가입니다.

쿼리 입력: {query_input}

후보 이메일 목록:
{chr(10).join([f"{i+1}. {name}" for i, name in enumerate(candidate_names)])}

매칭 규칙:
1. 정확한 일치 (100점): 
   - 이메일 주소가 완전히 일치
   - 이름이 완전히 일치 (예: "조효원" ↔ "조효원")
2. 이름 유사 (90점): 
   - 이름의 순서가 바뀐 경우 (예: "조효원" ↔ "효원 조")
   - 영어 이름과 한글 이름 매칭 (예: "hyowon cho" ↔ "조효원")
   - 약어나 별칭 포함 (예: "hyowon cho (KC)" ↔ "조효원")
   - 만약 이름이 아예 다르다면, 대상이 아님 (예: Cho, Selena는 조효원과 매칭될 수 없음)
3. 이메일 사용자명 일치 (80점): 
   - 이메일의 @ 앞 부분이 일치 (예: "hyyoka" ↔ "hyyoka@gmail.com")
4. 부분 일치 (30점): 
   - 이름의 일부가 일치하거나 유사
   - 이메일 주소의 일부가 일치
6. 관련성 (5점): 
   - 업무적, 조직적 관련성이 있는 경우

특별 고려사항:
- "hyowon cho (KC)"와 "조효원"은 같은 사람으로 간주
- "hyyoka@gmail.com"에서 "hyyoka"만 입력된 경우도 매칭
- 한글 이름과 영어 이름의 매칭을 우선적으로 고려
- 괄호 안의 약어나 별칭도 고려

다음 JSON 형식으로 응답하세요:
{{
    "matches": [
        {{
            "name": "이메일주소 혹은 이름",
            "similarity_score": 0.0-100.0,
            "reasoning": "매칭 이유 설명",
            "match_type": "exact|name_similar|username|domain|partial|related"
        }}
    ]
}}

가장 유사한 {limit}개의 이메일을 선택하고, 각각에 대해 유사도 점수와 매칭 이유를 제공하세요.
"""
        return prompt
    
    def _fallback_name_matching(self, query_input: str, candidate_names: List[str], 
                                limit: int) -> List[Dict[str, Any]]:
        """LLM 실패 시 간단한 문자열 유사도 기반 매칭으로 폴백합니다."""
        try:
            matches = []
            
            for name in candidate_names:
                if not name:
                    continue
                
                # 간단한 문자열 유사도 계산
                similarity_score = self._calculate_simple_similarity(query_input, name)
                
                if similarity_score > 0:
                    match_type = self._determine_match_type(query_input, name)
                    reasoning = f"문자열 유사도 기반 매칭: {similarity_score:.1f}%"
                    
                    matches.append({
                        "name": name,
                        "similarity_score": similarity_score,
                        "reasoning": reasoning,
                        "match_type": match_type
                    })
            
            # 유사도 점수 순으로 정렬
            matches.sort(key=lambda x: x["similarity_score"], reverse=True)
            
            return matches[:limit]
            
        except Exception as e:
            logger.error(f"폴백 이메일 매칭 중 오류: {e}")
            return []
    
    def _calculate_simple_similarity(self, query_input: str, candidate_name: str) -> float:
        """간단한 문자열 유사도를 계산합니다."""
        try:
            if not query_input or not candidate_name:
                return 0.0
            
            query_lower = query_input.lower()
            candidate_lower = candidate_name.lower()
            
            # 정확한 일치
            if query_lower == candidate_lower:
                return 100.0
            
            # 이메일 주소인지 확인
            if '@' in query_lower and '@' in candidate_lower:
                # 도메인과 사용자명 분리
                query_parts = query_lower.split('@')
                candidate_parts = candidate_lower.split('@')
                
                if len(query_parts) == 2 and len(candidate_parts) == 2:
                    query_user, query_domain = query_parts
                    candidate_user, candidate_domain = candidate_parts
                    
                    # 도메인 일치 (80점)
                    if query_domain == candidate_domain:
                        # 사용자명 유사도 계산
                        user_similarity = self._calculate_string_similarity(query_user, candidate_user)
                        return 80.0 + (user_similarity * 20.0)
                    
                    # 사용자명 일치 (60점)
                    if query_user == candidate_user:
                        # 도메인 유사도 계산
                        domain_similarity = self._calculate_string_similarity(query_domain, candidate_domain)
                        return 60.0 + (domain_similarity * 20.0)
                    
                    # 부분 일치 (최대 40점)
                    user_similarity = self._calculate_string_similarity(query_user, candidate_user)
                    domain_similarity = self._calculate_string_similarity(query_domain, candidate_domain)
                    
                    return max(user_similarity, domain_similarity) * 40.0
            
            # 이름 기반 매칭 (이메일이 아닌 경우)
            # 괄호와 특수문자 제거
            query_clean = self._clean_name_string(query_lower)
            candidate_clean = self._clean_name_string(candidate_lower)
            
            # 정확한 이름 일치 (90점)
            if query_clean == candidate_clean:
                return 90.0
            
            # 이름 유사도 계산 (최대 70점)
            name_similarity = self._calculate_name_similarity(query_clean, candidate_clean)
            return name_similarity * 70.0
            
        except Exception as e:
            logger.error(f"유사도 계산 중 오류: {e}")
            return 0.0
    
    def _calculate_string_similarity(self, str1: str, str2: str) -> float:
        """두 문자열 간의 유사도를 계산합니다 (Jaccard 유사도 기반)."""
        try:
            if not str1 or not str2:
                return 0.0
            
            # 문자 단위로 집합 생성
            set1 = set(str1)
            set2 = set(str2)
            
            # Jaccard 유사도 계산
            intersection = len(set1.intersection(set2))
            union = len(set1.union(set2))
            
            if union == 0:
                return 0.0
            
            return (intersection / union) * 100.0
            
        except Exception as e:
            logger.error(f"문자열 유사도 계산 중 오류: {e}")
            return 0.0
    
    def _determine_match_type(self, query_input: str, candidate_name: str) -> str:
        """매칭 타입을 결정합니다."""
        try:
            if not query_input or not candidate_name:
                return "unknown"
            
            query_lower = query_input.lower()
            candidate_lower = candidate_name.lower()
            
            if query_lower == candidate_lower:
                return "exact"
            
            # 이메일 주소인지 확인
            if '@' in query_lower and '@' in candidate_lower:
                query_parts = query_lower.split('@')
                candidate_parts = candidate_lower.split('@')
                
                if len(query_parts) == 2 and len(candidate_parts) == 2:
                    query_user, query_domain = query_parts
                    candidate_user, candidate_domain = candidate_parts
                    
                    if query_domain == candidate_domain:
                        return "domain"
                    elif query_user == candidate_user:
                        return "username"
                    else:
                        return "partial"
            
            # 이름 기반 매칭
            query_clean = self._clean_name_string(query_lower)
            candidate_clean = self._clean_name_string(candidate_lower)
            
            if query_clean == candidate_clean:
                return "name_similar"
            else:
                return "partial"
                
        except Exception as e:
            logger.error(f"매칭 타입 결정 중 오류: {e}")
            return "unknown"
    
    def _clean_name_string(self, name: str) -> str:
        """이름 문자열을 정리합니다."""
        try:
            if not name:
                return ""
            
            # 괄호와 그 안의 내용 제거
            import re
            name = re.sub(r'\([^)]*\)', '', name)
            
            # 특수문자 제거 (공백, 하이픈, 언더스코어는 유지)
            name = re.sub(r'[^\w\s\-_]', '', name)
            
            # 연속된 공백을 하나로 변환
            name = re.sub(r'\s+', ' ', name)
            
            # 앞뒤 공백 제거
            name = name.strip()
            
            return name
            
        except Exception as e:
            logger.error(f"이름 정리 중 오류: {e}")
            return name
    
    def _calculate_name_similarity(self, name1: str, name2: str) -> float:
        """두 이름 간의 유사도를 계산합니다."""
        try:
            if not name1 or not name2:
                return 0.0
            
            # 공백으로 분리하여 단어 단위로 비교
            words1 = set(name1.split())
            words2 = set(name2.split())
            
            if not words1 or not words2:
                return 0.0
            
            # Jaccard 유사도 계산
            intersection = len(words1.intersection(words2))
            union = len(words1.union(words2))
            
            if union == 0:
                return 0.0
            
            base_similarity = intersection / union
            
            # 추가적인 이름 매칭 로직
            # 1. 한글 이름과 영어 이름 매칭
            korean_match = self._check_korean_english_match(name1, name2)
            if korean_match:
                base_similarity = max(base_similarity, 0.8)
            
            # 2. 이름 순서 바뀐 경우
            if self._check_name_order_reversed(name1, name2):
                base_similarity = max(base_similarity, 0.7)
            
            # 3. 부분 이름 매칭
            partial_match = self._check_partial_name_match(name1, name2)
            if partial_match:
                base_similarity = max(base_similarity, 0.6)
            
            return base_similarity * 100.0
            
        except Exception as e:
            logger.error(f"이름 유사도 계산 중 오류: {e}")
            return 0.0
    
    def _check_korean_english_match(self, name1: str, name2: str) -> bool:
        """한글 이름과 영어 이름의 매칭을 확인합니다."""
        try:
            # 간단한 한글/영어 구분 (유니코드 범위 사용)
            def is_korean(text):
                return any('\uac00' <= char <= '\ud7af' for char in text)
            
            def is_english(text):
                return all(char.isascii() and char.isalpha() or char.isspace() for char in text)
            
            # 한쪽은 한글, 다른 쪽은 영어인 경우
            if (is_korean(name1) and is_english(name2)) or (is_english(name1) and is_korean(name2)):
                # 공통 단어나 부분 매칭 확인
                words1 = set(name1.lower().split())
                words2 = set(name2.lower().split())
                
                # 공통 단어가 있거나 부분 매칭이 있는 경우
                if words1.intersection(words2):
                    return True
                
                # 부분 문자열 매칭 확인
                for word1 in words1:
                    for word2 in words2:
                        if word1 in word2 or word2 in word1:
                            return True
                
                return False
            
            return False
            
        except Exception as e:
            logger.error(f"한글-영어 매칭 확인 중 오류: {e}")
            return False
    
    def _check_name_order_reversed(self, name1: str, name2: str) -> bool:
        """이름의 순서가 바뀐 경우를 확인합니다."""
        try:
            words1 = name1.split()
            words2 = name2.split()
            
            if len(words1) != len(words2) or len(words1) < 2:
                return False
            
            # 순서가 바뀐 경우 확인
            if words1 == words2[::-1]:
                return True
            
            # 부분적으로 순서가 바뀐 경우
            if len(words1) >= 2 and len(words2) >= 2:
                # 첫 번째와 마지막 단어가 바뀐 경우
                if words1[0] == words2[-1] and words1[-1] == words2[0]:
                    return True
            
            return False
            
        except Exception as e:
            logger.error(f"이름 순서 확인 중 오류: {e}")
            return False
    
    def _check_partial_name_match(self, name1: str, name2: str) -> bool:
        """부분적인 이름 매칭을 확인합니다."""
        try:
            words1 = set(name1.split())
            words2 = set(name2.split())
            
            # 공통 단어가 있는 경우
            if words1.intersection(words2):
                return True
            
            # 부분 문자열 매칭 확인
            for word1 in words1:
                for word2 in words2:
                    if len(word1) >= 2 and len(word2) >= 2:  # 최소 2글자 이상
                        if word1 in word2 or word2 in word1:
                            return True
            
            return False
            
        except Exception as e:
            logger.error(f"부분 이름 매칭 확인 중 오류: {e}")
            return False
