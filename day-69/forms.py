from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, Email, Length, EqualTo
from flask_ckeditor import CKEditorField


# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


# TODO: Create a RegisterForm to register new users
class RegisterForm(FlaskForm):
    name = StringField(label='Name', name='name', validators=[DataRequired()])
    email = StringField(label='Email', validators=[Email(message='This is not a valid Email')])
    password = PasswordField(label='Password', validators=[Length(min=5, max=20, message='This must be more than 8 characters')])
    submit = SubmitField("Sign Me Up!")

# TODO: Create a LoginForm to login existing users
class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[Email(message='This is not a valid Email')])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label="Let Me In")

# TODO: Create a CommentForm so users can leave comments below posts
class CommentForm(FlaskForm):
    comment = CKEditorField(label= "Comment", validators=[DataRequired()])
    submit = SubmitField(label="Submit Comment")