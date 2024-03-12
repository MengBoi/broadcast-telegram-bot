# import asyncio
# # Assuming you have defined the sendVideo function in sendVideo.py
# from sendVideo import sendVideo


# filePath = "uat.txt"

# with open(filePath, "r") as file:
#     lines = file.readlines()

# khmer_text_3 = """Your video file path or content"""

# for line in lines:
#     chat_id = line.strip('\ufeff').strip()
#     sendVideo(chat_id, khmer_text_3)
# # chunk_size = 5
# # for i in range(0, len(lines), chunk_size):
# #     chunk = lines[i:i+chunk_size]
# #     chat_ids = [line.strip('\ufeff').strip() for line in chunk]
# #     print(chat_ids)
# #     asyncio.gather(sendVideo(chat_ids[0], khmer_text_3), sendVideo(chat_ids[1], khmer_text_3), sendVideo(chat_ids[0], khmer_text_3), sendVideo(
# #         chat_ids[2], khmer_text_3), sendVideo(chat_ids[3], khmer_text_3), sendVideo(chat_ids[3], khmer_text_3), sendVideo(chat_ids[4], khmer_text_3))
