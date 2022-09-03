# print(list(range(10))) 
# print(list(range(10+1)))
# print(list(range(2,4)))
# print(list(range(10, 0, -1)))
# print(list(range(10, 0-1, -1)))

# flag = True
# i=0
# while flag:
#     i+=1
#     if i == 22:
#         flag = False
# print(i)


#Принимаем дробное число и выводим первую цифру после запятой
# a = float(input('Введите дробное число: '))
# print(int(a * 10) % 10)

#Принимаем число и проверяем кратно ли оно 5, 10 или 15, но не 30

# number = int(input('Введите число: '))

# if (number % 5 == 0 and number % 10 == 0) or (number % 15 == 0 and number % 30 != 0):
#     print('Yes')
# else:
#     print('No')


# найти второй максимум
n = int(input())
max1 = n
max2 = -1
while n != 0: #пока не введём 0
    n = int(input())
    if n > max1:
        max2 = max1
        max1 = n
    elif n > max2:
        max2 = n
print(max2)
