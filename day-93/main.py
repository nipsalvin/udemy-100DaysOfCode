import os
from time import sleep
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
        # self.driver.maximize_window()
        self.driver.get(SPEED_TEST)
        print(f'Going to {SPEED_TEST}')
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="show-more-details-link"]')))
        print(f'Checking more details on {SPEED_TEST}')
        more_details = self.driver.find_element(By.XPATH, '//*[@id="show-more-details-link"]')
        more_details.click()
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="upload-value"]')))
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="speed-value"]')))
        print('Getting Download and Upload speeds')
        self.down = self.driver.find_element(By.XPATH, '//*[@id="speed-value"]').text
        sleep(10)
        self.up = self.driver.find_element(By.XPATH, '//*[@id="upload-value"]').text

    def tweet_at_provider(self):
        '''Logging in to Twitter and posting a tweet'''
        message = f'''Hello World I am getting upload speeds of {self.up}mbps.
        Download speeds of {self.down}mbps
        My provider promised {PROMISED_UP}mbps uploads
        and {PROMISED_DOWN}mbps download speed.'''
        print(f'Going to {TWITTER_URL}')
        self.driver.get(TWITTER_URL)
        # self.driver.maximize_window()
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Sign in')))
        print('Signing in')
        sign_in = self.driver.find_element(By.LINK_TEXT, 'Sign in')
        sign_in.click()
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')))
        print('Entering Username')
        user_name = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        user_name.send_keys(TWITTER_EMAIL)
        submit = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
        submit.click()
        try:
            print('Incase of suspicious activity, enter phone number and submit')
            WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')))
            phone_number_input = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
            phone_number_input.send_keys('+254719712242')
            next_button = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div')
            next_button.click()
        except:
            pass
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')))
        print('Enterring Password')
        password = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(TWITTER_PASSWORD)
        print('Click on login')
        log_in = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div')
        log_in.click()
        print('Click on new post')
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')))
        new_post = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
        new_post.click()
        print('Write and post tweet')
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH , '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div')))
        tweet = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div')
        tweet.send_keys(message)
        post_tweet = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div/div[4]/div/span/span')
        post_tweet.click()
        self.driver.quit()

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()

