from . import main
from flask import render_template
from flask_login import login_required


@main.route('/')
def index():
    return render_template('index.html', title = 'Home Page')

@main.route('/blog/new', methods = ['POST'])
@login_required
def new_blog():
    # a for to create a blog post
    # flash a message
    # redirect to home
    return render_template('new_blog.html')
