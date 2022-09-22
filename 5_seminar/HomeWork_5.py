import os
from pickletools import int4
import random
os.system('CLS')


                                    # 1- Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
                                    # 'абвгдейка - это передача' = >" - это передача"

# text = input("Введите текст -> "'\n').split()
# simbol = (input("Введите слово для поиска -> "'\n'))

# new_text = ' '.join(filter(lambda j: simbol not in j, text))
# print(new_text)

                                    # 2- Создайте программу для игры с конфетами человек против человека.
                                    # Условие задачи: На столе лежит 2021 конфета(или сколько вы зададите). 
                                    # Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
                                    # За один ход можно забрать не более чем 28 конфет(или сколько вы зададите). 
                                    # Тот, кто берет последнюю конфету - проиграл.
                                    # Предусмотрите последний ход, ибо там конфет остается меньше.

                                    # a) Добавьте игру против бота
                                    # b) Подумайте как наделить бота "интеллектом"

player1 = input('Введите своё имя!')
print(f'привет {player1}')

def is_number_of_candies(): 
    '''
    начальное количество конфет
    ''' 
    while True:
        try:
            number_of_candies = int(input('Введите количество конфет -> '))
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
            max = int(input('Сколько конфет максимально можно брать? - > '))
            if max > min and max < number_of_candies/3:
                break
            else:
                print('Ошибка. Ещё раз.')
        except ValueError:
            print('Ошибка. Ожидалось вещественное число.')
    return max
max = max_candies()

print(f'у нас конфет -> {number_of_candies}, можно взять от {min} до {max}')
print(f'{player1}, давайте определим кто ходит первый рандомно и начнём игру!!!')

def step_ok(): 
    '''
    проверка на правильность хода
    ''' 
    while True:
        try:
            step_player = int(input(f'{player1} сколько конфет Вы возмёте - > '))
            if step_player >= min and step_player <= max:
                break
            else:
                print('Ошибка. Ещё раз.')
        except ValueError:
            print('Ошибка. Ожидалось вещественное число.')
    return step_player

def step_bot(number_of_candies, min, max):
    if number_of_candies == 1:
        print(f' {player1} - ВЫИГРАЛ! осталась {number_of_candies} конфета!')
    if number_of_candies > (min + max)+2: # если число конфет больше (min + max)+1
        step_bot = random.randint(1, max)
        number_of_candies = number_of_candies - step_bot
        print(f' бот взял {step_bot} осталось {number_of_candies} конфет')
        return player_step(number_of_candies, min, max)
    if number_of_candies == (min + max)+2: # если число конфет == (min + max)+1
        step_bot = min
        number_of_candies = number_of_candies - step_bot
        print(f'  бот взял {step_bot} осталось {number_of_candies} конфета')
        return player_step(number_of_candies, min, max)
    if number_of_candies == min + min: # если число конфет == (min + max)+1
        step_bot = min
        number_of_candies = number_of_candies - step_bot
        print(f'  бот взял {step_bot} осталось {number_of_candies} конфета')
        print(f' {player1} - ПРОИГРАЛ! осталась {number_of_candies} конфета!')
    if number_of_candies == max + max: # если число конфет == (min + max)+1
        step_bot = max - 1
        number_of_candies = number_of_candies - step_bot
        print(f'  бот взял {step_bot} осталось {number_of_candies} конфета')
        return player_step(number_of_candies, min, max)
    if number_of_candies == max: # если число конфет == max
        step_bot = max-1
        number_of_candies = number_of_candies - step_bot
        print(f'  бот взял {step_bot} осталось {number_of_candies} конфета')
        print(f' {player1} - ПРОИГРАЛ! осталась {number_of_candies} конфета!')
    if number_of_candies == max + min: # если число конфет == max
        step_bot = max
        number_of_candies = number_of_candies - step_bot
        print(f'  бот взял {step_bot} осталось {number_of_candies} конфета')
        print(f' {player1} - ПРОИГРАЛ! осталась {number_of_candies} конфета!')
    if number_of_candies == (min + max)+1: # если число конфет == (min + max)+1
        step_bot = min + max
        number_of_candies = number_of_candies - step_bot
        print(f'  бот взял {step_bot}  осталось {number_of_candies} конфет')
        print(f'  осталась {number_of_candies} конфета! {player1} - ВЫ проиграли!')
        return player_step(number_of_candies, min, max)
    

def player_step(number_of_candies, min, max):
    if number_of_candies != 1:
        step_player = step_ok()
        number_of_candies = number_of_candies - step_player #сделать  метод проверки числа от мин до макс
        print(f'{player1} взял {step_player} конфет. Осталось {number_of_candies}')
        return step_bot(number_of_candies, min, max)
    if number_of_candies == 1:
        print(f' {player1} - ВЫ проиграли! осталась {number_of_candies} конфета!')

first_step = random.randint(1, 2)
if first_step == 1:
    print(f'{player1}, Вы начинаете игру!!!')
    number_of_candies = player_step(number_of_candies, min, max)
    
if first_step == 2:  #  вызывает функцию, длля бота
    print('Игру начинает Бот!!!')
    number_of_candies = step_bot(number_of_candies, min, max) # шаг сделал бот
   
            # 3-Создайте два списка — один с названиями языков программирования, 
            # другой — с числами от 1 до длины первого.
            # ['python', 'c#']
            # [1,2]
            # Вам нужно сделать две функции: первая из которых создаст список кортежей, состоящих из номера и языка, написанного большими буквами.
            # [(1,'PYTHON'), (2,'C#')]
            # Вторая — которая отфильтрует этот список следующим образом: 
            # если сумма очков слова имеет в делителях номер, с которым она в паре в кортеже, 
            # то кортеж остается, его номер заменяется на сумму очков.
            # [сумма очков c# = 102, в делителях есть 2 с которым в паре. Значит список будет]
            # [(1,'PYTHON'), (102,'C#')]
            # Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове. 
            # Порядковые номера смотрите в этой таблице, в третьем столбце: https://www.charset.org/utf-8
            # Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы.
            # Cложите получившиеся числа и верните из функции в качестве ответа вместе с преобразованным списком
            # https://dzen.ru/media/simplichka/kak-tekst-hranitsia-v-kompiutere-chast-3-62d3d91515d67a522f78e1e6?&

# programming_languages = ['python', 'c#', 'Java', 'JavaScript', 'Visual development tools']
# list_numbers = list(range(1, len(programming_languages)+1))
# first_spisok = list(zip(list_numbers, programming_languages))
# print(first_spisok)

# def Sum(first_spisok):
#     list_ball = []
#     list_language = []
#     for i in first_spisok:   #(1, 'python') (2, 'c#')
#         sum = 0
#         for j in i[1]:        #python  c#
#             sum += ord(j)
#         if sum%i[0] == 0:
#             list_ball.append(sum)
#             list_language.append(i[1])
#     sum_spisok = list(zip(list_ball, list_language))
#     return sum_spisok

# sum_spisok = Sum(first_spisok)      
# print(sum_spisok)
