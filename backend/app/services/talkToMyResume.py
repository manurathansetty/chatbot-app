from google import genai
from google.genai import types
import base64

def genAiChat():
  client = genai.Client(
      vertexai=True,
      project="finance-project-468418",
      location="global",
  )


  model = "gemini-2.0-flash-001"
  contents = [
    types.Content(
      role="system",
      parts=[
        types.Part.from_text(text="""
                              - You are now a resume bot u only talk about the resume text i am going to give in the below prompts indexed by key(HERE) 
                              - You are to follow the above prompt strictly
                              key(HERE): 
                              {
                                resume holder name: manu
                              }
                            """)
      ]
    ),
    types.Content(
      role="user",
      parts=[
        types.Part.from_text(text="""What are you meant for?""")
      ]
    )
  ]

  generate_content_config = types.GenerateContentConfig(
    temperature = 1,
    top_p = 0.95,
    max_output_tokens = 8192,
    safety_settings = [types.SafetySetting(
      category="HARM_CATEGORY_HATE_SPEECH",
      threshold="OFF"
    ),types.SafetySetting(
      category="HARM_CATEGORY_DANGEROUS_CONTENT",
      threshold="OFF"
    ),types.SafetySetting(
      category="HARM_CATEGORY_SEXUALLY_EXPLICIT",
      threshold="OFF"
    ),types.SafetySetting(
      category="HARM_CATEGORY_HARASSMENT",
      threshold="OFF"
    )],
  )

  for chunk in client.models.generate_content_stream(
    model = model,
    contents = contents,
    config = generate_content_config,
    ):
    print(chunk.text, end="")

genAiChat()