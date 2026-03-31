import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Урок 5.27

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--incognito")  # или options.add_argument("--guest")
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://www.testmuai.com/selenium-playground/simple-form-demo/'
driver.get(base_url)
driver.maximize_window()

time.sleep(5)
# message = "Hello, world!"
# input_field = driver.find_element(By.XPATH, value="//input[@id='user-message']")
# input_field.send_keys(message)
# print("Message typed")
#
# button_get_checked_value = driver.find_element(By.XPATH, value="//button[@id='showInput']")
# button_get_checked_value.click()
# print("Message checked")
#
# field_message = driver.find_element(By.XPATH, value="//p[@id='message']")
# field_message_value = field_message.text
# print(field_message_value)
#
# assert field_message_value == message, "Значения не верны"
# print("Значения верны")

num_1 = 123
num_2 = 210

input_sum_field_1 = driver.find_element(By.XPATH, value="//input[@id='sum1']")
input_sum_field_1.send_keys(num_1)
print("First num typed")

input_sum_field_2 = driver.find_element(By.XPATH, value="//input[@id='sum2']")
input_sum_field_2.send_keys(num_2)
print("Second num typed")

sum_button = driver.find_element(By.XPATH, value="//button[contains(text(), 'Get Sum')]")
sum_button.click()
print("Got Sum")

sum_result = driver.find_element(By.XPATH, value="//p[@id='addmessage']")
sum_message_value = sum_result.text
print(sum_message_value)

sum_result = num_1 + num_2

assert sum_message_value == str(sum_result), "Значения не верны"
print("Значения верны")
