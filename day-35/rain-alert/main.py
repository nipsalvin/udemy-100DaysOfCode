import requests

OWM_Endpoint = 'https://api.openweathermap.org/data/2.5/weather'
api_key = ''
PARAMETERS = {
    'lon':-4.008256,
    'lat':5.359952,
    'appid':api_key,
}

# response = requests.get('https://api.openweathermap.org/data/2.5/onecall', params=PARAMETERS)
response = requests.get(OWM_Endpoint, params=PARAMETERS)
response.raise_for_status()

weather_data = response.json()
weather = weather_data['weather'] #Returns a list of dictionaries
rain = weather_data['weather'][0] #Picks a dictionary from the list
condition_code = weather_data['weather'][0]['id']

if condition_code < 700:
    print('Bring an umbrella')


# print(condition_code)
# # print(weather)
# print(weather_data)


