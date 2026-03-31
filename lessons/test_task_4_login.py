from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def authorization(self, login_name, login_password):
        username_field = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@id='user-name']")))
        username_field.send_keys(login_name)
        print("Input Login")

        password_field = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@id='password']")))
        password_field.send_keys(login_password)
        print("Input Password")

        button_login = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='login-button']")))
        button_login.click()
        print("Click Login Button")
