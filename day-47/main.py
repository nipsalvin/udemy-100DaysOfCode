import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

url = 'https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6'

headers = { 'Accept-Language' : 'en-US,en;q=0.5',
            'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/112.0'}

response = requests.get(url=url,headers=headers)
response.raise_for_status()
amazon_web_page = response.text

soup = BeautifulSoup(amazon_web_page, 'lxml')
print(soup.get_text())

