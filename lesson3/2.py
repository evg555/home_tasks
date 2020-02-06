# Написать функцию, которая производит поиск и выводит на экран
# вакансии с заработной платой больше введенной суммы

from pymongo import MongoClient

def find_salary(salary):
	client = MongoClient('localhost', 27017)
	db = client['jobs']

	jobs = db.hh.find({
		'min_salary': {'$exists': True, '$gt': salary},
		'currency': 'руб.'
	})

	for job in jobs:
		print(job)

	jobs = db.sj.find({
		'min_salary': {'$exists': True, '$gt': salary},
		'currency': '₽'
	})

	for job in jobs:
		print(job)

salary = int(input('Введите заработную плату: '))
find_salary(salary)

