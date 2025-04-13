import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.studio.nebius.com/v1/",
    api_key=os.environ.get("NEBIUS_API_KEY")
)

response = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-R1",
    max_tokens=8192,
    temperature=0.6,
    top_p=0.95,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": """explain me about fibonacci series"""
                }
            ]
        }
    ]
)



print(response.choices[0].message.content)