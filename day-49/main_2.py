from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import os
from dotenv import load_dotenv
import time

load_dotenv()

ACCOUNT_EMAIL = os.getenv('MY_EMAIL')
ACCOUNT_PASSWORD = os.getenv('LINKEDIN_PASSWORD')
PHONE_NUMBER = os.getenv('TWILIO_VERIFIED_NUMBER')
URL = 'https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0'

driver = webdriver.Firefox()
driver.get(URL)

# Find sign-in button and click on it
sign_in_button = driver.find_element(By.LINK_TEXT, 'Sign in')
sign_in_button.click()

#Wait for the next page to load.
time.sleep(5)
# Find email field and fill it and ENTER
email_field = driver.find_element(By.ID, 'username')
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element(By.ID, 'password')
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)


time.sleep(5)
all_jobs = driver.find_elements(By.CSS_SELECTOR, '.job-card-container--clickable')

for job in all_jobs: ##FIXME Crapping out on the second run of the loop
    print(f'{job.text} called')
    job.click()
    time.sleep(5)

    try:
        #Find Easy apply button and click on it
        button = driver.find_element(By.CSS_SELECTOR, '.jobs-s-apply button')
        button.click()
        time.sleep(5)
        
        labels = driver.find_elements(By.CLASS_NAME, 'artdeco-text-input--input' )

        for i in labels:
            if i.accessible_name == 'Mobile phone number':
                phone = i

        if phone.text == "":
            phone.send_keys(PHONE_NUMBER)

        submit = driver.find_element(By.CSS_SELECTOR, 'footer button')
        submit.click()

        #If the submit_button is a "Next" button, then this is a multi-step application, so skip.
        # if submit.get_attribute("data-control-name") == "continue_unify":
        if submit.accessible_name == 'Continue to next step':
            import ipdb;ipdb.set_trace()
            close_button = driver.find_element(By.CLASS_NAME, 'artdeco-modal__dismiss')
            close_button.click()
            time.sleep(3)

            discard_button = driver.find_elements(By.CLASS_NAME, 'artdeco-modal__confirm-dialog-btn')[0]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit.click()

        #Once application completed, close the pop-up window.
        time.sleep(3)
        close_button = driver.find_element(By.CLASS_NAME, 'artdeco-modal__dismiss')
        close_button.click()

        #If already applied to job or job is no longer accepting applications, then skip.
    except NoSuchElementException:
        print("No application button, skipped.")
        continue



time.sleep(5)
driver.quit()


