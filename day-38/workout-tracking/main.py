import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

APP_ID = os.getenv('NUTRITIONIX_APP_ID')
APP_KEY = os.getenv('NUTRITIONIX_APP_KEY')
SHEETY_APP_TOKEN = os.getenv('SHEETY_APP_TOKEN')

GENDER = 'male'
WEIGHT_KG = 75
HEIGHT_CM = 170
AGE = 28

nutrition_ix_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
# sheety_endpoint = 'https://api.sheety.co/9b55e9385f1db6dd5d944a0c111b8326/myWorkouts/workouts'
sheety_endpoint = 'https://api.sheety.co/9b55e9385f1db6dd5d944a0c111b8326/myWorkouts/workouts'

exercise_text = input('What exercise did you do ?')

nutrition_ix_headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

parameters = {
    "query":exercise_text,
    "gender":GENDER,
    "weight_kg":WEIGHT_KG,
    "height_cm":HEIGHT_CM,
    "age":AGE
}

response = requests.post(nutrition_ix_endpoint, headers=nutrition_ix_headers, json=parameters)
result = response.json()
print(result)
# print(response.text)


sheety_headers = {
    'Authorization': f'Bearer {SHEETY_APP_TOKEN}',
    'Content-Type': 'application/json',
}

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
for exercise in result["exercises"]:
    sheety_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheety_response = requests.post(sheety_endpoint, json=sheety_inputs, headers=sheety_headers)
    # sheety_response = requests.post(sheety_endpoint, json=sheety_inputs)

    print(sheety_response.text)