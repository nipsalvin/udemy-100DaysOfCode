import os
from dotenv import load_dotenv
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException

load_dotenv()


SIMILAR_ACCOUNT = 'rogersndegwamuraguri'
USERNAME = os.getenv('IG_USERNAME')
PASSWORD = os.getenv('IG_PASSWORD')
TARGET_ACCOUNT = os.getenv('IG_TARGET_ACCOUNT')
URL = 'https://www.instagram.com/accounts/login/'

class InstaFollower:
    def __init__(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

        

    def login(self):
        '''logs into your Instagram account'''
        self.driver.get(URL)
        sleep(10)
        username = self.driver.find_element(By.NAME,'username')
        username.send_keys(USERNAME)
        sleep(2)
        password = self.driver.find_element(By.NAME, 'password')
        password.send_keys(PASSWORD)
        sleep(2)
        password.send_keys(Keys.ENTER)
        sleep(20)
        # self.driver.quit()
        not_now = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div')
        not_now.click()
        sleep(5)
        no_notifications = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
        no_notifications.click()
        sleep(5)

    def find_followers(self):
        '''Finds followers in the target IG account'''
        import ipdb;ipdb.set_trace()
        self.driver.get(TARGET_ACCOUNT)
        sleep(5)
        Target_account_followers = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a')
        Target_account_followers.click()
        # scrolling
        scrollable = self.driver.find_element(By.CLASS_NAME, "_aano")
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable)
            sleep(3)



    def follow(self):
        '''Follows the followers in the target IG account'''
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, "li button")
        for follower in all_buttons:
            try:
                follower.click()
                sleep(2)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, '//*[@id="mount_0_0_pI"]/div/div/div[3]/div/div[2]/div[1]/div/div[2]/div/div/div/div/div/div/button[2]')
                cancel_button.click()


insta_bot = InstaFollower()
insta_bot.login()
insta_bot.find_followers()
insta_bot.follow()
