# *Написать функцию, которая будет добавлять в вашу базу данных только
# новые вакансии с сайта

from lesson2.jobs import get_from_hh, get_from_sj
from pymongo import MongoClient

def insert_to_DB(collection_name, data):
	client = MongoClient('localhost', 27017)
	db = client['jobs']
	collection = 'all'

	if collection_name == 'hh':
		collection = db.hh
	elif collection_name == 'sj':
		collection = db.sj

	collection.insert_many(data)
	print(f'Data are inserted to {collection_name}')

def filter_jobs(collection_name, jobs):
	client = MongoClient('localhost', 27017)
	db = client['jobs']

	if collection_name == 'hh':
		collection = db.hh
	elif collection_name == 'sj':
		collection = db.sj

	for job in jobs:
		obj = collection.find({'link': job['link']})
		if obj:
			jobs.remove(job)
		else:
			continue

	return jobs

def update_jobs(vacancy):
	jobs = []
	jobs = get_from_hh(vacancy, jobs)
	jobs = filter_jobs('hh',jobs)
	count = len(jobs)
	insert_to_DB('hh', jobs)

	jobs = []
	jobs = get_from_sj(vacancy, jobs)
	jobs = filter_jobs('sj', jobs)
	count += len(jobs)
	insert_to_DB('sj', jobs)

	return count

vacancy = input('Введите название вакансии: ')
vacancy = vacancy.replace(' ', '+')

updated_jobs = update_jobs(vacancy)
print(f'Обновлено {updated_jobs} вакансий')



