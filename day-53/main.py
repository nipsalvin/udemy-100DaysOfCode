import os
import requests
from time import sleep
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By

load_dotenv()

GOOGLE_FORM = 'https://forms.gle/ZWVD5R6sts1mTWid8'
headers = {'Accept-Language' : 'en-US,en;q=0.5',
           'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0',
           'Cookie':'PHPSESSID=c87572959c2de67070f1515f95bf91d5'}


#TODO 1: Use BeautifulSoup/Requests to scrape all the listings from the Zillow web address
response = requests.get('https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState={"pagination"%3A{}%2C"usersSearchTerm"%3Anull%2C"mapBounds"%3A{"west"%3A-122.56276167822266%2C"east"%3A-122.30389632177734%2C"south"%3A37.69261345230467%2C"north"%3A37.857877098316834}%2C"isMapVisible"%3Atrue%2C"filterState"%3A{"fr"%3A{"value"%3Atrue}%2C"fsba"%3A{"value"%3Afalse}%2C"fsbo"%3A{"value"%3Afalse}%2C"nc"%3A{"value"%3Afalse}%2C"cmsn"%3A{"value"%3Afalse}%2C"auc"%3A{"value"%3Afalse}%2C"fore"%3A{"value"%3Afalse}%2C"pmf"%3A{"value"%3Afalse}%2C"pf"%3A{"value"%3Afalse}%2C"mp"%3A{"max"%3A3000}%2C"price"%3A{"max"%3A872627}%2C"beds"%3A{"min"%3A1}}%2C"isListVisible"%3Atrue%2C"mapZoom"%3A12}', headers=headers)

zillow_web_page = response.text
soup = BeautifulSoup(zillow_web_page, 'html.parser')

#TODO 2: Create a list of links for all the listings scraped
all_address_elements = soup.select(".property-card-data a")

property_links = []
for link in all_address_elements:
    property_link = link.get("href")
    if "http" in property_link :
        property_links.append(property_link)
    else:
        property_links.append(f"https://www.zillow.com{property_link}")

#TODO 3: Create a list of prices for all the listings scraped
property_price_elements = soup.select(".photo-cards li span")

property_prices = []
for price in property_price_elements:
    property_price = price.getText()
    # Select only first span element which is the price
    if "$" in property_price:
        # If price string has string "/mo"
        if "/" in property_price:
            property_price = property_price.split("/")[0] #Splits into 2 items then gets [0]
            property_prices.append(property_price)
        # If price string has number of bedrooms
        if "+" in property_price:
            property_price = property_price.split("+")[0] #Splits into 2 items then gets [0]
            property_prices.append(property_price)

#TODO 4: Create a list of addresses for all the listings scraped
property_address_elements = soup.select(".property-card-data address")

property_addresses = []
for address in property_address_elements:
    property_address = address.getText()
    # If address is delineated from name by the "|" separator
    if "|" in property_address:
        property_address = property_address.split("|")[-1].strip()
    # If address is delineated from name by the "," separator
    else:
        property_address = property_address.split(", ", 1)[-1].strip()
    property_addresses.append(property_address)
    
#TODO 5: Use Selenium to fill in the form you created.
driver = webdriver.Firefox()
driver.maximize_window()

for address, price, link in zip(property_addresses, property_prices, property_links):
    # Go to Google form
    driver.get(GOOGLE_FORM)
    sleep(10)
    # Find input fields for address, price, and link
    address_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    # Fill in form fields
    address_input.send_keys(address)
    sleep(2)
    price_input.send_keys(price)
    sleep(2)
    link_input.send_keys(link)
    sleep(2)
    
    # Submit the form
    submit_button = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit_button.click()
    sleep(1)
    
# driver.quit()







