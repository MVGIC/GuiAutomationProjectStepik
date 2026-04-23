import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from utilities.logger import Logger


class CartPage(Base):
    """Класс содержащий локаторы и методы для страницы Корзины"""

    # Locators

    checkout_button = "//button[@data-test='checkout']"

    # Getters

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.checkout_button)))

    # Actions

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print("Click checkout button")

    # Methods (Steps)

    def move_to_checkout(self):
        with allure.step("Переход на страницу подтверждения товара"):
            Logger.add_start_step(method="move_to_checkout")
            self.get_current_url()
            self.click_checkout_button()
            Logger.add_end_step(url=self.driver.current_url, method="move_to_checkout")
