from audioop import mul
from functools import reduce
import math
import os
os.system('CLS')


            # 1- Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
            # Пример:
                    # [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
# import random_numb
    
# numbers = random_numb.Random_Number(-10,10,5)
# print(numbers)
    
# def Summa_Numbers(numbers2):
   
#     sum: int = 0
#     for i in numbers2:
#         sum = sum + i
#     return sum

# numbers2 = numbers[1::2]
# print(numbers2)

# print(Summa_Numbers(numbers2))

# '''второй вариант решения задачи'''
# print(numbers[1::2])
# print (sum(numbers[1::2]))

        # 2-Напишите программу, которая найдёт произведение пар чисел списка. 
        # Парой считаем первый и последний элемент, второй и предпоследний и т.д.
        # Пример: [2, 3, 4, 5, 6] => [12, 15, 16];    [2, 3, 5, 6] => [12, 15]

 #import random_numb
 #First_List = random_numb.Random_Number()
 #'''импортировала из вайла рандомно создание списка'''
 #print('First_List ', First_List)

# def Proizved_Alem(First_List): 
#     '''функция умножения элементов'''
#     if len(First_List) % 2 == 0:
#         size = len(First_List)/2
#     else:
#         size = int((len(First_List)/2)+0.5)
        
 #    Res_List = []
 #    i=0
 #    while i <= size-1:
 #        Res_List.append(First_List[i]*First_List[(i+1)*-1])
 #        i+=1
 #    # print('Res_List   ', Res_List)
 #    return Res_List

 #print('Res_List   ', Proizved_Alem(First_List))

            # 3-Задайте список из вещественных чисел. 
            # Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
            # Пример:

# [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
# [4.07, 5.1, 8.2444, 6.98] - 0.91 или 91

#Spisok_Numbers = [4.07, 5.1, 8.2444, 6.98] 
#print('Spisok_Numbers -> ', Spisok_Numbers)
#Integer_Numbers = []
#for i in Spisok_Numbers:
#    '''
#    берём часть после точки через split
#    '''
#    Integer_Numbers.append(str(str(i).split('.')[1]))
#print('второй вариант ', Integer_Numbers)

#def Min_Max(Integer_Numbers):
#    '''
#    в этой функции находим min и max, 
#    если максимальное число <10 добавляем поль
#    и вычисляем разницу
#    '''
#    raznica=0
#    maximum = max(Integer_Numbers)
#    minimum = min(Integer_Numbers)
#    print('min -> ', minimum, 'max -> ', maximum)
#    if int(maximum) < 10:
#        maximum = int(maximum) * 10
#        raznica = int(maximum)-int(minimum)
#    print(raznica)
#    return raznica

#Min_Max(Integer_Numbers)

            # 4- Напишите программу, которая будет преобразовывать десятичное число в двоичное. 
            # Подумайте, как это можно решить с помощью рекурсии.

# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

# def Binary(num):
    # '''без рекурсии'''
#     bin = []
#     while num > 0:
#         bin.append(num%2)
#         num//=2
#     return bin

 #bin = Binary(int(input('-> '))) 
 #print(bin[::-1])   

bin = []
def Binary(num, n):
    '''рекурсия'''
    if num == 0:
        return 1
    else:
        bin.insert(n, num%2)
        return Binary(num//2, n-1)
        
num = Binary(int(input('-> ')), -1)
print(bin)  



# 5-Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:

# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи
# Решение оформлять в виде функций
# По возможности добавляйте docstring

#def Fibonacci_Pos(num):
    # '''
    # функция последовательности Фибоначчи с положительными числами
    # '''
#    Fibonacci_Positive = []
#    fib1 = 0
#    fib2 = 1
#    for i in range(num+1):
#        if i == 0: Fibonacci_Positive.insert(i,fib1) 
#        elif i == 1: Fibonacci_Positive.insert(i,fib2)
#        else:
#            Fibonacci_Positive.insert(i,fib1+fib2)
#            time = fib2
#            fib2 = fib1+fib2
#            fib1 = time
#    return Fibonacci_Positive
#Fibonacci_Positive = Fibonacci_Pos(int(input('-> ')))
#print(Fibonacci_Positive)

#def Fibonacci_Neg(num):
#    '''
#    функция последовательности Фибоначчи с отрицательными числами
#    '''
#    Fibonacci_Negative = []
#    fib1 = 1
#    fib2 = -1
#    for i in range(num):
#        if i == 0: Fibonacci_Negative.insert(i,fib1)
#        elif i == 1: Fibonacci_Negative.insert(i,fib2)
#        else:
#            Fibonacci_Negative.insert(i,fib1-fib2)
#            time = fib2
#            fib2 = fib1-fib2
#            fib1 = time
#    return Fibonacci_Negative
#Fibonacci_Negative = Fibonacci_Neg(int(input('-> ')))
#print(Fibonacci_Negative)

#Oll_Fib = str(Fibonacci_Negative[::-1]+Fibonacci_Positive)
#print(Oll_Fib)