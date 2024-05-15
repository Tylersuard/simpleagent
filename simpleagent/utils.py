from abc import ABC, abstractmethod

import openai
from groq import Groq


class MODELS:
    GPT_4_PREVIEW = "gpt-4-0125-preview"
    MIXTRAL_8X_7B = "mixtral-8x7b-32768"


class SendToLLM(ABC):
    def __init__(self, endpoint: str, api_key: str, model: str):
        if api_key is None:
            raise ValueError("api_key is required")
        self.api_key = api_key
        self.endpoint = endpoint
        self.model = model

    @abstractmethod
    def send(self, message, system="You are a helpful assistant.") -> str:
        raise NotImplementedError("send method must be implemented.")


class SendToOpenai(SendToLLM):
    def __init__(self, endpoint: str, api_key: str, model: str = MODELS.GPT_4_PREVIEW):
        super().__init__(endpoint, api_key, model)
        self.client = openai.OpenAI(api_key=self.api_key)

    def send(self, message, system="You are a helpful assistant.") -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": message},
            ],
            temperature=0.3,
            max_tokens=800,
        )

        if response.choices[0].message.content is None:
            return "I am sorry, I do not have an answer for that."
        return response.choices[0].message.content


class SendToGroq(SendToLLM):
    def __init__(self, endpoint, api_key, model=MODELS.MIXTRAL_8X_7B):
        super().__init__(endpoint, api_key, model)
        self.client = Groq(api_key=self.api_key)

    def send(self, message, system="You are a helpful assistant.") -> str:
        response = self.client.chat.completions.create(
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": message},
            ],
            model=self.model,
        )

        if response.choices[0].message.content is None:
            return "I am sorry, I do not have an answer for that."
        return response.choices[0].message.content
