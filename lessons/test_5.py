import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Уроки 5.15-5.16

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--guest")  # или options.add_argument("--incognito")
options.page_load_strategy = 'eager'
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

login_standard_user = "standard_user"
password_all = "secret_sauce"

user_name = driver.find_element(By.XPATH, value="//input[@id='user-name']")
user_name.send_keys(login_standard_user)
print("Input Login")
# time.sleep(5)
# user_name.clear()

password = driver.find_element(By.XPATH, value="//input[@id='password']")
password.send_keys(password_all)
print("Input Password")

button_login = driver.find_element(By.XPATH, value="//input[@id='login-button']")
button_login.click()
print("Click Login Button")

menu = driver.find_element(By.XPATH, value="//button[@id='react-burger-menu-btn']")
menu.click()
print("Click Menu Button")
time.sleep(5)

link_about = driver.find_element(By.XPATH, value="//a[@id='about_sidebar_link']")
link_about.click()
print("Click Link Button")

driver.back()
print("Go back")
time.sleep(10)
driver.forward()
print("Go forward")
time.sleep(10)
