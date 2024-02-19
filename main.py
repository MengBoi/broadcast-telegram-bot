import json
# Import the send_message function from your API module
from api.sendMessage import send_message
from api.sendVideo import sendVideo


# filePath = "bot_member.txt"
filePath = "bot_member.txt"

with open(filePath, "r") as file:
    lines = file.readlines()

for line in lines:
    chat_id = line.strip('\ufeff').strip()
    print(chat_id)
    send_message(str(chat_id))
    # sendVideo(chat_id=chat_id)
