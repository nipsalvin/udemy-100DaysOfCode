import requests
from datetime import datetime
import os
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

SHEETY_APP_TOKEN = os.getenv('SHEETY_APP_TOKEN')
SHEETY_ENDPOINT = 'https://api.sheety.co/9b55e9385f1db6dd5d944a0c111b8326/flightDeals/prices'

sheety_headers = {
    'Authorization': f'Bearer {SHEETY_APP_TOKEN}',
    'Content-Type': 'application/json',
}
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    get_response = requests.get(url=SHEETY_ENDPOINT, headers=sheety_headers)
    data = get_response.json()
    # pprint(data)

    post_response = requests.put(url=f'{SHEETY_ENDPOINT}/3', headers=sheety_headers)
    # post_response.raise_for_status()
    print(post_response.status_code)
    sheety_inputs = {
        'prices':{

        }
    }

    # for exercise in result["exercises"]:
    # sheety_inputs = {
    #     "workout": {
    #         "date": today_date,
    #         "time": now_time,
    #         "exercise": exercise["name"].title(),
    #         "duration": exercise["duration_min"],
    #         "calories": exercise["nf_calories"]
    #     }
    # }
    # sheety_response = requests.post(sheety_endpoint, json=sheety_inputs, headers=sheety_headers)

# x = DataManager
