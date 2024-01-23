import requests
import os

url = "https://voicerss-text-to-speech.p.rapidapi.com/"

querystring = {"key":"hello"}

payload = {
	"src": "Hello, world!",
	"hl": "en-us",
	"r": "0",
	"c": "mp3",
	"f": "8khz_8bit_mono"
}
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": os.getenv('X_RapidAPI_Key'),
	"X-RapidAPI-Host": "voicerss-text-to-speech.p.rapidapi.com"
}

response = requests.post(url, data=payload, headers=headers, params=querystring)

print(response.json())