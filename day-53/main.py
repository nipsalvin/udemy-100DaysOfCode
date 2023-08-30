import os
import requests
from time import sleep
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException

load_dotenv()

GOOGLE_FORM = 'https://forms.gle/ZWVD5R6sts1mTWid8'
headers = {'Accept-Language' : 'en-US,en;q=0.5',
           'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0',
           'Cookie':'PHPSESSID=c87572959c2de67070f1515f95bf91d5'}


response = requests.get('https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState={"pagination"%3A{}%2C"usersSearchTerm"%3Anull%2C"mapBounds"%3A{"west"%3A-122.56276167822266%2C"east"%3A-122.30389632177734%2C"south"%3A37.69261345230467%2C"north"%3A37.857877098316834}%2C"isMapVisible"%3Atrue%2C"filterState"%3A{"fr"%3A{"value"%3Atrue}%2C"fsba"%3A{"value"%3Afalse}%2C"fsbo"%3A{"value"%3Afalse}%2C"nc"%3A{"value"%3Afalse}%2C"cmsn"%3A{"value"%3Afalse}%2C"auc"%3A{"value"%3Afalse}%2C"fore"%3A{"value"%3Afalse}%2C"pmf"%3A{"value"%3Afalse}%2C"pf"%3A{"value"%3Afalse}%2C"mp"%3A{"max"%3A3000}%2C"price"%3A{"max"%3A872627}%2C"beds"%3A{"min"%3A1}}%2C"isListVisible"%3Atrue%2C"mapZoom"%3A12}', headers=headers)

zillow_web_page = response.text
soup = BeautifulSoup(zillow_web_page, 'html.parser')

all_address_elements = soup.select('.search-page-container ul li article a')

 