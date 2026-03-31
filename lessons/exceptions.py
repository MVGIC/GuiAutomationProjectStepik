import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Урок 5.34

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--guest")  # или options.add_argument("--incognito")
options.page_load_strategy = 'eager'
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = "https://demoqa.com/radio-button"
driver.get(base_url)
driver.maximize_window()

# try:
#     visible_button = driver.find_element(By.XPATH, value="//button[@id='visibleAfter']")
#     visible_button.click()
# except NoSuchElementException as exception:
#     print("NoSuchElementException caught")
#     time.sleep(10)
#     visible_button = driver.find_element(By.XPATH, value="//button[@id='visibleAfter']")
#     visible_button.click()
#     print("Click Visible Button")

radio_button_yes = driver.find_element(By.XPATH, value="//label[@for='yesRadio']")
radio_button_yes.click()
try:
    message = driver.find_element(By.XPATH, value="//span[@class='text-success']")
    value_message = message.text
    print(value_message)
    assert value_message == "No"
except AssertionError as exception:
    driver.refresh()
    time.sleep(5)
    radio_button_yes = driver.find_element(By.XPATH, value="//label[@for='yesRadio']")
    radio_button_yes.click()
    message = driver.find_element(By.XPATH, value="//span[@class='text-success']")
    value_message = message.text
    print(value_message)
    assert value_message == "Yes"
print("Test over")
