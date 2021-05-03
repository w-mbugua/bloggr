from flask.app import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email


class BlogPost(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    body = TextAreaField('Post')
    submit = SubmitField('Publish')

class CommentForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    body = TextAreaField('Reply', validators=[DataRequired()])
    submit = SubmitField('Post')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Bio',validators = [DataRequired()])
    submit = SubmitField('Submit')

class SubscriptionForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = email = StringField('Email', validators=[DataRequired(),  Email()])
    submit = SubmitField('Join')