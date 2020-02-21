# Парсим хиты продаж на mvideo

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


chrome_options = Options()
chrome_options.add_argument('--start-maximized')
driver = webdriver.Chrome(options=chrome_options)

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
	EC.presence_of_all_elements_located((By.CLASS_NAME, "accessories-carousel-holder"))
)

actions = ActionChains(driver)
actions.move_to_element(hit_items[2]).perform()
arrow = driver.find_element_by_class_name("sel-hits-button-next").click()