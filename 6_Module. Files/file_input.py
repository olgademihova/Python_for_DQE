import os
import json
import xml.etree.ElementTree as ET
from locale import normalize
from manual_input import PrintMessage
from database import save_news_to_db, save_adv_to_db, save_guess_to_db
# sol 2


# create parent class File
class File:

    def __init__(self, output_file_name):
        self.output_file_name = output_file_name

# create a method to read files with different extension (txt/json/xml)
    def read_file(self, file_name):
        if '.txt' in file_name:
            with open(file_name, "r", encoding='utf-8') as file:
                f_contents = file.readlines()  # open txt file to read data
        elif '.json' in file_name:
            with open(file_name, "r") as file:
                f_contents = json.load(file)  # open json file to read data
        elif '.xml' in file_name:   # NEED TO ADD!!
            with open(file_name, "r") as read_file:
                f_contents = ET.parse(read_file)   # open XML file to read data
        return f_contents

# create method to get file content from file
    def get_file_content(self):
        original_path = os.path.dirname(os.path.realpath(__file__))
        print(f'Your default directory is "{os.getcwd()}"')
        is_true = True
        f_contents = ""    # new line
        while is_true:
            answer = int(input(
                f'If you want to ingest your file from default directory - enter 1, if you want to change it - enter 2: '))
            if answer == 1:  # choose default directory
                while True:
                    try:
                        file_name = input('Enter the file name with its format: ')
                        f_contents = self.read_file(file_name)  # read file with diff extension
                        print('Okay, such file exists')
                        path_for_remove = str(file_name)
                        is_true = False
                        break
                    except FileNotFoundError:
                        print('No file with such name. Try again')
                    except PermissionError:
                        print('No file with such name. Try again')
            elif answer == 2:  # choose own directory
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
                        f_contents = self.read_file(file_name)  # read file with diff extension
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


# create child class TextFile
class TextFile(File):

    def __init__(self, output_file_name):
        super().__init__(output_file_name)

# create method that parse text file
    def parse_file(self):
        f_contents, path_for_remove = self.get_file_content()
        num_records = int(input("Enter records num:\n"))  # ask to input count of our records (News/Adv/Guess)
        count = 0  # count of rows
        f_contents_new = ""   #new content
        for i, line in enumerate(f_contents): # create a loop
            if line == '\n':  # add condition with new line
                count += 1  # add 1
                if count == 2 * num_records:
                    f_contents_new = f_contents[:i + 1]
                    break
        with open(self.output_file_name, "a", encoding='utf-8') as file:  # add new data to output file
            file.writelines(f_contents_new)
        print(f'This file {path_for_remove} will be removed now\n')
        os.remove(path_for_remove)   # processed file is removed


# create child class JSONFile
class JSONFile(File):

    def __init__(self, output_file_name, records=""):
        super().__init__(output_file_name)
        self.records = records

# create method that parse JSON file
    def parse_file(self):
        f_contents, path_for_remove = self.get_file_content()
        self.records = f_contents["records"]
        for record in self.records:
            if record["type"] == 'news':
                #print("News", record)
                text = record["text"]
                loc = record["location"]
                dt = record["date"]
                news_record = f"News ----------------------------\n" \
                              f"{text}\n"\
                              f"{loc}, {dt}\n"\
                              f'---------------------------------\n\n'
                PrintMessage(normalize(news_record), self.output_file_name).print_message()  # print news text info to output file
                save_news_to_db('10test.db', text, loc, dt)  # call the function to save news data in db

            elif record["type"] == 'adv':
                #print("Advertising", record)
                text = record["text"]
                exp_dt = record["expired_date"]
                days_l = record["days_left"]
                news_record = f'Private Ad -----------------------\n' \
                              f'{text}\n' \
                              f'Actual until: {exp_dt}, {days_l} days left\n' \
                              f'----------------------------------\n\n'
                PrintMessage(normalize(news_record), self.output_file_name).print_message() # print adv text info to output file
                save_adv_to_db('10test.db', text, exp_dt, days_l)   # call the function to save adv data in db


            elif record["type"] == 'guess':
                #print("Guess", record)
                text = record["text"]
                ans = record["answer"]
                news_record = f'Ask me about your future? --------\n' \
                              f'Your question - "{text}",\n' \
                              f'Witch\'s answer will be - {ans}\n' \
                              f'----------------------------------\n\n'
                PrintMessage(normalize(news_record), self.output_file_name).print_message() # print guess text info to output file
                save_guess_to_db('10test.db', text, ans)  # call the function to save guess data in db

        print(f'This file {path_for_remove} will be removed now\n')
        os.remove(path_for_remove)  # processed file is removed


# create child class XMLFile
class XMLFile(File):

    def __init__(self, output_file_name):
        super().__init__(output_file_name)

# create method that parse XML file
    def parse_file(self):
        f_contents, path_for_remove = self.get_file_content()
        root = f_contents.getroot()
        for record in root.findall('type'):
            if record.get('name') == 'news':
                # print(record)
                text = record.find('text').text
                # print(text)
                loc = record.find('location').text
                # print(loc)
                dt = record.find('date').text
                # print(dt)  # увидим текст в тэгах для NEWS!!!!!!!
                news_record = f"News ----------------------------\n" \
                              f"{text}\n" \
                              f"{loc}, {dt}\n" \
                              f'---------------------------------\n\n'
                PrintMessage(normalize(news_record), self.output_file_name).print_message()  # print news text info to output file
                save_news_to_db('10test.db', text, loc, dt)  # call the function to save news data in db

            elif record.get('name') == 'adv':
                text = record.find('text').text
                # print(text)
                exp_dt = record.find('expired_date').text
                # print(exp_dt)
                days_l = record.find('days_left').text
                # print(days_l)  # увидим текст в тэгах для ADV!!!!!!!
                news_record = f'Private Ad -----------------------\n' \
                              f'{text}\n' \
                              f'Actual until: {exp_dt}, {days_l} days left\n' \
                              f'----------------------------------\n\n'
                PrintMessage(normalize(news_record), self.output_file_name).print_message()  # print adv text info to output file
                save_adv_to_db('10test.db', text, exp_dt, days_l)  # call the function to save adv data in db

            elif record.get('name') == 'guess':
                text = record.find('text').text
                # print(text)
                ans = record.find('answer').text
                # print(ans)  # увидим текст в тэгах для GUESS!!!!!!!
                news_record = f'Ask me about your future? --------\n' \
                              f'Your question - "{text}",\n' \
                              f'Witch\'s answer will be - {ans}\n' \
                              f'----------------------------------\n\n'
                PrintMessage(normalize(news_record), self.output_file_name).print_message()  # print guess text info to output file
                save_guess_to_db('10test.db', text, ans)  # call the function to save guess data in db

        print(f'This file {path_for_remove} will be removed now\n')
        os.remove(path_for_remove)  # processed file is removed



