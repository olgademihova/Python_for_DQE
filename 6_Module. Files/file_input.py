import os
import json
import xml.etree.ElementTree as ET
from locale import normalize
from manual_input import PrintMessage
# sol 2


class File:

    def __init__(self, output_file_name):
        self.output_file_name = output_file_name

    def read_file(self, file_name):
        if '.txt' in file_name:
            with open(file_name, "r", encoding='utf-8') as file:
                f_contents = file.readlines()
        elif '.json' in file_name:
            with open(file_name, "r") as file:
                f_contents = json.load(file)
        elif '.xml' in file_name:   # NEED TO ADD!!
            with open(file_name, "r") as read_file:
                xml_file = ET.parse(read_file)
                root = xml_file.getroot()
            pass
        return f_contents

    def get_file_content(self):
        original_path = os.path.dirname(os.path.realpath(__file__))
        print(f'Your default directory is "{os.getcwd()}"')
        is_true = True
        f_contents = ""    # new line
        while is_true:
            answer = int(input(
                f'If you want to ingest your file from default directory - enter 1, if you want to change it - enter 2: '))
            if answer == 1:
                while True:
                    try:
                        file_name = input('Enter the file name with its format: ')
                        f_contents = self.read_file(file_name)
                        print('Okay, such file exists')
                        path_for_remove = str(file_name)
                        is_true = False
                        break
                    except FileNotFoundError:
                        print('No file with such name. Try again')
                    except PermissionError:
                        print('No file with such name. Try again')
            elif answer == 2:
                while True:
                    try:
                        change_path = input('Enter the file path: ')
                        if not os.path.isdir(change_path):
                            os.mkdir(change_path)
                        os.chdir(change_path)
                        print(f'Now you directory is "{os.getcwd()}"')
                        break
                    except SyntaxError:
                        print('You made a mistake. Try again')
                    except FileNotFoundError:
                        print('You made a mistake. Try again')
                while True:
                    try:
                        file_name = input('Enter the file name with its format: ')
                        f_contents = self.read_file(file_name)  # new line
                        print('Such file exists')
                        path_for_remove = os.path.join(str(change_path), str(file_name))
                        os.chdir(original_path)
                        is_true = False
                        break
                    except FileNotFoundError:
                        print('No file with such name. Try again')
                    except PermissionError:
                        print('No file with such name. Try again')
            else:
                print('Try again here')

            return f_contents, path_for_remove


class TextFile(File):

    def __init__(self, output_file_name):
        super().__init__(output_file_name)

    def parse_file(self):
        f_contents, path_for_remove = self.get_file_content()
        num_records = int(input("Enter records num:\n"))
        pass
        # count = 0
        # f_contents_new = ""   #new line
        # for i, line in enumerate(f_contents):
        #     if line == '\n':
        #         count += 1
        #         if count == 2 * num_records:
        #             f_contents_new = f_contents[:i + 1]
        #             break
        # with open(self.output_file_name, "a", encoding='utf-8') as file:
        #     file.writelines(f_contents_new)
        # print(f'This file {path_for_remove} will be removed now\n')
        # os.remove(path_for_remove)


class JSONFile(File):

    def __init__(self, output_file_name, records=""):
        super().__init__(output_file_name)
        self.records = records

    def parse_file(self):
        f_contents, path_for_remove = self.get_file_content()
        self.records = f_contents["records"]
        for record in self.records:
            if record["type"] == 'news':
                print("News", record)
                text = record["text"]
                loc = record["location"]
                dt = record["date"]
                news_record = f"News ----------------------------\n" \
                              f"{text}\n"\
                              f"{loc}, {dt}\n"\
                              f'---------------------------------\n\n'
                PrintMessage(normalize(news_record), self.output_file_name).print_message()

            elif record["type"] == 'adv':
                print("Advertising", record)
                text = record["text"]
                exp_dt = record["expired_date"]
                days_l = record["days_left"]
                news_record = f'Private Ad -----------------------\n' \
                              f'{text}\n' \
                              f'Actual until: {exp_dt}, {days_l} days left\n' \
                              f'----------------------------------\n\n'
                PrintMessage(normalize(news_record), self.output_file_name).print_message()

            elif record["type"] == 'guess':
                print("Guess", record)
                text = record["text"]
                ans = record["answer"]
                news_record = f'Ask me about your future? --------\n' \
                              f'Your question - "{text}",\n' \
                              f'Witch\'s answer will be - {ans}\n' \
                              f'----------------------------------\n\n'
                PrintMessage(normalize(news_record), self.output_file_name).print_message()


class XMLFile(File):

    def __init__(self, output_file_name):
        super().__init__(output_file_name)

    def parse_file(self):
        f_contents, path_for_remove = self.get_file_content()
        #root = self.get_data()
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
                    PrintMessage(normalize(news_record), self.output_file_name).print_message()

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
                    PrintMessage(normalize(news_record), self.output_file_name).print_message()

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
                    PrintMessage(normalize(news_record), self.output_file_name).print_message()

        pass



