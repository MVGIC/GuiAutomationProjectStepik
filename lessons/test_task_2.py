import datetime
from datetime import timedelta

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Урок 5.24 - Тестовое задание №2

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--guest")  # или options.add_argument("--incognito")
options.page_load_strategy = 'eager'
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = "https://practice-automation.com/calendars/"
driver.get(base_url)
driver.maximize_window()

current_date = datetime.date.today()
print(f"Текущая дата: {current_date.strftime('%d.%m.%Y')}")

future_date = (current_date + timedelta(days=10)).strftime('%d.%m.%Y')
print(f"Дата через 10 дней: {future_date}")

input_calendar_field = driver.find_element(By.XPATH, value="//input[@id='g1065-1-selectorenteradate']")
input_calendar_field.send_keys(future_date)
print("Успешно ввели будущую дату в календарь")
