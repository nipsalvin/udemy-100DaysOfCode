from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

URL = 'https://orteil.dashnet.org/cookieclicker/'

driver = webdriver.Firefox()
driver.get(URL)

cookie = driver.find_element(By.CSS_SELECTOR, '#cookies button')
print(cookie)
timeout = time.time() + 5
five_min = time.time() + 60*5

all_prices = driver.find_elements(By.CLASS_NAME, ".storeSection")
print(all_prices)
# while True:
#     cookie.send_keys(Keys.ENTER)
#     if time.time > timeout:
        # all_prices = driver.find_elements(By.CSS_SELECTOR, '.product locked disabled')


driver.quit()



