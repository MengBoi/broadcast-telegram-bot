import requests


def sendVideo(chat_id):
    url = "https://api.telegram.org/bot6032345792:AAFOVOjeZDXma0r6cTd54mvXq09enfs0hT0/sendVideo"

    payload = {'chat_id': chat_id,
               'video': 'BAACAgUAAxkDAALwp2W3LM2U4pxH_SXRnuIUHfzJxZI7AAJxDAACybK4VcOOQBqiSzeANAQ',
               'caption': 'ងាយៗ ក្នុងការភ្ជាប់បណ្ណសន្យារ៉ាប់រងរបស់អ្នកជាមួយ Prudential Bot តាមការបង្ហាញជំហាននីមួយៗក្នុងវីដេអូខាងក្រោម។ ជាមួយ Prudential Bot លោកអ្នកអាចរីករាយជាមួយនឹងអត្ថប្រយោជន៍ជាច្រើនរួមមាន\n\n• ការឆែកមើលព័ត៌មានបណ្ណសន្យារ៉ាប់រងទូទៅ\n• ការពិនិត្យមើលព័ត៌មានបង់ប្រាក់ និងមុខងារពិជាច្រើនទៀត!\n• តស់មកភ្ជាប់បណ្ណសន្យារ៉ាប់រងរបស់ជាមួយយើងឥឡូវនេះ!'}
    files = [

    ]
    headers = {}

    response = requests.request(
        "POST", url, headers=headers, data=payload, files=files)
