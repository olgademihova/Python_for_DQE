import pyodbc
import sqlite3


class DB:
    """create a method to connect to db"""
    def __init__(self, database_name):
        with sqlite3.connect(database_name) as self.conn:
            self.cur = self.conn.cursor()  # create a cursor

    """create a method of Creation the table in db"""
    def create(self, table_name, field1_name, field1_type, field2_name, field2_type, field3_name, field3_type):
        self.cur.execute(f'CREATE TABLE IF NOT EXISTS {table_name} ({field1_name} {field1_type}, {field2_name} {field2_type}, {field3_name} {field3_type}, CONSTRAINT unique_{table_name} UNIQUE ({field1_name}, {field2_name}, {field3_name}))')
        return self.cur.fetchall()

    """create a method of Creation the guess table in db"""
    def create_guess(self, table_name, field1_name, field1_type, field2_name, field2_type):
        self.cur.execute(f'CREATE TABLE IF NOT EXISTS {table_name} ({field1_name} {field1_type}, {field2_name} {field2_type}, CONSTRAINT unique_{table_name} UNIQUE ({field1_name}, {field2_name}))')
        return self.cur.fetchall()

    """create a method of insert news in db"""
    def insert_news(self, field1, field2, field3):
        insert_with_param = """INSERT INTO news (description, location, date_news) VALUES (?, ?, ?) """
        data = (field1, field2, field3)
        self.cur.execute(insert_with_param, data)
        self.conn.commit()  # !!!

    """create a method of insert adv in db"""
    def insert_adv(self, field1, field2, field3):
        insert_with_param = """INSERT INTO advertising (description, exp_date, days_left) VALUES (?, ?, ?) """
        data = (field1, field2, field3)
        self.cur.execute(insert_with_param, data)
        self.conn.commit()

    """create a method of insert guess in db"""
    def insert_guess(self, field1, field2):
        insert_with_param = """INSERT INTO guess (question, answer) VALUES (?, ?) """
        data = (field1, field2)
        self.cur.execute(insert_with_param, data)
        self.conn.commit()

    """create a method of select from db"""
    def select(self, field1, field2, field3, table_name):
        self.cur.execute(f'select {field1}, {field2}, {field3} from {table_name}')
        return self.cur.fetchall()

    """create a method of select guess from db"""
    def select_guess(self, field1, field2, table_name):
        self.cur.execute(f'select {field1}, {field2} from {table_name}')
        return self.cur.fetchall()


def save_news_to_db(database_name, news_text, news_loc, news_date):
    """create a function that save news data to db"""
    try:
        dbcon = DB(database_name)
        dbcon.create('news', 'description', 'text', 'location', 'text', 'date_news', 'text')
        dbcon.insert_news(news_text, news_loc, news_date)
    except Exception as e:
        print('The record exists in db', e)


def save_adv_to_db(database_name, adv_text, adv_date, adv_days):
    """create a function that save adv data to db"""
    try:
        dbcon = DB(database_name)
        dbcon.create('advertising', 'description', 'text', 'exp_date', 'text', 'days_left', 'text')
        dbcon.insert_adv(adv_text, adv_date, adv_days)
    except Exception as e:
        print('The record exists in db', e)


def save_guess_to_db(database_name, guess_ask, guess_ans):
    """create a function that save guess data to db"""
    try:
        dbcon = DB(database_name)
        dbcon.create_guess('guess', 'question', 'text', 'answer', 'text')  # call the create method
        dbcon.insert_guess(guess_ask, guess_ans)  # call the insert_guess method
    except Exception as e:
        print('The record exists in db', e)





# dbcon = DB('10test.db')   # object of class DB
# create = dbcon.create('news', 'description', 'text', 'location', 'text', 'date_news', 'date')  # call the create method
# insert = dbcon.insert_news('something happened', 'London', '2023-03-23')  # call the insert_news method
# select = dbcon.select('description', 'location', 'date_news', 'news')  # call the select method
# print(select)
#print(a[0][0])

# create_adv = dbcon.create('advertising', 'description', 'text', 'exp_date', 'text', 'days_left', 'text')  # call the create method
# insert_adv = dbcon.insert_adv('sell the bike', '2023/03/30', 7)  # call the insert_adv method
# select_adv = dbcon.select('description', 'exp_date date', 'days_left', 'advertising')  # call the select method
# print(select_adv)


# create_guess = dbcon.create_guess('guess', 'question', 'text', 'answer', 'text')  # call the create method
# insert_guess = dbcon.insert_guess('yes or no?', 'yes')  # call the insert_guess method
# select_guess = dbcon.select_guess('question text', 'answer text', 'guess')  # call the select method
# print(select_guess)


