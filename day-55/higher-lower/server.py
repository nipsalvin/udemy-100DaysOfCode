from flask import Flask
import random

app = Flask(__name__)
number = random.randint(0, 9)

@app.route('/')
def home():
    return '<h1  style="text-align:center">Guess a number between 0 and 9</h1>'\
    '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" style="text-align:center">'

@app.route('/<int:guess>')
def query(guess):
    if guess > number:
        return '<h1  style="text-align:center" color="red">Too high, try again!</h1>'\
        '<img src="https://media.giphy.com/media/UFRtykmfyBA8F7qPh9/giphy.gif" style="text-align:center">'
    elif guess < number:
        return '<h1  style="text-align:center" color="red">Too low, try again!</h1>'\
        '<img src="https://media.giphy.com/media/rS2uLYRGkGWySNX69v/giphy.gif" style="text-align:center">'
    else:
        return '<h1  style="text-align:center" color="green">You found me!</h1>'\
        '<img src="https://media.giphy.com/media/kyLYXonQYYfwYDIeZl/giphy.gif" style="text-align:center">'


if __name__ == '__main__':
    app.run(debug=True)