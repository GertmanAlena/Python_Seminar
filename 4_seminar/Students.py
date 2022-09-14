import os
os.system('CLS')

Students = {}
Students = \
	{
		'Соловьёва Дарья': 1,
		'Сорока Евшений': 4,
		'Курочкина Мария': 4,
		'Чижик Иван': 3,
		'Уточкина Наталья': 5
	}

with open('students.txt', 'w', encoding='utf-8') as data:  # пока работа в txt через data
	for i in Students:
		data.write(i + '\n') #записали в txt файл через data.write наш словарь
	
	Students['Василий'] = 5    #добавляем в словарь Василия
	data.write('Василий\n')  #добавляем в txt Василия через data.write

	print(Students)
	
with open('students.txt', 'a', encoding='utf-8') as data:
	for k in Students:
		'''
		Students 'Соловьёва Дарья': 5  читается как
		имя с индексом [к] имеет значение 5

		'''
		n = 5
		if Students[k] == n:
			data.write('\n'+k.upper())
			x = k.upper()
			print(x)
		else:
			data.write('\n'+k)


