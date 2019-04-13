from flask_wtf import Form
from wtforms import TextField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(Form):
    username = TextField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign in')
