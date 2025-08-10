from google import genai
from google.genai.types import GenerateContentConfig, HttpOptions

client = genai.Client(http_options=HttpOptions(api_version="v1"))
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Why is the sky blue?",
    config=GenerateContentConfig(
        system_instruction=[
            "You're a language translator.",
            "Your mission is to translate text in English to French.",
        ]
    ),
)
print(response.text)