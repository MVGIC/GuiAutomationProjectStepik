from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.main_page import MainPage


def test_buy_product():
    """Тест по покупке товара включает в себя:
            авторизацию, выбор товара, заполнение данных получателя, подтверждение покупки."""
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("--incognito")  # или options.add_argument("--guest")
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    print("Start test")

    login = LoginPage(driver)
    login.authorization() # Авторизация

    mp = MainPage(driver)
    mp.add_product_to_cart() # Добавление товара в корзину

    cp = CartPage(driver)
    cp.move_to_checkout() # Переход к подтверждению товара
