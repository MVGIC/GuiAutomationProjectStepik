import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Урок 5.23

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--guest")  # или options.add_argument("--incognito")
options.page_load_strategy = 'eager'
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = "https://www.testmuai.com/selenium-playground/jquery-date-picker-demo/"
driver.get(base_url)
driver.maximize_window()

date_from = driver.find_element(By.XPATH, value="//input[@id='date-input']")
time.sleep(5)
date_from.send_keys("21.02.2026")
