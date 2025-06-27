from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

# Enable CORS so frontend (localhost:3000) can talk to it
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_message = data.get("message", "")

    payload = {
        "model": "deepseek-coder",
        "messages": [
            {"role": "system", "content": "You are an expert code assistant."},
            {"role": "user", "content": user_message}
        ]
    }

    try:
        res = requests.post("http://localhost:11434/api/chat", json=payload)
        res.raise_for_status()
        reply = res.json()["message"]["content"]
        return {"response": reply}
    except Exception as e:
        return {"error": str(e)}
