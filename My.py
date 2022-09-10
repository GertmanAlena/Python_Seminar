# import os
# os.system('CLS')

# def random(_min:int, _max:int) -> int:
#     '''
#     Генерация случайного числа
#     params:
#     min - начало диапазона
#     max - конец диапазона
#     '''
#     d = _max - _min#9
#     ms = datetime.datetime.today().microsecond / (10 ** 6)
#     #print(f'{ms=}')
#     return _min + math.ceil(d * ms)
def GetFibonacciList(n, L):
    # Проверить, корректна ли длина списка
    count = len(L)

    if len(L)<2:
        return []

    # Получить последние числа в списке L
    num1 = L[count-2]
    num2 = L[count-1]

    # Формула расчета следующего числа
    if (num1+num2) < n:
        L = L + [num1+num2]
        return GetFibonacciList(n, L) # вызвать рекурсивно функцию
    else:
        return L # если достигнут конец, то обычный выход

# Вызвать функцию GetFibonacciList()
LL = GetFibonacciList(100, [0, 1])