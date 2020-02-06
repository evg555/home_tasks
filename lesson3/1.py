# 1. Развернуть у себя на компьютере/виртуальной машине/хостинге MongoDB
# и реализовать функцию, записывающую собранные вакансии в созданную БД

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


vacancy = input('Введите название вакансии: ')
vacancy = vacancy.replace(' ', '+')

jobs = []
jobs = get_from_hh(vacancy, jobs)
insert_to_DB('hh',jobs)

jobs = []
jobs = get_from_sj(vacancy, jobs)
insert_to_DB('sj',jobs)