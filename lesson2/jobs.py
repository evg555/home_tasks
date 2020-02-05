# Необходимо собрать информацию о вакансиях на вводимую должность
# (используем input или через аргументы) с сайта superjob.ru и hh.ru.
# Приложение должно анализировать несколько страниц сайта
# (также вводим через input или аргументы).
# Получившийся список должен содержать в себе минимум:
#
#     *Наименование вакансии
#     *Предлагаемую зарплату (отдельно мин. и отдельно макс.)
#     *Ссылку на саму вакансию
#     *Сайт откуда собрана вакансия
# По своему желанию можно добавить еще работодателя и расположение.
# Данная структура должна быть одинаковая для вакансий с обоих сайтов.
# Общий результат можно вывести с помощью dataFrame через pandas.

import requests
from bs4 import BeautifulSoup as bs
import re
import pandas as pd

# Парсим hh.ru
def get_from_hh(vacancy, jobs):
	hh_main_link = 'https://hh.ru/'
	headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0'}
	page = 0

	search_link = hh_main_link + f'/search/vacancy?st=searchVacancy&text={vacancy}'
	response = requests.get(search_link, headers=headers)

	while (response.ok):
		html = bs(response.text, 'lxml')

		job_blocks = html.findAll('div', {'class': 'vacancy-serp-item'})

		for job in job_blocks:
			job_data = {}
			job_data['source'] = 'hh.ru'
			job_data['title'] = job.find('a', {'data-qa': 'vacancy-serp__vacancy-title'}).getText()
			job_data['link'] = job.find('a', {'data-qa': 'vacancy-serp__vacancy-title'})['href']

			employer = job.find('a', {'data-qa': 'vacancy-serp__vacancy-employer'})

			if employer:
				job_data['employer'] = employer.getText()

			job_data['city'] = job.find('span', {'data-qa': 'vacancy-serp__vacancy-address'}).getText().split(',')[0]

			salary_str = job.find('div', {'data-qa': 'vacancy-serp__vacancy-compensation'})

			if not salary_str:
				job_data['min_salary'] = 0
				job_data['max_salary'] = 0
			else:
				salary_all = re.search('\d(.*)\d', salary_str.getText())[0].replace(u'\xa0', u'')
				salary = salary_all.split('-')
				salary_part = []

				for i in re.split('\d(.*)\d', salary_str.getText()):
					salary_part.append(i.strip())

				if len(salary) > 1:
					job_data['min_salary'] = int(salary[0])
					job_data['max_salary'] = int(salary[1])
				elif salary_part[0].lower() == 'от':
					job_data['min_salary'] = int(salary_all)
					job_data['max_salary'] = 0
				elif salary_part[0].lower() == 'до':
					job_data['min_salary'] = 0
					job_data['max_salary'] = int(salary_all)
				else:
					job_data['min_salary'] = int(salary_all)
					job_data['max_salary'] = int(salary_all)

				job_data['currency'] = salary_part[-1]

			jobs.append(job_data)

		page += 1
		search_link = hh_main_link + f'/search/vacancy?st=searchVacancy&text={vacancy}&page={page}'
		response = requests.get(search_link, headers=headers)

	return jobs

# Парсим superjob.ru
def get_fom_sj(vacancy, jobs):
	sj_main_link = 'https://www.superjob.ru'
	headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0'}
	page = 1

	search_link = sj_main_link + f'/vacancy/search?keywords={vacancy}'
	response = requests.get(search_link, headers=headers)
	html = bs(response.text, 'lxml')
	job_blocks = html.findAll('div', {'class': 'f-test-vacancy-item'})

	while (job_blocks):
		for job in job_blocks:
			job_data = {}
			job_data['source'] = 'superjob.ru'
			job_data['title'] = job.find('div', {'class': 'CuJz5'}).getText()
			job_data['link'] = sj_main_link + job.find('a', {'class': '_1QIBo'})['href']

			employer = job.find('a', {'class': '_205Zx'})

			if employer:
				job_data['employer'] = employer.getText()

			city = job.find('span', {'class': 'f-test-text-company-item-location'}).findChildren(recursive=False)[
				-1].getText()
			job_data['city'] = city.split(',')[0]

			salary_str = job.find('span', {'class': 'f-test-text-company-item-salary'})

			if not salary_str or salary_str.getText() == 'По договорённости':
				job_data['min_salary'] = 0
				job_data['max_salary'] = 0
			else:
				salary_all = re.search('\d(.*)\d', salary_str.getText())[0].replace(u'\xa0', u'')
				salary = salary_all.split('—')
				salary_part = []

				for i in re.split('\d(.*)\d', salary_str.getText()):
					salary_part.append(i.strip())

				if len(salary) > 1:
					job_data['min_salary'] = int(salary[0])
					job_data['max_salary'] = int(salary[1])
				elif salary_part[0].lower() == 'от':
					job_data['min_salary'] = int(salary_all)
					job_data['max_salary'] = 0
				elif salary_part[0].lower() == 'до':
					job_data['min_salary'] = 0
					job_data['max_salary'] = int(salary_all)
				else:
					job_data['min_salary'] = int(salary_all)
					job_data['max_salary'] = int(salary_all)

				job_data['currency'] = salary_part[-1]
			jobs.append(job_data)

		page += 1
		search_link = sj_main_link + f'/vacancy/search?keywords={vacancy}&page={page}'
		response = requests.get(search_link, headers=headers)
		html = bs(response.text, 'lxml')
		job_blocks = html.findAll('div', {'class': 'f-test-vacancy-item'})

	return jobs

if __name__ == '__main__':
	vacancy = input('Введите название вакансии: ')
	vacancy = vacancy.replace(' ', '+')

	jobs = []
	jobs = get_from_hh(vacancy, jobs)
	jobs = get_fom_sj(vacancy, jobs)

	df = pd.DataFrame(jobs)
	df.to_csv('jobs.csv')
	print(df)

