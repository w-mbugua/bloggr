from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(),  Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    # def validate_email(self,data_field):
    #         if User.query.filter_by(email =data_field.data).first():
    #             raise ValidationError('That email already exists')

    # def validate_username(self,data_field):
    #     if User.query.filter_by(username = data_field.data).first():
    #         raise ValidationError('That username is taken')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),  Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')