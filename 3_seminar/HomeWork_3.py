from audioop import mul
from functools import reduce
import math
import os
os.system('CLS')


            # 1- Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
            # Пример:
                    # [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
# import random_numb
# numbers = random_numb.Random_Number()
# print(numbers)

# def Summa_Numbers(numbers2):
#     sum: int = 0
#     for i in numbers2:
#         sum = sum + i
#     return sum

# numbers2 = numbers[1::2]
# print(numbers2)

# print(Summa_Numbers(numbers2))

# '''второй вариант решения задачи'''
# print(numbers[1::2])
# print (sum(numbers[1::2]))

        # 2-Напишите программу, которая найдёт произведение пар чисел списка. 
        # Парой считаем первый и последний элемент, второй и предпоследний и т.д.
        # Пример: [2, 3, 4, 5, 6] => [12, 15, 16];    [2, 3, 5, 6] => [12, 15]

# import random_numb
# First_List = random_numb.Random_Number()
# '''импортировала из вайла рандомно создание списка'''
# print('First_List ', First_List)

# def Proizved_Alem(First_List): 
#     '''функция умножения элементов'''
#     if len(First_List) % 2 == 0:
#         size = len(First_List)/2
#     else:
#         size = int((len(First_List)/2)+0.5)
        
#     Res_List = []
#     i=0
#     while i <= size-1:
#         Res_List.append(First_List[i]*First_List[(i+1)*-1])
#         i+=1
#     # print('Res_List   ', Res_List)
#     return Res_List

# print('Res_List   ', Proizved_Alem(First_List))

# 3-Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:

# [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
# [4.07, 5.1, 8.2444, 6.98] - 0.91 или 91

num = [4.07, 5.1, 8.2444, 6.98]
print('num -> ', num)
num2 = []
for i in num:
    i =("{:.2f}".format(i))
    num2.append(i)
print('num2 -> ',num2)
num3 = []
for i in num:
    num3.append(i)
print('num3 -> ',num3)

print(round(max(num3)-min(num3),2))


# 4- Напишите программу, которая будет преобразовывать десятичное число в двоичное. 
# Подумайте, как это можно решить с помощью рекурсии.

# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10


# 5-Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:

# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи
# Решение оформлять в виде функций
# По возможности добавляйте docstring