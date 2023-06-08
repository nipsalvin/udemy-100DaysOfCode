import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

OWM_Endpoint = 'https://api.openweathermap.org/data/2.5/weather'
api_key = os.getenv('API_KEY')
account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')

PARAMETERS = {
    'lon':36.825500,
    'lat':-1.167240,
    'appid':api_key,
}

# response = requests.get('https://api.openweathermap.org/data/2.5/onecall', params=PARAMETERS)
response = requests.get(OWM_Endpoint, params=PARAMETERS)
response.raise_for_status()

weather_data = response.json()
weather = weather_data['weather'] #Returns a list of dictionaries
rain = weather_data['weather'][0] #Picks a dictionary from the list
condition_code = weather_data['weather'][0]['id']

will_rain = False

if condition_code < 700:
    will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body="It might Rain Today",
                     from_='+13204349475',
                     to=os.getenv('PHONE_NUMBER')
                 )
    print(message.sid)
print(condition_code)

# print(weather)
# print(weather_data)


