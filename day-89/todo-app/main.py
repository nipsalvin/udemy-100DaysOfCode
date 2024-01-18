from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select
from flask_bootstrap import Bootstrap5
from datetime import date
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
Bootstrap5(app)

db = SQLAlchemy()
db.init_app(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    complete = db.Column(db.Boolean)
    date = db.Column(db.String(250), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    tasks = Task.query.all()
    return render_template('index.html',tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    title = request.form.get('title')
    today = date.today().strftime("%B %d, %Y")
    new_task = Task(title=title, complete=False, date=today)
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for("home"))




if __name__ == '__main__':
    app.run(debug=True)