import datetime
from collections import Counter

import math
import os
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
# array = [1,2,2,5,7,7,8,1,2] 

# def Search_Alement(array, al, count):
#     while array:
#         alement = array[0]
#         count_Alement = 0

#         alement2 = array[1]
#         count_Alement2 = 0          
#         al = 0
#         count = 0
#         z = len(array)
        
#         i=0
#         if len(array) < 2:return
#         while i < z:
#             if array[i] == alement: 
#                 count_Alement+=1
#                 array.remove(array[i])
#                 z-=1
#             elif array[i] == alement2:
#                 count_Alement2+=1
#                 array.remove(array[i])
#                 z-=1
#             else: i+=1
#         if count_Alement > count_Alement2:
#             al = int(alement)
#             count = count_Alement
#         else: 
#             al = int(alement2)
#             count = count_Alement2

#     return Search_Alement(array, al, count)

# al = Search_Alement(array, 1, int(input('->')))

# print(al)


