import datetime
import math
import os
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




def Fibonacci_Pos(num):
    '''
    функция последовательности Фибоначчи с положительными числами
    '''
    Fibonacci_Positive = []
    fib1 = 0
    fib2 = 1
    for i in range(num+1):
        if i == 0: Fibonacci_Positive.insert(i,fib1) 
        elif i == 1: Fibonacci_Positive.insert(i,fib2)
        else:
            Fibonacci_Positive.insert(i,fib1+fib2)
            time = fib2
            fib2 = fib1+fib2
            fib1 = time
    return Fibonacci_Positive
Fibonacci_Positive = Fibonacci_Pos(int(input('-> ')))
print(Fibonacci_Positive)

def Fibonacci_Neg(num):
    '''
    функция последовательности Фибоначчи с отрицательными числами
    '''
    Fibonacci_Negative = []
    fib1 = 1
    fib2 = -1
    for i in range(num):
        if i == 0: Fibonacci_Negative.insert(i,fib1)
        elif i == 1: Fibonacci_Negative.insert(i,fib2)
        else:
            Fibonacci_Negative.insert(i,fib1-fib2)
            time = fib2
            fib2 = fib1-fib2
            fib1 = time
    return Fibonacci_Negative
Fibonacci_Negative = Fibonacci_Neg(int(input('-> ')))
print(Fibonacci_Negative)

Oll_Fib = str(Fibonacci_Negative[::-1]+Fibonacci_Positive)
print(Oll_Fib)


'''
Найти наиболее часто встречающийся элемент в массиве целых чисел.
'''
# array = [1,2,5,7,9,45,2,1,2]
# for i in array:
#     print(array.count(i))  