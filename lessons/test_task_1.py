from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Урок 5.18 - Тестовое задание №1

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--guest")  # или options.add_argument("--incognito")
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

login_standard_user = "standard_user"
password_all = "secret_sauce"

user_name = driver.find_element(By.XPATH, value="//input[@id='user-name']")
user_name.send_keys(login_standard_user)
print("Input Login")

password = driver.find_element(By.XPATH, value="//input[@id='password']")
password.send_keys(password_all)
print("Input Password")

button_login = driver.find_element(By.XPATH, value="//input[@id='login-button']")
button_login.click()
print("Click Login Button")

"""INFO Product №1"""
product_1 = driver.find_element(By.XPATH, value="//a[@id='item_4_title_link']")
product_1_info = product_1.text
print(product_1_info)

price_product_1 = driver.find_element(By.XPATH, value="(//div[@data-test='inventory-item-price'])[1]")
price_product_1_info = price_product_1.text
print(price_product_1_info)

select_product_1 = driver.find_element(By.XPATH, value="//button[@id='add-to-cart-sauce-labs-backpack']")
select_product_1.click()
print("Select product 1")

"""INFO Product №2"""
product_2 = driver.find_element(By.XPATH, value="//a[@id='item_1_title_link']")
product_2_info = product_2.text
print(product_2_info)

price_product_2 = driver.find_element(By.XPATH, value="(//div[@data-test='inventory-item-price'])[3]")
price_product_2_info = price_product_2.text
print(price_product_2_info)

select_product_2 = driver.find_element(By.XPATH, value="//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']")
select_product_2.click()
print("Select product 2")

cart = driver.find_element(By.XPATH, value="//a[@class='shopping_cart_link']")
cart.click()
print("Enter Cart")

"""INFO Cart Product 1 """
cart_product_1 = driver.find_element(By.XPATH, value="//a[@id='item_4_title_link']")
cart_product_1_info = cart_product_1.text
print(cart_product_1_info)
assert product_1_info == cart_product_1_info
print("Product 1 INFO is correct")

price_cart_product_1 = driver.find_element(By.XPATH, value="(//div[@data-test='inventory-item-price'])[1]")
price_cart_product_1_info = price_cart_product_1.text
print(price_cart_product_1_info)
assert price_product_1_info == price_cart_product_1_info
print("Product 1 PRICE is correct")

"""INFO Cart Product 2"""
cart_product_2 = driver.find_element(By.XPATH, value="//a[@id='item_1_title_link']")
cart_product_2_info = cart_product_2.text
print(cart_product_2_info)
assert product_2_info == cart_product_2_info
print("Product 2 INFO is correct")

price_cart_product_2 = driver.find_element(By.XPATH, value="(//div[@data-test='inventory-item-price'])[2]")
price_cart_product_2_info = price_cart_product_2.text
print(price_cart_product_2_info)
assert price_product_2_info == price_cart_product_2_info
print("Product 2 PRICE is correct")

checkout = driver.find_element(By.XPATH, value="//button[@id='checkout']")
checkout.click()
print("Moved to Checkout")

"""Select User INFO"""
first_name = driver.find_element(By.XPATH, value="//input[@id='first-name']")
first_name.send_keys("First Name")
print("Input First Name")

last_name = driver.find_element(By.XPATH, value="//input[@id='last-name']")
last_name.send_keys("Last Name")
print("Input Last Name")

postal_code = driver.find_element(By.XPATH, value="//input[@id='postal-code']")
postal_code.send_keys("123456")
print("Input Postal Code")

button_continue = driver.find_element(By.XPATH, value="//input[@id='continue']")
button_continue.click()
print("Moved to Checkout Overview")

"""INFO Finish Product 1"""
finish_product_1 = driver.find_element(By.XPATH, value="//a[@id='item_4_title_link']")
finish_product_1_info = finish_product_1.text
print(finish_product_1_info)
assert product_1_info == finish_product_1_info
print("Product 1 Finish INFO is correct")

price_finish_product_1 = driver.find_element(By.XPATH, value="(//div[@data-test='inventory-item-price'])[1]")
price_finish_product_1_info = price_finish_product_1.text
print(price_finish_product_1_info)
assert price_product_1_info == price_finish_product_1_info
print("Product 1 Finish PRICE is correct")

"""INFO Finish Product 2"""
finish_product_2 = driver.find_element(By.XPATH, value="//a[@id='item_1_title_link']")
finish_product_2_info = finish_product_2.text
print(finish_product_2_info)
assert product_2_info == finish_product_2_info
print("Product 2 Finish INFO is correct")

price_finish_product_2 = driver.find_element(By.XPATH, value="(//div[@data-test='inventory-item-price'])[2]")
price_finish_product_2_info = price_finish_product_2.text
print(price_finish_product_2_info)
assert price_product_2_info == price_finish_product_2_info
print("Product 2 Finish PRICE is correct")

"""FINAL STEP"""
only_price_product_1 = float(price_finish_product_1_info.replace("$", ""))
only_price_product_2 = float(price_finish_product_2_info.replace("$", ""))

summary_price = driver.find_element(By.XPATH, value="//div[@data-test='subtotal-label']")
summary_only_price = float(summary_price.text.replace("Item total: $", ""))
print(summary_only_price)

assert summary_only_price == only_price_product_1 + only_price_product_2
print("Summary price is correct")
