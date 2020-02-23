# Парсим хиты продаж на mvideo

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


chrome_options = Options()
chrome_options.add_argument('--start-maximized')
driver = webdriver.Chrome()

driver.get('https://mvideo.ru/')
assert 'М.Видео' in driver.title

try:
	WebDriverWait(driver, 20).until(
		EC.frame_to_be_available_and_switch_to_it("fl-306642")
	)
	driver.find_element_by_class_name("close").click()
	driver.switch_to.default_content()
except:
	print('Всплывающеее окно не найдено')


hit_items = WebDriverWait(driver, 10).until(
	EC.presence_of_element_located((By.CLASS_NAME, "sel-hits-block"))
)

actions = ActionChains(driver)
actions.move_to_element(hit_items).perform()
arrow = hit_items.find_element_by_class_name("sel-hits-button-next")

while arrow.is_displayed():
	arrow.click()

items = hit_items.find_elements_by_class_name('gallery-list-item')

for item in items:
	title = item.find_element_by_class_name('sel-product-tile-title').text()
	print(title)
	break





