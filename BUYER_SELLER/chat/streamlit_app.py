import os
import json
import time
import logging
import requests
import streamlit as st
# spa_prompt_utils에서 함수 임포트
from spa_prompt_utils import create_enhanced_prompt, get_available_spa_options
import re


# 로깅 설정
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)



def _split_think_blocks(text: str):
    if not text:
        return text, []
    think_blocks = re.findall(r"<think>([\s\S]*?)</think>", text, flags=re.DOTALL)
    visible = re.sub(r"<think>[\s\S]*?</think>", " _(thinking done)_ ", text, flags=re.DOTALL)
    return visible, think_blocks

def format_structured_output(data: dict) -> str:
    """구조화된 출력을 포맷팅된 마크다운 문자열로 변환"""
    if not isinstance(data, dict):
        return str(data)
    
    output_parts = []
    
    # 분석 필드가 있으면 표시
    if "analysis" in data:
        output_parts.append(f"## 📊 분석\n\n{data['analysis']}\n")
    
    # 점수 필드가 있으면 표시 (매수인/매도인 친화 판단)
    if "score" in data:
        score = data["score"]
        score_desc = "매수인 친화" if score <= 1.0 else "중립" if score <= 3.0 else "매도인 친화"
        output_parts.append(f"## 📈 점수\n\n**{score:.1f}점** ({score_desc})\n")
    
    # 변환된 문장 필드가 있으면 표시 (전환, Tone Up-Down)
    if "converted_sentence" in data:
        output_parts.append(f"## ✨ 변환된 조항\n\n```\n{data['converted_sentence']}\n```\n")
    
    return "\n".join(output_parts) if output_parts else json.dumps(data, ensure_ascii=False, indent=2)

# 백엔드 URL 설정 (환경 변수 또는 기본값)
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8001")
LLM_API_BASE= os.getenv("LLM_API_BASE", "http://10.10.190.10:8124")
LLM_API_KEY = os.getenv("LLM_API_KEY", "token-abc123")
LLM_MODEL = os.getenv("LLM_MODEL", "/data/models/Qwen3-Next-80B-A3B-Instruct")

USE_STREAM = True  # vLLM 서버는 스트리밍을 잘 지원하므로 True로 설정

