import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.studio.nebius.com/v1/",
    api_key="eyJhbGciOiJIUzI1NiIsImtpZCI6IlV6SXJWd1h0dnprLVRvdzlLZWstc0M1akptWXBvX1VaVkxUZlpnMDRlOFUiLCJ0eXAiOiJKV1QifQ.eyJzdWIiOiJnb29nbGUtb2F1dGgyfDExMzQ1NjgyNDU1OTM5NDE0MTA3OSIsInNjb3BlIjoib3BlbmlkIG9mZmxpbmVfYWNjZXNzIiwiaXNzIjoiYXBpX2tleV9pc3N1ZXIiLCJhdWQiOlsiaHR0cHM6Ly9uZWJpdXMtaW5mZXJlbmNlLmV1LmF1dGgwLmNvbS9hcGkvdjIvIl0sImV4cCI6MTkwMjIzODk4NiwidXVpZCI6IjcwN2VlMTBhLWU3ZjktNGQ3ZS1hYTg3LTRjOTY3YzRjYzI5NiIsIm5hbWUiOiJBc3luYyBkZW1vIiwiZXhwaXJlc19hdCI6IjIwMzAtMDQtMTJUMTU6NDM6MDYrMDAwMCJ9.S3tS2c4luF6UYViiBFsGj60jKT1fAtgHtm74YJYmv-o"
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