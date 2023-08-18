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

sleep(10)
log_in_text = driver.find_element(By.LINK_TEXT, 'Log in')
log_in_text.click()

sleep(5)
log_in_with_fb = driver.find_element(By.XPATH, '/html/body/div[2]/main/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div/div')
log_in_with_fb.click()

#Store browser windows as variables
tinder_window = driver.window_handles[0]
fb_window =  driver.window_handles[1]

#Switch to pop-up login window
driver.switch_to.window(fb_window)
driver.maximize_window()
email = driver.find_element(By.NAME, 'email')
email.send_keys('')
password =  driver.find_element(By.NAME, 'pass')
password.send_keys('')
fb_login_button = driver.find_element(By.ID, 'loginbutton')
fb_login_button.click()

#Switch back to original page
driver.switch_to.window(tinder_window)
#Allow location
allow_location = driver.find_element(By.CLASS_NAME, 'l17p5q9z')
allow_location.click()
#Finding all `allow buttons`
allows = driver.find_elements(By.CLASS_NAME, 'l17p5q9z')
#Accepting cookies
cookies = allows[2]
cookies.click()
#Disabling Notifications
disable_notifications = allows[1]
disable_notifications.click()






driver.quit()

