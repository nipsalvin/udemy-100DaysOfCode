import requests

OWM_Endpoint = 'https://api.openweathermap.org/data/2.5/weather'
api_key = '70095d9961c79543025ff269663e4e87'
PARAMETERS = {
    'lon':-4.008256,
    'lat':5.359952,
    'appid':api_key,
}

# response = requests.get('https://api.openweathermap.org/data/2.5/onecall', params=PARAMETERS)
response = requests.get(OWM_Endpoint, params=PARAMETERS)
response.raise_for_status()

data = response.json()
weather = data['weather']
rain = data['rain']
# phonetic_dict ={row.letter:row.code for (index, row) in data.iterrows()}
data_dict = {x:y for (x, y) in rain}
print(data_dict)
print(weather)


