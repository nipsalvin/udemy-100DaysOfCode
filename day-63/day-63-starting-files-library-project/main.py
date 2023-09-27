from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

all_books = []


@app.route('/')
def home():
    has_books = False if all_books==[] else True
    return render_template('index.html', books=all_books, has_books=has_books)


@app.route("/add", methods=['GET','POST'])
def add():
    if request.method == "POST":
        new_book = {
            "title": request.form["title"], # Method 1
            "author": request.form.get('author'), # Method 2
            "rating": request.form["rating"]
        }
        all_books.append(new_book)
        return redirect(url_for('home'))
    return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=True)

