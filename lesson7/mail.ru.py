# Парсим письма из ящика на mail.ru

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pymongo import MongoClient

# Авторизуемся
def authorize(driver):
	login = 'study.ai_172@mail.ru'
	password = 'NewPassword172'

	input = driver.find_element_by_id('mailbox:login')
	input.send_keys(login)

	button = driver.find_element_by_css_selector('input.o-control')
	button.click()

	input = WebDriverWait(driver, 10).until(
		EC.element_to_be_clickable((By.ID, 'mailbox:password'))
	)

	input.send_keys(password)
	button.click()


# Получаем все ссылки на письма
def get_links(driver):
	links = []
	while True:
		letters = WebDriverWait(driver, 30).until(
			EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a.js-letter-list-item"))
		)

		letters_count = len(links)

		for letter in letters:
			links.append(letter.get_attribute('href'))

		links = list(set(links))

		if letters_count == len(links):
			return links

		actions = ActionChains(driver)
		actions.move_to_element(letters[-1])
		actions.perform()

# Собираем информацию по письмам
def get_items(driver, links):
	data = []
	for link in links:
		driver.get(link)
		assert 'Почта Mail.ru' in driver.title

		topic = WebDriverWait(driver, 20).until(
			EC.presence_of_element_located((By.CLASS_NAME, "thread__subject"))
		)

		item = {}
		item['topic'] = topic.text
		item['author'] = driver.find_element_by_class_name('letter-contact').text
		item['date'] = driver.find_element_by_class_name('letter__date').text
		data.append(item)

	return data

# Складываем письма в Mongo
def load_to_db(data):
	client = MongoClient('localhost', 27017)
	collection = client['letters'].mailru
	collection.insert_many(data)


driver = webdriver.Chrome()

driver.get('https://mail.ru/')
assert 'Mail.ru: почта' in driver.title

authorize(driver)
data = get_items(driver, get_links(driver))
load_to_db(data)

driver.quit()