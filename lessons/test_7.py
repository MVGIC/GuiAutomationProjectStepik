import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Уроки 5.20-5.21

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--guest")  # или options.add_argument("--incognito")
options.page_load_strategy = 'eager'
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = "https://testpages.eviltester.com/pages/forms/html-form/"
driver.get(base_url)
driver.maximize_window()

driver.execute_script("window.scrollTo(0, 200)")
time.sleep(5)

checkbox = driver.find_element(By.XPATH, value="//input[@value='cb1']")
checkbox.click()
print("Click checkbox №1")

radio_button = driver.find_element(By.XPATH, value="//input[@value='rd1']")
radio_button.click()
print("Click radiobutton №1")
