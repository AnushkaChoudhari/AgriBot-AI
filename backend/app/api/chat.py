from fastapi import APIRouter
from pydantic import BaseModel

from app.chatbot.rag import ask_agribot

router = APIRouter()


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    response: str


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    answer = ask_agribot(request.message)

    return ChatResponse(response=answer)