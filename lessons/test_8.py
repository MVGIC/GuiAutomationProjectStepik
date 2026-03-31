from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Урок 5.22

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--guest")  # или options.add_argument("--incognito")
options.page_load_strategy = 'eager'
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = "https://demoqa.com/buttons"
driver.get(base_url)
driver.maximize_window()

tost_menu = driver.find_element(By.XPATH, value="(//div[@class='card-body'])[1]")
tost_menu.click()

buttons = driver.find_element(By.XPATH, value="(//a[@class='router-link'])[5]")  # Не находит локатор
buttons.click()

action = ActionChains(driver)
double_click_button = driver.find_element(By.XPATH, value="//button[@id='doubleClickBtn']")
action.double_click(double_click_button).perform()

success_message_double_click = driver.find_element(By.XPATH, value="//p[@id='doubleClickMessage']").text
assert success_message_double_click == "You have done a double click"

right_click_button = driver.find_element(By.XPATH, value="//button[@id='rightClickBtn']")
action.context_click(right_click_button).perform()

success_message_right_click = driver.find_element(By.XPATH, value="//p[@id='rightClickMessage']").text
assert success_message_double_click == "You have done a right click"
