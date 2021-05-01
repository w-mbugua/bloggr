from flask.app import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class BlogPost(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    body = TextAreaField('Post')
    submit = SubmitField('Publish')

class CommentForm(FlaskForm):
    username = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Reply', validators=[DataRequired()])
    submit = SubmitField('Post')