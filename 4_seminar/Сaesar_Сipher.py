import os
os.system('CLS')

with open('Сaesar_Сipher.txt', 'w', encoding='utf-8') as data:  # пока работа в txt через data
    
    def Сaesar_Сipher():
        word = input('введите слово для шиврования -> ')
        sdvig = int(input('введите ключ для шифрования: -> '))
        alphabet_Eng = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
        alphabet_Ru = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', 'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
        cipher_word = ' ' 

        for i in range(len(word)):
            if word[i] in alphabet_Eng:
                try:
                    cipher_word+=alphabet_Eng[alphabet_Eng.index(word[i])+sdvig]
                except IndexError:
                    print('no')
            if word[i] in alphabet_Ru:
                try:
                    cipher_word+=alphabet_Ru[alphabet_Ru.index(word[i])+sdvig]
                except IndexError:
                    print('таких букв нет')
        
        return cipher_word

    Сaesar_Word = Сaesar_Сipher()
    for i in Сaesar_Word:
        data.write(i) #записали в txt файл через data.write наш словарь


with open('Сaesar_Сipher.txt', 'r', encoding='utf-8') as data:  # пока работа в txt через data
    De_Cipher_Word = ' '
    for i in data:
        De_Cipher_Word += i
    
    def De_Сaesar_Сipher(De_Cipher_Word):
        
        sdvig = int(input('введите ключ для ДЕшифрования: -> '))
        alphabet_Eng = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
        alphabet_Ru = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', 'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
        de_cipher_word = ' ' 

        for i in range(len(De_Cipher_Word)):
            if De_Cipher_Word[i] in alphabet_Eng:
                try:
                    de_cipher_word+=alphabet_Eng[alphabet_Eng.index(De_Cipher_Word[i])-sdvig]
                except IndexError:
                    print('no')
            if De_Cipher_Word[i] in alphabet_Ru:
                try:
                    de_cipher_word+=alphabet_Ru[alphabet_Ru.index(De_Cipher_Word[i])-sdvig]
                except IndexError:
                    print('таких букв нет')
        
        return de_cipher_word    
    rez = De_Сaesar_Сipher(De_Cipher_Word)
    print('ваше слово: ', rez)

    