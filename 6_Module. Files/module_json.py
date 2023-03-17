import json
from locale import normalize
from modules_5_6 import PrintMessage


class JSONInput:

    def __init__(self, file_path, records=""):
        self.file_path = file_path
        self.records = records

    def get_data(self):
        with open(self.file_path, "r") as read_file:
            data = json.load(read_file)
            self.records = data["records"]

    def parse_file(self):
        for record in self.records:
            if record["type"] == 'news':
                print("News", record)
                text = record["type"]["text"]
                loc = record["type"]["location"]
                dt = record["type"]["date"]
                news_record = f"News ----------------------------\n" \
                              f"{text}\n"\
                              f"{loc}, {dt}\n"\
                              f'---------------------------------\n\n'
                PrintMessage(normalize(news_record)).print_message()

            elif record["type"] == 'adv':
                print("Advertising", record)
                text = record["type"]["text"]
                exp_dt = record["type"]["expired_date"]
                days_l = record["type"]["days_left"]
                news_record = f'Private Ad -----------------------\n' \
                              f'{text}\n' \
                              f'Actual until: {exp_dt}, {days_l} days left\n' \
                              f'----------------------------------\n\n'
                PrintMessage(normalize(news_record)).print_message()

            elif record["type"] == 'guess':
                print("Guess", record)
                text = record["type"]["text"]
                ans = record["type"]["answer"]
                news_record = f'Ask me about your future? --------\n' \
                              f'Your question - "{text}",\n' \
                              f'Witch\'s answer will be - {ans}\n' \
                              f'----------------------------------\n\n'
                PrintMessage(normalize(news_record)).print_message()







