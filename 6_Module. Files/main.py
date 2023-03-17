from modules_5_6 import PrintMessage, News, Advertising, Guess, add_news, add_adv, add_guess
from module_json import JSONInput
import os
from module_text import File, TextFile


# Function for main menu call
def menu():
    print('Please enter your choice:',
          '1 - Add News',
          '2 - Add Private Ad',
          '3 - Add Divination',
          '4 - Add data from TEXT file',
          '5 - Add data from JSON file',
          '6 - Add data from XML file',
          '7 - Add data from Database',
          '8 - Exit', sep='\n')


# ask a user what data he wants to print and then call a class and insert the data into file using inserting method
if __name__ == "__main__":
    while True:
        menu()
        flag = input('Choose the appropriate number: ')
        if flag == '1':
            add_news()
        elif flag == '2':
            add_adv()
        elif flag == '3':
            add_guess()
        elif flag == '4':
            #sol 1
            #FromAnotherSource().read_file('Module6_paste.txt')
            # sol 2
            TextFile('Module6_paste.txt').write_to_file()

            # f_contents_new, path_for_remove = FromAnotherSource().read_file()
            # with open("Module6_paste.txt", "a", encoding='utf-8') as file:
            #     file.writelines(f_contents_new)
            # print(f'This file {path_for_remove} will be removed now\n')
            # os.remove(path_for_remove)
        elif flag == '5':
            JSONInput('Module6_paste.txt').parse_file()
            pass
        elif flag == '6':
            pass
        elif flag == '7':
            pass
        elif flag == '8':
            print('That is all. Thank you. Goodbye.')
            break
        else:
            print('Try again')
