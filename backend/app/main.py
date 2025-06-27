# from fastapi import FastAPI, Request
# from fastapi.middleware.cors import CORSMiddleware
# import requests

# app = FastAPI()

# # Enable CORS to allow frontend (on localhost:3000) to call backend (on 8000)
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# faq_context = (
#     "You are an FAQ bot for XYZ Company. Only answer questions "
#     "based on the following FAQs:\n"
#     "- What is the return policy? Answer: You can return items within 30 days.\n"
#     "- How do I track my order? Answer: Visit the orders page and enter your ID.\n"
#     "- Do you ship internationally? Answer: Yes, we ship worldwide.\n"
#     "If a question is not part of the FAQs, respond with: 'Sorry, I can only help with listed FAQs.'"
# )

# @app.post("/chat")
# async def chat(request: Request):
#     data = await request.json()
#     user_message = data.get("message", "")

#     payload = {
#         "model": "llama3",
#         "messages": [
#             {"role": "system", "content": "You are an expert code assistant."},
#             {"role": "user", "content": user_message}
#         ],
#         "stream": False  # make sure stream is false for simple response
#     }

#     try:
#         res = requests.post(
#             "http://host.docker.internal:11434/api/chat",  # docker-to-host communication
#             headers={"Content-Type": "application/json"},
#             json=payload
#         )
#         res.raise_for_status()
#         reply = res.json()["message"]["content"]
#         return {"response": reply}
#     except Exception as e:
#         return {"error": str(e)}

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router as chat_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router, prefix="/api")
