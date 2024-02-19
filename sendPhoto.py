import requests


def sendPhoto(chat_id):
    url = "https://api.telegram.org/bot6032345792:AAFOVOjeZDXma0r6cTd54mvXq09enfs0hT0/sendPhoto"
    payload = {'chat_id': chat_id,
               'caption': "Join us in the Sharing Session under the topic of Money Mindset: Basic Financial Intelligence from Mr. Bunthet Cham, Director of Agency Distribution at Prudential Cambodia.\n\nYou will learn essential financial intelligence to build wealth and happiness and exciting career opportunities with Prudential Cambodia.\n\n📅  Wednesday, 21st Feb 2024\n⏰ 5:30 – 7:30 PM\n📍 V-trust Tower, 5th Floor\n\nDon't miss this opportunity to enhance your financial knowledge and transform your money mindset. Reserve your seat now! Link to register: https://bit.ly/BOP_1 \n\nFor more information, please contact: 095 203 222.",
               'photo': "AgACAgUAAxkDAAEBXcNl0s4JXBHFzN5kHGaWwEDrm494wAACv7kxGxGSmVZqkrRHf7YK4AEAAwIAA3MAAzQE"}
    # files = [
    #     ('photo', ('IMG_7861.JPG', open('IMG_7861.JPG', 'rb'), 'application/jpg'))
    # ]
    headers = {}
    # response = requests.request(
    #     "POST", url, headers=headers, data=payload, files=files)
    response = requests.request(
        "POST", url, headers=headers, data=payload)

    print(response.text)
