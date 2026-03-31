from faker import Faker
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Уроки 5.29

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--guest")  # или options.add_argument("--incognito")
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

faker = Faker("en_US")
# faker = Faker("ru_RU")

faker_login = faker.first_name() + str(faker.random_int())
print(faker_login)

faker_password = faker.password()
print(faker_password)

login_standard_user = "standard_user"
password_all = "secret_sauce"

user_name = driver.find_element(By.XPATH, value="//input[@id='user-name']")  # XPATH
user_name.send_keys(faker_login)
print("Input Login")

password = driver.find_element(By.XPATH, value="//input[@id='password']")  # XPATH
password.send_keys(faker_password)
print("Input Password")
