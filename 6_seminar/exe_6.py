import os
import random
os.system('CLS')

# numbers = [random.randrange(1, 100, 1) for i in range(5)]

# n = [lambda i: False if not i%2 else True]
# print(n)

# f = list(filter(lambda i: False if not i%2 else True, numbers))
# print(f)

# Задана натуральная степень n. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и 
# записать в файл многочлен степени n.
# Пример:
# - n=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 (коэф: []) или 10*x² = 0

# Уточнения:
# n - это степень икса первого элемента полинома >0
# при n =3 => 5*x*3 + 18*x**2 + 7*x + 19 = 0 - коэффициенты = [5,18,7,19]
# при n=2 => 2*x² + 4*x + 5 = 0(коэф: [2,4,5]) или x² + 5 = 0 (коэф: [1,0,5]) или 10*x²(коэф: [10,0,0]) = 0
# при n=10 => 56 * x*10 = 0

# коэффициенты - это числа перед элементами полинома.
# коэффициенты могут быть нулем, кроме первого





while True:
    try:
        n = int(input('Введите число: '))
        break
    except:
        continue

koaf = [random.randrange(0, 5) if i > 0 else random.randrange(1, 5) for i in range(n+1)] 
print(koaf)


amount = len(koaf)
mult_list = ['*']*(amount-1)+['']
x_list = ['x']*(amount-1)+['']
step_list = ['**'] * (amount - 1) +['']*2
n_step_list = list(reversed(range(n+1)))[:-2]+['']*2
print(mult_list, x_list, step_list, n_step_list)
print(list(zip(koaf, mult_list, x_list, step_list, n_step_list)))


# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,. приоритет операций стандартный.
# Дополнительное задание: Добавьте возможность использования скобок, меняющих приоритет операций
# *Пример:
# 2+2 => 4;
# 1+2*3 => 7;

# 10/2*5 => 25;
# 10 * 5 * => недостаточно числовых данных
# -5 + 5 => 0
# два + три => неправильный ввод: нужны числа
# (2+((5-3)*(16-14)))/3 => 2
