import requests
import os
from dotenv import load_dotenv

load_dotenv()

SHEETY_APP_TOKEN = os.getenv('SHEETY_APP_TOKEN')
SHEETY_ENDPOINT = 'https://api.sheety.co/9b55e9385f1db6dd5d944a0c111b8326/'

PROJECT = 'flightDeals'
SHEET = 'users'

def post_new_row(first_name, last_name, email):
    sheety_headers = {
        'Authorization': f'Bearer {SHEETY_APP_TOKEN}',
        'Content-Type': 'application/json',
        }

    body = {
        "user": {
            "firstName": first_name,
            "lastName": last_name,
            "email": email,
        }
    }

    response = requests.post(
        url=f'{SHEETY_ENDPOINT}/{PROJECT}/{SHEET}', 
        headers=sheety_headers, 
        json=body
        )
    response.raise_for_status()
    print(response.text)
