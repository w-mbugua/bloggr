from flask.app import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class BlogPost(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    body = TextAreaField('Post')
    submit = SubmitField('Publish')