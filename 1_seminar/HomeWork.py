
from ast import Del
from os import remove
from random import randint
import string
                                                # Задача 1

# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# a = int(input("Введите день недели: "))
# if a==6 or a==7:
#     print("Спим")
# elif a>=1 and a <=5:
#     print("Go трудиться")
# else: print("не понтно что делать!")


                                                # Задача 2

#Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.                                                
# ⋁ или ложь, когда оба ложь
# ⋀ и   истина, когда оба истина
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# x y z 
# 0 0 0  1 = 1
# 0 0 1  0 = 0
# 0 1 0  0 = 0
# 0 1 1  0 = 0
# 1 0 0  0 = 0
# 1 0 1  0 = 0
# 1 1 0  0 = 0
# 1 1 1  0 = 0 


# x = int(input(' x = '))
# y = int(input(' y = '))
# z = int(input(' z = '))

# i = 0
# xyz = list(range(1,4))
# while i < 3:
#     num = randint(0,1)
#     xyz[i] = num
#     i += 1
# print(xyz)

# x = xyz[0]
# y = xyz[1]
# z = xyz[2]
# left = not(x or y or z)
# right = (not x) and (not y) and (not z)
# if left == right:
#     print(True)
# else: print(False)


#                                                     # Задача 3

# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

# from tkinter import Y


# x = int(input('Введите x: '))
# y = int(input('Введите y: '))

# if x > 0 and y > 0:
#     print('точка находится в 1 четверти')
# elif x < 0 and y > 0:
#     print('точка находится во 2 четверти')
# elif x < 0 and y < 0:
#     print('точка находится в 3 четверти')
# else:
#     print('точка находится в 4 четверти')

#                                                     #    Задача 4

# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

# a = int(input('Введите четверть: ->'))
# if a == 1:
#     print(f'диапазон возможных координат x > 0 и y > 0')
# elif a == 2:
#     print(f'диапазон возможных координат x < 0 и y > 0')
# elif a == 3:
#     print(f'диапазон возможных координат x < 0 и y < 0')
# elif a == 4:
#     print(f'диапазон возможных координат x > 0 и y < 0')
# else:
#     print('такого диатазона не существует')

                                                    #    Задача 5

# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
# import math

# Xa = float(input('Введите координат точки А на оси x '))
# Xb = float(input('Введите координат точки В на оси x '))
# Ya = float(input('Введите координат точки А на оси y '))
# Yb = float(input('Введите координат точки В на оси y '))
# ab = math.sqrt((Xb - Xa)**2 + (Yb - Ya)**2)
# print(ab)

# print('{:.2f}'.format(ab))

# import math
# num = 25
# sqrt = math.sqrt(num)
# print("Квадратный корень из числа " + str(num) + " это " + str(sqrt))

                                                #    Задача ДОП

# Требуется найти N-е число Фибоначчи.

# fib1 = 1
# fib2 = 1
# n = int(input('Введите число: '))
# i = 0
# while i < n-2:
#     fib = fib1 + fib2
#     fib1 = fib2
#     fib2 = fib
#     i+=1
# print(fib)

# fib1 = 1
# fib2 = 1

# i = 0

# def inputFloat(prompt=None):  # ПРОВЕРКА НА INT
#     while True:
#         n = input(prompt)
#         try:
#             return int(n)
#         except ValueError:
#             print('Ошибка. Ожидалось вещественное число.')
# f = inputFloat('Введите число: ')
# print('Вы ввели', f)
# while i < f-2:
#     fib = fib1 + fib2
#     fib1 = fib2
#     fib2 = fib
#     i+=1
# print(fib)

