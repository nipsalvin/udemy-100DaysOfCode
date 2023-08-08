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

time.sleep(5)
div_elements = driver.find_elements(By.TAG_NAME, 'div')
div_class = 'jobs-s-apply'
# filtered_class = [button for button in div_elements if button.get_attribute('class') == div_class]
# print(filtered_class)
for div in div_elements:
    print(div.get_attribute('class'))




# phone = driver.find_element(By.CLASS_NAME, 'artdeco-text-input--input' )
# if phone.text == "":
#     phone.send_keys(PHONE_NUMBER)

# submit = driver.find_element(By.CLASS_NAME, 'artdeco-button__text')
# submit.click()



# driver.quit()


