import requests


def sendPhoto(chat_id):
    url = "https://api.telegram.org/bot6032345792:AAFOVOjeZDXma0r6cTd54mvXq09enfs0hT0/sendPhoto"
    payload = {'chat_id': chat_id,
               'caption': "រីករាយថ្ងៃកំណើតសម្រាប់អតិថិជន ដែលមានខែកំណើតនៅក្នុងខែមករា និងខែកុម្ភៈ ត្រៀមខ្លួនទទួលយករង្វាន់ពី ព្រូដិនសល ហើយឬនៅ!\n\nដើម្បីជាការថ្លែងអំណរគុណចំពោះអតិថិជនទាំងអស់ដែលតែងតែគាំទ្រ និងផ្ដល់ការទុកចិត្តលើ ព្រូដិនសល ក្នុងការការពារហិរញ្ញវត្ថុក្រុមគ្រួសារនិងអនាគតបុត្រធីតារបស់លោកអ្នក អតិថិជនដែលមានខែមករា និងខែកុម្ភៈ គ្រាន់តែចុះឈ្មោះចូលរួមផ្សងសំណាង លោកអ្នកនឹងមានឱកាសឈ្នះរង្វាន់ជាច្រើន។ រីករាយជាមួយសុភមង្គលជីវិត ជាមួយព្រូដិនសល!\n\nសម្រាប់ព័ត៌មានបន្ថែម និងការចុះឈ្មោះ៖  https://bit.ly/cbcfbpost \n\n#PrudentialCambodia #CustomerBirthdayRewards #LifeInsurance #TermInsurance #ProtectionPlans #SavingsPlan",
               'photo': "AgACAgUAAxkDAAEBcoRl1WgmYQp7qUrD_TLWrgyK2cq73wAC37YxG_2JsFYenA4-nBDnlgEAAwIAA3MAAzQE"
               }
    # files = [
    #     ('photo', ('IMG_6906.JPG', open('IMG_6906.JPG', 'rb'), 'application/jpg'))
    # ]
    headers = {}
    # response = requests.request(
    #     "POST", url, headers=headers, data=payload, files=files)
    response = requests.request(
        "POST", url, headers=headers, data=payload)

    print(response.text)
