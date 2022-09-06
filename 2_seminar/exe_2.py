import os
os.system('CLS')

# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов в виде списка
# *Пример:*
# - Для N = 5: 1, -3, 9, -27, 81

def inputFloat(prompt=None):  # ПРОВЕРКА НА INT
    while True:
        n = input(prompt)
        try:
            return int(n)
        except ValueError:
            print('Ошибка. Ожидалось вещественное число.')
number = inputFloat('Введите количество элементов: ')
print('Вы ввели', number)

for i in range(number):
    print(((-3)**i), end= ' ')
    
# print(*[(-3) ** i for i in range(int(input('Введите количество элементов: ')))])

# 2.Найти сумму элементов массива, лежащих между максимальным и минимальным по значению элементами

from distutils.command.clean import clean
from itertools import count
from random import randint
from turtle import clear


# list = [2, 5, 1, 9, 4]

# def min_max(list):
#     min = list[0]
#     max = list[0]
#     i_min = 0
#     i_max = 0
#     i = 0
#     while i < len(list):
#         if min > list[i]:
#             min = list[i]
#             i_min = i
#         elif max < list[i]:
#             max = list[i]
#             i_max = i
#         i+=1
#     print(f' max = {max}, min = {min}, i_max = {i_max}, i_min = {i_min}')

    
#     if i_max < i_min:
#         i = i_max
#         sum = 0
#         while i <= i_min:
#             sum = sum +list[i]
#             i+=1
#     else: 
#         i = i_min
#         sum = 0
#         while i <= i_max:
#             sum = sum +list[i]
#             i+=1
#     print(sum)
  
# min_max(list)


# 3.Найдите количество элементов массива, которые отличны от наибольшего элемента не более чем на 10% ( 10% от наибольшего)


# os.system('CLS')
# list = [randint(1, 20) for i in range(10)]
# print(list, end= ' ')
# max = list[0]
# count = 0
# for i in list[1:]:
#     if i > max:
#         max = i
# for i in list:    
#     if max*0.9 < i and i != max:
#         count+=1
    
# print(max, end= ' ')
# print(f'количество чисел 10% = {count}')

