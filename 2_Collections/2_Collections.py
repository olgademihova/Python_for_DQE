# module 2, task 1
# create a list of random number of dicts (from 2 to 10)
# dict's random numbers of keys should be letter,
# dict's values should be a number (0-100),
# example: [{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]

import string  # import of module
import random  # import of module

dict_list = []  # empty list for dict list
for d in range(random.randint(2, 10)):  # random number of dictionaries (from 2 to 10)
    #size = 3  # size of dict = 3
    size = random.randint(1, 3)    # random dictionary size
    keys = random.sample(string.ascii_lowercase, size)  # random keys of letters in lowercase
    values = (random.randint(0, 100) for d in range(size))  # random values of numbers from 0 to 100
    one_dict = dict(zip(keys, values))                      # assemble dict
    dict_list.append(one_dict)                              # add it to the list

print(dict_list)  # see the result

# module 2, task 2
# get previously generated list of dicts and create one common dict:
# if dicts have same key, we will take max value, and rename key with dict number with max value
# if key is only in one dict - take it as is,
# example: {'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}

final_dict, tmp_dict, dict_keys = {}, {}, {}  # создаю новые пустые словари

for dictionary in dict_list:  # запускаю цикл по каждому элементу из словаря
    dict_num = dict_list.index(dictionary)+1  # это счетчик словарей в списке dict_list
    for k, v in dictionary.items():  # запускаю под-цикл по ключу и значению
        dict_keys[k+"_" + str(dict_num)] = v # маркирую каждый ключ в зависимости от номера словаря
        tmp_dict.setdefault(k, []).append(v)  # добавляю к каждому ключу значение для словаря tmp_dict
# print(tmp_dict)
# print(dict_keys)
for k, v in tmp_dict.items():  # теперь запускаю цикл по словарю tmp_dict
    if len(v) > 1:  # если ключ в словаре повторяется
        final_dict[str(list(dict_keys.keys())[list(dict_keys.values()).index(max(v))])] = max(v)  # то беру максимальное значение по ключу и переименовываю ключ
    else:
        final_dict[k] = v[0]  # иначе вывожу ключ-значение as-is
print(final_dict)  # смотрю результат