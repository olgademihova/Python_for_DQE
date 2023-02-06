# module 2, task 1
# create a list of random number of dicts (from 2 to 10)
# dict's random numbers of keys should be letter,
# dict's values should be a number (0-100),
# example: [{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]

import string  # import of module
import random  # import of module

dictList = []  # empty list for dict list
for d in range(random.randint(2, 10)):  # random number of dictionaries (from 2 to 10)
    #size = 3  # size of dict = 3
    size = random.randint(1, 3)    # random dictionary size
    keys = random.sample(string.ascii_lowercase, size)  # random keys of letters in lowercase
    values = (random.randint(0, 100) for d in range(size))  # random values of numbers from 0 to 100
    oneDict = dict(zip(keys, values))                      # assemble dict
    dictList.append(oneDict)                              # add it to the list

print(dictList)  # see the result

# module 2, task 2
# get previously generated list of dicts and create one common dict:
# if dicts have same key, we will take max value, and rename key with dict number with max value
# if key is only in one dict - take it as is,
# example: {'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}

# dict_merged = {}
# for

