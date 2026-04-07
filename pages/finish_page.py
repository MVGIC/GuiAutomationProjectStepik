from base.base_class import Base


class FinishPage(Base):
    """Класс содержащий локаторы и методы для финальной страницы"""

    # Locators

    # Getters

    # Actions

    # Methods (Steps)

    def check_last_page(self):
        """Проверка последней страницы"""
        self.get_current_url()
        self.assert_url("https://www.saucedemo.com/checkout-complete.html")
        self.get_screenshot()
