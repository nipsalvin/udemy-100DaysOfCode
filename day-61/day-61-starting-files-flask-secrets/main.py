from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo
import os    


app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY')

class LoginForm(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired()])
    email = StringField(label='Email', validators=[Email(message='This is not a valid Email')])
    password = PasswordField(label='Password', validators=[Length(min=8, max=20, message='This must be more than 8 characters'),
                                                           EqualTo(fieldname='confirm_password', message='Passwords must match')])
    confirm_password = PasswordField(label='confirm password')
    submit = SubmitField(label='Log in')


@app.route("/")
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        print('email is:', login_form.email.data)
        print('password is:', login_form.password.data)
        if login_form.email.data == 'admin@email.com' and login_form.password.data == '12345678':
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=login_form)

if __name__ == '__main__':
    app.run(debug=True)
