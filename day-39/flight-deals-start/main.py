import requests
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint
from notification_manager import NotificationManager

load_dotenv()

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
data_manager = DataManager()
sheet_data = data_manager.get_destination_data() #This gets the list of dictionaries (City DATA)
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "LON"

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

#Check if IATA Code is empty
if sheet_data[0]['iataCode'] == '':
    for row in sheet_data:
        row['iataCode'] = flight_search.get_destication_code(row['city'])
        
    # pprint(f'sheet data:\n{sheet_data}')    
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    if flight is None:
        continue

    # if flight.price < destination['lowestPrice']:
    #     import ipdb;ipdb.set_trace()
    #     MESSAGE=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
    #     # notification_manager.send_sms(
    #     #     message=MESSAGE
    #     # )
    #     print(MESSAGE)
    #     if flight.stop_overs > 0:
    #         import ipdb;ipdb.set_trace()
    #         MESSAGE += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."
    #         print(MESSAGE)
    
    if flight.price < destination['lowestPrice']:
        MESSAGE=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        new_message = MESSAGE.replace("£", "\u00A3")
        notification_manager.send_email(
            message=new_message
        )
        print(MESSAGE)
        if flight.stop_overs > 0:
            new_message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."
            print(new_message)




        
        
