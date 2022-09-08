
from ast import Compare, Del
from datetime import datetime
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
                                                # Задача 3  ПЕРВЫЙ ВАРИАНТ
# Палиндромом называется слово, которое в обе стороны читается одинаково: "шалаш", "кабак".
# А еще есть палиндром числа - смысл также в том, чтобы число в обе стороны читалось одинаково, 
# но есть одно "но".
# Если перевернутое число не равно исходному, то они складываются и проверяются на палиндром еще раз.
# Это происходит до тех пор, пока не будет найден палиндром.
# Напишите такую программу, которая найдет палиндром введенного пользователем числа.  

# def pol(number):
#     number2 = 0
#     while number:
#         z = number % 10
#         number2 = number2*10 + z
#         number //= 10
#     return int(number2)

# def Polindrom(number):
#     number2 = number[len(number)-1::-1] #строка первая наоборот записана
#     return number2
   

# def check_palindrome(pol_num1, pol_num2):

#     if pol_num1 == pol_num2:
#         print(f'{pol_num1}   --  полиндром')
   
#     else:
#         print(f'{pol_num1}   --  НЕ полиндром')
#         try:
            
#             while pol_num1 != pol_num2: 
#                 pol_num1 = int(pol_num1)
#                 pol_num2 = int(pol_num2)
#                 pol_num1 = pol_num1 + pol_num2
#                 pol_num2 = pol(pol_num1)
#                 check_palindrome(pol_num1, pol_num2)
#                 print(f'теперь получился {pol_num2}  полиндром')
#                 return pol_num2
#         except ValueError:
#             print('Ошибка.')

# number = input('Введите число: ')
# print('Вы ввели -> ', number)

# number2 = Polindrom(number)
# print('перевёртыш ->', number2)

# check_palindrome(number, number2)

                                                # Задача 4
# Реализуйте выдачу случайного числа
# не использовать random.randint и вообще библиотеку random
# Можете использовать xor, биты, библиотеку time или datetime (миллисекунды или наносекунды) - 
# для задания случайности
# Учтите, что есть диапазон: от(минимальное) и до (максимальное)           
# 
from datetime import datetime

def gen_rand():
    current_datetime = datetime.now()
    print(current_datetime.microsecond%10)
gen_rand()

#                                         # второй вариант ПОЛИНДРОМА!!!!!!!!!!!!!!!!!!
# def polindrome(number):
#     number2 = 0
#     while number:
#         z = number % 10
#         number2 = number2*10 + z
#         number //= 10
#     return int(number2)

# try:
#     def inputInt(prompt=None):  # ПРОВЕРКА НА INT
#         while True:
#             p = input(prompt)
#             try:
#                 return int(p)
#             except ValueError:
#                 print('Ошибка. Ожидалось вещественное число.')
#     number = inputInt('Введите число: ')
#     print('первое число', number)  
#     number2 = polindrome(number)
#     print('второе число', number2)
#     if number == number2:
#       print(f'число {number} полиндром')  
#     else:
#         while number != number2:
#             number = number + number2
#             number2 = polindrome(number)
#         else: print(f'полинромом является сумма чисел {number}')

# except ValueError:
#     print('Ошибка.')


                            #  **************** третий вариант полиндрома ****************

# def Polindrom(number):
#     number2 = number[len(number)-1::-1] #строка первая наоборот записана
#     return number2
   

# def check_palindrome(pol_num1, pol_num2):

#     if pol_num1 == pol_num2:
#         print(f'{pol_num1}   --  полиндром')
   
#     else:
#         try:
#             if len(pol_num1) == len(pol_num2):
#                 while pol_num1 != pol_num2: 
#                     c = [x+y for x, y in zip(pol_num1, pol_num2)]
#                     z = str(c)
#                     print(f'теперь получился {z}  полиндром')
#                     return z
#         except ValueError:
#             print('Ошибка.')

# number = input('Введите число: ')
# print('Вы ввели -> ', number)

# number2 = Polindrom(number)
# print('перевёртыш ->', number2)

# check_palindrome(number, number2)