#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
로컬 테스트용: OpenAI API를 사용하여 Style Transfer 예측 생성
vLLM 서버 없이 OpenAI API를 통해 예측 생성 (로컬 테스트용)
"""

import json
import os
import time
from typing import List, Dict, Optional
from pathlib import Path
from datetime import datetime

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field

from spa_prompt_utils import create_enhanced_prompt
from test_data_manager import load_test_data

# server_langgraph.py의 구조화된 출력 모델 재사용
try:
    from server_langgraph import StyleTransferOutput, determine_output_schema
except ImportError:
    # server_langgraph가 없으면 직접 정의 (server_langgraph.py와 동일)
    class StyleTransferOutput(BaseModel):
        """매수인 ↔ 매도인 전환 응답"""
        analysis: str = Field(description="전환 전 조항에 대한 분석")
        converted_sentence: str = Field(description="전환된 조항 문장")
    
    def determine_output_schema(selected_tasks):
        """선택된 작업에 따라 적절한 출력 스키마 반환 (server_langgraph.py와 동일)"""
        if not selected_tasks:
            return None
        if "매수인 ↔ 매도인 전환" in selected_tasks:
            return StyleTransferOutput
        return None

# 환경 변수 로드
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))

# OpenAI API 설정 (로컬 테스트용)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")  # 기본값: gpt-4o-mini (가격 효율적)


def get_llm(temperature: float = 0.0, max_tokens: int = 16384):
    """OpenAI API를 사용하는 ChatOpenAI 인스턴스 생성 (로컬 테스트용)"""
    if not OPENAI_API_KEY:
        raise ValueError(
            "OPENAI_API_KEY 환경 변수가 설정되지 않았습니다. "
            ".env 파일에 OPENAI_API_KEY=your_api_key를 추가하세요."
        )
    
    # 모델별 max_tokens 제한 확인 및 조정
    # gpt-4o: 16384
    # gpt-4o-mini: 16000 (실제 제한은 16000, 하지만 16384도 허용될 수 있음)
    # gpt-4-turbo: 모델 버전에 따라 다름
    if "gpt-4o-mini" in OPENAI_MODEL.lower():
        # GPT-4o-mini는 최대 16000 토큰까지 생성 가능
        if max_tokens > 16000:
            max_tokens = 16000
    elif "gpt-4o" in OPENAI_MODEL.lower() and "mini" not in OPENAI_MODEL.lower():
        # GPT-4o는 16384 토큰까지 생성 가능
        if max_tokens > 16384:
            max_tokens = 16384
    elif "turbo" in OPENAI_MODEL.lower():
        # turbo는 모델 버전에 따라 다를 수 있으므로 기본값 유지
        pass
    
    return ChatOpenAI(
        model=OPENAI_MODEL,
        api_key=OPENAI_API_KEY,
        temperature=temperature,
        max_tokens=max_tokens,
        timeout=120.0,
    )


def get_structured_llm(temperature: float = 0.0, max_tokens: int = 16384, output_schema=None):
    """구조화된 출력을 위한 LLM 인스턴스 생성"""
    llm = get_llm(temperature=temperature, max_tokens=max_tokens)
    if output_schema:
        return llm.with_structured_output(output_schema)
    return llm


def extract_score_from_response(response_text: str) -> Optional[float]:
    """
    LLM 응답에서 점수 추출
    다양한 형식의 응답에서 점수를 찾아냄
    """
    import re
    
    # 패턴 1: "점수: 4.0" 또는 "score: 4.0"
    patterns = [
        r'점수[:\s]+([0-9.]+)',
        r'score[:\s]+([0-9.]+)',
        r'([0-9.]+)\s*점',
        r'\(([0-9.]+)\)',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, response_text, re.IGNORECASE)
        if match:
            try:
                score = float(match.group(1))
                if 0.0 <= score <= 4.0:
                    return score
            except ValueError:
                continue
    
    # 패턴 2: JSON 형식에서 추출
    try:
        json_match = re.search(r'\{[^}]*"score"[^}]*\}', response_text)
        if json_match:
            data = json.loads(json_match.group())
            if 'score' in data:
                score = float(data['score'])
                if 0.0 <= score <= 4.0:
                    return score
    except:
        pass
    
    return None


def extract_clause_from_response(response_text: str) -> str:
    """
    LLM 응답에서 변환된 조항 추출
    """
    import re
    
    # ```로 감싸진 부분 추출
    code_block_match = re.search(r'```[^\n]*\n(.*?)```', response_text, re.DOTALL)
    if code_block_match:
        return code_block_match.group(1).strip()
    
    # "변환된 조항:" 또는 "converted_sentence:" 뒤의 텍스트 추출
    patterns = [
        r'변환된\s*조항[:\s]+(.*?)(?:\n\n|\n##|$)',
        r'converted_sentence[:\s]+(.*?)(?:\n\n|\n##|$)',
        r'재작성[:\s]+(.*?)(?:\n\n|\n##|$)',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, response_text, re.DOTALL | re.IGNORECASE)
        if match:
            clause = match.group(1).strip()
            # 마크다운 포맷팅 제거
            clause = re.sub(r'\*\*([^*]+)\*\*', r'\1', clause)
            clause = re.sub(r'`([^`]+)`', r'\1', clause)
            if clause:
                return clause
    
    # 전체 응답 반환 (추출 실패 시)
    return response_text.strip()


def generate_prediction_for_item(
    test_item: Dict,
    use_utils_v2: bool = True,
    use_context_v2: bool = True,
    temperature: float = 0.0
) -> Dict:
    """
    단일 test_data 항목에 대해 LLM 예측 생성
    
    Args:
        test_item: 테스트 데이터 항목
        use_v2: spa_prompt_utils_v2 사용 여부
        temperature: LLM temperature
    
    Returns:
        예측 결과 딕셔너리
    """
    input_clause = test_item.get("input", "")
    target_score = test_item.get("target_score", 0.0)
    spa_term = test_item.get("spa_term", "")
    
    # 프롬프트 생성
    if use_utils_v2:
        from spa_prompt_utils_v2 import create_enhanced_prompt as create_enhanced_prompt_v2
        create_prompt_func = create_enhanced_prompt_v2
    else:
        create_prompt_func = create_enhanced_prompt
    
    # 목표 성향 결정 (점수 기반)
    if target_score <= 1.0:
        target_orientation = "buyer"  # 매수인 친화
    elif target_score >= 3.0:
        target_orientation = "seller"  # 매도인 친화
    else:
        target_orientation = "buyer"  # 기본값
    
    user_message = f"요청 사항: 다음 조항을 {target_score}점 목표로 변환해주세요.\n\n검토 대상: {input_clause}"
    
    selected_options = [spa_term] if spa_term else []
    selected_tasks = ["매수인 ↔ 매도인 전환"]
    task_params = {
        "style_target_orientation": target_orientation,
        "style_k": 2
    }
    
    enhanced_prompt = create_prompt_func(
        user_message,
        selected_options,
        selected_tasks,
        task_params,
        use_context_v2=use_context_v2
    )
    
    # LLM 호출 (구조화된 출력 사용)
    # streamlit_app.py와 server_langgraph.py의 로직을 반영:
    # - streamlit_app.py: 백엔드 API → JSON 문자열 → json.loads() → 딕셔너리
    # - server_langgraph.py: 구조화된 LLM → Pydantic 모델 → model_dump() → 딕셔너리
    # - generate_predictions_local.py: OpenAI API → Pydantic 모델 → model_dump() → 딕셔너리
    try:
        # server_langgraph.py와 동일한 방식으로 구조화된 출력 스키마 결정
        # streamlit_app.py에서는 백엔드 API가 이 로직을 수행
        output_schema = determine_output_schema(selected_tasks)
        
        if output_schema:
            # 구조화된 출력 사용 (server_langgraph.py의 get_structured_llm과 동일)
            llm = get_structured_llm(temperature=temperature, output_schema=output_schema)
            
            # server_langgraph.py와 동일한 메시지 구성 방식
            # streamlit_app.py에서는 백엔드가 이 메시지 구성을 수행
            system_message = SystemMessage(content="당신은 M&A 주식매매계약(SPA) 전문 변호사입니다.")
            user_message = HumanMessage(content=enhanced_prompt)
            messages_to_send = [system_message, user_message]
            
            # 동기 호출 (streamlit_app.py는 백엔드 API를 통해 비동기 호출)
            structured_output = llm.invoke(messages_to_send)
            
            # 구조화된 출력을 딕셔너리로 변환
            # streamlit_app.py: structured_data = json.loads(full_text) (백엔드에서 JSON 문자열로 받음)
            # server_langgraph.py: output_dict = structured_output.model_dump() (동일)
            # generate_predictions_local.py: 직접 Pydantic 모델을 받으므로 model_dump() 사용
            output_dict = structured_output.model_dump() if hasattr(structured_output, 'model_dump') else dict(structured_output)
            
            # 구조화된 출력에서 추출
            # streamlit_app.py의 format_structured_output() 함수와 동일한 필드 사용:
            # - "converted_sentence": 변환된 조항
            # - "analysis": 분석 텍스트
            converted_sentence = output_dict.get("converted_sentence", "")
            response_text = output_dict.get("analysis", "")
            
            # 점수는 분석 텍스트에서 추출 시도, 실패 시 목표 점수 사용
            score = extract_score_from_response(response_text)
            if score is None:
                score = target_score
            
            return {
                "converted_sentence": converted_sentence,
                "score": float(score),
                "raw_response": response_text,  # 디버깅용
                "metadata": {
                    "spa_term": spa_term,
                    "target_score": target_score,
                    "model": OPENAI_MODEL,
                    "temperature": temperature,
                    "structured_output": True,
                    "output_schema": output_schema.__name__ if output_schema else None,
                    "api_type": "openai"
                }
            }
        else:
            # 구조화된 출력 스키마를 찾지 못한 경우 일반 호출
            llm = get_llm(temperature=temperature)
            messages = [
                SystemMessage(content="당신은 M&A 주식매매계약(SPA) 전문 변호사입니다."),
                HumanMessage(content=enhanced_prompt)
            ]
            
            response = llm.invoke(messages)
            response_text = response.content if hasattr(response, 'content') else str(response)
            
            # 일반 응답에서 추출
            converted_sentence = extract_clause_from_response(response_text)
            score = extract_score_from_response(response_text)
            if score is None:
                score = target_score
            
            return {
                "converted_sentence": converted_sentence,
                "score": float(score),
                "raw_response": response_text,
                "metadata": {
                    "spa_term": spa_term,
                    "target_score": target_score,
                    "model": OPENAI_MODEL,
                    "temperature": temperature,
                    "structured_output": False,
                    "api_type": "openai"
                }
            }
    except Exception as e:
        print(f"⚠️ 오류 발생 (항목: {spa_term}, 점수: {target_score}): {e}")
        return {
            "converted_sentence": f"[오류: {str(e)}]",
            "score": target_score,
            "raw_response": "",
            "metadata": {
                "error": str(e),
                "spa_term": spa_term,
                "target_score": target_score,
                "api_type": "openai"
            }
        }


def generate_predictions(
    test_data_path: str,
    output_path: str,
    use_utils_v2: bool = True,
    use_context_v2: bool = True,
    temperature: float = 0.0,
    batch_size: int = 1
) -> List[Dict]:
    """
    test_data의 모든 항목에 대해 예측 생성
    
    Args:
        test_data_path: 테스트 데이터 파일 경로
        output_path: 예측 결과 저장 경로
        use_v2: spa_prompt_utils_v2 사용 여부
        temperature: LLM temperature
        batch_size: 배치 크기 (현재는 1만 지원)
    
    Returns:
        예측 결과 리스트
    """
    # 테스트 데이터 로드
    print(f"📂 테스트 데이터 로드: {test_data_path}")
    test_data = load_test_data(test_data_path)
    print(f"   총 {len(test_data)}개 항목")
    
    predictions = []
    start_time = time.time()
    
    print(f"\n🚀 예측 생성 시작 (모델: {OPENAI_MODEL}, API: OpenAI)")
    print(f"   Utils 버전: {'v2' if use_utils_v2 else 'v1'}")
    print(f"   Context 버전: {'v2' if use_context_v2 else 'v1'}")
    print(f"   Temperature: {temperature}")
    print("-" * 60)
    
    for i, item in enumerate(test_data, 1):
        spa_term = item.get("spa_term", "N/A")
        target_score = item.get("target_score", 0.0)
        
        print(f"[{i}/{len(test_data)}] {spa_term} - {target_score}점 목표...", end=" ", flush=True)
        
        pred = generate_prediction_for_item(item, use_utils_v2=use_utils_v2, use_context_v2=use_context_v2, temperature=temperature)
        predictions.append(pred)
        
        elapsed = time.time() - start_time
        avg_time = elapsed / i
        remaining = avg_time * (len(test_data) - i)
        
        print(f"✅ 완료 (예상 남은 시간: {remaining/60:.1f}분)")
        
        # 중간 저장 (매 5개마다)
        if i % 5 == 0:
            temp_output = output_path.replace('.json', f'_temp_{i}.json')
            with open(temp_output, 'w', encoding='utf-8') as f:
                json.dump(predictions, f, ensure_ascii=False, indent=2)
            print(f"   💾 중간 저장: {temp_output}")
    
    # 최종 저장
    output_data = {
        "version": "1.0",
        "created_at": datetime.now().isoformat(),
        "model": OPENAI_MODEL,
        "api_type": "openai",
        "utils_version": "v2" if use_utils_v2 else "v1",
        "context_version": "v2" if use_context_v2 else "v1",
        "temperature": temperature,
        "total_samples": len(predictions),
        "predictions": predictions
    }
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)
    
    total_time = time.time() - start_time
    print("\n" + "=" * 60)
    print(f"✅ 예측 생성 완료!")
    print(f"   총 소요 시간: {total_time/60:.1f}분")
    print(f"   평균 시간/항목: {total_time/len(test_data):.1f}초")
    print(f"   저장 위치: {output_path}")
    print("=" * 60)
    
    return predictions


def main():
    """메인 실행 함수"""
    import argparse
    
    parser = argparse.ArgumentParser(description='OpenAI API를 사용한 Style Transfer 예측 생성 (로컬 테스트용)')
    parser.add_argument('--test_data', type=str, required=True,
                       help='테스트 데이터 JSON 파일 경로')
    parser.add_argument('--output', type=str, default=None,
                       help='예측 결과 저장 경로 (기본값: predictions_local_<timestamp>.json)')
    parser.add_argument('--use_utils_v1', action='store_true',
                       help='spa_prompt_utils.py 사용 (기본값: v2)')
    parser.add_argument('--use_context_v1', action='store_true',
                       help='spa_term_context.py 사용 (기본값: v2)')
    parser.add_argument('--temperature', type=float, default=0.0,
                       help='LLM temperature (기본값: 0.0)')
    parser.add_argument('--model', type=str, default=None,
                       help='OpenAI 모델명 (기본값: .env의 OPENAI_MODEL 또는 gpt-4o)')
    
    args = parser.parse_args()
    
    # 모델 설정 (명령줄 인자가 우선)
    global OPENAI_MODEL
    if args.model:
        OPENAI_MODEL = args.model
    
    # 출력 경로 결정
    if args.output is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        utils_ver = "v1" if args.use_utils_v1 else "v2"
        context_ver = "v1" if args.use_context_v1 else "v2"
        args.output = f"predictions_local_utils{utils_ver}_ctx{context_ver}_{timestamp}.json"
    
    # 버전 결정 (기본값: 둘 다 v2)
    use_utils_v2 = not args.use_utils_v1
    use_context_v2 = not args.use_context_v1
    
    # API 키 확인
    if not OPENAI_API_KEY:
        print("❌ 오류: OPENAI_API_KEY 환경 변수가 설정되지 않았습니다.")
        print("   .env 파일에 다음을 추가하세요:")
        print("   OPENAI_API_KEY=your_api_key_here")
        print("   OPENAI_MODEL=gpt-4o-mini  # 선택사항")
        return
    
    # 예측 생성
    try:
        generate_predictions(
            test_data_path=args.test_data,
            output_path=args.output,
            use_utils_v2=use_utils_v2,
            use_context_v2=use_context_v2,
            temperature=args.temperature
        )
    except Exception as e:
        print(f"❌ 오류 발생: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()

