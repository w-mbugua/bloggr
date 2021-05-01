from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from ..models import Writer

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(),  Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_email(self, data_field):
        if Writer.query.filter_by(email = data_field.data).first():
            raise ValidationError('There is an account with that email')

    def validate_username(self, data_field):
        if Writer.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is already taken')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),  Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')