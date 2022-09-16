import os
os.system('CLS')

                        # 1 - Задайте натуральное число N. 
                        # Напишите программу, которая составит список простых множителей числа N.
                        # N = 20 -> [2,5]
                        # N = 30 -> [2, 3, 5]

# def Search_Numbers(number):
#     Simple_Factor = []
#     i=2
#     # '''
#     # если число делится на i без остатка, то в строке 21 добавляем это число
#     # делим на i до тех пор пока число делится на него без остатка
#     # но в отдельном цикле, чтобы не записывать одинаковые числа (строки 22-23)
#     # если число не делится на i переходим на новое i (строка 25) и возвращаемя на 19 строку
#     # последняя проверка, чтобы записать оставшееся от делений число (строка 26)
#     # '''
#     while i*i <= number:
#         if number % i == 0:
#             Simple_Factor.append(i)
#             while number % i == 0:
#                 number /= i
#         else:
#             i+=1
#     if number > i:
#         Simple_Factor.append(int(number))      
#     return Simple_Factor
# number = Search_Numbers(int(input('введите число -> ')))
# print(number)

                                # 2 - Задайте последовательность чисел.
                                # Напишите программу, которая выведет список 
                                # неповторяющихся элементов исходной последовательности. 
                                # Не использовать множества.
                                # [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]

numbers = [1,1,1,1,2,2,2,3,3,3,4]

def Sort(number):                
   Sort_Number = []
   num = number[0]
   Sort_Number.append(num)
   for i in number:
       if i == num:
           continue
       else:
           num = i
           Sort_Number.append(i)

   return Sort_Number
print(Sort(numbers))

                                # 3 - В файле, содержащем фамилии студентов и их оценки, 
                                # изменить на прописные буквы фамилии тех студентов,
                                # которые имеют средний балл более «4».
# Нужно перезаписать файл.
# Пример:
# Ангела Меркель 5
# Андрей Валетов 5
# Фредди Меркури 3
# Анастасия Пономарева 4

# Программа выдаст:
# АНГЕЛА МЕРКЕЛЬ 5
# АНДРЕЙ ВАЛЕТОВ 5
# Фредди Меркури 3
# Анастасия Пономарева 4
'''
решение в файле Students.py и в students.txt
'''
  
                    # 4- Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное количество 
                    # символов влево или вправо. 
                    # При расшифровке происходит обратная операция. К примеру, слово "абба" можно зашифровать "бввб" - 
                    # сдвиг на 1 вправо. 
                    # "вггв" - сдвиг на 2 вправо, "юяяю" - сдвиг на 2 влево.
                    # Сдвиг часто называют ключом шифрования.
                    # Ваша задача - написать функцию, которая записывает в файл шифрованный текст, а также функцию, 
                    # которая спрашивает ключ, считывает текст и дешифровывает его.

# with open('Сaesar_Сipher.txt', 'w', encoding='utf-8') as data:  # пока работа в txt через data
    
#     def Сaesar_Сipher():
#         word = input('введите слово для шиврования -> ')
#         sdvig = int(input('введите ключ для шифрования: -> '))
#         alphabet_Eng = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
#         alphabet_Ru = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', 'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
#         cipher_word = ' ' 

#         for i in range(len(word)):
#             if word[i] in alphabet_Eng:
#                 try:
#                     cipher_word+=alphabet_Eng[alphabet_Eng.index(word[i])+sdvig]
#                 except IndexError:
#                     print('no')
#             if word[i] in alphabet_Ru:
#                 try:
#                     cipher_word+=alphabet_Ru[alphabet_Ru.index(word[i])+sdvig]
#                 except IndexError:
#                     print('таких букв нет')
        
#         return cipher_word

#     Сaesar_Word = Сaesar_Сipher()
#     for i in Сaesar_Word:
#         data.write(i) #записали в txt файл через data.write наш словарь

# with open('Сaesar_Сipher.txt', 'r', encoding='utf-8') as data:  # пока работа в txt через data
    # De_Cipher_Word = ' '
    # for i in data:
    #     De_Cipher_Word += i
    
    # def De_Сaesar_Сipher(De_Cipher_Word):
        
    #     sdvig = int(input('введите ключ для ДЕшифрования: -> '))
    #     alphabet_Eng = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    #     alphabet_Ru = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', 'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
    #     de_cipher_word = ' ' 

    #     for i in range(len(De_Cipher_Word)):
    #         if De_Cipher_Word[i] in alphabet_Eng:
    #             try:
    #                 de_cipher_word+=alphabet_Eng[alphabet_Eng.index(De_Cipher_Word[i])-sdvig]
    #             except IndexError:
    #                 print('no')
    #         if De_Cipher_Word[i] in alphabet_Ru:
    #             try:
    #                 de_cipher_word+=alphabet_Ru[alphabet_Ru.index(De_Cipher_Word[i])-sdvig]
    #             except IndexError:
    #                 print('таких букв нет')
        
    #     return de_cipher_word    
    # rez = De_Сaesar_Сipher(De_Cipher_Word)
    # print('ваше слово: ', rez)

                    # 5 - Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
                    # Входные и выходные данные хранятся в отдельных текстовых файлах.
                    # файл первый:
                    # AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool
                    # файл второй:
                    # сжатый текст.

# with open('RLE.txt', 'w', encoding='utf-8') as data:
#     simbol = 'AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool'
#     for i in simbol:
#         data.writelines(i)

# with open('RLE.txt', 'r', encoding='utf-8') as data:
#     source_text = ''
#     for i in data:
#         source_text += i
    
#     compressed_text = ''
#     # no_alements = ' '
#     alements = ''
#     i=0
#     while i < len(source_text):
        
#         alements = source_text[i]
#         count_alements = 1
#         while i + 1 < len(source_text) and source_text[i] == source_text[i+1]:
#                 count_alements+=1
#                 i+=1
#         compressed_text = compressed_text + (str(count_alements) + alements)
#         i+=1
#     print(compressed_text)
#     new = open('rez_RLE.txt', 'w',encoding='utf-8')
#     new.writelines(compressed_text)
#     new.close()
# with open('rez_RLE.txt', 'r', encoding='utf-8') as data:
#     text = ''
#     for i in data:
#         text+= i
#     print(text)
   
#     decod = ''
#     alements = ''
#     vrem_int = ''
#     for i in text:
#         if i.isdigit():
#             vrem_int+=i
#         else: 
#             alements = i
#             decod += int(vrem_int)*alements
#             vrem_int = ''
#     print('decod -> ', decod)


            