import requests

SYSTEM_PROMPT = (
    "You are an FAQ bot for XYZ Company. Answer only based on these:\n"
    "- Your name: Personalizable chat bot \n"
    "- Return policy: 30 days.\n"
    "- Order tracking: Use orders page.\n"
    "- International shipping: Yes.\n"
    "If not part of the FAQs, reply: 'Sorry, I can only help with listed FAQs.'"
)

async def get_ai_response(user_message: str) -> dict:
    payload = {
        "model": "llama3",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_message}
        ],
        "stream": False
    }

    try:
        res = requests.post("http://host.docker.internal:11434/api/chat", json=payload)
        res.raise_for_status()
        reply = res.json().get("message", {}).get("content", "")
        return {"response": reply}
    except Exception as e:
        return {"error": str(e)}
