import string  # import of module
import random  # import of module


def create_list_of_dicts(num_of_dicts, size_of_dict):
    dict_list = []  # empty list for dict list
    for d in range(num_of_dicts):  # random number of dictionaries (from 2 to 10)
        keys = random.sample(string.ascii_lowercase, size_of_dict)  # random keys of letters in lowercase
        values = (random.randint(0, 100) for d in range(size_of_dict))  # random values of numbers from 0 to 100
        one_dict = dict(zip(keys, values))                      # assemble dict
        dict_list.append(one_dict)                              # add it to the list
    return dict_list


result = create_list_of_dicts(3, 3)  # set any number of dicts and set any size of each dict
print(result)  # see the result


def one_dict(dict_list):
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
    return final_dict


result2 = one_dict(result)
print(result2)  # смотрю результат