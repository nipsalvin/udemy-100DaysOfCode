from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

URL = 'https://orteil.dashnet.org/cookieclicker/'

driver = webdriver.Firefox()
driver.get(URL)

timeout = time.time() + 5
five_min = time.time() + 60*5

#Get cookie to be click
cookie = driver.find_element(By.ID, 'bigCookie')

#Getting item IDs
items = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_ids = [item.get_attribute("id") for item in items]
print(item_ids)

language = driver.find_element(By.ID, 'loader')
print(language)

while True:
    cookie.click()

    #Every 5 secs
    if time.time() > timeout:
        #Gets all upgrades <b>
        all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        item_prices = []
        #Convert all_prices into an integer list
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)
                print(f'2{item_prices}')
        
        #Dict to store items and prices
        cookie_upgrades = {}
        for i in range(len(item_prices)):
            cookie_upgrades[item_prices[i]] = item_ids[i]
        
        #Getting current cookies clicked
        money = driver.find_element(By.ID, 'money').text
        if ',' in money:
            money.replace(',','')
        cookie_count = int(money)

        #Finding upgrades I can afford
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id
            
        #Buying most expensive upgrade
        most_expensive_affordable_upgrade = max(affordable_upgrades)
        to_purchase_id = affordable_upgrades[most_expensive_affordable_upgrade]

        driver.find_element(By.ID, to_purchase_id).click()

        #Adding another 5 secs
        timeout = time.time() + 5

    if time.time() > five_min:
        cookies_per_sec = driver.find_element(By.ID, 'cookiesPerSecond').text
        print(cookies_per_sec)
        break



