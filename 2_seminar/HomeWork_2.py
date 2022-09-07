
from ast import Compare, Del
import numbers
from os import remove
import os
from random import randint
import string
os.system('CLS')
                                                # Задача 1

# 1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. 
# Учтите, что числа могут быть отрицательными
# Пример:
# 67.82 -> 23
# 0.56 -> 11

# def inputFloat(prompt=None):  # ПРОВЕРКА НА INT
#     while True:
#         p = input(prompt)
#         try:
#             return int(p)
#         except ValueError:
#             print('Ошибка. Ожидалось вещественное число.')
# number = inputFloat('Введите дробное число: ')
# print('Вы ввели', number, end= ' ')

# separation = number.split('.')
# num1 = int(separation[0])
# num2 = int(separation[1])
    
# print(f'num1 [', num1, ']', 'num2 [', num2, ']')

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

# print(sum_num(num1) + sum_num(num2))


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

# def Proizvedenie(number):
#     i=1
#     rez = 1
#     while i <= number:
#         rez *= i
#         i+=1
#         print(rez, end= ' ')
#     return rez
# Proizvedenie(number)
                                                # Задача 3
# Палиндромом называется слово, которое в обе стороны читается одинаково: "шалаш", "кабак".
# А еще есть палиндром числа - смысл также в том, чтобы число в обе стороны читалось одинаково, 
# но есть одно "но".
# Если перевернутое число не равно исходному, то они складываются и проверяются на палиндром еще раз.
# Это происходит до тех пор, пока не будет найден палиндром.
# Напишите такую программу, которая найдет палиндром введенного пользователем числа.  

def inputInt(prompt=None):  # ПРОВЕРКА НА INT
    while True:
        p = input(prompt)
        try:
            return int(p)
        except ValueError:
            print('Ошибка. Ожидалось вещественное число.')
number = inputInt('Введите число: ')
print('Вы ввели', number)

def Polindrom(number):
    pol_num1 = []
    for i in number:
        pol_num1.append(int(i))
    return pol_num1
    
def PolindromTwo(pol_num1):
    pol_num2 = pol_num1[len(pol_num1)-1::-1] #строка первая наоборот записана
    return pol_num2

def check_palindrome(pol_num1, pol_num2):
    
    # if pol_num1 == pol_num2:
    #     print(f'число {pol_num1} полиндром')
   
    # elif len(pol_num1) == len(pol_num2):
    #     c = [x+y for x, y in zip(pol_num1, pol_num2)]
            
    #     print(c)

    if pol_num1 == pol_num2:
        print(f'число {pol_num1} полиндром')
   
    else:
        try:
            if len(pol_num1) == len(pol_num2):
                while pol_num1 != pol_num2: 
                    c = [x+y for x, y in zip(pol_num1, pol_num2)]
                    print(f'число {c} теперь полиндром')
                    return c
        except ValueError:
            print('Ошибка.')


pol_num1 = Polindrom(str(number))
print('первое число ->', pol_num1)
pol_num2 = PolindromTwo(pol_num1)
print('второе число ->', pol_num2)
check_palindrome(pol_num1, pol_num2)
                                                # Задача 4
# Реализуйте выдачу случайного числа
# не использовать random.randint и вообще библиотеку random
# Можете использовать xor, биты, библиотеку time или datetime (миллисекунды или наносекунды) - 
# для задания случайности
# Учтите, что есть диапазон: от(минимальное) и до (максимальное)                                            