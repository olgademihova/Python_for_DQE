import datetime
from locale import normalize
import random
import text_statistic as ts
import database as db


class PrintMessage:
    def __init__(self, message, file_name):
        self.message = message
        self.file_name = file_name  # file name

    # create a method which inserts the formatted text into text file
    def print_message(self):
        ptf = open(self.file_name, "a")      # open file to add data
        print(self.message, file=ptf)
        ptf.close()                            # close file

        with open(self.file_name, "r") as file2:   # open file on read mode
            ts.update_counts(file2)     # call the function to update words/letters statistic


class News:
    def __init__(self, news_msg, location, file_name):
        self.news_msg = news_msg               # news_info
        self.location = location               # location where it has happened
        self.file_name = file_name  # file name

    # create a method which creates a news (text, city, time)
    def news_message(self):
        message = f'News ----------------------------\n{self.news_msg}\n{self.location},' \
                  f'{datetime.datetime.now().strftime("%d/%m/%Y %H:%M")}\n' \
                  f'---------------------------------\n\n'
        PrintMessage(normalize(message), self.file_name).print_message()  # call the method to print msg in file
        dbcon = db.DB('10test.db')  #obj of class DB
        dbcon.save_news_in_db(self.news_msg, self.location, datetime.datetime.now().strftime("%d/%m/%Y %H:%M"))
        print(dbcon.select('description', 'location', 'date_news', 'news'))



class Advertising:
    def __init__(self, adv_message, expired_dt, file_name):
        self.adv_message = adv_message  # text of adv msg
        self.file_name = file_name  # file name
        self.expired_dt = expired_dt  # expired date of adv

    # create a method which creates an advertisement (text, expiration day, how many days left)
    def advertising(self):
        message = f'Private Ad -----------------------\n{self.adv_message}\n' \
                  f'Actual until: {self.expired_dt},' \
                  f'{(datetime.datetime.strptime(self.expired_dt, "%d/%m/%Y") - datetime.datetime.now()).days} days left\n' \
                  f'----------------------------------\n\n'
        PrintMessage(normalize(message), self.file_name).print_message()  # call the method to print msg in file


class Guess:
    def __init__(self, guessing, file_name):
        self.guessing = guessing  # text of guess
        self.file_name = file_name  # file name

    # create an interactive method with indicating possibility using random elements from list
    def ask_future(self):
        """create a list of answers"""
        test_list = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes – definitely', 'As I see it, yes',
                        'Most likely', 'Ask again later', 'Better not tell you now', 'Cannot predict now',
                        'Don\'t count on it', 'My reply is no', 'My sources say no', 'Very doubtful']
        random_test_list = random.randint(0, len(test_list) - 1)   # choose random element from the list
        prediction = f'Ask me about your future? --------\n' \
                     f'Your question - "{self.guessing}",\n' \
                     f'Witch\'s answer will be - {test_list[random_test_list]}\n' \
                     f'----------------------------------\n\n'
        PrintMessage(normalize(prediction), self.file_name).print_message()  # call the method to print msg in file


#create a function for user input text and location
def add_news(file_name):  # add file_name
    text = input('Please enter news text:\n')
    location = input('Please enter location:\n')
    news = News(text, location, file_name)  # create an object with params
    news.news_message()  # call the method of News class


#create a function for user input text and exp date
def add_adv(file_name):  # add file_name
    text = input('Please enter advertisement text:\n')
    exp_dt = input('Please enter expire date in the format dd/mm/yyyy:\n')
    adv = Advertising(text, exp_dt, file_name)  # create an object with params
    adv.advertising()  # call the method of Advertising class


#create a function for user input text
def add_guess(file_name):  # add file_name
    guessing = input('Ask me about your near future:\n')
    guess = Guess(guessing, file_name)  # create an object with params
    guess.ask_future()  # call the method of Guess class






