import json
# Import the send_message function from your API module
# from sendVideo import sendVideo
from sendPhoto import sendPhoto
from sendMediaGroup import sendMediaGroup
from sendMessage import sendMessage
import time
filePath = "botmember.txt"

with open(filePath, "r") as file:
    lines = file.readlines()


first_five = """[{ "type": "photo", "media": "AgACAgUAAxkDAAEBjUxl3DAotvzMT4AbiRv3dXFp6BKA4QACtb0xG-YD4VYKCFM76KgxFAEAAwIAA3kAAzQE" },
        { "type": "photo", "media": "AgACAgUAAxkDAAEBjU1l3DBKs1YJ_HDbQ1khtrg2PaFjsQACt70xG-YD4VYBkSTskR0-3wEAAwIAA3kAAzQE" },
        { "type": "photo", "media": "AgACAgUAAxkDAAEBjU5l3DCiHCXROovSzBll6RIZJMnDjAACub0xG-YD4VZnflAqrnz0hgEAAwIAA3kAAzQE" }, 
        { "type": "photo", "media": "AgACAgUAAxkDAAEBjU9l3DC6OtwkfGN9kUnjumdy6tRViwACvL0xG-YD4VZ-3onaw8_qlAEAAwIAA3kAAzQE" }, 
        { "type": "photo", "media": "AgACAgUAAxkDAAEBjVBl3DDR9684kmRHprS6_U71_kvxjgACvb0xG-YD4Van88juaYFy0gEAAwIAA3kAAzQE" }]"""

second_nine = """[{ "type": "photo", "media": "AgACAgUAAxkDAAEBjVFl3DDikKsarlr80hPDsRJ_CGzIYgACvr0xG-YD4Vb64C19pB-z8QEAAwIAA3kAAzQE" },
        { "type": "photo", "media": "AgACAgUAAxkDAAEBjVJl3DD2gUiDyPUw_2ZNqnwmy46zYwACv70xG-YD4VYBXgMyrC3BxAEAAwIAA3kAAzQE" },
        { "type": "photo", "media": "AgACAgUAAxkDAAEBjVNl3DEF_3BHdfkkE-0cYTPH4WA9KwACwr0xG-YD4VbMeesyYEbRtQEAAwIAA3kAAzQE" }, 
        { "type": "photo", "media": "AgACAgUAAxkDAAEBjVRl3DEY59ePZ5-YAzO15uv470FyyAACx70xG-YD4VY3ZQ2IXsqmCwEAAwIAA3kAAzQE" }, 
        { "type": "photo", "media": "AgACAgUAAxkDAAEBjVVl3DE3CwpPyQABNsR8kgoddOKf_fsAAsi9MRvmA-FWZ8sbN-Ryc3cBAAMCAAN5AAM0BA" },
        { "type": "photo", "media": "AgACAgUAAxkDAAEBjVZl3DFICbJrFso4qh5hMfaz9dbrcQACy70xG-YD4VYhDDmIoYrWgwEAAwIAA3kAAzQE" },
        { "type": "photo", "media": "AgACAgUAAxkDAAEBjVdl3DFZw3Vk4S1H6jtO441RzKBOvgACzL0xG-YD4VY5Dg7WSZR1HQEAAwIAA3kAAzQE" },
        { "type": "photo", "media": "AgACAgUAAxkDAAEBjVhl3DFumWJYJRqzR7LPk2DojGxp0gACzr0xG-YD4VZzhXFr-Dh3PwEAAwIAA3kAAzQE" },
        { "type": "photo", "media": "AgACAgUAAxkDAAEBjVll3DF87EgHGCPa8NyIA3o1SMkjxwACz70xG-YD4VZjiq-fSUsaegEAAwIAA3kAAzQE" }]"""
khmer_text_3 = """ក្រុមហ៊ុន ព្រូដិនសល (ខេមបូឌា) ឡាយហ្វ៍ អឹសួរ៉ិនស៍ ម.ក និង ធនាគារ វីង (ខេមបូឌា) ម.ក បានប្រកាសជាផ្លូវការពីកិច្ចសហការដៃគូអាជីវកម្ម ប៊េនកាសួរេន ដើម្បីផ្តល់ភាពងាយស្រួលទៅដល់អតិថិជនក្នុងការទទួលបានផលិតផលធានារ៉ាប់រងអាយុជីវិត និងសុខភាពរបស់ក្រុមហ៊ុន ព្រូដិនសលកម្ពុជា នៅតាមទីតាំងសាខារបស់ធនាគារ វីង។ 

សេវាធានារ៉ាប់រងអាយុជីវិត ពិតជាមានសារៈសំខាន់ក្នុងការជួយការពារហិរញ្ញវត្ថុ ក៏ដូចជាសុវត្ថិភាពពីហេតុការណ៍កើតឡើងដោយមិនអាចដឹងមុនដូចជាករណី បាត់បង់ជីវិត ឬគ្រោះថ្នាក់បង្កឱ្យពិការភាព ដោយប្រាកដថា សុខមាលភាពក្រុមគ្រួសារអ្នកត្រូវបានការពារទាំងស្រុង។"""
for line in lines:
    chat_id = line.strip('\ufeff').strip()
    print(chat_id)
    sendMediaGroup(chat_id, first_five)
    sendMediaGroup(chat_id, second_nine)
    sendMessage(chat_id, khmer_text_3)
    # sendPhoto(chat_id)


# file six AgACAgUAAxkDAAEBjVFl3DDikKsarlr80hPDsRJ_CGzIYgACvr0xG-YD4Vb64C19pB-z8QEAAwIAA3kAAzQE
# file seven AgACAgUAAxkDAAEBjVJl3DD2gUiDyPUw_2ZNqnwmy46zYwACv70xG-YD4VYBXgMyrC3BxAEAAwIAA3kAAzQE
# file eight AgACAgUAAxkDAAEBjVNl3DEF_3BHdfkkE-0cYTPH4WA9KwACwr0xG-YD4VbMeesyYEbRtQEAAwIAA3kAAzQE
# file nine AgACAgUAAxkDAAEBjVRl3DEY59ePZ5-YAzO15uv470FyyAACx70xG-YD4VY3ZQ2IXsqmCwEAAwIAA3kAAzQE

# file ten AgACAgUAAxkDAAEBjVVl3DE3CwpPyQABNsR8kgoddOKf_fsAAsi9MRvmA-FWZ8sbN-Ryc3cBAAMCAAN5AAM0BA

# file eleven AgACAgUAAxkDAAEBjVZl3DFICbJrFso4qh5hMfaz9dbrcQACy70xG-YD4VYhDDmIoYrWgwEAAwIAA3kAAzQE

# file twelve AgACAgUAAxkDAAEBjVdl3DFZw3Vk4S1H6jtO441RzKBOvgACzL0xG-YD4VY5Dg7WSZR1HQEAAwIAA3kAAzQE

# file thirteen AgACAgUAAxkDAAEBjVhl3DFumWJYJRqzR7LPk2DojGxp0gACzr0xG-YD4VZzhXFr-Dh3PwEAAwIAA3kAAzQE

# file fourteen AgACAgUAAxkDAAEBjVll3DF87EgHGCPa8NyIA3o1SMkjxwACz70xG-YD4VZjiq-fSUsaegEAAwIAA3kAAzQE
