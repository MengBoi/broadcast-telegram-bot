import requests


def send_message(chat_id):
    try:
        url = "https://api.telegram.org/bot6032345792:AAFOVOjeZDXma0r6cTd54mvXq09enfs0hT0/sendPhoto"

        payload = {'chat_id': chat_id,
                   'caption': "ធានាអនាគតរបស់កូនលោកអ្នកជាមួយ PRUអនាគតកូនខ្ញុំ ដែលជាផលិតផលធានារ៉ាប់រងដែលអាចឱ្យលោកអ្នករៀបចំផែនការហិរញ្ញវត្ថុ និងការពារអ្នក និងគ្រួសារអ្នកពីព្រឹត្តិការណ៍អកុសលណាមួយ។ ហើយកាន់តែពិសេស ពេលលោកអ្នកជាវនូវកញ្ចប់ផលិតផល PRUអនាគតកូនខ្ញុំ សម្រាប់កូនៗ និងមនុស្សជាទីស្រលាញរបស់អ្នក អ្នកនឹងទទួលបានរង្វាន់ភ្លាមៗជាច្រើន។ ទាក់ទងមកកាន់បុគ្គលិកធានារ៉ាប់រង ព្រូដិនសល ដើម្បីទទួលបានការប្រឹក្សាដោយឥតគិតថ្លៃ។ តាមរយៈ 1800212223 (មិនគិតថ្លៃសេវា) ឬ 023 964 222 ឬ www.prudential.com.kh/km/ និងលក្ខខណ្ឌត្រូវបានអនុវត្ត\n\n#PrudentialCambodia #PRUMyChildFuture #LifeInsurance #Insurance #TermInsurance #HealthInsurance #ProtectionPlans #SavingsPlans",
                   #    'reply_markup': '{"inline_keyboard": [[{ "text": "ចុចទីនេះ ដើម្បីយករង្វាន់", "callback_data": "reward_game"}]]}'
                   'photo': "AgACAgUAAxkDAAEBI0RlzZHjNRTwTSfGBrAckVTAuL_CPgACVLkxG9xfcFbCcOeNH6MVaAEAAwIAA3MAAzQE"
                   }

        # files = [
        #     ('photo', ('pru-anakot.jpeg', open(
        #         'pru-anakot.jpeg', 'rb'), 'image/png'))
        # ]

        headers = {}

        # response = requests.request(
        #     "POST", url, headers=headers, data=payload, files=files)
        response = requests.request(
            "POST", url, headers=headers, data=payload)
        print(response.json())
    except Exception as e:
        print(f"An error occurred: {str(e)}")
