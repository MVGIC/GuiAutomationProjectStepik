from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class MainPage(Base):
    """Класс содержащий локаторы и методы для Главной страницы"""


    # Locators

    select_product_1 = "//button[@id='add-to-cart-sauce-labs-backpack']"
    cart = "//div[@id='shopping_cart_container']"
    burger_menu = "//button[@id='react-burger-menu-btn']"
    link_about = "//a[@data-test='about-sidebar-link']"



    # Getters

    def get_select_product_1(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.select_product_1)))

    def get_cart(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_burger_menu(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.burger_menu)))


    def get_link_about(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.link_about)))

    # Actions

    def click_select_product_1(self):
        self.get_select_product_1().click()
        print("Add product 1 to cart")


    def click_cart(self):
        self.get_cart().click()
        print("Click cart")

    def click_burger_menu(self):
        self.get_burger_menu().click()
        print("Click burger menu")

    def click_link_about(self):
        self.get_link_about().click()
        print("Click link about")


    # Methods (Steps)

    def add_product_to_cart(self):
        """Добавление товара в корзину"""
        self.get_current_url()
        self.click_select_product_1()
        self.click_cart()

    def select_burger_menu_about(self):
        """Переход в раздел About"""
        self.get_current_url()
        self.click_burger_menu()
        self.click_link_about()
        self.assert_url("https://saucelabs.com/")
