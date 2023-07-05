import requests
from datetime import datetime
import os
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

SHEETY_APP_TOKEN = os.getenv('SHEETY_APP_TOKEN')
SHEETY_ENDPOINT = 'https://api.sheety.co/9b55e9385f1db6dd5d944a0c111b8326/flightDeals/prices'
SHEET_USERS_ENDPOINT = 'https://api.sheety.co/9b55e9385f1db6dd5d944a0c111b8326/flightDeals/users'

sheety_headers = {
    'Authorization': f'Bearer {SHEETY_APP_TOKEN}',
    'Content-Type': 'application/json',
}
class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        '''Returns a list of destination prices'''
        get_response = requests.get(url=SHEETY_ENDPOINT, headers=sheety_headers)
        data = get_response.json()
        self.destination_data = data['prices'] #self.destination_data the list
        # pprint(self.destination_data)
        return self.destination_data
    
    def update_destination_codes(self):
        '''Updates the IATA code'''
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=sheety_headers
            )
            print(response.text)
        
    def get_customer_emails(self):
        response = requests.get(url = SHEET_USERS_ENDPOINT, headers=sheety_headers)
        data = response.json()
        print(data)
        self.customer_data = data["users"]
        return self.customer_data