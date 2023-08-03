from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://www.python.org/'

driver = webdriver.Chrome()
driver.get(url)

event_names = driver.find_elements(By.CSS_SELECTOR, '.event-widget a')
event_times = driver.find_elements(By.CSS_SELECTOR, '.event-widget time')

## TODO complete this code
for time in event_times:
    print(time.text)

for event in event_names:
    print(event.text)

driver.quit()


