import smtplib
import requests
import os
from dotenv import load_dotenv

load_dotenv()

MY_EMAIL = os.getenv('MY_EMAIL')
MY_EMAIL_2 = os.getenv('MY_EMAIL_2')
password = os.environ.get('GMAIL_APP_PASSWORD')
OWM_Endpoint = 'https://api.openweathermap.org/data/2.5/weather'
api_key = os.getenv('RAIN_API_KEY')
account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')

PARAMETERS = {
    'lon':36.825500,
    'lat':-1.167240,
    'appid':api_key,
}

response = requests.get(OWM_Endpoint, params=PARAMETERS)
response.raise_for_status()

weather_data = response.json()
weather = weather_data['weather'] #Returns a list of dictionaries
rain = weather_data['weather'][0] #Picks a dictionary from the list
condition_code = weather_data['weather'][0]['id']

will_rain = False

if condition_code < 700:
    will_rain = True

import ipdb;ipdb.set_trace()
if will_rain:
    # with smtplib.SMTP('smtp.gmail.com') as connection:
    #     connection.starttls()
    #     connection.login(user=MY_EMAIL, password=password)
    #     connection.sendmail(from_addr=MY_EMAIL, 
    #                         to_addrs='MY_EMAIL_2' , 
    #                         msg='Subject:RAIN ALERT\n\nIt might Rain Today, Carry an umbrella')
    #     connection.close()
    
    url = "https://whin2.p.rapidapi.com/send"

    payload = { "text": "It might Rain Today, Carry an umbrella" }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": os.getenv('X-RapidAPI-Key_WHATSAPP'),
        "X-RapidAPI-Host": os.getenv('X-RapidAPI-Host_WHATSAPP')
    }

    response = requests.post(url, json=payload, headers=headers)

    # print(response.json())