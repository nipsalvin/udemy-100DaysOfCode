from flask import Flask, render_template
import requests
import os

app = Flask(__name__)

@app.route('/')
def display_joke():
    api_key = os.getenv('X-RapidAPI-Key')
    api_host = os.getenv('X-RapidAPI-Host')

    url = "https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes/random"

    headers = {
        "accept": "application/json",
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": api_host,
    }

    response = requests.get(url, headers=headers).json()

    joke = response.get('value')
    icon = response.get('icon_url')

    return render_template('index.html', icon=icon, joke=joke)

if __name__ == '__main__':
    app.run(debug=True)