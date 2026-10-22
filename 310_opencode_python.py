# WORKS
from openai import OpenAI
import os

# use my openapi key, already displays in opencode/zen, just copy
# works for some of the zen models
# 
#  
client = OpenAI(
    base_url="https://opencode.ai/zen/v1",
    api_key=os.getenv("OPENCODE_API_KEY")
)

resp = client.chat.completions.create(
    model="deepseek-v4-flash-free",  
    messages=[
        {"role": "user", "content": "Say hello in one sentence."}
    ]
)

print(resp.choices[0].message.content)
