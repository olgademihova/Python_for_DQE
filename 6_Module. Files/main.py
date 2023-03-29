from manual_input import add_news, add_adv, add_guess
from file_input import TextFile, JSONFile, XMLFile
# from database import DB


# Function for main menu call
def menu():
    print('Please enter your choice:',
          '1 - Add News',
          '2 - Add Private Ad',
          '3 - Add Divination',
          '4 - Add data from TEXT file',
          '5 - Add data from JSON file',
          '6 - Add data from XML file',
          '7 - Exit', sep='\n')


# ask a user what data he wants to print and then call a class and insert the data into file using inserting method
if __name__ == "__main__":
    target_file_name = input("Please specify target file name (ex. news_feed.txt): ")   # input target file name
    while True:
        menu()
        flag = input('Choose the appropriate number: ')
        if flag == '1':
            add_news(target_file_name)  # call the function of News for input data
        elif flag == '2':
            add_adv(target_file_name)  # call the function of Advertising for input data
        elif flag == '3':
            add_guess(target_file_name)  # call the function of Guess for input data
        elif flag == '4':
            TextFile(target_file_name).parse_file()  # call the method of TextFile class to parse data
            #sol 1
            #FromAnotherSource().read_file('Module6_paste.txt')
            # sol 2
            # TextFile('Module6_paste.txt').write_to_file()

            # f_contents_new, path_for_remove = FromAnotherSource().read_file()
            # with open("Module6_paste.txt", "a", encoding='utf-8') as file:
            #     file.writelines(f_contents_new)
            # print(f'This file {path_for_remove} will be removed now\n')
            # os.remove(path_for_remove)
        elif flag == '5':
            JSONFile(target_file_name).parse_file()  # call the method of JSONFile class to parse data
            # JSONInput('Module6_paste.txt').parse_file()
        elif flag == '6':
            XMLFile(target_file_name).parse_file()  # call the method of XMLFile class to parse data
        elif flag == '7':
            print('That is all. Thank you. Goodbye.')   # exit of program
            break
        else:
            print('Try again')
