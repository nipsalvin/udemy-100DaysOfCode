import requests
from datetime import datetime
import os
from dotenv import load_dotenv
from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint

load_dotenv()

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
data_manager = DataManager()
sheet_data = data_manager.get_destination_data() #This gets the list of dictionaries
# print (sheet_data)

#Check if IATA Code is empty
if sheet_data[0]['iataCode'] == '':
    flight_search = FlightSearch()
    for row in sheet_data:
        row['iataCode'] = flight_search.get_destication_code(row['city'])
    pprint(f'sheet data:\n{sheet_data}')
    
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()
