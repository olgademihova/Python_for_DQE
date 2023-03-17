import xml.etree.ElementTree as ET
from locale import normalize
from modules_5_6 import PrintMessage


class XMLInput:

    def __init__(self, file_path, records=""):
        self.file_path = file_path
        self.records = records

    def get_data(self):
        with open(self.file_path, "r") as read_file:
            xml_file = ET.parse(read_file)
            root = xml_file.getroot()
        return root

    def parse_file(self):
        root = self.get_data()
        for element in root.iter('type'):
            if element.get('name') == 'news':  # получить аттрибут
                # print(element.attrib)
                for record in root.findall('type'):
                    text = record.find('text').text
                    loc = record.find('location').text
                    dt = record.find('date').text
                    print(text)  # увидим текст в тэгах для NEWS!!!!!!!
                    news_record = f"News ----------------------------\n" \
                                  f"{text}\n" \
                                  f"{loc}, {dt}\n" \
                                  f'---------------------------------\n\n'
                    PrintMessage(normalize(news_record)).print_message()

            elif element.get('name') == 'adv':
                # print(element.attrib)
                for record in root.findall('type'):
                    text = record.find('text').text
                    exp_dt = record.find('expired_date').text
                    days_l = record.find('days_left').text
                    # print(text.text)  # увидим текст в тэгах для ADV!!!!!!!
                    news_record = f'Private Ad -----------------------\n' \
                                  f'{text}\n' \
                                  f'Actual until: {exp_dt}, {days_l} days left\n' \
                                  f'----------------------------------\n\n'
                    PrintMessage(normalize(news_record)).print_message()

            elif element.get('name') == 'guess':
                # print(element.attrib)
                for record in root.findall('type'):
                    text = record.find('text').text
                    ans = record.find('answer').text
                    # print(text.text)  # увидим текст в тэгах для GUESS!!!!!!!
                    news_record = f'Ask me about your future? --------\n' \
                                  f'Your question - "{text}",\n' \
                                  f'Witch\'s answer will be - {ans}\n' \
                                  f'----------------------------------\n\n'
                    PrintMessage(normalize(news_record)).print_message()



