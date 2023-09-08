from flask import Flask, render_template
from random import randint
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    random_number = randint(1 ,10)
    year = datetime.today().year
    return render_template('index.html', num = random_number, year = year)

if __name__ == '__main__':
    app.run(debug=True)