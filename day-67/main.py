from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY')
Bootstrap5(app)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy()
db.init_app(app)
ckeditor = CKEditor(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

class CreatePostForm(FlaskForm):
    title = StringField(label='Blog Title', validators=[DataRequired()])
    subtitle = StringField(label='Subitle', validators=[DataRequired()]) 
    author = StringField(label='Author', validators=[DataRequired()])
    img_url = StringField(label='Image Link', validators=[DataRequired()])
    body = CKEditorField(label='Body', validators=[DataRequired()])
    submit = SubmitField(label='Submit')

with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    # TODO: Query the database for all the posts. Convert the data to a python list.
    posts = []
    all_post = db.session.execute(db.select(BlogPost)).scalars().all()
    for post in all_post:
        posts.append(post)
    return render_template("index.html", all_posts=posts)

# TODO: Add a route so that you can click on individual posts.
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # TODO: Retrieve a BlogPost from the database based on the post_id
    # requested_post = None
    # all_post = db.session.execute(db.select(BlogPost)).scalars().all()
    # for blog_post in all_post:
    #     if blog_post.id == post_id:
    #         requested_post = blog_post
    # requested_post = db.get_or_404(BlogPost, post_id) #Method 2
    requested_post = db.session.get(BlogPost, post_id) #Method 3
    return render_template("post.html", post=requested_post)


# TODO: add_new_post() to create a new blog post
@app.route('/new-post', methods=['GET', 'POST'])
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        title = request.form.get('title') #Method 1
        subtitle = form.subtitle.data #Method 2
        author = request.form.get('author')
        img_url = form.img_url.data
        body = request.form.get('body')
        
        new_post = BlogPost(
            title = title,
            subtitle = subtitle,
            author = author,
            img_url = img_url,
            body=body,
            date=date.today().strftime("%B %d, %Y")
        )
        with app.app_context(): #creates a temporary application context.
            db.session.add(new_post)
            db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template('make-post.html', form = form)

# TODO: edit_post() to change an existing blog post
@app.route('/edit-post/<post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    post = db.session.get(BlogPost, post_id)
    edit_form = CreatePostForm(    
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body)
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = edit_form.author.data
        post.body = edit_form.body.data    
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    return render_template('make-post.html', post=post, form=edit_form)

# TODO: delete_post() to remove a blog post from the database
@app.route('/delete/<post_id>')
def delete_post(post_id):
    post = db.session.get(BlogPost, post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('get_all_posts'))

# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
