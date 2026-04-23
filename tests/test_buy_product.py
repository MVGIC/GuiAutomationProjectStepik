import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.cart_page import CartPage
from pages.client_information_page import ClientInformationPage
from pages.finish_page import FinishPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.payment_page import PaymentPage


# @pytest.mark.run(order=3)
@allure.description("Test buy product 1")
def test_buy_product_1(set_group):
    """Тест по покупке товара включает в себя:
            авторизацию, выбор товара, заполнение данных получателя, подтверждение покупки."""
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("--incognito")  # или options.add_argument("--guest")
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    print("Start test 1")

    login = LoginPage(driver)
    login.authorization() # Авторизация

    mp = MainPage(driver)
    mp.add_product_1_to_cart()  # Добавление товара в корзину

    cp = CartPage(driver)
    cp.move_to_checkout() # Переход к подтверждению товара

    cip = ClientInformationPage(driver)
    cip.input_client_information() # Ввод информации клиента для оформления покупки

    p = PaymentPage(driver)
    p.finish_payment()

    f = FinishPage(driver)
    f.check_last_page()

    print("Finish Test 1")
    time.sleep(5)
    driver.quit()

# @pytest.mark.run(order=1)
def test_buy_product_2(set_up):
    """Тест по покупке товара включает в себя:
            авторизацию, выбор товара, заполнение данных получателя, подтверждение покупки."""
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("--incognito")  # или options.add_argument("--guest")
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    print("Start test 2")

    login = LoginPage(driver)
    login.authorization() # Авторизация

    mp = MainPage(driver)
    mp.add_product_2_to_cart()  # Добавление товара в корзину

    cp = CartPage(driver)
    cp.move_to_checkout() # Переход к подтверждению товара

    print("Finish Test 2")
    time.sleep(5)
    driver.quit()

# @pytest.mark.run(order=2)
def test_buy_product_3():
    """Тест по покупке товара включает в себя:
            авторизацию, выбор товара, заполнение данных получателя, подтверждение покупки."""
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("--incognito")  # или options.add_argument("--guest")
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    print("Start test 3")

    login = LoginPage(driver)
    login.authorization() # Авторизация

    mp = MainPage(driver)
    mp.add_product_3_to_cart()  # Добавление товара в корзину

    cp = CartPage(driver)
    cp.move_to_checkout() # Переход к подтверждению товара

    print("Finish Test 3")
    time.sleep(5)
    driver.quit()
