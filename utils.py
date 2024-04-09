from abc import ABC
import openai
import requests
from groq import Groq

class SendToLLM(ABC):
    def __init__(self, endpoint, api_key):
        pass
    def send(self, data):
        pass

class SendToOpenai(SendToLLM):
    def __init__(self, endpoint, api_key):
        if not api_key:
            raise ValueError("api_key is required")
        self.api_key = api_key
        self.endpoint = endpoint

    def send(self, message):
        client = openai.OpenAI(api_key=self.api_key)
        response = client.chat.completions.create(
            model="gpt-4-0125-preview",
            messages=[{"role": "system", "content": message}],
            temperature=0.3,
            max_tokens=500,
        )
        return response.choices[0].message.content
    
class SendToGroq(SendToLLM):
    def __init__(self, endpoint, api_key):
        self.api_key=api_key

    def send(self, message):
        client = Groq(api_key=self.api_key)
        chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": f"{message}",
        }
    ],
    model="mixtral-8x7b-32768",
)

        return chat_completion.choices[0].message.content
