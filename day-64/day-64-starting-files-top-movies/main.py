from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, IntegerField
from wtforms.validators import DataRequired
import requests
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY')
Bootstrap5(app)

db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
db.init_app(app=app)

TMDB_API_KEY = os.getenv('TMDB_API_KEY')
TMDB_API_TOKEN = os.getenv('TMDB_API_TOKEN')
TMDB_URL_BY_NAME = 'https://api.themoviedb.org/3/search/movie' #This is used for searching by name
TMDB_URL_BY_ID = 'https://api.themoviedb.org/3/movie'
headers = {
    "accept": "application/json",
    'Authorization': f'Bearer {TMDB_API_TOKEN}'}
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(255), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(255), nullable=True)
    img_url = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<Movie {self.title}>'

with app.app_context():
    db.create_all()
class RateMovieForm(FlaskForm):
    rating = FloatField(label='Rating', validators=[DataRequired()])
    review = StringField(label='Review', validators=[DataRequired()])
    ranking = IntegerField(label='Ranking', validators=[DataRequired()])
    submit = SubmitField(label='Done')

class FindMovieForm(FlaskForm):
    movie_title = StringField(label='Movie Title', validators=[DataRequired()])
    submit = SubmitField(label='Add Movie')


@app.route("/")
def home():
    all_movies = db.session.execute(db.select(Movie).order_by(Movie.rating)).scalars().all()

    for i in range(len(all_movies)):
        import ipdb;ipdb.set_trace()
        all_movies[i].ranking = len(all_movies) - i
        db.session.commit()

    return render_template("index.html", movies = all_movies)

@app.route("/add", methods=['GET', 'POST'])
def add():
    # if request.method == 'POST':
    #     new_movie = Movie(title = request.form['title'],
    #         year = request.form['year'],
    #         description = request.form['description'],
    #         rating = request.form['rating'],
    #         ranking = request.form['ranking'],
    #         review = request.form['review'],
    #         img_url = request.form['image'])
    #     db.session.add(new_movie)
    #     db.session.commit()
        # return redirect(url_for('home'))
    form = FindMovieForm()
    if form.validate_on_submit():
        movie_title = request.form['movie_title']
        # response = requests.get(f'{TMDB_URL}?query={movie_title}', headers=headers).json()
        response = requests.get(TMDB_URL_BY_NAME, params={'api_key': TMDB_API_KEY, 'query':movie_title}).json()
        data = response['results']
        return render_template('select.html', options=data)
    return render_template('add.html', form=form)

@app.route('/find')
def find_movie():
    movie_api_id = request.args.get('id')
    if movie_api_id:
        movie_api_url = f'{TMDB_URL_BY_ID}/{movie_api_id}'
        response = requests.get(movie_api_url, params={'api_key':TMDB_API_KEY, 'language':'en-US'})
        data = response.json()
        new_movie = Movie(
            title=data['title'],
            year = data['release_date'].split('-')[0],
            img_url = f"{MOVIE_DB_IMAGE_URL}{data['poster_path']}",
            description = data['overview']
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("edit", id = new_movie.id))


@app.route('/edit', methods=['GET','POST'])
def edit():
    rate_movie_form = RateMovieForm()
    # if request.method == 'POST':
    #     movie_id=request.form['id']
    #     movie_edit = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()
    #     movie_edit.rating = request.form['rating']
    #     movie_edit.review = request.form['review']
    #     db.session.commit()
    #     return redirect(url_for('home'))        
    movie_id = request.args.get('id')
    movie = db.get_or_404(Movie, movie_id)
    # return render_template('edit.html', movie=movie)
    if rate_movie_form.validate_on_submit():
        movie.rating = rate_movie_form.rating.data
        movie.review = rate_movie_form.review.data
        movie.ranking = rate_movie_form.ranking.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', form=rate_movie_form, movie=movie)

@app.route('/delete', methods=['GET','POST'])
def delete():
    movie_id = request.args.get('id')
    movie = db.get_or_404(Movie, movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
