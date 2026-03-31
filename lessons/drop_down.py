import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Урок 5.26

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--guest")  # или options.add_argument("--incognito")
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

login_standard_user = "standard_user"
password_all = "secret_sauce"
#
user_name = driver.find_element(By.XPATH, value="//input[@id='user-name']")
user_name.send_keys(login_standard_user)
print("Input Login")

password = driver.find_element(By.XPATH, value="//input[@id='password']")
password.send_keys(password_all)
print("Input Password")

button_login = driver.find_element(By.XPATH, value="//input[@id='login-button']")
button_login.click()
print("Click Login Button")

# select = Select(driver.find_element(By.XPATH, value="//select[@data-test='product-sort-container']"))
# time.sleep(3)
# # select.select_by_visible_text("Name (Z to A)")
# select.select_by_value("za")
# print("Выбрали значение в выпадающем списке")


click_drop = driver.find_element(By.XPATH, value="//select[@data-test='product-sort-container']")
time.sleep(3)
click_drop.click()
print("Click dropdown")

click_country = driver.find_element(By.XPATH, value="//option[@value='lohi']")
time.sleep(3)
click_country.click()
print("Filter selected")
