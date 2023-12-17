import requests
import json
from django.conf import settings


def send_message(message):
    prompt = generate_prompt(message)
    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Api-Key " + settings.YAGPT_API_KEY
    }

    response = requests.post(url, headers=headers, json=prompt)
    try:
        return json.loads(response.text).get("result").get("alternatives")[0].get('message').get('text')
    except Exception:
        return ""


def generate_prompt(message):
    prompt = {
        "modelUri": "gpt://" + settings.YAGPT_REPO + "/yandexgpt-lite",
        "completionOptions": {
            "stream": False,
            "temperature": 0.6,
            "maxTokens": "2000"
        },
        "messages": [{
            "role": "system",
            "text": message
        }],
    }
    return prompt
