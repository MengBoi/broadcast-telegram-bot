import requests


def send_message(chat_id):
    try:
        url = "https://api.telegram.org/bot6032345792:AAFOVOjeZDXma0r6cTd54mvXq09enfs0hT0/sendMessage"

        payload = {'chat_id': chat_id,
                   'text': 'សូមអបអរសាទរ 🎊\nអ្នកឈ្នះកាតទូរស័ព្ទពីហ្គេមកាតកោស\n\nនេះគឺជាលេខកូដកាត: 86000871857889\nចំនួន: 5$\n\nអរគុណសម្រាប់ការជ្រើសរើស ព្រូដិនសល',
                   #    'reply_markup': '{"inline_keyboard": [[{ "text": "ចុចទីនេះ ដើម្បីយករង្វាន់", "callback_data": "reward_game"}]]}'
                   }
        # files = [
        #     ('photo', ('photo.png', open(
        #         'T_Bot_Static2.png', 'rb'), 'image/png'))
        # ]
        headers = {}

        response = requests.request(
            "POST", url, headers=headers, data=payload, files=[])
        print(response.json())
    except Exception as e:
        print(f"An error occurred: {str(e)}")
