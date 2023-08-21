import os
from time import sleep
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By

load_dotenv()

SPEED_TEST = 'https://fast.com/'
TWITTER_URL = 'https://twitter.com/'
PROMISED_UP = 15
PROMISED_DOWN = 20
TWITTER_EMAIL = os.getenv('MY_EMAIL')
TWITTER_PASSWORD = os.getenv('TWITTER_PASSWORD')

class InternetSpeedTwitterBot:
    def __init__(self) -> None:
        self.driver = webdriver.Chrome()
        self.up = 0
        self.down = 0
    
    def get_internet_speed(self):
        '''Getting current internet speed'''
        self.driver.maximize_window()
        self.driver.get(SPEED_TEST)
        sleep(20)
        more_details = self.driver.find_element(By.XPATH, '//*[@id="show-more-details-link"]')
        more_details.click()
        sleep(20)
        self.down = self.driver.find_element(By.XPATH, '//*[@id="speed-value"]').text
        self.up = self.driver.find_element(By.XPATH, '//*[@id="upload-value"]').text

    def tweet_at_provider(self):
        '''Logging in to Twitter and posting a tweet'''
        message = f'''Hello World I am getting upload speeds of {self.up}mbps.
                        Download speeds of {self.down}mbps
                        My provider promised {PROMISED_UP}mbps uploads
                        and {PROMISED_DOWN}mbps download speed.'''
        self.driver.get(TWITTER_URL)
        self.driver.maximize_window()
        sleep(10)
        sign_in = self.driver.find_element(By.LINK_TEXT, 'Sign in')
        sign_in.click()
        sleep(15)
        user_name = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        user_name.send_keys(TWITTER_EMAIL)
        submit = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
        submit.click()
        sleep(5)
        password = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(TWITTER_PASSWORD)
        log_in = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div')
        log_in.click()
        sleep(10)
        new_post = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
        new_post.click()
        sleep(5)
        pop_up = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[3]/div/div/div[2]/div/div[2]/div/div/div/div/div/div[2]/div[4]/div/span/span')
        pop_up.click()
        tweet = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        tweet.send_keys(message)
        post_tweet = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/div[4]/div/span/span')
        post_tweet.click()
        self.driver.quit()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()

