from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

URL = 'http://secure-retreat-92358.herokuapp.com/'

driver = webdriver.Firefox()
driver.get(URL)

f_name = driver.find_element(By.NAME, 'fName')
f_name.send_keys('Nips')
time.sleep(5)
l_name = driver.find_element(By.NAME, 'lName')
l_name.send_keys('Alvin')
time.sleep(5)
email = driver.find_element(By.NAME, 'email')
email.send_keys('test@gmail.com')
time.sleep(5)
button = driver.find_element(By.TAG_NAME, 'button')




button.send_keys(Keys.ENTER)

# driver.quit()
