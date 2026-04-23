import allure
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class ClientInformationPage(Base):
    """Класс содержащий локаторы и методы для страницы клиентской информации"""

    # Locators

    first_name = "//input[@data-test='firstName']"
    last_name = "//input[@data-test='lastName']"
    postal_code = "//input[@data-test='postalCode']"
    continue_button = "//input[@data-test='continue']"

    # Getters

    def get_first_name(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_postal_code(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.postal_code)))

    def get_continue_button(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.continue_button)))

    # Actions

    def input_first_name(self, first_name):
        self.get_first_name().send_keys(first_name)
        print("Input first name")

    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print("Input last name")

    def input_postal_code(self, postal_code):
        self.get_postal_code().send_keys(postal_code)
        print("Input postal code")

    def click_continue_button(self):
        self.get_continue_button().click()
        print("Click continue button")

    # Methods (Steps)

    def input_client_information(self):
        with allure.step("Ввод клиентской информации при подтверждении покупки"):
            fake = Faker()
            self.get_current_url()
            self.input_first_name(fake.first_name())
            self.input_last_name(fake.last_name())
            self.input_postal_code(fake.postcode())
            self.click_continue_button()
