from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html',name='Jarvis')

@app.route('/guest/<name>')
def guest(name):
    guest = name.title()
    params = {'name': name}
    age_response = requests.get('https://api.agify.io?', params=params).json()
    gender_response = requests.get('https://api.genderize.io?', params=params).json()
    age = age_response['age']
    gender = gender_response['gender']
    return render_template('guess.html', name=guest, age=age, gender=gender)

@app.route('/blog')
def get_blog():
    response = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
    blogs = response.json()
    return render_template('blog.html', blogs=blogs)

if __name__ == '__main__':
    app.run(debug=True)

