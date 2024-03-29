import datetime
from locale import normalize
import random
import text_statistic as ts
from database import save_news_to_db, save_adv_to_db, save_guess_to_db


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
    def __init__(self, news_msg, location, file_name, date_news=datetime.datetime.now().strftime("%d/%m/%Y %H:%M")):
        self.news_msg = news_msg               # news_info
        self.location = location               # location where it has happened
        self.file_name = file_name  # file name
        self.date_news = date_news

    # create a method which creates a news (text, city, time)
    def news_message(self):
        message = f'News ----------------------------\n{self.news_msg}\n{self.location},' \
                  f'{self.date_news}\n' \
                  f'---------------------------------\n\n'
        PrintMessage(normalize(message), self.file_name).print_message()  # call the method to print msg in file


class Advertising:
    def __init__(self, adv_message, expired_dt, file_name):
        self.adv_message = adv_message  # text of adv msg
        self.file_name = file_name  # file name
        self.expired_dt = expired_dt  # expired date of adv
        self.adv_days_left = (datetime.datetime.strptime(expired_dt, "%d/%m/%Y") - datetime.datetime.now()).days

    # create a method which creates an advertisement (text, expiration day, how many days left)
    def advertising(self):
        message = f'Private Ad -----------------------\n{self.adv_message}\n' \
                  f'Actual until: {self.expired_dt},' \
                  f'{self.adv_days_left} days left\n' \
                  f'----------------------------------\n\n'
        PrintMessage(normalize(message), self.file_name).print_message()  # call the method to print msg in file


class Guess:
    def __init__(self, guessing, file_name):
        self.guessing = guessing  # text of guess
        self.file_name = file_name  # file name
        self.ans = ""

    # create an interactive method with indicating possibility using random elements from list
    def ask_future(self):
        """create a list of answers"""
        test_list = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes – definitely', 'As I see it, yes',
                        'Most likely', 'Ask again later', 'Better not tell you now', 'Cannot predict now',
                        'Don\'t count on it', 'My reply is no', 'My sources say no', 'Very doubtful']
        random_test_list = random.randint(0, len(test_list) - 1)   # choose random element from the list
        self.ans = test_list[random_test_list]
        prediction = f'Ask me about your future? --------\n' \
                     f'Your question - "{self.guessing}",\n' \
                     f'Witch\'s answer will be - {self.ans}\n' \
                     f'----------------------------------\n\n'
        PrintMessage(normalize(prediction), self.file_name).print_message()  # call the method to print msg in file


#create a function for user input text and location
def add_news(file_name):  # add file_name
    text = input('Please enter news text:\n')
    location = input('Please enter location:\n')
    news = News(text, location, file_name)  # create an object with params
    news.news_message()  # call the method of News class
    # print(news.news_msg, news.location, news.date_news)
    save_news_to_db('10test.db', news.news_msg, news.location, news.date_news)  # call the function to save news to db


#create a function for user input text and exp date
def add_adv(file_name):  # add file_name
    text = input('Please enter advertisement text:\n')
    exp_dt = input('Please enter expire date in the format dd/mm/yyyy:\n')
    adv = Advertising(text, exp_dt, file_name)  # create an object with params
    adv.advertising()  # call the method of Advertising class
    save_adv_to_db('10test.db', adv.adv_message, adv.expired_dt, adv.adv_days_left)  # call the function to save adv to db


#create a function for user input text
def add_guess(file_name):  # add file_name
    guessing = input('Ask me about your near future:\n')
    guess = Guess(guessing, file_name)  # create an object with params
    guess.ask_future()  # call the method of Guess class
    save_guess_to_db('10test.db', guess.guessing, guess.ans)  # call the function to save guess to db






