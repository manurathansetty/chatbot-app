from fastapi import APIRouter, Request
from app.services.chat_service import get_ai_response
from app.services.chat_service_open_source import chat_endpoint
from app.services.talkToMyResume import genAiChat

router = APIRouter()

@router.post("/chat")
async def chat(request: Request):
    data = await request.json()
    message = data.get("message", "")
    return await get_ai_response(message)

@router.post("/chat-groq")
async def chatAi(request: Request):
    data = await request.json()
    message = data.get("message", "")
    return await chat_endpoint(message)

@router.post("/talkToMyResume")
async def chatGem(request:Request);
    data = await request.json()
    message = data.get("message", "")
    return await genAiChat(message)