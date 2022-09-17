import datetime
from collections import Counter
from functools import reduce

import math
from multiprocessing.sharedctypes import Value
import os
import random
os.system('CLS')

# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
# ['gfh5', 'gfh2', '67', 'jy32', '3put'] - ищем 32 - находим по индексу 3

# word = ['gfh5', 'gfh2', '67', 'jy32', '3put']
# n = '32'
# count = 0
# for i in word:
#     if n in i:
#         print(i, 'индекс ', count)
#     count+=1

# Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
# Пример:
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

# word = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
# n = 'йцу'

# def Word_Search(word, n):
#     count = 0
#     count2 = 0
#     for i in word:
#         if n == i:
#             count2+=1
#         if count2 >1:
#             return count
#         count+=1
#     else: return -1
# print(Word_Search(word, n))

'''
Для натурального n создать словарь индекс-значение, 
состоящий из элементов последовательности 3n + 1.
Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
'''

# def number(number):
#     d = {}
#     for i in range(1, number+1):
#         d[i] = 3 * i + 1
#     print(d)
# number = number(int(input('-> ')))

'''
Найти наиболее часто встречающийся элемент в массиве целых чисел.
'''

# numbers = [random.randrange(1, 15, 1) for i in range(15)]

# max = 0
# v_max = 0
# max_al = ''
# j = 0
# while j < len(numbers):
#     alement = numbers[j]
#     count = 0
#     for i in numbers:
        
#         if i == alement:
#             count+=1
    
#     v_max = count
#     if v_max > max:
#         max = v_max
#         max_al = alement
#     j+=1
# print(numbers)
# print(f'число {max_al} повторяется {max} раз(а)')

numbers = [random.randrange(1, 5, 1) for i in range(10)]
print(numbers)
max = 0
v_max = 0
max_al = ''
j = 0
while j < len(numbers):
    alement = numbers[0]
    count = 0
    i=numbers[0]
    while i in numbers:
        
        if i == alement:
            count+=1
            numbers.remove(i)
    
    v_max = count
    if v_max > max:
        max = v_max
        max_al = alement
    j+=1

print(f'число {max_al} повторяется {max} раз(а)')