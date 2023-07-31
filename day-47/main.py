import os
import requests
import smtplib
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv('MY_EMAIL')
PASSWORD = os.environ.get('GMAIL_APP_PASSWORD')
EMAIL_2 = os.getenv('MY_EMAIL_2')

url = 'https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6'

# headers = { 'Accept-Language' : 'en-US,en;q=0.5',
#             'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/112.0'}
headers = { 'Accept-Language' : 'en-US,en;q=0.5',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0'}


response = requests.get(url=url,headers=headers)
amazon_web_page = response.text

soup = BeautifulSoup(amazon_web_page, 'lxml')
price = soup.find(class_="a-offscreen").get_text()
price_without_symbol = price.split('$')[1]
price_as_float = float(price_without_symbol)

title = soup.find(id="productTitle").get_text().strip()
BUY_PRICE = 200

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs=EMAIL_2,
                            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8"))
        connection.close()
        




