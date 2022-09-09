import os
from random import randint
os.system('CLS')

# 1- Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
        # [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

min = int(input('min ->: '))
max = int(input('max ->: '))
size = int(input('size ->: '))

def Random_Number(*params):
    rand_num = [randint(min, max) for i in range(size)]
    return rand_num

def Summa_Numbers(numbers2):
    sum: int = 0
    for i in numbers2:
        sum = sum + i
    return sum

numbers = (Random_Number(min, max, size))
print(numbers)
numbers2 = numbers[1::2]
print(numbers2)

print(Summa_Numbers(numbers2))


# 2-Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:

# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]



# 3-Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:

# [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
# [4.07, 5.1, 8.2444, 6.98] - 0.91 или 91
# 4- Напишите программу, которая будет преобразовывать десятичное число в двоичное. 
# Подумайте, как это можно решить с помощью рекурсии.

# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10


# 5-Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:

# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи
# Решение оформлять в виде функций
# По возможности добавляйте docstring