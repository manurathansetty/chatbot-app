from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

# Enable CORS to allow frontend (on localhost:3000) to call backend (on 8000)
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
        "model": "deepseek-coder:6.7b",
        "messages": [
            {"role": "system", "content": "You are an expert code assistant."},
            {"role": "user", "content": user_message}
        ],
        "stream": False  # make sure stream is false for simple response
    }

    try:
        res = requests.post(
            "http://host.docker.internal:11434/api/chat",  # docker-to-host communication
            headers={"Content-Type": "application/json"},
            json=payload
        )
        res.raise_for_status()
        reply = res.json()["message"]["content"]
        return {"response": reply}
    except Exception as e:
        return {"error": str(e)}
