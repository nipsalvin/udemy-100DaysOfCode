from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# create the SQLite database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"
# Create the extension
db = SQLAlchemy()
# Initialise the app with the extension
db.init_app(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'

# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()

# Create table schema in the database. Requires application context.
# with app.app_context():
#     new_book = Book(title= "TGR", author= "Napoleon Hill", rating= 9.3)
#     db.session.add(new_book)
#     db.session.commit()

#Read All Records
with app.app_context():
    # import ipdb;ipdb.set_trace()
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()
    print(all_books.all())

#Read A Particular Record By Query
with app.app_context():
    # import ipdb;ipdb.set_trace()
    book = db.session.execute(db.select(Book).where(Book.title == 'TGR'))
    book = book.scalar()
    print(book)

#Update A Particular Record By Query
# with app.app_context():
#     # import ipdb;ipdb.set_trace()
#     update = db.session.execute(db.select(Book).where(Book.author == 'Naps Hill')).scalar()
#     update.author = 'Napoleon Hill'
#     db.session.commit()

#Update A Particular Record By PRIMARY KEY
with app.app_context():
    # import ipdb;ipdb.set_trace()
    update = db.session.execute(db.select(Book).where(Book.id == 1)).scalar()
    update.author = 'James Clear'
    update.title = 'Atomic Habits'
    db.session.commit()

#Delete a particular Record
with app.app_context():
    deletion = db.session.execute(db.select(Book).where(Book.id == 3)).scalar()
    # or book_to_delete = db.get_or_404(Book, book_id) ## this function gets object by id
    db.session.delete(deletion)
    db.session.commit()

# if __name__ == '__main__':
#     app.run(debug=True)