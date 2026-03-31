import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Уроки 5.8-5.9

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

button_login = driver.find_element(By.XPATH, value="//input[@id='login-button']")  # XPATH
button_login.click()
print("Click Login Button")

now_date = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
name_screenshot = "screenshot_" + now_date + ".png"
driver.save_screenshot(".\\screen\\" + name_screenshot)

header = driver.find_element(By.XPATH, value="//span[@class='title']")  # XPATH
value_text_products = header.text
print(value_text_products)
assert value_text_products == "Products", "Incorrect title"
print("Correct title")

url = "https://www.saucedemo.com/inventory.html"
get_url = driver.current_url
print(get_url)
assert url == get_url, "Incorrenct URL"
print("Correct URL")
