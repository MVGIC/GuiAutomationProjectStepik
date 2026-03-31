import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Урок 5.25

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--guest")  # или options.add_argument("--incognito")
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://www.schoolsw3.com/howto/howto_js_rangeslider.php'
driver.get(base_url)
driver.maximize_window()

action = ActionChains(driver)
time.sleep(10)

price_slider = driver.find_element(By.XPATH, value="//input[@id='id2']")
action.click_and_hold(price_slider).move_by_offset(5, 0).release().perform()
print("Ползунок подвинули")
