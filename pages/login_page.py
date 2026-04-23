import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from utilities.logger import Logger


class LoginPage(Base):
    """Класс содержащий локаторы и методы для страницы Авторизации"""

    url = 'https://www.saucedemo.com/'

    # Locators

    user_name = "//input[@id='user-name']"
    password = "//input[@id='password']"
    login_button = "//input[@id='login-button']"
    products_title = "//span[@class='title']"


    # Getters

    def get_user_name(self):
        return WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_products_title(self):
        return WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, self.products_title)))


    # Actions

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("Input user name")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_login_button(self):
        self.get_login_button().click()
        print("Click login button")

    # Methods (Steps)

    def authorization(self):
        with allure.step("Авторизация в системе"):
            Logger.add_start_step(method="authorization")
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.input_user_name("standard_user")
            self.input_password("secret_sauce")
            self.click_login_button()
            self.assert_word(self.get_products_title(), "Products")
            Logger.add_end_step(url=self.driver.current_url, method="authorization")
