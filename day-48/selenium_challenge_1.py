from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://www.python.org/'

driver = webdriver.Firefox()
driver.get(url)

event_names = driver.find_elements(By.CSS_SELECTOR, '.event-widget ul li a')
event_times = driver.find_elements(By.CSS_SELECTOR, '.event-widget time')

## TODO complete this code
# for time in event_times:
#     print(time.text)
times = [time.text for time in event_times]
# print(times)
# for event in event_names:
#     print(event.text)
events = [event.text for event in event_names]
# print(events)

data = {}
for index in range(len(times)):
    data[index] = {
        'time':times[index],
        'name':events[index]
    }
# print(data)

# Using Dictionary comprehension
data_dict = {index: {'time': times[index], 'name': events[index]} for index in range(len(times))}
# print(data_dict)

driver.quit()


