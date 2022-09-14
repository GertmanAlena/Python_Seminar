import os
os.system('CLS')

Students = {}
Students = \
	{
		'Соловьёва Дарья': '5',
		'Сорока Евшений': '4',
		'Курочкина Мария': '4',
		'Чижик Иван': '3',
		'Уточкина Наталья': '5'
	}
with open('students.txt', 'a', encoding='utf-8') as data:
	data.writelines(Students)
	
print(Students)


# for k in Students.keys():
# 	print(k)
for item in Students:
	for k in Students.values():
		if k == 5:
			print('{}:{}'.format(item, Students[k]))
# for z in Students:
# 	print(Students[z], end=' ')