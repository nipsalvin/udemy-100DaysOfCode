from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY')
Bootstrap5(app)

db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
db.init_app(app=app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(255), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(255), nullable=False)
    img_url = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<Movie {self.title}>'

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    all_movies = db.session.execute(db.select(Movie).order_by(Movie.ranking)).scalars().all()
    return render_template("index.html", movies = all_movies)

@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        new_movie = Movie(
            title = request.form['title'],
            year = request.form['year'],
            description = request.form['description'],
            rating = request.form['rating'],
            ranking = request.form['ranking'],
            review = request.form['review'],
            img_url = request.form['image']
        )
        with app.app_context():
            db.session.add(new_movie)
            db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')

@app.route('/edit', methods=['GET','POST'])
def edit():
    # import ipdb;ipdb.set_trace()
    if request.method == 'POST':
        movie_id=request.form['id']
        movie_edit = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()
        movie_edit.rating = request.form['rating']
        movie_edit.review = request.form['review']
        db.session.commit()
        return redirect(url_for('home'))        
    movie_id = request.args.get('id')
    movie = db.get_or_404(Movie, movie_id)
    return render_template('edit.html', movie=movie)

if __name__ == '__main__':
    app.run(debug=True)
