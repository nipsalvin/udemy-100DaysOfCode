from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from dotenv import load_dotenv
import time

load_dotenv()

ACCOUNT_EMAIL = os.getenv('MY_EMAIL')
ACCOUNT_PASSWORD = os.getenv('LINKEDIN_PASSWORD')
PHONE_NUMBER = os.getenv('TWILIO_VERIFIED_NUMBER')
URL = 'https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0'

driver = webdriver.Firefox()
driver.get(URL)

sign_in_button = driver.find_element(By.LINK_TEXT, 'Sign in')
sign_in_button.click()

#Wait for the next page to load.
time.sleep(5)
email_field = driver.find_element(By.ID, 'username')
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element(By.ID, 'password')
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)

time.sleep(10)
button = driver.find_element(By.CSS_SELECTOR, '.jobs-s-apply button')
button.click()

time.sleep(5)
phone = driver.find_element(By.CLASS_NAME, 'artdeco-text-input--input' )
if phone.text == "":
    phone.send_keys(PHONE_NUMBER)

time.sleep(5)
next = driver.find_element(By.CSS_SELECTOR, 'footer button')
print('submit',next)
print('submit tagname', next.tag_name)
print('submit text', next.text)
next.click()


driver.quit()


