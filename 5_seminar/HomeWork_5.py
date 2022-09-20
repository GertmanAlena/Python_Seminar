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

# player1 = int(input("введите число от 1 до 28 -> "))
# player2 = int(input("введите число от 1 до 28 -> "))
# total = 51
# count1 = 0
# count2 = 0
# player1 = 0
# player2 = 0
# min = 1
# max = 7
# x=1
# # x = random.randint(1, 3) 
# print(x)
# if x == 1: # играю за первого
#     print(f'{player1} начинает игру первым!!!')
#     player1 = int(total%(min+max)+1)
#     count1+=1
#     total = total - player1
#     while count1 < 5:
#         player2 = int(input("введите число от 1 до 7 -> "))
#         total = total - player2
#         count2+=1
#         if count1 == 5:
#             player1 = (min+max) - player2
#             count1+=1
#             total = total - player1
            
#         elif total != (min+max)+1:
#             player1 = (min+max) - player2
#             count1+=1
#             total = total - player1
#         else:
#             print("сколько бы второй не взял, первый выиграл")
   
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

# programming_languages = ['python', 'c#', 'Java', 'JavaScript']
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
