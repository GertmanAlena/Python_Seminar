from enum import Flag
import math
from random import randint
from re import A
# print(list(range(10)))
# print(list(range(10+1)))
# print(list(range(2,4)))
# print(list(range(10, 0, -1)))
# print(list(range(10, 0-1, -1)))

# flag = True
# i=0
# while flag:
#     i+=1
#     if i == 22:
#         flag = False
# print(i)


#Принимаем дробное число и выводим первую цифру после запятой
# a = float(input('Введите дробное число: '))
# print(int(a * 10) % 10)

#Принимаем число и проверяем кратно ли оно 5, 10 или 15, но не 30

# number = int(input('Введите число: '))

# if (number % 5 == 0 and number % 10 == 0) or (number % 15 == 0 and number % 30 != 0):
#     print('Yes')
# else:
#     print('No')


# найти второй максимум
# n = int(input())
# max1 = n
# max2 = -1
# while n != 0: #пока не введём 0
#     n = int(input())
#     if n > max1:
#         max2 = max1
#         max1 = n
#     elif n > max2:
#         max2 = n
# print(max2)

# найти сумму минимума и максимума

# num = [2, 8, -9, 7, 55, -1, 41]
# max = num[0]
# min = num[1]
# for i in num:
#     if i > max:
#         max = i
#     elif i < min:
#         min = i
# sum = min + max
# print(sum)

# coll = int(input('...'))
# min = int(input('min -> '))
# max = int(input('max -> '))

# num = [randint(min, max) for i in range(coll)]
# print(num)
# max = num[0]
# min = num[1]
# for i in num:
#     if i > max:
#         max = i
#     elif i < min:
#         min = i
# sum = min + max
# print(sum)


# В первый день спортсмен пробежал X километров.
# В каждый последующий день он увеличивал пробег на 15% от предыдущего дня.
# По данному числу Y требуется определить номер дня,
# в который пробег спортсмена составил не менее Y километров.

# x = float(input('x '))  #10
# y = float(input('y '))  #20

# # n = (x * 15 / 100)     #1.5

# count = 1
# while x<y:
#     n = (x * 15 / 100)
#     x = (x+n)
#     count += 1
# else:
#     print(count)


# Qx = int(input('координата x преземления дачника: -> '))
# Qy = int(input('координата y преземления дачника: -> '))

# Ax = 2
# Ay = 2
# Bx = 2
# By = 5
# Cx = 8
# Cy = 5
# Dx = 8
# Dy = 2

# a = math.sqrt((Bx - Ax)**2 + (By - Ay)**2)
# d = math.sqrt((Dx - Ax)**2 + (Dy - Ay)**2)
# c = a
# b = d
# PlPr = int(a*b)
# print()
# print(f'a = {a}, b = {b}, c = {c}, d = {d}')
# print(f'площадь прямоугольника = {PlPr}')
# print()

# SerA = float(a/2)
# SerD = float(d/2)
# SerC = SerA
# SerB = SerD
# print(f'SerA = {SerA}, SerB = {SerB}, SerC = {SerC}, SerD = {SerD}')

# Qa = math.sqrt((Qx - Ax)**2 + (Qy - (Ay+SerA))**2)
# Qb = math.sqrt((Qx - (Bx+SerB))**2 + (By - Qy)**2)
# Qc = math.sqrt((Cx - Qx)**2 + (Qy - (Cy-SerC))**2)
# Qd = math.sqrt((Qx - (Dx-SerD))**2 + (Qy - Dy)**2)
# Sum = int(Qa+ Qb + Qc + Qd)
# print(f'сумма площадей треугольников = {Sum}')



                    #       1      Напишите программу, которая принимает на вход два числа и проверяет, 
                    # является ли одно число квадратом другого.
                    # Примеры:
                    # 5, 25 -> да
                    # 4, 16 -> да
                    # 25, 5 -> да
                    # 8,9 -> нет

# a = int(input('Введите число a: '))
# b = int(input('Введите число b: '))

# if a == b**2 or b == a**2:
#     print('Yes')
# else: print('No')

                            #        2      Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
                            # Примеры:
                            # 1, 4, 8, 7, 5 -> 8
                            # 78, 55, 36, 90, 2 -> 90
# a = int(input('Введите a: '))
# b = int(input('Введите b: '))
# c = int(input('Введите c: '))
# d = int(input('Введите d: '))
# e = int(input('Введите e: '))
# print(a, b, c, d, e)
# min = a
# if b > a: max = b
# if c > a: max = c
# if d > a: max = d
# if e > a: max = e
# print(max)

                    #вариант с for
# numbers = [randint(-10, 50) for i in range(10)]
# print(numbers)
# max = numbers[0]
# for i in numbers[1:]:
#     if i > max:
#         max = i
# print(max)


# i = 1
# a = list(range(1,6)) #a = list(range(5))
# while i <= 5:
#     number = input('Введите {i}-е число + enter: ')
#     a[i-1] = number
#     if i == 1:
#         max = number
#     elif number > max:
#         max = number
#     i += 1
# print(f'max = {max}')



                        #        3      Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
                        # Примеры:
                        # 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5
# n = int(input('Введите n: '))
# start = -n
# while start < n:
#     print(start)
#     start+=1

                        #        4      Напишите программу, которая будет принимать на вход дробь 
                        # и показывать первую цифру дробной части числа.
                        # Примеры:
                        # 6,78 -> 7
                        # 5 -> нет
                        # 0,34 -> 3
# num = float(input('-> '))
# if num % 10 != 0:
#    print('No')
# else: 
#     res = (num * 10) % 10
#     print(int(res))

                                                        # ДОП *********************** 1
# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. 
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

# n = (input('Введите n: -> '))
# n1 = n+n
# print(n1)
# print()
# n2 = n+n+n
# print(n2)
# print()
# Sum = int(n) + int(n1) + int(n2)
# print(Sum)

                                                        # ДОП *********************** 2
# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе. 
# Для решения используйте цикл while и арифметические операции.

a = input()
max = 0
for num in a:
    if int(num) > max:
        max = int(num)
print(max)

# i = 0
# flag = True
# while flag:
#     if num[i] > max:
#         max = num[i]
#         i+=1
        
#     if i == len(num): flag = False
# print(max)
