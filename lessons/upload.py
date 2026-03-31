import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Урок 5.32

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--incognito")  # или options.add_argument("--guest")
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://www.testmuai.com/selenium-playground/upload-file-demo/'
driver.get(base_url)
driver.maximize_window()
time.sleep(3)

path_upload = r"upload_files/Байкал.jpg"

choose_file_button = driver.find_element(By.XPATH, value="//input[@id='file']")
choose_file_button.send_keys(path_upload)
print("File uploaded")
