from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Урок 5.36

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--incognito")  # или options.add_argument("--guest")
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


print("Приветствую тебя в нашем интернет-магазине")
print("Выбери один из следующих товаров и укажи его номер: 1 - Sauce Labs Backpack, 2 - Sauce Labs Bike Light, "
      "3 - Sauce Labs Bolt T-Shirt, 4 - Sauce Labs Fleece Jacket, 5 - Sauce Labs Onesie, 6 - Test.allTheThings() T-Shirt (Red)")
product = input("Введите цифру интересующего товара: ")
print(product)


"""Info about product"""
product_name = driver.find_element(By.XPATH, value=f"(//div[@data-test='inventory-item-name'])[{product}]")
product_name_info = product_name.text
print(product_name_info)

price_product = driver.find_element(By.XPATH, value=f"(//div[@data-test='inventory-item-price'])[{product}]")
price_product_info = price_product.text
print(price_product_info)

product_add_button = driver.find_element(By.XPATH, value=f"(//button[@class='btn btn_primary btn_small btn_inventory '])[{product}]")
product_add_button.click()
print("Product added to cart")

cart = driver.find_element(By.XPATH, value="//a[@class='shopping_cart_link']")
cart.click()
print("Moved to cart")


"""Info about product in cart"""
product_name_in_cart = driver.find_element(By.XPATH, value="//div[@data-test='inventory-item-name']")
product_name_in_cart_info = product_name_in_cart.text
print(product_name_in_cart_info)
assert product_name_info == product_name_in_cart_info
print("Product name is correct")

product_price_in_cart = driver.find_element(By.XPATH, value=f"//div[@data-test='inventory-item-price']")
product_price_in_cart_info = product_price_in_cart.text
print(product_price_in_cart_info)
assert price_product_info == product_price_in_cart_info
print("Product price is correct")

checkout = driver.find_element(By.XPATH, value="//button[@id='checkout']")
checkout.click()
print("Moved to Checkout")


"""Select user info"""
first_name = driver.find_element(By.XPATH, value="//input[@id='first-name']")
first_name.send_keys("First Name")
print("Input First Name")

last_name = driver.find_element(By.XPATH, value="//input[@id='last-name']")
last_name.send_keys("Last Name")
print("Input Last Name")

postal_code = driver.find_element(By.XPATH, value="//input[@id='postal-code']")
postal_code.send_keys("123456")
print("Input Postal Code")

continue_button = driver.find_element(By.XPATH, value="//input[@id='continue']")
continue_button.click()
print("Moved to Checkout Overview")


"""Info about product in Checkout"""
product_checkout_name = driver.find_element(By.XPATH, value="//div[@data-test='inventory-item-name']")
product_checkout_name_info = product_checkout_name.text
print(product_checkout_name_info)
assert product_name_info == product_checkout_name_info
print("Product checkout name is correct")

product_checkout_price = driver.find_element(By.XPATH, value="//div[@data-test='inventory-item-price']")
product_checkout_price_info = product_checkout_price.text
print(product_checkout_price_info)
assert price_product_info == product_checkout_price_info
print("Product checkout price is correct")

item_total_price = driver.find_element(By.XPATH, value="//div[@data-test='subtotal-label']")
item_total_price_info = item_total_price.text
print(item_total_price_info)
product_checkout_total_price = "Item total: " + product_checkout_price_info
print(product_checkout_total_price)
assert item_total_price_info == product_checkout_total_price
print("Total item price is correct")
