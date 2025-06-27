from fastapi import APIRouter, Request
from app.services.chat_service import get_ai_response

router = APIRouter()

@router.post("/chat")
async def chat(request: Request):
    data = await request.json()
    message = data.get("message", "")
    return await get_ai_response(message)
