from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select
from flask_bootstrap import Bootstrap5
import random
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY')
Bootstrap5(app)
API_KEY = os.getenv('POSTMAN_CAFE_API_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)

class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        dictionary = {column.name: getattr(self, column.name) for column in self.__table__.columns}
        return dictionary

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    all_cafes = Cafe.query.all()
    return render_template('index.html')

@app.route('/random', methods=['GET'])
def get_random_cafe():
    # # Method 1
    # result = db.session.execute(db.select(Cafe))
    # all_cafes = result.scalars().all()
    # Method 2
    all_cafes = Cafe.query.all()
    random_cafe = random.choice(all_cafes)
    return jsonify(cafe=random_cafe.to_dict())

@app.route('/all')
def all_cafes():
    # # Method 1
    # all_cafes = db.session.execute(db.select(Cafe)).scalars().all()
    # Method 2
    all_cafes = Cafe.query.all()
    cafes = [cafe.to_dict() for cafe in all_cafes]
    return render_template('cafes.html', cafes=cafes)


if __name__ == '__main__':
    app.run(debug=True)