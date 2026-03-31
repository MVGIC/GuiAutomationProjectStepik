import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Урок 5.28

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--incognito")  # или options.add_argument("--guest")
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://www.testmuai.com/selenium-playground/iframe-demo/'
driver.get(base_url)
driver.maximize_window()
time.sleep(5)

iframe = driver.find_element(By.XPATH, value="//iframe[@id='iFrame1']")
driver.switch_to.frame(iframe)

field = driver.find_element(By.XPATH, value="//div[@id='__next']/div/div/div[2]")
field_value = field.text
print(field_value)

field.send_keys(Keys.CONTROL + "a")

bold_button = driver.find_element(By.XPATH, value="//button[@title='Bold']")
bold_button.click()
print("Bold clicked")

bold_field = driver.find_element(By.XPATH, value="//div[@id='__next']/div/div/div[2]/b")
bold_field_value = bold_field.text
print(bold_field_value)

assert field_value == bold_field_value, "Значения не равны"
print("Редактирование успешно")
