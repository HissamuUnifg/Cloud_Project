from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email


class RegisterForm(FlaskForm):
    email = StringField('Username', validators=[DataRequired(), Email("This field requires a valid email address")])
    username = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Go!')
