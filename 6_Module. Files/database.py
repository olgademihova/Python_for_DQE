import pyodbc
import sqlite3


class DB:
    def __init__(self, database_name):
        with sqlite3.connect(database_name) as self.conn:
            self.cur = self.conn.cursor()

    def create(self, table_name, field1, field2, field3):
        self.cur.execute(f'CREATE TABLE IF NOT EXISTS {table_name} ({field1}, {field2}, {field3})')
        return self.cur.fetchall()

    def create_guess(self, table_name, field1, field2):
        self.cur.execute(f'CREATE TABLE IF NOT EXISTS {table_name} ({field1}, {field2})')
        return self.cur.fetchall()

    def insert_news(self, field1, field2, field3):
        insert_with_param = """INSERT INTO news (description, location, date_news) VALUES (?, ?, ?) """
        data = (field1, field2, field3)
        self.cur.execute(insert_with_param, data)
        return self.cur.fetchall()

    def insert_adv(self, field1, field2, field3):
        insert_with_param = """INSERT INTO advertising (description, exp_date, days_left) VALUES (?, ?, ?) """
        data = (field1, field2, field3)
        self.cur.execute(insert_with_param, data)
        return self.cur.fetchall()

    def insert_guess(self, field1, field2):
        insert_with_param = """INSERT INTO guess (question, answer) VALUES (?, ?) """
        data = (field1, field2)
        self.cur.execute(insert_with_param, data)
        return self.cur.fetchall()

    def select(self, field1, field2, field3, table_name):
        self.cur.execute(f'select {field1}, {field2}, {field3} from {table_name}')
        return self.cur.fetchall()

    def select_guess(self, field1, field2, table_name):
        self.cur.execute(f'select {field1}, {field2} from {table_name}')
        return self.cur.fetchall()


dbcon = DB('10test.db')   # object of class DB
create = dbcon.create('news', 'description text', 'location text', 'date_news date')  # call the create method
insert = dbcon.insert_news('something happened', 'London', '2023-03-23')  # call the insert_news method
select = dbcon.select('description', 'location', 'date_news', 'news')  # call the select method
print(select)
#print(a[0][0])

create_adv = dbcon.create('advertising', 'description text', 'exp_date date', 'days_left real')  # call the create method
insert_adv = dbcon.insert_adv('sell the bike', '2023/03/30', 7)  # call the insert_adv method
select_adv = dbcon.select('description', 'exp_date date', 'days_left', 'advertising')  # call the select method
print(select_adv)


create_guess = dbcon.create_guess('guess', 'question text', 'answer text')  # call the create method
insert_guess = dbcon.insert_guess('yes or no?', 'yes')  # call the insert_guess method
select_guess = dbcon.select_guess('question text', 'answer text', 'guess')  # call the select method
print(select_guess)


