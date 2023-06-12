import requests
import os
from dotenv import load_dotenv

load_dotenv()

APP_ID = os.getenv('NUTRITIONIX_APP_ID')
APP_KEY = os.getenv('NUTRITIONIX_APP_KEY')

GENDER = 'male'
WEIGHT_KG = 75
HEIGHT_CM = 170
AGE = 28

nutrition_ix_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

exercise_text = input('What exercise did you do ?')

headers = {
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

response = requests.post(nutrition_ix_endpoint, headers=headers, json=parameters)
result = response.json()
print(result)
print(response.text)