from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class MainPage(Base):
    """Класс содержащий локаторы и методы для Главной страницы"""


    # Locators

    select_product_1 = "//button[@id='add-to-cart-sauce-labs-backpack']"
    cart = "//div[@id='shopping_cart_container']"


    # Getters

    def get_select_product_1(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.select_product_1)))

    def get_cart(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.cart)))


    # Actions

    def click_select_product_1(self):
        self.get_select_product_1().click()
        print("Add product 1 to cart")


    def click_cart(self):
        self.get_cart().click()
        print("Click cart")


    # Methods (Steps)

    def add_product_to_cart(self):
        """Добавление товара в корзину"""
        self.get_current_url()
        self.click_select_product_1()
        self.click_cart()
