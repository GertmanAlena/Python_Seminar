                                                # Задача 1
# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# a = int(input("Введите день недели: "))
# if a==6 or a==7:
#     print("Сегодня выходной")
# elif a>=1 and a <=5:
#     print("Сегодня на работу")
# else: print("Такого дня нет!")


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

from cmath import sqrt


Xa = int(input('Введите координат точки А на оси x '))
Xb = int(input('Введите координат точки В на оси x '))
Ya = int(input('Введите координат точки А на оси y '))
Yb = int(input('Введите координат точки В на оси y '))
ab = int(sqrt((Xb - Xa)**2 + (Yb - Ya)**2))
print(ab)

