
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

# numbers = [random.randrange(1, 5, 1) for i in range(10)]
# print(numbers)
# max = 0
# v_max = 0
# max_al = ''
# j = 0
# while j < len(numbers):
#     alement = numbers[0]
#     count = 0
#     i=numbers[0]
#     while i in numbers:
#         if i == alement:
#             count+=1
#             numbers.remove(i)
#     v_max = count
#     if v_max > max:
#         max = v_max
#         max_al = alement
#     j+=1
# print(f'число {max_al} повторяется {max} раз(а)')


#семинар 6
import re
 
# actions = {
#   "^": lambda x, y: str(float(x)**float(y)),
#   "*": lambda x, y: str(float(x) * float(y)),
#   "/": lambda x, y: str(float(x) / float(y)),
#   "+": lambda x, y: str(float(x) + float(y)),
#   "-": lambda x, y: str(float(x) - float(y))
# }
 
# priority_reg_exp = r"\((.+?)\)"
# action_reg_exp = r"(-?\d+(?:\.\d+)?)\s*\{}\s*(-?\d+(?:\.\d+)?)"
 
# def my_eval(expresion: str) -> str:
 
#     while (match := re.search(priority_reg_exp, expresion)):
#         expresion: str = expresion.replace(match.group(0), my_eval(match.group(1)))
 
#     for symbol, action in actions.items():
#         while (match := re.search(action_reg_exp.format(symbol), expresion)):
#             expresion: str = expresion.replace(match.group(0), action(*match.groups()))
 
#     return expresion
 
 
# exp = "(1 + 5) * (5 * (18 - 2)) / 5"
# print(my_eval(exp), eval(exp))
# expression = '-22+2'


# def get_numbers(expression):
#     numbers = []
#     temp = ''
#     expression += '='
#     minus = -1 if expression[0]=='-' else 1
#     expression = expression[1:] if expression[0]=='-' else expression
#     for char in expression:
#         if char.isdigit():
#             temp += char
#         else:
#             numbers.append(temp)
#             temp = ''
#     numbers = list(filter(lambda char: char.isdigit(), numbers))
#     numbers[0] = f'-{numbers[0]}'
#     return numbers


# def get_operators(expression):
#     return list(filter(lambda char: char in '+-*/', expression))


# def check_alpha(expression):
#     return not any(filter(lambda char: char.isalpha(), expression))


# def check_expression(numbers: list, opers: list):
#     return True if len(numbers) > len(opers)  else False


# if check_alpha(expression):
#     numbers = get_numbers(expression)
#     list_operators = get_operators(expression)
#     if check_expression(numbers, list_operators):
#         print(numbers, list_operators)
#     else:
#         print('Выражение неполное', numbers, list_operators)
# else:
#     print('Вы ввели буквы')

player1 = input('Введите своё имя!')
print(f'привет {player1}')

def is_number_of_candies(): 
    '''
    начальное количество конфет
    ''' 
    while True:
        try:
            number_of_candies = int(input('Введите количество конфет'))
            if number_of_candies > 0 and number_of_candies > 10:
                break
            else:
                print('Ошибка. Ещё раз.')
        except ValueError:
            print('Ошибка. Ожидалось вещественное число.')
    return number_of_candies
number_of_candies = is_number_of_candies()

min = 1

def max_candies(): 
    '''
    начальное количество конфет
    ''' 
    while True:
        try:
            max = int(input('Введите сколько можно максимум брать конфет'))
            if max > min and max < number_of_candies/3:
                break
            else:
                print('Ошибка. Ещё раз.')
        except ValueError:
            print('Ошибка. Ожидалось вещественное число.')
    return max
max = max_candies()

print(f'у нас конфет {number_of_candies}, можно взять конфет от {min} до {max}')
print(f'{player1}, давайте определим кто ходит первый и начнём игру!!!')


def step_bot(number_of_candies, min, max):
    if number_of_candies > (min + max)+1: # если число конфет больше (min + max)+1
        step_bot = random.randint(1, max)
        number_of_candies = number_of_candies - step_bot
        print(f' бот взял {step_bot} конфет и осталось {number_of_candies} конфет')
        return player_step(number_of_candies, min, max)
    elif number_of_candies == (min + max): # если число конфет == (min + max)+1
        step_bot = max
        number_of_candies = number_of_candies - step_bot
        print(f'  бот взял {step_bot} конфет и осталось {number_of_candies} конфета')
        print(f' {player1} - ПРОИГРАЛ! осталась {number_of_candies} конфета!')
    elif number_of_candies == max: # если число конфет == max
        step_bot = max-1
        number_of_candies = number_of_candies - step_bot
        print(f'  бот взял {step_bot} конфет и осталось {number_of_candies} конфета')
        print(f' {player1} - ПРОИГРАЛ! осталась {number_of_candies} конфета!')
    elif number_of_candies == (min + max)+1: # если число конфет == (min + max)+1
        step_bot = min + max
        number_of_candies = number_of_candies - step_bot
        print(f'  бот взял {step_bot} конфет и осталось {number_of_candies} конфет')
        print(f'  осталась {number_of_candies} конфета! {player1} - ВЫ проиграли!')
        return player_step(number_of_candies, min, max)
    elif number_of_candies == 1:
        print(f' {player1} - ВЫИГРАЛ! осталась {number_of_candies} конфета!')

def player_step(number_of_candies, min, max):
    if number_of_candies != 1:
        step_player = int(input(f'{player1} введите число конфет - >'))
        number_of_candies = number_of_candies - step_player
        print(f'{player1} взял {step_player} конфет. Осталось {number_of_candies}')
        return step_bot(number_of_candies, min, max)
    if number_of_candies == 1:
        print(f' {player1} - ВЫ проиграли! осталась {number_of_candies} конфета!')

first_step = random.randint(1, 2)
if first_step == 1:
    print(f'{player1}, Вы начинаете игру!!!')
    number_of_candies = player_step(number_of_candies, min, max)
    #функция если первым ходит игрок
if first_step == 2:
    print('Игру начинает Бот!!!')
    number_of_candies = step_bot(number_of_candies, min, max) # шаг сделал бот