logger.info(f"Streamlit 앱 시작 - BACKEND_URL: {BACKEND_URL}")
logger.info(f"Streamlit 앱 시작 - LLM_API_BASE: {LLM_API_BASE}")
logger.info(f"Streamlit 앱 시작 - LLM_API_KEY: {LLM_API_KEY}")
logger.info(f"Streamlit 앱 시작 - LLM_MODEL: {LLM_MODEL}")
# 백엔드 연결 확인 함수
def check_backend_health():
    """백엔드 서버 상태 확인"""
    try:
        health_url = f"{BACKEND_URL.rstrip('/')}/health"
        logger.debug(f"백엔드 헬스 체크: {health_url}")
        response = requests.get(health_url, timeout=5)
        if response.status_code == 200:
            logger.info(f"✅ 백엔드 서버 연결 성공: {response.json()}")
            return True
        else:
            logger.warning(f"⚠️ 백엔드 서버 응답 이상: {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        logger.error(f"❌ 백엔드 서버 연결 실패: {e}")
        return False

# --- 페이지 설정 ---
st.set_page_config(page_title="M&A Buyer-Seller Transfer", page_icon="⚖️", layout="centered")
st.title("⚖️ M&A SPA Buyer-Seller Transfer")

# --- 사이드바: 분석 항목 선택 ---
# 체크박스 옵션들을 동적으로 생성
available_options = get_available_spa_options()
# '기타' 옵션이 있다면 맨 뒤로 보냄
if "기타" in available_options:
    available_options.remove("기타")
    available_options.append("기타")

checkbox_options = {option: option for option in available_options}

with st.sidebar:
    # 백엔드 상태 표시
    st.header("🔌 서버 상태")
    backend_status = check_backend_health()
    if backend_status:
        st.success(f"✅ 백엔드 연결됨: {BACKEND_URL}")
    else:
        st.error(f"❌ 백엔드 연결 실패: {BACKEND_URL}")
        st.warning("백엔드 서버가 실행 중인지 확인하세요.")
    
    st.divider()
    
    st.header("📋 분석 항목 선택")
    st.write("분석하고 싶은 항목을 선택하세요:")
    
    selected_options = []
    for key, label in checkbox_options.items():
        if st.checkbox(label, key=f"checkbox_{key}"):
            selected_options.append(label)
    
    st.divider()
    st.write(f"선택된 항목: {len(selected_options)}개")
    if selected_options:
        for option in selected_options:
            st.write(f"• {option}")
            
    # --- (수정) 작업 유형 선택 UI (Multi-select로 변경) ---
    st.divider()
    st.header("⚙️ 작업 유형 선택")
    
    # 작업 목록 정의 (spa_prompt_utils.py와 일치)
    task_options = [
        "매수인/매도인 친화 판단", 
        "매수인 ↔ 매도인 전환", 
        "Tone Up-Down"
    ]
    
    selected_tasks = st.multiselect( # st.radio -> st.multiselect
        "수행할 작업을 선택하세요 (다중 선택 가능):",
        task_options,
        key="selected_tasks" # selected_task -> selected_tasks
    )

    # --- (신규) 작업별 파라미터 입력 UI ---
    task_params = {}

    if "매수인 ↔ 매도인 전환" in selected_tasks:
        st.subheader("🔁 Style Transfer 설정")
        style_direction = st.radio(
            "전환 방향을 선택하세요:",
            ["매수인 친화 → 매도인 친화", "매도인 친화 → 매수인 친화"],
            horizontal=False,
            key="style_transfer_direction"
        )
        # 내부 파라미터로 목표 성향을 저장
        if style_direction.startswith("매수인"):
            task_params["style_target_orientation"] = "seller"  # 매도인 친화 목표
        else:
            task_params["style_target_orientation"] = "buyer"   # 매수인 친화 목표
        # 샘플 개수는 고정 (인접 점수 2개)
        task_params["style_k"] = 2

    if "Tone Up-Down" in selected_tasks:
        st.subheader("📈📉 Tone Up/Down 설정")
        # 목표 점수 슬라이더만 유지
        tone_target_score = st.slider(
            "목표 점수 (0.0 = 매수인 친화 ~ 4.0 = 매도인 친화)",
            0.0, 4.0, 3.0, 0.5,
            key="tone_target_score"
        )
        task_params["tone_target_score"] = float(tone_target_score)
        task_params["tone_k"] = 2

# --- 채팅 세션 초기화 ---
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "당신은 M&A 주식매매계약(SPA) 전문 변호사입니다. 사용자의 질문을 분석하고, 제공되는 M&A 협상 쟁점과 참고 조항을 바탕으로 전문가 수준의 법률 자문과 실용적인 조언을 제공합니다."}
    ]

# --- 기존 대화 렌더링 ---
for m in st.session_state.messages:
    if m["role"] == "system":
        continue
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

# --- 사용자 입력 섹션 (레이블 수정) ---
st.subheader("💬 질문 입력")

# 두 개의 입력 필드
col1, col2 = st.columns([1, 1])

with col1:
    user_query = st.text_area(
        "1. 요청 사항", 
        placeholder="예: 조항 검토, 매수인/매도인 친화도 분석, 조항 수정 등",
        height=100,
        key="user_query"
    )

with col2:
    user_input = st.text_area(
        "2. 검토 대상 조항 (필요 시)", 
        placeholder="예: '매도인이 알고 있는 한'이라 함은 매도인의 등기 임원이 실제로 알고 있는 것을 의미한다.",
        height=100,
        key="user_input"
    )

# 전송 버튼
submit_button = st.button("🚀 질문 전송", type="primary", use_container_width=True)

# 입력값이 있을 때만 처리
if submit_button and (user_query.strip() or user_input.strip()):
    # 두 입력을 결합하여 프롬프트 생성
    if user_query.strip() and user_input.strip():
        prompt = f"요청 사항: {user_query.strip()}\n\n검토 대상: {user_input.strip()}"
    elif user_query.strip():
        prompt = user_query.strip()
    else:
        # 검토 대상만 입력된 경우, 요청 사항을 '조항 분석'으로 간주
        prompt = f"요청 사항: 다음 조항을 분석해주세요.\n\n검토 대상: {user_input.strip()}"
else:
    prompt = None

# --- 백엔드 통신 함수 ---

