import os
os.system('CLS')

# 1. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
# ['апап4', 'fdgg3', 'fgdf', '6', 'fg24'] - ищем 24 - найдено на 4 индексе


data = ['апап4', 'fdgg3', 'fgdf', '6', 'fg24']
count = 0
for i in data:
    if '24' in i:
        print([i], count)
    count += 1

# 2. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

# *Пример:*
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1
# 5: 16, 6: 19}

# data = ["123", "234", 123, "567"]

# def second(data, qwe):
#     count = 0
#     count2 = 0
#     for i in data:
        
#         if qwe == i:
#             count2 += 1
#         if count2 > 1:
#             return count
#         count += 1
#     return -1    
# print(second(data, "123"))

# *****

# Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# number = int(input('-> '))

# d = {}
# for i in range(1, number+1):
#     d[i] = 3 * i + 1
# print(d)
   