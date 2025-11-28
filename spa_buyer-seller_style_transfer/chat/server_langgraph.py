import os
import json
from typing import List, Optional, AsyncGenerator, TypedDict, Annotated, Union, Type
from operator import add

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse, JSONResponse
from pydantic import BaseModel, Field
from dotenv import load_dotenv

from langchain_core.messages import BaseMessage, HumanMessage, AIMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, END
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import MemorySaver

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))

LLM_API_BASE = os.getenv("LLM_API_BASE", "http://10.10.190.10:8124")
LLM_API_KEY = os.getenv("LLM_API_KEY", "token-abc123")
LLM_MODEL = os.getenv("LLM_MODEL", "/data/models/Qwen3-Next-80B-A3B-Instruct")
ALLOWED_ORIGINS = [o.strip() for o in os.getenv("ALLOWED_ORIGINS", "http://localhost:8501").split(",") if o.strip()]

app = FastAPI(title="Chatbot Backend (LangGraph)", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS or ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatMessage(BaseModel):
    role: str   # "system" | "user" | "assistant"
    content: str

# Task별 구조화된 출력 모델 정의
class BuyerSellerAnalysisOutput(BaseModel):
    """매수인/매도인 친화 판단 응답"""
    analysis: str = Field(description="조항에 대한 상세 분석")
    score: float = Field(description="매수인/매도인 친화도 점수 (0.0=매수인 친화 ~ 4.0=매도인 친화)", ge=0.0, le=4.0)

class StyleTransferOutput(BaseModel):
    """매수인 ↔ 매도인 전환 응답"""
    analysis: str = Field(description="전환 전 조항에 대한 분석")
    converted_sentence: str = Field(description="전환된 조항 문장")

class ToneUpDownOutput(BaseModel):
    """Tone Up-Down 응답"""
    analysis: str = Field(description="조항에 대한 분석 및 조정 방향")
    converted_sentence: str = Field(description="조정된 조항 문장")

class ChatRequest(BaseModel):
    messages: List[ChatMessage]
    temperature: Optional[float] = 0.7
    max_tokens: Optional[int] = 32768
    stream: Optional[bool] = False
    thread_id: Optional[str] = None
    selected_tasks: Optional[List[str]] = Field(default=None, description="선택된 작업 유형 목록") 

class ChatResponse(BaseModel):
    content: str
    model: str
    usage: Optional[dict] = None

class GraphState(TypedDict):
    messages: Annotated[List[BaseMessage], add_messages]

def get_llm(temperature: float = 0.7, max_tokens: int = 32768):
    """OpenAI 호환 API를 사용하는 ChatOpenAI 인스턴스 생성"""
    return ChatOpenAI(
        model=LLM_MODEL,
        base_url=LLM_API_BASE.rstrip('/') + "/v1",
        api_key=LLM_API_KEY if LLM_API_KEY and LLM_API_KEY.lower() not in ["none", "empty"] else None,
        temperature=temperature,
        max_tokens=max_tokens,
        timeout=60.0,
    )

def get_structured_llm(temperature: float = 0.7, max_tokens: int = 32768, output_schema=None):
    """구조화된 출력을 위한 LLM 인스턴스 생성"""
    llm = get_llm(temperature=temperature, max_tokens=max_tokens)
    if output_schema:
        return llm.with_structured_output(output_schema)
    return llm

def determine_output_schema(selected_tasks: Optional[List[str]]) -> Optional[Type[BaseModel]]:
    """선택된 작업에 따라 적절한 출력 스키마 반환"""
    if not selected_tasks:
        return None
    
    if "매수인/매도인 친화 판단" in selected_tasks:
        return BuyerSellerAnalysisOutput
    elif "매수인 ↔ 매도인 전환" in selected_tasks:
        return StyleTransferOutput
    elif "Tone Up-Down" in selected_tasks:
        return ToneUpDownOutput
    
    return None


def chatbot_node(state: GraphState):
    """LLM을 호출하여 응답 생성"""
    llm = get_llm()
    response = llm.invoke(state["messages"])
    return {"messages": [response]}

def create_chatbot_graph():
    """채팅봇 그래프 생성"""
    workflow = StateGraph(GraphState)

    workflow.add_node("chatbot", chatbot_node)
    

    workflow.set_entry_point("chatbot")
    workflow.add_edge("chatbot", END)
    

    memory = MemorySaver()
    

    return workflow.compile(checkpointer=memory)

graph = create_chatbot_graph()

def convert_messages(messages: List[ChatMessage]) -> List[BaseMessage]:
    """ChatMessage 리스트를 LangChain BaseMessage 리스트로 변환"""
    langchain_messages = []
    for msg in messages:
        if msg.role == "system":
            langchain_messages.append(SystemMessage(content=msg.content))
        elif msg.role == "user":
            langchain_messages.append(HumanMessage(content=msg.content))
        elif msg.role == "assistant":
            langchain_messages.append(AIMessage(content=msg.content))
    return langchain_messages

def extract_content_from_messages(messages: List[BaseMessage]) -> str:
    """BaseMessage 리스트에서 마지막 AI 응답 내용 추출"""
    for msg in reversed(messages):
        if isinstance(msg, AIMessage):
            return msg.content
    return ""

@app.get("/health")
async def health():
    return {"ok": True, "model": LLM_MODEL, "framework": "langgraph"}

# @app.post("/chat", response_model=ChatResponse)
# async def chat(req: ChatRequest):
#     """
#     비-스트리밍 응답 (LangGraph 사용)
#     """
#     try:
#         # 메시지 변환
#         langchain_messages = convert_messages(req.messages)
        
#         # 그래프 실행
#         config = {"configurable": {"thread_id": req.thread_id or "default"}}
#         result = await graph.ainvoke(
#             {"messages": langchain_messages},
#             config=config
#         )
        
#         # 응답 추출
#         content = extract_content_from_messages(result["messages"])
        
#         # Usage 정보는 LLM 응답에서 추출 (가능한 경우)
#         usage = None
#         if result["messages"]:
#             last_msg = result["messages"][-1]
#             if hasattr(last_msg, "response_metadata") and "token_usage" in last_msg.response_metadata:
#                 usage = last_msg.response_metadata["token_usage"]
        
#         print(content)
        
#         return ChatResponse(content=content, model=LLM_MODEL, usage=usage)
    
#     except Exception as e:
#         return JSONResponse(
#             status_code=500,
#             content={"error": str(e)},
#         )

@app.post("/chat/stream")
async def chat_stream(req: ChatRequest):
    """
    토큰 스트리밍 (SSE 스타일) 엔드포인트 (LangGraph 사용)
    """
    
    async def sse_gen() -> AsyncGenerator[bytes, None]:
        try:
            # 메시지 변환
            langchain_messages = convert_messages(req.messages)
            
            # 그래프 스트리밍 실행
            config = {"configurable": {"thread_id": req.thread_id or "default"}}
            
            # LangGraph의 astream_events를 사용하여 스트리밍
            async for event in graph.astream_events(
                {"messages": langchain_messages},
                config=config,
                version="v2"
            ):
                # LLM 토큰 스트림 이벤트 처리
                if event["event"] == "on_chat_model_stream":
                    chunk = event.get("data", {}).get("chunk")
                    if chunk and hasattr(chunk, "content"):
                        content = chunk.content
                        if content:
                            # OpenAI 호환 SSE 형식으로 변환
                            delta_data = {
                                "choices": [{
                                    "delta": {"content": content},
                                    "index": 0,
                                    "finish_reason": None
                                }]
                            }
                            yield f"data: {json.dumps(delta_data)}\n\n".encode("utf-8")
                
                # 완료 이벤트
                elif event["event"] == "on_chain_end" and event.get("name") == "chatbot":
                    # [DONE] 신호 전송
                    yield b"data: [DONE]\n\n"
                    break
            
        except Exception as e:
            # 에러를 SSE로 보냄
            error_data = {"error": str(e)}
            yield f"event: error\ndata: {json.dumps(error_data)}\n\n".encode("utf-8")
    
    return StreamingResponse(sse_gen(), media_type="text/event-stream")


@app.post("/chat")
async def chat_stream_simple(req: ChatRequest):
    """
    간단한 스트리밍 방식 (astream 사용)
    구조화된 출력 지원
    """
    
    async def sse_gen() -> AsyncGenerator[bytes, None]:
        try:
            langchain_messages = convert_messages(req.messages)
            
            # 출력 스키마 결정
            output_schema = determine_output_schema(req.selected_tasks)
            
            # LLM 설정
            if output_schema:
                # 구조화된 출력 사용
                llm = get_structured_llm(
                    temperature=req.temperature, 
                    max_tokens=req.max_tokens,
                    output_schema=output_schema
                )
                
                # 구조화된 출력은 스트리밍이 어려우므로 전체 응답 후 전송
                last_user_msg = None
                system_messages = []
                for msg in langchain_messages:
                    if isinstance(msg, SystemMessage):
                        system_messages.append(msg)
                    elif isinstance(msg, HumanMessage):
                        last_user_msg = msg
                
                if last_user_msg:
                    # 시스템 메시지와 함께 전달
                    messages_to_send = system_messages + [last_user_msg]
                    structured_output = await llm.ainvoke(messages_to_send)
                    
                    # 구조화된 출력을 JSON 문자열로 변환하여 전송
                    output_dict = structured_output.model_dump() if hasattr(structured_output, 'model_dump') else dict(structured_output)
                    output_json = json.dumps(output_dict, ensure_ascii=False)
                    
                    # JSON을 청크로 나누어 스트리밍처럼 보이게 (실제로는 한 번에 전송)
                    chunk_size = 3
                    for i in range(0, len(output_json), chunk_size):
                        chunk = output_json[i:i+chunk_size]
                        delta_data = {
                            "choices": [{
                                "delta": {"content": chunk},
                                "index": 0,
                                "finish_reason": None
                            }]
                        }
                        yield f"data: {json.dumps(delta_data, ensure_ascii=False)}\n\n".encode("utf-8")
            else:
                # 일반 스트리밍
                llm = get_llm(temperature=req.temperature, max_tokens=req.max_tokens)
                
                # 마지막 사용자 메시지만 전달
                last_user_msg = None
                for msg in reversed(langchain_messages):
                    if isinstance(msg, HumanMessage):
                        last_user_msg = msg
                        break
                
                if last_user_msg:
                    async for chunk in llm.astream([last_user_msg]):
                        if hasattr(chunk, "content") and chunk.content:
                            delta_data = {
                                "choices": [{
                                    "delta": {"content": chunk.content},
                                    "index": 0,
                                    "finish_reason": None
                                }]
                            }
                            yield f"data: {json.dumps(delta_data, ensure_ascii=False)}\n\n".encode("utf-8")
            
            # 구조화된 출력인 경우 메타데이터 추가
            if output_schema:
                metadata = {
                    "structured": True,
                    "schema_type": output_schema.__name__
                }
                yield f"data: {json.dumps({'metadata': metadata}, ensure_ascii=False)}\n\n".encode("utf-8")
            
            yield b"data: [DONE]\n\n"
            
        except Exception as e:
            error_data = {"error": str(e)}
            yield f"event: error\ndata: {json.dumps(error_data, ensure_ascii=False)}\n\n".encode("utf-8")
    
    return StreamingResponse(sse_gen(), media_type="text/event-stream")

