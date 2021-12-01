from selenium import webdriver
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

os.environ['PATH'] += r"C:\Users\Alex\Desktop\Apps\web_scraping_selenium\chromedriver.exe"
driver = webdriver.Chrome()

address = r"https://xiongemi.github.io/angular-form-ngxs/delivery"

driver.get(address)

name_input = driver.find_element(By.CSS_SELECTOR, "input[formcontrolname='firstName']")
last_name_input = driver.find_element(By.CSS_SELECTOR, "input[formcontrolname='lastName']")
address_line_1 = driver.find_element(By.CSS_SELECTOR, "input[formcontrolname='addressLine1']")
city = driver.find_element(By.CSS_SELECTOR, "input[formcontrolname='city']")
province = driver.find_element(By.CSS_SELECTOR, "input[formcontrolname='province']")
country = driver.find_element(By.CSS_SELECTOR, "input[formcontrolname='country']")
postal_code = driver.find_element(By.CSS_SELECTOR, "input[formcontrolname='postalCode']")
checkout_as_guest = driver.find_elements(By.CSS_SELECTOR, "mat-radio-button")
email = driver.find_element(By.CSS_SELECTOR, "input[formcontrolname='email']")
submit = driver.find_element(By.CSS_SELECTOR, "button[color='primary']")

name_input.send_keys("FirstName")
last_name_input.send_keys("LastName")
address_line_1.send_keys("AddressLine1")
city.send_keys("City")
province.send_keys("Province")
country.send_keys("Country")
postal_code.send_keys("123456")
checkout_as_guest[1].click()
email.send_keys("myemail@email.com")

time.sleep(1)
submit.click()

