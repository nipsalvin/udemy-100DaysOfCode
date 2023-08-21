import os
from dotenv import load_dotenv
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

load_dotenv()


SIMILAR_ACCOUNT = 'rogersndegwamuraguri'
USERNAME = os.getenv('IG_USERNAME')
PASSWORD = os.getenv('IG_PASSWORD')
URL = 'https://www.instagram.com/accounts/login/'

class InstaFollower:
    def __init__(self) -> None:
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get(URL)
        sleep(10)
        username = self.driver.find_element(By.NAME,'username')
        username.send_keys(USERNAME)
        sleep(2)
        password = self.driver.find_element(By.NAME, 'password')
        password.send_keys(PASSWORD)
        sleep(2)
        password.send_keys(Keys.ENTER)
        sleep(5)
        self.driver.quit()

        

    def login():
        '''logs into your Instagram account'''
        pass

    def find_followers():
        '''Finds followers in the target IG account'''
        pass

    def follow():
        '''Follows the followers in the target IG account'''
        pass


insta_bot = InstaFollower()
insta_bot.login()
insta_bot.find_followers()
insta_bot.follow()
