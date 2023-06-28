import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = os.getenv('TEQUILA_API_KEY')
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def get_destication_code(self, city_name):
        location_endpoint = f'{TEQUILA_ENDPOINT}/locations/query'
        headers = {'apikey':TEQUILA_API_KEY}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code
    
    