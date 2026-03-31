import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Уроки 5.10-5.11

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--guest")  # или options.add_argument("--incognito")
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

login_standard_user = "standard_use"
password_all = "secret_sauce"

user_name = driver.find_element(By.XPATH, value="//input[@id='user-name']")  # XPATH
user_name.send_keys(login_standard_user)
print("Input Login")

password = driver.find_element(By.XPATH, value="//input[@id='password']")  # XPATH
password.send_keys(password_all)
print("Input Password")

button_login = driver.find_element(By.XPATH, value="//input[@id='login-button']")  # XPATH
button_login.click()
print("Click Login Button")

warring_text = button_login = driver.find_element(By.XPATH, value="//h3[@data-test='error']")  # XPATH
value_warring_text = warring_text.text
assert value_warring_text == "Epic sadface: Username and password do not match any user in this service", "Negative test failed"
print("Negative tests succeeded")

time.sleep(3)
driver.refresh()
