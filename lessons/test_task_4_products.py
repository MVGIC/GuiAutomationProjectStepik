from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class ProductsPage:

    def __init__(self, driver):
        self.driver = driver

    def check_page_title(self):
        title = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, "//span[@class='title']")))
        title_value = title.text
        assert title_value == "Products"

    def logout(self):
        burger_menu = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, "//button[@id='react-burger-menu-btn']")))
        burger_menu.click()
        logout_option = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@id='logout_sidebar_link']")))
        logout_option.click()
