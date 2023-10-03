from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# create the SQLite database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"
# Create the extension
db = SQLAlchemy()
# Initialise the app with the extension
db.init_app(app)

# all_books = []
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

with app.app_context(): #creates a temporary application context.
    db.create_all()


@app.route('/')
def home():
    all_books = db.session.execute(db.select(Book).order_by(Book.title)).scalars().all()
    return render_template('index.html', books=all_books)

@app.route("/add", methods=['GET','POST'])
def add():
    if request.method == "POST":
    #     new_book = {
    #         "title": request.form["title"], # Method 1
    #         "author": request.form.get('author'), # Method 2
    #         "rating": request.form["rating"]
    #     }
    #     all_books.append(new_book)
    #     return redirect(url_for('home'))
    # return render_template('add.html')
        new_book = Book(
            title= request.form["title"], 
            author= request.form.get('author'), 
            rating= request.form["rating"])
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')

@app.route('/edit', methods=['GET', 'POST'])
def edit():
    #Once you submit the requst is sent as a 'POST' 
    if request.method == 'POST':
        book_id = request.form['id']
        edit_book = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
        edit_book.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))
    #This is what is rendered in the first run when request is still not 'POST'
    book_id = request.args.get('id')
    book_selected = db.get_or_404(Book, book_id)
    return render_template("edit.html", book=book_selected)

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    import ipdb;ipdb.set_trace()
    book_id = request.args.get('id')
    # book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    book_selected = db.get_or_404(Book, book_id)
    db.session.delete(book_selected)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

