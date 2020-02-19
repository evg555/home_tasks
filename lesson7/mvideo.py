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

WebDriverWait(driver, 20).until(
	EC.frame_to_be_available_and_switch_to_it("fl-306642")
)
driver.find_element_by_class_name("close").click()
driver.switch_to.default_content()


hit_items = WebDriverWait(driver, 10).until(
	EC.presence_of_element_located((By.CLASS_NAME, "sel-hits-block"))
)

actions = ActionChains(driver)
actions.move_to_element(hit_items).perform()
arrow = driver.find_element_by_class_name("sel-hits-button-next").click()