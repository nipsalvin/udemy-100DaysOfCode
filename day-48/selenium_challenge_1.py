from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://www.python.org/'

driver = webdriver.Chrome()
driver.get(url)

upcoming_events = driver.find_elements(By.CSS_SELECTOR, '.shrubbery ul li')
print(upcoming_events)

## TODO complete this code
for event in upcoming_events:
    print(event.text)





