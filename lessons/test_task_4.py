from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from test_task_4_login import LoginPage
from test_task_4_products import ProductsPage

# Урок 6.5

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--incognito")  # или options.add_argument("--guest")
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

logins = ["standard_user", "locked_out_user", "problem_user", "performance_glitch_user", "error_user",
          "visual_user"]
password = "secret_sauce"

for login in logins:
    try:
        login_sample = LoginPage(driver)
        login_sample.authorization(login, password)

        product_sample = ProductsPage(driver)
        product_sample.check_page_title()
        product_sample.logout()

    except TimeoutException as exception:
        error_close_element = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='error-button']")))
        error_close_element.click()
        print("Close Error")
        driver.refresh()
        continue
