from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class PaymentPage(Base):
    """Класс содержащий локаторы и методы для страницы Оплаты"""


    # Locators

    finish_button = "//button[@data-test='finish']"


    # Getters

    def get_finish_button(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.finish_button)))


    # Actions

    def click_finish_button(self):
        self.get_finish_button().click()
        print("Click finish button")


    # Methods (Steps)

    def finish_payment(self):
        """Завершение оплаты"""
        self.get_current_url()
        self.click_finish_button()
