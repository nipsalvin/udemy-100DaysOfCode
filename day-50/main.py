import os
from time import sleep
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.chrome.service import Service

load_dotenv()

EMAIL = os.getenv('MY_EMAIL_2')
FB_PASSWORD = os.getenv('FACEBOOK_PASSWORD')
URL = 'https://tinder.com/app/recs'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--use-fake-ui-for-media-stream')  # Suppress location prompt

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)
driver.maximize_window()

sleep(10)
#Allow cookies
pop_up = driver.find_elements(By.CLASS_NAME, 'l17p5q9z')
allow_cookies = pop_up[3]
allow_cookies.click()

log_in_text = driver.find_element(By.LINK_TEXT, 'Log in')
log_in_text.click()

sleep(5)
log_in_with_fb = driver.find_element(By.XPATH, '/html/body/div[2]/main/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div/div')
log_in_with_fb.click()

#Store browser windows as variables
tinder_window = driver.window_handles[0]
fb_window =  driver.window_handles[1]

#Switch to pop-up login window
sleep(10)
driver.switch_to.window(fb_window)
email = driver.find_element(By.NAME, 'email')
email.send_keys(EMAIL)
sleep(2)
password =  driver.find_element(By.NAME, 'pass')
password.send_keys(FB_PASSWORD)
sleep(2)
fb_login_button = driver.find_element(By.ID, 'loginbutton')
fb_login_button.click()

#Switch back to original page
driver.switch_to.window(tinder_window) 
#Allow location
sleep(20)
allow_location = driver.find_element(By.CLASS_NAME, 'l17p5q9z')
allow_location.click()

sleep(10)
#Accepting cookies and Disabling Notifications
disable_notifications = driver.find_elements(By.CLASS_NAME, 'l17p5q9z')
disable_notifications = disable_notifications[1]
disable_notifications.click()
sleep(10)
# TODO: Start swiping
for n in range(50):
    sleep(2)
    try:   
        dislike_button = driver.find_element(By.XPATH,'//*[@id="q1298270057"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div/div[2]/button')
        like_button = driver.find_element(By.XPATH,'//*[@id="q1298270057"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div/div[4]/button')
        if n%2 == 0:
            like_button.click()
            print('Swipped Right')
        else:
            dislike_button.click()
            print('Swipped Left')

    # Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
            match_popup.click()
        #Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            sleep(2)


driver.quit()

