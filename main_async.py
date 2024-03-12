import multiprocessing
from sendVideo import sendVideo
from sendPhoto import sendPhoto


def process_chunk(chunk, khmer_text):
    for line in chunk:
        chat_id = line.strip('\ufeff').strip()
        sendPhoto(chat_id, khmer_text,
                  "AgACAgUAAxkDAAEDdzdl8CL-RZi5C64exeu-7ljYsukpMgACJbsxG0txgVcta_FwTW4qqAEAAwIAA3gAAzQE")


if __name__ == "__main__":
    filePath = "uat.txt"
    with open(filePath, "r") as file:
        lines = file.readlines()

    khmer_text_3 = """សារជូនដំណឹងពីការបោកបញ្ឆោត!

អតិថិជនជាទីគោរព! យើងខ្ញុំបានសង្កេតឃើញមាន សកម្មភាពបោកប្រាស់តាមរយៈការទូរស័ព្ទទំនាក់ទំនង ដោយជនឆបោកសុំឱ្យអតិថិជន ព្រូដិនសលធ្វើការផ្ទេរទឹកប្រាក់តាម QRកូដ ដែលបានចែករំលែកពី គណនី Telegram របស់ជនឆបោក។ សូមបង្កើនការប្រុងប្រយ័ត្ន និងកុំធ្លាក់ក្នុងកលល្បិចនេះ ព្រោះថានេះជាការឆបោកសុទ្ធសាធ! 


ប្រសិនបើលោកអ្នកធ្លាប់ទទួលបាន ការទាក់ទងតាមទូរស័ព្ទ ឬសារបែបនេះ  សូមកុំទទួល ឬធ្វើការឆ្លើយតប ឬ ផ្ដល់ព័ត៌មានទាក់ទងនឹងបណ្ណសន្យារ៉ាប់រងរបស់លោកអ្នក ឬពាក្យសម្ងាត់ឱ្យសោះ។ ផ្ទុយទៅវិញ សូមផ្តល់ដំណឹងមកយើងខ្ញុំភ្លាមៗ តាមរយៈលេខ 023 964 222 ឬ 1 800 203 203 (ឥតគិតថ្លៃ ក្នុងប្រទេសកម្ពុជា)។"""

    chunk_size = 500
    chunks = [lines[i:i+chunk_size] for i in range(0, len(lines), chunk_size)]

    processes = []
    for chunk in chunks:
        process = multiprocessing.Process(
            target=process_chunk, args=(chunk, khmer_text_3))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