def call_backend_non_stream(messages):
    """
    /chat (Non-Stream)으로 요청 전송
    """
    url = f"{BACKEND_URL.rstrip('/')}/chat"
    
    
    try:
        r = requests.post(url, json={"messages": messages}, timeout=60)
        
        r.raise_for_status()
        response_data = r.json()
        
        return response_data["content"]
    except requests.exceptions.Timeout as e:
        st.error(f"백엔드 호출 타임아웃: {e}")
        return None
    except requests.exceptions.ConnectionError as e:
        st.error(f"백엔드 서버에 연결할 수 없습니다: {e}")
        return None
    except requests.exceptions.RequestException as e:
        st.error(f"백엔드 호출 중 오류 발생: {e}")
        return None
    except Exception as e:
        st.error(f"예상치 못한 오류 발생: {e}")
        return None

def call_backend_stream(messages, selected_tasks=None):
    """
    /chat/stream (SSE)로 토큰 스트리밍 수신
    """
    url = f"{BACKEND_URL.rstrip('/')}/chat"
    
    payload = {"messages": messages}
    if selected_tasks:
        payload["selected_tasks"] = selected_tasks
    
    try:
        with requests.post(url, json=payload, stream=True, timeout=180) as r:
            r.raise_for_status()
            
            full_text = ""
            chunk_count = 0
            is_structured = False
            
            for raw in r.iter_lines(decode_unicode=True):
                if not raw:
                    continue
                if raw.startswith("data: "):
                    payload = raw[len("data: "):]
                    if payload.strip() == "[DONE]":
                        break
                    try:
                        data = json.loads(payload)
                        
                        # 메타데이터 확인
                        if "metadata" in data:
                            is_structured = data["metadata"].get("structured", False)
                            continue
                        
                        # OpenAI 호환: choices[0].delta.content 에 토큰 누적
                        delta = data["choices"][0].get("delta", {}).get("content", "")
                        if delta:
                            chunk_count += 1
                            full_text += delta
                            
                            # 구조화된 출력이 아닌 경우에만 스트리밍 표시
                            if not is_structured:
                                # 스트림 중간에는 think 블록을 숨긴 가시 텍스트만 반환
                                visible_partial, _ = _split_think_blocks(full_text)
                                yield visible_partial
                    except json.JSONDecodeError as e:
                        # 가끔 payload가 완전한 JSON이 아닐 수 있음
                        pass
                    except KeyError as e:
                        pass
                    except Exception as e:
                        pass
            
            # 구조화된 출력인 경우 JSON 파싱 및 포맷팅
            if is_structured and full_text:
                try:
                    # JSON 문자열을 파싱
                    structured_data = json.loads(full_text)
                    # 구조화된 데이터를 포맷팅된 문자열로 변환
                    formatted_output = format_structured_output(structured_data)
                    yield formatted_output
                except json.JSONDecodeError:
                    # JSON 파싱 실패 시 원본 반환
                    yield full_text
            else:
                # 마지막으로 전체 텍스트(원문) 반환 보장
                yield full_text
            
    except requests.exceptions.Timeout as e:
        st.error(f"백엔드 스트리밍 타임아웃: {e}")
        yield None
    except requests.exceptions.ConnectionError as e:
        st.error(f"백엔드 서버에 연결할 수 없습니다: {e}")
        yield None
    except requests.exceptions.RequestException as e:
        st.error(f"백엔드 스트리밍 중 오류 발생: {e}")
        yield None
    except Exception as e:
        st.error(f"알 수 없는 스트림 오류: {e}")
        yield None


