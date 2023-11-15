import json
# Import the send_message function from your API module
from api.sendMessage import send_message


# filePath = "BotMemberIds.txt"

# with open(filePath, "r") as file:
#     lines = file.readlines()

# for line in lines:
#     chat_id = line.strip('\ufeff').strip()
#     print(chat_id)
#     send_message(str(chat_id))

# chat_id = "799155485"
chat_id = "1012183944"
print(chat_id)
send_message(str(chat_id))
