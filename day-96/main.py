from flask import Flask, render_template
import requests
import os

app = Flask(__name__)

@app.route('/')
def display_joke():
    import ipdb;ipdb.set_trace()
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

    return render_template('index.html', joke=joke)

if __name__ == '__main__':
    app.run(debug=True)