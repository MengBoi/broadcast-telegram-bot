import json
# Import the send_message function from your API module
# from sendVideo import sendVideo
from sendPhoto import sendPhoto
filePath = "botmember.txt"

with open(filePath, "r") as file:
    lines = file.readlines()

for line in lines:
    chat_id = line.strip('\ufeff').strip()
    print(chat_id)
    sendPhoto(chat_id)
