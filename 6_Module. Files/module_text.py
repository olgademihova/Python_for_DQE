import os
from locale import normalize
from modules_5_6 import PrintMessage
# sol 2


class File:

    def __init__(self, output_file_name):
        self.output_file_name = output_file_name

    def get_file_path(self):
        original_path = os.path.dirname(os.path.realpath(__file__))
        print(f'Your default directory is "{os.getcwd()}"')
        is_true = True
        while is_true:
            answer = int(input(
                f'If you want to ingest your file from default directory - enter 1, if you want to change it - enter 2: '))
            if answer == 1:
                while True:
                    try:
                        file_name = input('Enter the file name with its format: ')
                        with open(file_name, "r", encoding='utf-8') as source:
                            f_contents = source.readlines()
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
                        with open(file_name, "r", encoding='utf-8') as source:
                            f_contents = source.readlines()
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

    def write_to_file(self):
        f_contents, path_for_remove = get_file_content()
        num_records = int(input("Enter records num:\n"))
        count = 0
        for i, line in enumerate(f_contents):
            if line == '\n':
                count += 1
                if count == 2 * num_records:
                    f_contents_new = f_contents[:i + 1]
                    break
        with open(self.output_file_name, "a", encoding='utf-8') as file:
            file.writelines(f_contents_new)
        print(f'This file {path_for_remove} will be removed now\n')
        os.remove(path_for_remove)

