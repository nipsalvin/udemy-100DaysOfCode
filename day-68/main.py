from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY')

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy()
db.init_app(app)

# LOGGIN IN
login_manager = LoginManager()
login_manager.init_app(app)


# CREATE A user_loader CALL BACK
@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)

# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
 
 
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        user = db.session.execute(db.select(User).where(User.email == email)).scalar()

        hashed_password = generate_password_hash(
            password=request.form.get('password'), 
            method='pbkdf2:sha256', 
            salt_length=8)
        
        if user:
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('login'))
        else:
            new_user = User(
                name = request.form.get('name'),
                email = request.form.get('email'),
                password = hashed_password,
            )
            db.session.add(new_user)
            db.session.commit()

            # Log in and authenticate user after adding details to database.
            login_user(new_user)

            return render_template("secrets.html", user=new_user)
    return render_template("register.html")


@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        inputted_pass = request.form.get('password')
        user = db.session.execute(db.select(User).where(User.email == email)).scalar()
        if check_password_hash(user.password, inputted_pass):
            # Log in and authenticate user
            login_user(user=user)
            return redirect(url_for('secrets'))
        else:
            flash('Invalid Email or Password')
        return redirect(url_for('login'))
    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    user = current_user
    return render_template("secrets.html", user = user)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory(directory='static', path='files/cheat_sheet.pdf')


if __name__ == "__main__":
    app.run(debug=True)
