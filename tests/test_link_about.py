from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import LoginPage
from pages.main_page import MainPage


def test_link_about():
    """Тест по переходу на новую страницу - в раздел About"""
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("--incognito")  # или options.add_argument("--guest")
    options.page_load_strategy = 'eager'
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    print("Start test")

    login = LoginPage(driver)
    login.authorization()  # Авторизация

    mp = MainPage(driver)
    mp.select_burger_menu_about()
