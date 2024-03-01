import requests
import json


def sendMessage(chat_id, text):
    url = "https://api.telegram.org/bot6032345792:AAFOVOjeZDXma0r6cTd54mvXq09enfs0hT0/sendMessage"

    payload = json.dumps({
        "chat_id": str(chat_id),
        "text": str(text)
    })
    headers = {
        'Content-Type': 'application/json'
    }

    try:
        response = requests.post(url, headers=headers, data=payload)
        # Raise an exception for HTTP errors (status codes 4xx or 5xx)
        response.raise_for_status()
        print("Message sent successfully!")
    except requests.exceptions.RequestException as e:
        print("Error sending message:", e)
