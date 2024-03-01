import requests


def sendPhoto(chat_id):
    khmer_text_3 = """ក្រុមហ៊ុន ព្រូដិនសល (ខេមបូឌា) ឡាយហ្វ៍ អឹសួរ៉ិនស៍ ម.ក និង ធនាគារ វីង (ខេមបូឌា) ម.ក បានប្រកាសជាផ្លូវការពីកិច្ចសហការដៃគូអាជីវកម្ម ប៊េនកាសួរេន ដើម្បីផ្តល់ភាពងាយស្រួលទៅដល់អតិថិជនក្នុងការទទួលបានផលិតផលធានារ៉ាប់រងអាយុជីវិត និងសុខភាពរបស់ក្រុមហ៊ុន ព្រូដិនសលកម្ពុជា នៅតាមទីតាំងសាខារបស់ធនាគារ វីង។ 

សេវាធានារ៉ាប់រងអាយុជីវិត ពិតជាមានសារៈសំខាន់ក្នុងការជួយការពារហិរញ្ញវត្ថុ ក៏ដូចជាសុវត្ថិភាពពីហេតុការណ៍កើតឡើងដោយមិនអាចដឹងមុនដូចជាករណី បាត់បង់ជីវិត ឬគ្រោះថ្នាក់បង្កឱ្យពិការភាព ដោយប្រាកដថា សុខមាលភាពក្រុមគ្រួសារត្រូវបានការពារទាំងស្រុង។"""

    url = "https://api.telegram.org/bot6032345792:AAFOVOjeZDXma0r6cTd54mvXq09enfs0hT0/sendPhoto"
    payload = {'chat_id': chat_id,
               'caption': khmer_text_3,
               'photo': "AgACAgUAAxkDAAEBcoRl1WgmYQp7qUrD_TLWrgyK2cq73wAC37YxG_2JsFYenA4-nBDnlgEAAwIAA3MAAzQE"
               }
    # files = [
    #     ('photo', ('14.jpg', open('14.jpg', 'rb'), 'application/jpg'))
    # ]
    headers = {}
    # response = requests.request(
    #     "POST", url, headers=headers, data=payload, files=files)
    response = requests.request(
        "POST", url, headers=headers, data=payload)

    print(response.text)
