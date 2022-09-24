
import math
import numbers
import os
from pickletools import int4
import random
import re
os.system('CLS')

# 1- Определить, присутствует ли в заданном списке строк, некоторое число

# data = input('Введите что-то ')
# print(["Yes" if len([print(i) for i in data if i.isdigit()]) > 0 else "No"])

# 2- Найти сумму чисел списка стоящих на нечетной позиции

# number = list(map(int, input('Введите числа через пробел -> ').split(' ')))
# print (f' сумма чисел на нечётных позициях = {sum(number[1::2])}')

# 4- Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

# data = ["цук", "йцу", "цук", "фыв", "ячс", "цук", "йцукен", "йцу"]
# elem = "цук"

# oll_list = list(enumerate(data))
# list_elem = list(filter(lambda x: elem in x, oll_list))
# print(list_elem)
# print([list_elem[1][0] if len else "No"])


                # 6-Сформировать список из N членов последовательности.
                # Для N = 5: 1, -3, 9, -27, 81 и т.д.

# def inputFloat(prompt=None):  # ПРОВЕРКА НА INT
#     while True:
#         n = input(prompt)
#         try:
#             if int(n) > 0:
#                 return int(n)
#         except ValueError:
#             print('Ошибка. Ожидалось вещественное число.')
  
# print(*[(-3) ** i for i in range(int(inputFloat('Введите количество элементов: ')))])


            # 5- Найти произведение пар чисел в списке. 
            # Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# First_List = [random.randint(1, 10) for i in range (7)]
# print('First_List ', First_List)

# Proizved_Alem = [First_List[i] * First_List[-i-1] for i in range(math.ceil(len(First_List)/2))]
# print('Proizved_Alem ', Proizved_Alem)

                    # Задание с семинара
                    # Напишите программу вычисления арифметического выражения заданного строкой.
                    # Используйте операции +,-,/,. приоритет операций стандартный.
                    # Дополнительное задание: Добавьте возможность использования скобок, 
                    # меняющих приоритет операций
                    # *Пример:
                    # 2+2 => 4;
                    # 1+2*3 => 7;

data = input('Введите пример - > ')    
operators_list = ['/', '*', '-', '+']
priority_list = [1, 1, 2, 2]
'''
[(1, '/'), (1, '*'), (2, '+'), (2, '-')]
'''
unite_list = list(zip(priority_list, operators_list))
print(unite_list)

def get_number(data):
    number = []
    alem = []
    temp_num = '' # тут склеиваем цифры
    data += '='
    for char in data:
        if char.isdigit():
            temp_num += char
        else:
            number.append(temp_num)
            alem.append(char)
            temp_num = ''
    
    return number, alem[:-1]

def div(a, b):
    return int(a) // int(b)
def mult(a, b):
    return int(a) * int(b)
def sum(a, b):
    return int(a) + int(b)
def sub(a, b):
    return int(a) - int(b)

                                          #  [(1, '/'), (1, '*'), (2, '+'), (2, '-')]  unite_list
number_list, oper_list = get_number(data)  # ['22', '2', '5', '2']   ['-', '+', '*', '=']

def calk(unite_list, oper_list, number_list):

    for i in unite_list:                
        if i[0] == 1:           # i в (1, '/'), (1, '*')
            for j in oper_list: # ['-', '+', '*', '=']
                if j == i[1]:
                    index_alem = oper_list.index(j)
                    if j == '*':
                        while '*' in oper_list:
                            mult_num = mult(number_list[index_alem], number_list[index_alem+1])
                            number_list.pop(index_alem)
                            number_list.pop(index_alem)
                            number_list.insert(index_alem, mult_num)
                            oper_list.pop(index_alem)
                    if j == '/':
                        while '/' in oper_list:
                            div_num = div(number_list[index_alem], number_list[index_alem+1])
                            number_list.pop(index_alem)
                            number_list.pop(index_alem)
                            number_list.insert(index_alem, div_num)
                            oper_list.pop(index_alem)
    for i in unite_list:    
        if i[0] == 2:           
            for j in oper_list:
                
                if j == i[1]:
                    index_alem = oper_list.index(j)
                    # print(index_alem)
                    if j == '-':
                        while '-' in oper_list:
                            sub_num = sub(number_list[index_alem], number_list[index_alem+1])
                            number_list.pop(index_alem)
                            number_list.pop(index_alem)
                            number_list.insert(index_alem, sub_num)
                            oper_list.pop(index_alem)
                    if j == '+':
                        while '+' in oper_list:
                            sum_num = sum(number_list[index_alem], number_list[index_alem+1])
                            number_list.pop(index_alem)
                            number_list.pop(index_alem)
                            number_list.insert(index_alem, sum_num)
                            oper_list.pop(index_alem)
    return number_list
                        
rezult = calk(unite_list, oper_list, number_list)
print(rezult)