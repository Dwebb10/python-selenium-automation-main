from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# simple built-in wait so finds/clicks don’t race the page
driver.implicitly_wait(10)

# open the url
driver.get('https://www.target.com/')


driver.find_element(By.XPATH, "//a[@data-test='@web/AccountLink']").click()

driver.find_element(By.XPATH, "//Button[@data-test='accountNav-signIn']").click()

expected_text = "Sign in or create account"
header = driver.find_element(By.XPATH, "//h1[text()='Sign in or create account']")
actual_text = header.text.strip()

assert expected_text == actual_text, f" Expected '{expected_text}' but got '{actual_text}'"
print(" Test passed: header text is correct")

print('Test case passed')
time.sleep(10)
driver.quit()

