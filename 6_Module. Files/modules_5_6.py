import datetime
import os
from locale import normalize
import random
import module_7 as m7


class PrintMessage:
    def __init__(self, message):
        self.message = message

    # create a method which inserts the formatted text into text file
    def print_message(self):
        ptf = open("Module6_paste.txt", "a")      # open file to add
        print(self.message, file=ptf)
        ptf.close()                            # close file

        with open("Module6_paste.txt", "r") as file2:
            m7.update_counts(file2)


class News:
    def __init__(self, news_msg, location):
        self.news_msg = news_msg               # news_info
        self.location = location               # location where it has happened

    # create a method which creates a news (text, city, time)
    def news_message(self):
        message = f'News ----------------------------\n{self.news_msg}\n{self.location},' \
                  f'{datetime.datetime.now().strftime("%d/%m/%Y %H:%M")}\n' \
                  f'---------------------------------\n\n'
        PrintMessage(normalize(message)).print_message()


class Advertising:
    def __init__(self, adv_message, actual_until=None):
        self.adv_message = adv_message
        self.actual_until = actual_until

    # create a method which creates an advertisement (text, expiration day, how many days left)
    def advertising(self):
        message = f'Private Ad -----------------------\n{self.adv_message}\n' \
                  f'Actual until: {self.actual_until},' \
                  f'{(datetime.datetime.strptime(self.actual_until, "%d/%m/%Y") - datetime.datetime.now()).days} days left\n' \
                  f'----------------------------------\n\n'
        PrintMessage(normalize(message)).print_message()


class Guess:
    def __init__(self, guessing):
        self.guessing = guessing

    # create an interactive method with indicating possibility using random elements from list
    def ask_future(self):
        test_list = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes – definitely', 'As I see it, yes',
                        'Most likely', 'Ask again later', 'Better not tell you now', 'Cannot predict now',
                        'Don\'t count on it', 'My reply is no', 'My sources say no', 'Very doubtful']
        random_test_list = random.randint(0, len(test_list) - 1)
        prediction = f'Ask me about your future? --------\n' \
                     f'Your question - "{self.guessing}",\n' \
                     f'Witch\'s answer will be - {test_list[random_test_list]}\n' \
                     f'----------------------------------\n\n'
        PrintMessage(normalize(prediction)).print_message()


def add_news():
    news = News(input('Please enter news text:\n'),
                input('Please enter location:\n'))
    news_mess = news
    news_mess.news_message()


def add_adv():
    advng = Advertising(input('Please enter advertisement text:\n'),
                        input('Please enter expire date in the format dd/mm/yyyy:\n'))
    adv_message = advng
    adv_message.advertising()


def add_guess():
    guessing = Guess(input('Ask me about your near future:\n'))
    question_divination = guessing
    question_divination.ask_future()



