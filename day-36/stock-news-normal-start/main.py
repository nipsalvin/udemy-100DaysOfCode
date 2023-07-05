from datetime import datetime, timedelta
import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')

alpha_vantage_parameters = {
    'function' : 'TIME_SERIES_DAILY_ADJUSTED',
    'symbol': STOCK_NAME,
    'apikey': os.getenv('ALPHAVANTAGE_API_KEY'),
}
    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

price_response  = requests.get(STOCK_ENDPOINT, params=alpha_vantage_parameters)
price_response.raise_for_status()
price_data = price_response.json()

closing_prices = [value for (key, value) in price_data.items()]

#TODO 2. - Get the day before yesterday's closing stock price

yesterday = datetime.now().date() - timedelta(days=1)
day_before_yesterday = yesterday - timedelta(days=1)
yesterday_close = closing_prices[1][yesterday.strftime('%Y-%m-%d')]['4. close']
day_before_yesterday_close = closing_prices[1][day_before_yesterday.strftime('%Y-%m-%d')]['4. close']

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

difference = float(day_before_yesterday_close) - float(yesterday_close)

up_down = None
if difference > 0:
    up_down = '🔺'
else:
    up_down = '🔻'

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

percentage_change = round((difference / float(day_before_yesterday_close)) * 100,2)

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

if abs(percentage_change) > 1:

    #TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
   
    news_parameters = {
        'qInTitle': COMPANY_NAME,
        'apiKey': os.getenv('NEWS_API_KEY'),
        'language': 'en',
        'pageSize': 3,
        'from': day_before_yesterday,
        'to': yesterday,
        'sortBy': 'publishedAt',
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    news_response.raise_for_status()
    news_list = news_response.json()['articles']

    #TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

        ## STEP 3: Use twilio.com/docs/sms/quickstart/python
        #to send a separate message with each article's title and description to your phone number. 

    #TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

    news_data = [f"Stock: {STOCK_NAME}:{up_down}{percentage_change}% \n Headline: {article['title']}. \n Brief: {article['description']}" for article in news_list]
    
    client = Client(account_sid, auth_token)
    for article in news_data:
        message = client.messages.create(
                        body=article,
                        from_=os.getenv('TWILIO_VIRTUAL_NUMBER'),
                        to=os.getenv('PHONE_NUMBER')
                    )
        print(message.sid)
        print(article)
    

    #TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

