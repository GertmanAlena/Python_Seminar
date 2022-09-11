import datetime
import math
import os
from re import I
os.system('CLS')
                                                # Задача 1

# 1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. 
# Учтите, что числа могут быть отрицательными
# Пример:
# 67.82 -> 23
# 0.56 -> 11

# number = input('Введите дробное число: ')
# print('Вы ввели', number, end= ' ')

# separation = number.split('.')
# num = separation[0] + separation[1]
    
# print('число = ', num)

# def sum_num(num):
#     sum = 0
#     if int(num) < 0: num *= -1      
#     while int(num) > 0:
#         if num % 10 != 0:
#             a = num%10
#             sum += a
#             num = int(num/10)
#     else: sum = sum + num
#     return sum

# print(sum_num(int(num)))


                                                # Задача 2
# Напишите программу, которая принимает на вход число N и 
# выдает набор произведений (набор - это список) чисел от 1 до N.
# Не используйте функцию math.factorial.
# Добавьте проверку числа N: чтобы пользователь не мог ввести буквы.

# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# def inputInt(prompt=None):  # ПРОВЕРКА НА INT
#     while True:
#         p = input(prompt)
#         try:
#             return int(p)
#         except ValueError:
#             print('Ошибка. Ожидалось вещественное число.')
# number = inputInt('Введите число: ')
# print('Вы ввели', number)

# rez = []
# step = 1
# for i in range(1, number+1):
#     step*=i
#     rez.append(step)
# print(rez)


                                                # Задача 3  ПЕРВЫЙ ВАРИАНТ
# Палиндромом называется слово, которое в обе стороны читается одинаково: "шалаш", "кабак".
# А еще есть палиндром числа - смысл также в том, чтобы число в обе стороны читалось одинаково, 
# но есть одно "но".
# Если перевернутое число не равно исходному, то они складываются и проверяются на палиндром еще раз.
# Это происходит до тех пор, пока не будет найден палиндром.
# Напишите такую программу, которая найдет палиндром введенного пользователем числа.  

# def Polindrom(number):
#     number2 = str(number)[::-1] #развернули
#     if str(number) == str(number2):
#         # print(f'{number2}   --  полиндром')
#         return number2
#     return Polindrom(int(number2)+int(number))       
    

# number = input('Введите число: ')
# print('Вы ввели -> ', number)

# print(Polindrom(number))

# check_palindrome(number, number2)

                                                # Задача 4
# Реализуйте выдачу случайного числа
# не использовать random.randint и вообще библиотеку random
# Можете использовать xor, биты, библиотеку time или datetime (миллисекунды или наносекунды) - 
# для задания случайности
# Учтите, что есть диапазон: от(минимальное) и до (максимальное)           
# 
# from datetime import datetime

def random(_min:int, _max:int) -> int: 
    ''' Генерация случайного числа params: min - начало диапазона max - конец диапазона '''
    d = _max - _min
    ms = datetime.datetime.today().microsecond / (10 ** 6) 
    print(f'{ms=}') 
    return _min + math.ceil(d * ms)

print(random(1,10))
