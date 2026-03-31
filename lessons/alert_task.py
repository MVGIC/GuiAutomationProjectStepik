import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Урок 5.31

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--incognito")  # или options.add_argument("--guest")
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://the-internet.herokuapp.com/javascript_alerts'
driver.get(base_url)
driver.maximize_window()
time.sleep(3)

# Взаимодействие с сообщением, в котором только кнопка "ОК"

# alert_button = driver.find_element(By.XPATH, value="//button[@onclick='jsAlert()']")
# alert_button.click()
# print("Click alert button")
# time.sleep(3)
# driver.switch_to.alert.accept()

# Взаимодействие с сообщением, в котором кнопки "ОК" и "ОТМЕНА"

confirm_button = driver.find_element(By.XPATH, value="//button[@onclick='jsConfirm()']")
confirm_button.click()
print("Click confirmed button")
time.sleep(3)

# driver.switch_to.alert.accept() # Подтверждение
# print("Alert confirmed")
driver.switch_to.alert.dismiss()  # Отклонение
print("Alert dismissed")
