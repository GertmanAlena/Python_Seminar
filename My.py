import os
os.system('CLS')

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

# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
# ['gfh5', 'gfh2', '67', 'jy32', '3put'] - ищем 32 - находим по индексу 3

word = ['gfh5', 'gfh2', '67', 'jy32', '3put']
n = '32'
count = 0
for i in word:
    if n in i:
        print(i, 'индекс ', count)
    count+=1
    