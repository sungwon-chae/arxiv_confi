import os
import json
import asyncio
from typing import List, Optional, AsyncGenerator

import httpx
from fastapi import FastAPI, Response, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse, JSONResponse
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

LLM_API_BASE = "http://10.10.190.10:8124"
LLM_API_KEY = "token-abc123"
LLM_MODEL = "/data/models/Qwen3-Next-80B-A3B-Instruct"

# CORS
ALLOWED_ORIGINS = [o.strip() for o in os.getenv("ALLOWED_ORIGINS", "http://localhost:8501").split(",") if o.strip()]

app = FastAPI(title="Chatbot Backend", version="1.0")

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

class ChatRequest(BaseModel):
    messages: List[ChatMessage]
    temperature: Optional[float] = 0.7
    max_tokens: Optional[int] = 32768
    stream: Optional[bool] = False

class ChatResponse(BaseModel):
    content: str
    model: str
    usage: Optional[dict] = None

def _auth_headers():
    headers = {"Content-Type": "application/json"}
    if LLM_API_KEY and LLM_API_KEY.lower() not in ["none", "empty"]:
        headers["Authorization"] = f"Bearer {LLM_API_KEY}"
    return headers

@app.get("/health")
async def health():
    return {"ok": True, "model": LLM_MODEL}

@app.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    """
    비-스트리밍 응답 (간단/안정)
    """
    payload = {
        "model": LLM_MODEL,
        "messages": [m.model_dump() for m in req.messages],
        "temperature": req.temperature,
        "max_tokens": req.max_tokens,
        "stream": False,
    }

    async with httpx.AsyncClient(timeout=httpx.Timeout(60.0)) as client:
        r = await client.post(
            f"{LLM_API_BASE.rstrip('/')}/v1/chat/completions",
            headers=_auth_headers(),
            json=payload,
        )
        if r.status_code != 200:
            return JSONResponse(
                status_code=r.status_code,
                content={"error": r.text},
            )
        data = r.json()
        content = data["choices"][0]["message"]["content"]
        usage = data.get("usage", None)
        return ChatResponse(content=content, model=LLM_MODEL, usage=usage)

@app.post("/chat/stream")
async def chat_stream(req: ChatRequest):
    """
    토큰 스트리밍 (SSE 스타일) 엔드포인트
    - 프론트에서 'text/event-stream'을 읽어가며 실시간 표시 가능
    """

    async def sse_gen() -> AsyncGenerator[bytes, None]:
        payload = {
            "model": LLM_MODEL,
            "messages": [m.model_dump() for m in req.messages],
            "temperature": req.temperature,
            "max_tokens": req.max_tokens,
            "stream": True,
        }
        async with httpx.AsyncClient(timeout=None) as client:
            async with client.stream(
                "POST",
                f"{LLM_API_BASE.rstrip('/')}/v1/chat/completions",
                headers=_auth_headers(),
                json=payload,
            ) as r:
                if r.status_code != 200:
                    # 에러를 SSE로 보냄
                    err = await r.aread()
                    yield f"event: error\ndata: {err.decode('utf-8')}\n\n".encode("utf-8")
                    return

                async for line in r.aiter_lines():
                    if not line:
                        continue
                    # OpenAI 호환 스트림은 "data: {...}" 형태
                    if line.startswith("data: "):
                        data_str = line[len("data: "):]
                        if data_str.strip() == "[DONE]":
                            yield b"data: [DONE]\n\n"
                            break
                        # 그대로 프록시 (프론트에서 json 파싱)
                        yield f"data: {data_str}\n\n".encode("utf-8")
                    # heartbeat 등은 무시

    return StreamingResponse(sse_gen(), media_type="text/event-stream")
