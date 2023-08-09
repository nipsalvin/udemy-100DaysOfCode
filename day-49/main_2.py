from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
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

# Find sign-in button and click on it
sign_in_button = driver.find_element(By.LINK_TEXT, 'Sign in')
sign_in_button.click()

#Wait for the next page to load.
time.sleep(5)
# Find email field and fill it and ENTER
email_field = driver.find_element(By.ID, 'username')
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element(By.ID, 'password')
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)

#Wait for the next page to load.
time.sleep(10)
#Find Easy apply button and click on it
buttons = driver.find_elements(By.CSS_SELECTOR, '.jobs-s-apply button')
easy_apply = buttons[0]
save_for_later = buttons[1]
save_for_later.click()

time.sleep(5)
## TODO
''' Get all divs from the navigation panel then loop through all of them'''


driver.quit()


