import os
from time import sleep
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

load_dotenv()

PHONE_NUMBER = os.getenv('TWILIO_VERIFIED_NUMBER')
URL = 'https://tinder.com/app/recs'

driver = webdriver.Firefox()
driver.get(URL)

sleep(5)
log_in_text = driver.find_element(By.LINK_TEXT, 'Log in')
log_in_text.click()
sleep(5)
# log_in_with_number = driver.find_element(By.XPATH, '/html/body/div[2]/main/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[3]/button')
log_in_with_fb = driver.find_element(By.XPATH, '//*[@id="email"]')



driver.quit()

