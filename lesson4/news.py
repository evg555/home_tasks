# 1) Написать приложение, которое собирает основные новости с сайтов mail.ru, lenta.ru, yandex.news
# Для парсинга использовать xpath. Структура данных должна содержать:
# *название источника,
# *наименование новости,
# *ссылку на новость,
# *дата публикации
#
# 2)Сложить все новости в БД

import requests
from lxml import html
from pymongo import MongoClient
from datetime import datetime
import re

# Парсим lenta.ru
def get_news_from_lenta(news):
	lenta_link = "https://lenta.ru"
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0'}
	today = datetime.today().strftime("%d.%m.%Y")

	try:
		response = requests.get(lenta_link, headers=headers)
		root = html.fromstring(response.text)
		items = root.xpath("//div[@class='first-item']//h2//a | //div[@class='span4']/div[contains(@class,'item')]/a")

		for item in items:
			new_data = {}
			new_data['source'] = 'lenta.ru'
			title = item.xpath("./text()")

			if not title:
				continue
			else:
				new_data['name'] = title[0]

			new_data['link'] = lenta_link + item.xpath("./@href")[0]
			new_data['date_published'] = today + " " + item.xpath("./time/text()")[0]
			news.append(new_data)
	except:
		print(f'Ошибка запроса {lenta_link}')

	return news

# Парсим yandex.ru
def get_news_from_yandex(news):
	yandex_link = "https://yandex.ru"
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0'}
	today = datetime.today().strftime("%d.%m.%Y")

	try:
		response = requests.get(yandex_link + '/news/', headers=headers)
		root = html.fromstring(response.text)
		items = root.xpath("//td[@class='stories-set__item']")

		for item in items:
			new_data = {}
			story_date = item.xpath(".//div[@class='story__date']/text()")[0].split()

			new_data['source'] = story_date[0]
			new_data['name'] = item.xpath(".//h2//a/text()")[0]
			new_data['link'] = yandex_link + item.xpath(".//h2//a/@href")[0]
			new_data['date_published'] = today + " " + story_date[1]
			news.append(new_data)
	except:
		print(f'Ошибка запроса {yandex_link}')

	return news

# Парсим mail.ru
def get_news_from_mail(news):
	mail_link = "https://news.mail.ru"
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0'}

	try:
		response = requests.get(mail_link, headers=headers)
		root = html.fromstring(response.text)
		items = root.xpath("//a[@class='newsitem__title link-holder'] | //a[@class='list__text'] | //a[@class='link link_flex'] | //a[@class='item__title link-holder']")

		for item in items:
			new_data = {}
			title = item.xpath("./text()")

			if title:
				new_data['name'] = title[0]
			else:
				new_data['name'] = item.xpath("./span/text()")[0]

			link = item.xpath("./@href")[0]

			if re.search('https://', link):
				new_data['link'] = link
			else:
				new_data['link'] = mail_link + link

			response = requests.get(new_data['link'], headers=headers)
			item_detail = html.fromstring(response.text)
			news_datetime = item_detail.xpath("//span[@class='note__text breadcrumbs__text js-ago']/@datetime")

			if not news_datetime:
				news_datetime = item_detail.xpath("//time[contains(@class,'breadcrumbs__text')]/@datetime")

			if not news_datetime:
				news_datetime = item_detail.xpath("//span[@class='breadcrumbs__item js-ago']/@datetime")

			if news_datetime:
				news_datetime_split = news_datetime[0].split('T')
				news_time = news_datetime_split[1].split("+")
				news_date = datetime.strptime(news_datetime_split[0], '%Y-%m-%d').strftime('%d.%m.%Y')
				new_data['date_published'] = news_date + " " + news_time[0]
			else:
				new_data['date_published'] = ''

			source = item_detail.xpath("//a[@class='link color_gray breadcrumbs__link']//span[@class='link__text']/text()")

			if not source:
				new_data['source'] = 'mail.ru'
			else:
				new_data['source'] = source

			news.append(new_data)
	except:
		print(f'Ошибка запроса {mail_link}')

	return news

news = []
news = get_news_from_lenta(news)
news = get_news_from_yandex(news)
news = get_news_from_mail(news)

client = MongoClient('localhost',27017)
db = client['news']

for new in news:
	db.all.update_one({'link': new['link']},{'$set': new},upsert=True)

print(f'Добавлено {len(news)} новостей')