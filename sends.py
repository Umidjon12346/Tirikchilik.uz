import requests
from settings import URL


def send_message(url: str, chat_id: int, text: str, reply_markup: dict):
    endpoint = '/sendMessage'
    url += endpoint

    data = {
        'chat_id': chat_id,
        'text': text,
        'reply_markup': reply_markup,
    }
    requests.post(url, json=data)

