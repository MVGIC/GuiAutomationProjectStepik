import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Урок 5.12

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--guest")  # или options.add_argument("--incognito")
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

login_standard_user = "standard_user"
password_all = "secret_sauce"

user_name = driver.find_element(By.XPATH, value="//input[@id='user-name']")  # XPATH
user_name.send_keys(login_standard_user)
print("Input Login")

password = driver.find_element(By.XPATH, value="//input[@id='password']")  # XPATH
password.send_keys(password_all)
print("Input Password")
password.send_keys(Keys.RETURN)

filter = driver.find_element(By.XPATH, value="//select[@data-test='product-sort-container']") # XPATH
filter.click()
print("Click Filter")
time.sleep(5)
filter.send_keys(Keys.DOWN)
time.sleep(5)
filter.send_keys(Keys.RETURN)
