from datetime import date
from flask import Flask, abort, render_template, redirect, url_for, flash, request, current_app, session
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_gravatar import Gravatar
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship
from forms import RegisterForm, LoginForm, AddProductForm #, CommentForm
import os
import smtplib

app = Flask(__name__, static_folder='static')
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY')
app.config['UPLOAD_FOLDER'] = '/home/nips/Projects/udemy-100DaysOfCode/day-97/static/assets/img'
ckeditor = CKEditor(app)
Bootstrap5(app)


# Configure Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, user_id)


# # For adding profile images to the comment section
gravatar = Gravatar(app,
                    size=100,
                    rating='g',
                    default='retro',
                    force_default=False,
                    force_lower=False,
                    use_ssl=False,
                    base_url=None)

# # CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///e_commerce.db"
db = SQLAlchemy()
db.init_app(app)

class Like(db.Model):
    __tablename__ = 'likes'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    perfume_id = db.Column(db.Integer, db.ForeignKey('perfumes.id'))

class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    first_name = db.Column(db.String(100))
    surname = db.Column(db.String(100))
    likes = db.relationship('Like', backref='user', lazy=True)

    def __repr__(self):
        return f"<User: {self.first_name}>"

class Perfume(db.Model):
    __tablename__ = 'perfumes'
    id = db.Column(db.Integer, primary_key=True)
    scent_code = db.Column(db.String(100), nullable=True)
    scent_name = db.Column(db.String(100))
    scent_brand = db.Column(db.String(100))
    scent_gender = db.Column(db.String(10)) 
    grammage = db.Column(db.Integer)
    is_discounted = db.Column(db.Boolean, default=False)
    is_out = db.Column(db.Boolean, default=False)
    image = db.Column(db.String(255), nullable=True)
    original_price = db.Column(db.Integer)
    current_price = db.Column(db.Integer)
    description = db.Column(db.String(100))
    likes = db.relationship('Like', backref='perfume', lazy=True)

    def __repr__(self):
        return f"<Perfume: {self.scent_code} {self.scent_name}>"

    
with app.app_context():
    db.create_all()

# Create an admin-only decorator
def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # If id is not 1 then return abort with 403 error
        if current_user.id != 1:
            return abort(403)
        # Otherwise continue with the route function
        return f(*args, **kwargs)

    return decorated_function

@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():

        # Check if user email is already present in the database.
        result = db.session.execute(db.select(User).where(User.email == form.email.data))
        user = result.scalar()
        if user:
            # User already exists
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('login'))

        hash_and_salted_password = generate_password_hash(
            form.password.data,
            method='pbkdf2:sha256',
            salt_length=8
        )
        new_user = User(
            email=form.email.data,
            first_name=form.first_name.data,
            surname=form.surname.data,
            password=hash_and_salted_password,
        )
        db.session.add(new_user)
        db.session.commit()
        # This line will authenticate the user with Flask-Login
        login_user(new_user)
        return redirect(url_for("home"))
    return render_template("register.html", form=form, current_user=current_user)

@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        password = form.password.data
        result = db.session.execute(db.select(User).where(User.email == form.email.data))
        # Note, email in db is unique so will only have one result.
        user = result.scalar()
        # Email doesn't exist
        if not user:
            flash("That email does not exist, please try again.")
            return redirect(url_for('login'))
        # Password incorrect
        elif not check_password_hash(user.password, password):
            flash('Password incorrect, please try again.')
            return redirect(url_for('login'))
        else:
            login_user(user)
            return redirect(url_for('home'))

    return render_template("login.html", form=form, current_user=current_user)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/like/<int:perfume_id>', methods=["POST"])
def toggle_like_perfume(perfume_id):
    if current_user.is_authenticated:
        like = Like.query.filter_by(user_id=current_user.id, perfume_id=perfume_id).first()
        if like:
            db.session.delete(like)
            db.session.commit()
            flash('Perfume unliked successfully!')
        else:
            like = Like(user_id=current_user.id, perfume_id=perfume_id)
            db.session.add(like)
            db.session.commit()
            flash('Perfume liked successfully!')
    else:
        flash('Please log in to like/unlike perfumes.')
    return redirect(url_for('home'))

def save_image(image):
    if image:
        filename = image.filename
        image_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        image.save(image_path)
        return filename
    else:
        return None

@app.route('/add_product', methods=['GET', 'POST'])
@admin_only
def add_product():
    form = AddProductForm()
    if form.validate_on_submit():
        # Handle file upload and store image filename in the database
        image_filename = None
        if form.image.data:
            image_filename = save_image(form.image.data)  # Function to save image file and return filename
        # Create a new Perfume object
        new_perfume = Perfume(
            scent_code=form.scent_code.data,
            scent_name=form.scent_name.data,
            scent_brand=form.scent_brand.data,
            scent_gender=form.scent_gender.data,
            grammage=form.grammage.data,
            is_discounted=form.is_discounted.data,
            original_price=form.price.data,
            current_price=form.price.data,
            description=form.description.data,
            image=image_filename  # Store the image filename in the Perfume object
        )
        # Add the new Perfume object to the database
        db.session.add(new_perfume)
        db.session.commit()
        flash(f'{new_perfume.scent_name} added successfully!', 'success')
        return redirect(url_for('home'))
    return render_template('add_product.html', form=form, current_user=current_user)

@app.route('/product/<int:perfume_id>', methods=['GET','POST'])
def view_perfume(perfume_id):
    requested_perfume = db.get_or_404(Perfume, perfume_id)
    return render_template('details.html', product=requested_perfume, current_user=current_user)

@app.route('/products')
def get_all_products():
    result = db.session.execute(db.select(Perfume))
    products = result.scalars().all()
    return render_template('products.html', products=products, current_user=current_user)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    import ipdb;ipdb.set_trace()
    if 'cart' not in session:
        session['cart'] = []

    cart = session['cart']
    
    # Assuming each product is represented as a dictionary in the cart
    if product_id not in [item['id'] for item in cart]:
        cart.append({'id': product_id, 'quantity': 1})
        session['cart'] = cart  # Make sure to reassign the session['cart'] to update it
        flash('Product added to cart successfully!', 'success')
    else:
        flash('Product already in cart', 'info')
    return redirect(url_for('get_all_products'))

@app.route('/cart')
def view_cart():
    import ipdb;ipdb.set_trace()
    cart_items = session.get('cart', [])
    products = []  # This will store product details fetched based on cart item IDs
    
    for item in cart_items:
        import ipdb;ipdb.set_trace()
        product = db.get_or_404(Perfume, item['id'])  # You need to implement this function
        if product:
            product['quantity'] = item['quantity']
            products.append(product)
    
    return render_template('cart.html', cart_items=products)

if __name__ == "__main__":
    app.run(debug=True)
