from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from flask_wtf.file import FileAllowed, FileField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField

# Create a form to register new users
class RegisterForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired()])
    surname = StringField("Surname", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Sign Me Up!")


# Create a form to login existing users
class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Let Me In!")

class AddProductForm(FlaskForm):
    scent_code = StringField(label='Scent Code', validators=[DataRequired()])
    scent_name = StringField(label='Scent Name', validators=[DataRequired()])
    scent_brand = StringField(label='Brand', validators=[DataRequired()])
    scent_gender = StringField(label='Gender', validators=[DataRequired()])
    grammage = StringField(label='Grammage', validators=[DataRequired()])
    is_discounted = BooleanField(label='Is Discounted', default=False)
    image = FileField('Image', validators=[FileAllowed(['jpg', 'png'], 'Images only!')])
    submin = SubmitField('Submit Product')
