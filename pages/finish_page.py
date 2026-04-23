import allure

from base.base_class import Base
from utilities.logger import Logger


class FinishPage(Base):
    """Класс содержащий локаторы и методы для финальной страницы"""

    # Locators

    # Getters

    # Actions

    # Methods (Steps)

    def check_last_page(self):
        with allure.step("Проверка последней страницы"):
            Logger.add_start_step(method="check_last_page")
            self.get_current_url()
            self.assert_url("https://www.saucedemo.com/checkout-complete.html")
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method="check_last_page")
