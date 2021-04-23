"""
В этой задаче вам необходимо воспользоваться API сайта numbersapi.com

Вам дается набор чисел. Для каждого из чисел необходимо узнать, существует ли интересный математический факт об этом числе.

Для каждого числа выведите Interesting, если для числа существует интересный факт, и Boring иначе.
Выводите информацию об интересности чисел в таком же порядке, в каком следуют числа во входном файле.

Пример запроса к интересному числу:
http://numbersapi.com/31/math?json=true

Пример запроса к скучному числу:
http://numbersapi.com/999/math?json=true
"""
import requests as re
import sys
with open('C:\\Users\\nikit\\Downloads\\dataset_24476_3(1).txt') as ds:
	numbers=ds.readlines()
	numbers=list(map(lambda x:x[0:-1],numbers))
for number in numbers:
	res=re.get(f'http://numbersapi.com/{number}/math?json=true')
	data=res.json()
	if data['found']==True:
		print('Interesting')
	else:
		print('Boring')
