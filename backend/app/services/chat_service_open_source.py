from fastapi import FastAPI
from pydantic import BaseModel
import httpx

app = FastAPI()

GROQ_API_KEY = "your_groq_api_key"  # Replace with your real one
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

class ChatRequest(BaseModel):
    message: str

@app.post("/chatOpenAi")
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
        "Authorization": "",
        "Content-Type": "application/json"
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(GROQ_API_URL, json=payload, headers=headers)
        response.raise_for_status()
        result = response.json()
    
    return {"response": result["choices"][0]["message"]["content"]}
