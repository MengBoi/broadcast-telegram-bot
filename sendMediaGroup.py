

import requests


def sendMediaGroup(chat_id, media):
    url = "https://api.telegram.org/bot6032345792:AAFOVOjeZDXma0r6cTd54mvXq09enfs0hT0/sendMediaGroup"

    payload = {
        'chat_id': str(chat_id),
        'media': str(media)
    }

    headers = {}

    try:
        response = requests.post(url, headers=headers, data=payload)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print(response.text)
    except requests.exceptions.RequestException as e:
        print("Error:", e)
