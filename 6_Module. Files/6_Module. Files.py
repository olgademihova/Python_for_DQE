import sys
import os
#import 5_Classes. OOP.5_Classes. OOP as m5
from datetime import datetime, date

# a = sys.argv[1]
# print(a)
#print(sys.argv)


class GlobalNewsLenta:
    '''class GlobalNewsLenta  - parent'''
    def __init__(self, name, text):
        self.name = name  # attribute of category name
        self.text = text  # attribute of text

    def write_to_file(self, all_lenta, file_name):  # method to write any category to txt file
        my_file = open(file_name, 'a')  # open file w/o rewove old data ('a' parameter)
        my_file.write(all_lenta)  # write any category to file
        my_file.close()  # close the file


class News(GlobalNewsLenta):
    '''class News - child'''
    def __init__(self, name, text, city):
        GlobalNewsLenta.__init__(self, name=name, text=text)  # inheritance of 2 parameters from parent class
        self.city = city  # attribute of city (specific for class News)

    def calc_of_publish_date(self):  # specific method of class News
        today = datetime.now().strftime("%d/%m/%Y %H.%M")  # calc current date in special format
        return today


class PrivateAdv(GlobalNewsLenta):
    '''class PrivateAdv - child'''
    def __init__(self, name, text, exp_date):
        GlobalNewsLenta.__init__(self, name=name, text=text)  # inheritance of 2 parameters from parent class
        self.exp_date = exp_date  # attribute of expiration date (specific for class PrivateAdv)

    def calc_of_left_days(self, exp_date): # specific method of class PrivateAdv
        exp_date = datetime.strptime(exp_date, '%d/%m/%Y').date()  # convert exp_date in date format
        date_diff = str((exp_date - date.today()).days)  # result convert to string and shows only diff of DAYS
        return date_diff


class LearningProgram(GlobalNewsLenta):
    '''class LearningProgram - child'''
    def __init__(self, name, text, start_date):
        GlobalNewsLenta.__init__(self, name=name, text=text)  # inheritance of 2 parameters from parent class
        self.start_date = start_date  # attribute of start_date (specific for class LearningProgram)

    def calc_of_days_before_start(self, start_date):  # specific method of class LearningProgram
        start_date = datetime.strptime(start_date, '%d/%m/%Y').date()  # convert start_date in date format
        date_diff = str((start_date - date.today()).days)  # result convert to string and shows only diff of DAYS
        return date_diff


class TextFile(GlobalNewsLenta):
    '''class for TextFile lenta'''
    def __init__(self, input_path):
        self.input_path = input()
        self.txt_file = ''

    def get_file(self, input_path):  # method to get file via input path
        try:
            txt_file = open(input_path, 'r')  # open file and read ('r' parameter)
            read_file = txt_file.read()  # read the file
            return read_file
        except FileNotFoundError:
            print(f'Incorrect file path: {input_path}')
        finally:
            txt_file.close()  # close the file
# with open(file, 'r') as f:
#     lines = f.readlines()
#     for line in lines:
#         pub_type = line[0]
#         if pub_type = "news":
#             city = line[1]
#             text = line[2]


def menu():
    '''create menu function for user input'''
    print('[1] Manual input')
    print('[2] From file')


menu()
input_source = input('Select source (1 or 2):')

'''for manual source'''
if input_source == '1':
    print('[1] Category 1 - News')
    print('[2] Category 2 - PrivateAdv')
    print('[3] Category 3 - LearningProgram')
    print('[0] Exit the program.')

    category = input('Select one category (1, 2 or 3):')

    if category == '1':  # category News
        text = input('Input text for your News:')  # param 1 for input text
        city = input('Input city:')  # param 2 for input city
        news = News('News', text, city)  # create object of class News with params
        all_lenta = '\n' + news.name + ' ' + '-'*25 + '\n' + news.text + '\n' + news.city + ', ' \
                + news.calc_of_publish_date() + '\n' + '-' * 30 + '\n'  # param all_lenta that concatinate News content
        news.write_to_file(all_lenta, 'lenta.txt')  # write all content of News to txt file

    elif category == '2':  # category PrivateAdv
        text = input('Input text of your PrivateAdv:')  # param 1 for input text
        exp_date = input('Input expiration date of your PrivateAdv in such format DD/MM/YYYY:')  # param 2 for input date
        pr = PrivateAdv('PrivateAdv', text, exp_date)  # create object of class PrivateAdv with params
        all_lenta = '\n' + pr.name + ' ' + '-' * 19 + '\n' + pr.text + '\n' + 'Actual until: ' + pr.exp_date + ', ' \
                + pr.calc_of_left_days(exp_date) + ' day(s) left' + '\n' +\
                '-' * 30 + '\n'  # param all_lenta that concatinate PrivateAdv content
        pr.write_to_file(all_lenta, 'lenta.txt')  # write all content of PrivateAdv to txt file

    elif category == '3':  # category Learning Program
        text = input('Input text of your Learning Program:') # param 1 for input text
        start_date = input('Input start date of the Learning Program in such format DD/MM/YYYY:')  # param 2 for input date
        learn = LearningProgram('LearningProgram', text, start_date)  # create object of class LearningProgram with params
        all_lenta = '\n' + learn.name + ' ' + '-' * 14 + '\n' + learn.text + '\n' + 'Start Date: ' + learn.start_date + '\n'\
                + 'Days before start: ' + learn.calc_of_days_before_start(start_date) + ' day(s)' + '\n'\
                + '-' * 30 + '\n'  # param all_lenta that concatinate Learning Program content
        learn.write_to_file(all_lenta, 'lenta.txt')  # write all content of Learning Program to txt file

    elif category == '0':  # category Exit of program
        exit()

    else:
        print('Invalid category. Please choose 1, 2 or 3.')

    print('Thanks for using this program. Goodbye.')

'''for file source'''
if input_source == '2':
    file_ext = input(r'Input file extension (like: .txt) :')  # param 1 for input
    file_path = input(r'Input path for file:')  # param 2 for input
    txt_file = TextFile(file_path)  # create object of class TextFile with params
    all_lenta = '\n' + txt_file.input_path + txt_file.get_file(file_path) + '\n' # param all_lenta that concatinate TextFile content
    txt_file.write_to_file(all_lenta, 'lenta.txt')  # write all content of TextFile to txt file
    if file_ext == '.txt':
        if file_path == '':
            print('Empty file path')

    print('Thanks for using this program. Goodbye.')












