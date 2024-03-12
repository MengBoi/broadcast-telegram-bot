import requests


def sendVideo(chat_id, caption):
    url = "https://api.telegram.org/bot6032345792:AAFOVOjeZDXma0r6cTd54mvXq09enfs0hT0/sendVideo"

    payload = {'chat_id': str(chat_id),
               'caption': str(caption),
               'video': 'BAACAgUAAxkDAAEDJJFl6YfPwSRaEhSN3juOVPDU10B4fwACjA4AAg_GUVc-0QwxPNsUNTQE'}
    # files = [
    #     ('video', ('IWD Video.mp4', open(
    #         '/Users/aingearmeng/Downloads/IWD Video.mp4', 'rb'), 'application/octet-stream'))
    # ]
    headers = {}

    # response = requests.request(
    #     "POST", url, headers=headers, data=payload, files=files)
    response = requests.request(
        "POST", url, headers=headers, data=payload)

    print(response.text)
