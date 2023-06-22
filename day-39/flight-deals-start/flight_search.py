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
        code = 'TESTING'
        return code