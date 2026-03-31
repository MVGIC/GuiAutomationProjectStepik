import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--headless=new")  # запуск теста без открытия браузера
options.add_argument("--guest")  # или options.add_argument("--incognito")
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()
time.sleep(3)

login_standard_user = "standard_user"
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

header = driver.find_element(By.XPATH, value="//span[@class='title']")  # XPATH
print(header.text)
assert header.text == "Products", "Incorrect title"
print("Correct title")
