from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, PasswordField, SubmitField, validators


class RegistrationForm(FlaskForm):
    username = StringField('Username', 
                [validators.DataRequired(), validators.Length(min=2, max=20)])
    email = StringField('Email', 
                [validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', [
                validators.DataRequired(),
                validators.EqualTo('confirm_password', message='Passwords must match')])
    confirm_password = PasswordField('Confirm Password')
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email', 
                [validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', [validators.DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')