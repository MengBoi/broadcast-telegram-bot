import requests


def sendPhoto(chat_id, caption, file_id):

    url = "https://api.telegram.org/bot6032345792:AAFOVOjeZDXma0r6cTd54mvXq09enfs0hT0/sendPhoto"
    payload = {'chat_id': chat_id,
               'caption': caption,
               'photo': file_id
               }

    headers = {}
    response = requests.request(
        "POST", url, headers=headers, data=payload)
    # response = requests.request(
    #     "POST", url, headers=headers, data=payload)

    print(response.text)