# --- 메인 로직: 프롬프트 처리 ---
if prompt:
    # (수정) 선택된 체크박스와 *다중 작업* 및 작업 파라미터에 따라 프롬프트 강화
    try:
        enhanced_prompt = create_enhanced_prompt(prompt, selected_options, selected_tasks, task_params if 'task_params' in locals() else None)
    except Exception as e:
        st.error(f"프롬프트 처리 중 오류 발생: {e}")
        enhanced_prompt = prompt  # 원본 사용 
    
    # 유저 메시지 추가 & 표시 (원본 메시지 표시)
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
        
        # 선택된 항목이 있으면 표시
        if selected_options:
            st.info(f"🔍 분석 중점: {', '.join(selected_options)}")
        
        # (수정) 선택된 작업 유형 표시 (리스트 처리)
        if selected_tasks:
            st.info(f"⚙️ 작업 유형: {', '.join(selected_tasks)}")
            # (신규) 작업 파라미터 요약 표시
            if 'task_params' in locals() and task_params:
                pretty_params = []
                if task_params.get("style_target_orientation"):
                    pretty_params.append(f"Style 목표: {'매도인 친화' if task_params['style_target_orientation']=='seller' else '매수인 친화'} (인접 점수 샘플)")
                if task_params.get("tone_target_score") is not None:
                    pretty_params.append(f"Tone 목표: {task_params['tone_target_score']}점")
                if pretty_params:
                    st.info(", ".join(pretty_params))
        else:
            st.info("⚙️ 작업 유형: 조항 분석 (Default)") # 작업 미선택 시 기본값 표시


    # 어시스턴트 자리 마련
    with st.chat_message("assistant"):
        # 강화된 프롬프트로 메시지 생성
        # (주의: enhanced_messages는 실제 API 호출에만 사용, 세션에는 원본 prompt가 저장됨)
        enhanced_messages = []
        
        # 시스템 프롬프트 찾기
        system_prompt = next((m for m in st.session_state.messages if m["role"] == "system"), None)
        if system_prompt:
            enhanced_messages.append(system_prompt)
            
        # (참고: 현재 로직은 이전 대화 맥락 없이, 항상 현재 요청만으로 프롬프트를 구성함)
        
        # 현재의 강화된 사용자 프롬프트 추가
        enhanced_messages.append({"role": "user", "content": enhanced_prompt})
        
        
        assistant_text = ""
        think_blocks_final = []
        if USE_STREAM:
            # 상단 고정 컨테이너 (expander 전용)
            debug_top = st.container()
            placeholder = st.empty()
            acc_text = ""
            try:
                for partial in call_backend_stream(enhanced_messages, selected_tasks):
                    if partial is None: # 스트림 오류 시
                        assistant_text = "오류가 발생했습니다."
                        placeholder.error(assistant_text)
                        break
                    
                    acc_text = partial
                    placeholder.markdown(acc_text + "▌") # 커서 효과
                
                # 최종 원문 재가공: think 블록 숨김 + expander (위쪽 컨테이너)에 표시
                visible_final, think_blocks_final = _split_think_blocks(acc_text)
                assistant_text = visible_final

                # 중복 방지: 동일한 think 내용이면 재표시하지 않음
                think_key = "\n\n".join(tb.strip() for tb in think_blocks_final) if think_blocks_final else ""
                if think_blocks_final:
                    if st.session_state.get("__last_think_key__") != think_key:
                        with debug_top.expander("🧠 내부 추론 과정 (think block)"):
                            for idx, tb in enumerate(think_blocks_final, 1):
                                st.code(tb.strip() or "(empty)")
                        st.session_state["__last_think_key__"] = think_key
                
                # 그 다음 최종본(think 숨김) 표시
                placeholder.markdown(assistant_text)
            except Exception as e:
                assistant_text = f"스트림 처리 중 예외 발생: {e}"
                placeholder.error(assistant_text)
        else:
            with st.spinner("생각 중..."):
                assistant_text_result = call_backend_non_stream(enhanced_messages)
                if assistant_text_result is None:
                    assistant_text = "오류가 발생했습니다."
                    st.error(assistant_text)
                else:
                    # 상단 고정 컨테이너 (expander 전용)
                    debug_top = st.container()
                    # think 블록 숨김 처리 및 expander 제공
                    visible_final, think_blocks_final = _split_think_blocks(assistant_text_result)
                    assistant_text = visible_final
                    
                    # 중복 방지: 동일한 think 내용이면 재표시하지 않음
                    think_key = "\n\n".join(tb.strip() for tb in think_blocks_final) if think_blocks_final else ""
                    if think_blocks_final:
                        if st.session_state.get("__last_think_key__") != think_key:
                            with debug_top.expander("🧠 내부 추론 과정 (think block)"):
                                for idx, tb in enumerate(think_blocks_final, 1):
                                    st.code(tb.strip() or "(empty)")
                            st.session_state["__last_think_key__"] = think_key

                    # 그 다음 본문 표시
                    st.markdown(assistant_text)

    # 대화 상태 업데이트 (오류가 아닐 때만)
    if assistant_text and "오류" not in assistant_text:
        st.session_state.messages.append({"role": "assistant", "content": assistant_text})
    
    # (디버깅용) 강화된 프롬프트 내용 확인
    with st.expander("🔍 전송된 강화 프롬프트 보기 (디버깅용)"):
       st.text(enhanced_prompt)
