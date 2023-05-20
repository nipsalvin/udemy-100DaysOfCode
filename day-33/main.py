import requests
import datetime

#requets.get(endpoint.url), returns response code
response = requests.get('http://api.open-notify.org/iss-now.json')
# print(response)
response.raise_for_status()

#get data in json format. You can get value from a key
data = response.json()
# print(data)

iss_longitude = data['iss_position']['longitude']
iss_latitude = data['iss_position']['latitude']

iss_position = (f'latitude:{iss_latitude}\nlongitude:{iss_longitude}')
print(iss_position)

LATITUDE = -1.249970
LONGITUDE = 36.685459

parameters = {
    'lat':LATITUDE,
    'lng':LONGITUDE,
    'formatted':0
}
response_2 = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
response_2.raise_for_status()
data_2 = response_2.json()

sunrise_data = data_2['results']['sunrise']
sunset_data = data_2['results']['sunset']

#.split('T') - splits at 'T'
# [1].split(':') - get item at index 1 and splits at ':'
#[0] picks itema t index [0]
sunrise = int(sunrise_data.split('T')[1].split(':')[0])
sunset = int(sunset_data.split('T')[1].split(':')[0])

print(sunrise, sunset)


