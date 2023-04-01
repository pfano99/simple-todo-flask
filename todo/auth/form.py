from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email, EqualTo, Optional
from wtforms import StringField, SubmitField, PasswordField


class LoginForm(FlaskForm):
    email = StringField('Your email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class SignUpForm(FlaskForm):
    first_name = StringField('First name', validators=[DataRequired()])
    last_name = StringField('Last name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[Optional()])
    confirm_password = PasswordField('Confirm password', validators=[Optional(), EqualTo('password')])
    submit = SubmitField('Login')
