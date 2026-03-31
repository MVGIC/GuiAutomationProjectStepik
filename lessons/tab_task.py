import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Урок 5.30

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--incognito")  # или options.add_argument("--guest")
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://demoqa.com/browser-windows'
driver.get(base_url)
driver.maximize_window()
time.sleep(3)

# Переключение между вкладками

# tab_button = driver.find_element(By.XPATH, value="//button[@id='tabButton']")
# tab_button.click()
# print("Tab Button click")
# time.sleep(3)
# print(driver.current_url)
#
# header_1 = driver.find_element(By.XPATH, value="//h1[@class='text-center']")
# print(header_1.text)
#
# driver.switch_to.window(driver.window_handles[1])
# time.sleep(3)
# print(driver.current_url)
#
# header_2 = driver.find_element(By.XPATH, value="//h1[@id='sampleHeading']")
# print(header_2.text)
#
# driver.switch_to.window(driver.window_handles[0])
# time.sleep(3)
# print(driver.current_url)

# Переключение между окнами

window_button = driver.find_element(By.XPATH, value="//button[@id='windowButton']")
window_button.click()
print("Window Button click")
time.sleep(3)
print(driver.current_url)

header_1 = driver.find_element(By.XPATH, value="//h1[@class='text-center']")
print(header_1.text)

window_1 = driver.window_handles[0]
window_2 = driver.window_handles[1]

driver.switch_to.window(window_2)
print(driver.current_url)

header_2 = driver.find_element(By.XPATH, value="//h1[@id='sampleHeading']")
print(header_2.text)

driver.switch_to.window(window_1)
print(driver.current_url)
print(header_1.text)
