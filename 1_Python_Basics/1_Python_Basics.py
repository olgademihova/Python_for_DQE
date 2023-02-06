# module 1, task 1
# create list of 100 random numbers from 0 to 1000

from random import randint # обращаемся к модулю random для целых чисел
my_list = [randint(0, 1000) for i in range(100)] # формируем список из 100 рандомных целых чисел от 0 до 1000
print("List of 100 random numbers from 0 to 1000:", my_list) #смотрим результат

# module 1, task 2
# sort list from min to max (without using sort())

for i in range(len(my_list)): # цикл по элементам списка
     for j in range(i + 1, len(my_list)): # для каждого следующего элемента списка
         if my_list[i] > my_list[j]: # сравниваем текущий со следующим, если текущий больше следующего
             my_list[i], my_list[j] = my_list[j], my_list[i] # то меняем их местами
print("Sort list from min to max:", my_list) # смотрим результат

# module 1, task 3
#  calculate average for even and odd numbers
#  print both average result in console

even_list = []  # пустой список из четных чисел
odd_list = []   # пустой список из нечетных чисел
for d in my_list:  # цикл для каждого числа из моего списка
    if d % 2 == 0:  # если остаток от деления на 2 равен 0
        even_list.append(d) # то добавляем это число в список четных чисел
    else: # если остаток от деления на 2 НЕ равен 0
        odd_list.append(d) # то добавляем это число в список НЕчетных чисел
try:
    avrg_even_list = sum(even_list)/len(even_list) # формируем среднее арифметическое для четных чисел. Сумму четных чисел делим на кол-во четных числе
    print("Average for even numbers:", avrg_even_list)  # смотрим результат
except ZeroDivisionError as z: # обработка ошибки деления на ноль
    print(z)
try:
    avrg_odd_list = sum(odd_list)/len(odd_list) # формируем среднее арифметическое для НЕчетных чисел. Сумму НЕчетных чисел делим на кол-во НЕчетных чисел
    print("Average for odd numbers:", avrg_odd_list)  # смотрим результат
except ZeroDivisionError as z: # обработка ошибки деления на ноль
    print(z)


