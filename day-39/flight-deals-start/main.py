import requests
from datetime import datetime
import os
from dotenv import load_dotenv
from data_manager import DataManager

load_dotenv()

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
data = DataManager.data
sheet_data = data['prices'] #This is a list of dictionaries
# print (sheet_data)

for x in sheet_data:
    print (x['iataCode'])
    if x['iataCode'] == None or x['iataCode'] == '':
        x['iataCode'] = 'TESTING'
    print (sheet_data)
