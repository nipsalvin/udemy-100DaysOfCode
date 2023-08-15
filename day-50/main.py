import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

load_dotenv()

URL = 'https://tinder.com/app/recs'

driver = webdriver.Firefox()
driver.get(URL)






driver.quit()