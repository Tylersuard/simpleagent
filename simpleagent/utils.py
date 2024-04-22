from abc import ABC
import openai
from groq import Groq


class MODELS:
    GPT_4_PREVIEW = "gpt-4-0125-preview"
    MIXTRAL_8X_7B = "mixtral-8x7b-32768"


class SendToLLM(ABC):
    def __init__(self, endpoint, api_key, model):
        pass

    def send(self, data):
        pass


class SendToOpenai(SendToLLM):
    def __init__(self, endpoint, api_key, model=MODELS.GPT_4_PREVIEW):
        if not api_key:
            raise ValueError("api_key is required")
        self.api_key = api_key
        self.endpoint = endpoint
        self.model = model

    def send(self, message):
        client = openai.OpenAI(api_key=self.api_key)
        response = client.chat.completions.create(
            model=self.model,
            messages=[{"role": "system", "content": message}],
            temperature=0.3,
            max_tokens=500,
        )
        return response.choices[0].message.content


class SendToGroq(SendToLLM):
    def __init__(self, endpoint, api_key, model=MODELS.MIXTRAL_8X_7B):
        self.api_key = api_key
        self.model = model

    def send(self, message):
        client = Groq(api_key=self.api_key)
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"{message}",
                }
            ],
            model=self.model,
        )

        return chat_completion.choices[0].message.content
