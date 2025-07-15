import os
from fastapi import FastAPI
from pydantic import BaseModel
import httpx
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()
class ChatRequest(BaseModel):
    message: str
    
GROQ_URL = os.getenv("GROQ_API_URL")
GROQ_KEY = os.getenv("GROQ_API_KEY")
@app.post("/chat-groq")
async def chat_endpoint(data: ChatRequest):
    payload = {
        "model": "llama3-8b-8192",
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are an FAQ bot for XYZ Company. Answer only based on these:\n"
                    "- Name: Personalisable chatbot.\n"
                    "- Return policy: 30 days.\n"
                    "- Order tracking: Use orders page.\n"
                    "- International shipping: Yes.\n"
                    "If not part of the FAQs, reply: 'Sorry, I can only help with listed FAQs.'"
                )
            },
            {
                "role": "user",
                "content": data
            }
        ]
    }

    headers = {
        "Authorization": GROQ_KEY,
        "Content-Type": "application/json"
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(GROQ_URL, json=payload, headers=headers)
        response.raise_for_status()
        result = response.json()
    
    return {"response": result["choices"][0]["message"]["content"]}
