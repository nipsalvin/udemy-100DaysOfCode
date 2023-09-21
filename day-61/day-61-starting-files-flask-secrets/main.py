from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
import os    


app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY')

class LoginForm(FlaskForm):
    name = StringField('Name')
    email = StringField('Email')
    password = PasswordField('Password')


@app.route("/")
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    return render_template('login.html', form=login_form)

if __name__ == '__main__':
    app.run(debug=True)
