from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = 'http://secure-retreat-92358.herokuapp.com/'

driver = webdriver.Firefox()
driver.get(URL)

f_name = driver.find_element(By.NAME, 'fName')
l_name = driver.find_element(By.NAME, 'lName')
email = driver.find_element(By.NAME, 'email')
button = driver.find_element(By.TAG_NAME, 'button')

f_name.send_keys('Nips')
l_name.send_keys('Alvin')
email.send_keys('test@gmail.com')
button.send_keys(Keys.ENTER)

driver.quit()
