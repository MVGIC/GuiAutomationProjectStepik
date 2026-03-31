import glob
import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Урок 5.33

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--incognito")  # или options.add_argument("--guest")
path_download = r"/download_files\\"

options = webdriver.ChromeOptions()
prefs = {'download.default_directory': path_download}
options.add_experimental_option('prefs', prefs)
options.add_experimental_option("detach", True)
options.page_load_strategy = 'eager'
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://practice-automation.com/file-download/'
driver.get(base_url)
driver.maximize_window()

# driver.execute_script("window.scrollTo(0, 500)")
time.sleep(3)

click_button = driver.find_element(By.XPATH, "(//div[@class='ml-3'])[1]")
click_button.click()
print("Download file button clicked")

# Директория не пустая
# if os.listdir(path_download):
#     print("Файл в наличии")
# else:
#     print("Файла нет")

# Содержимое директории
# print(os.listdir(path_download))

# Наличие требуемого файла
file_name = "test.pdf"

file_path = path_download + file_name

assert os.access(file_path, os.F_OK) == True
print("Файл в директории")

# Файл не пуст
files = glob.glob(os.path.join(path_download, "*.*"))

for file in files:
    a = os.path.getsize(file)
    if a > 10:
        print("Файл не пуст")
    else:
        print("Файл пуст")

# Очистка директории
files = glob.glob(os.path.join(path_download, "*.*"))
for file in files:
    os.remove(file)
print("Директория очищена")
