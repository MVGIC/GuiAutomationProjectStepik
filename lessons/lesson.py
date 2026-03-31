import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Уроки 5.1-5.7

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--guest")  # или options.add_argument("--incognito")
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

# user_name = driver.find_element(By.ID, value="user-name") # ID
# user_name = driver.find_element(By.NAME, value="user-name") # NAME
user_name = driver.find_element(By.XPATH, value="//input[@id='user-name']")  # XPATH
user_name.send_keys("standard_user")
password = driver.find_element(By.CSS_SELECTOR, value="#password")  # CSS_SELECTOR
password.send_keys("secret_sauce")
button_login = driver.find_element(By.XPATH, value="//input[@value='Login']")  # XPATH
button_login.click()
time.sleep(10)
driver.close()
print("Браузер закрылся")
