import datetime
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Уроки 5.13-5.14

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

# driver.execute_script("window.scrollTo(0, 200)")
action = ActionChains(driver)
red_tshirt = driver.find_element(By.XPATH, value="//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']")
action.move_to_element(red_tshirt).perform()

time.sleep(5)

now_date = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
name_screenshot = "screenshot_" + now_date + ".png"
driver.save_screenshot(".\\screen\\" + name_screenshot)
