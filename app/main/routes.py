from . import main
from flask import render_template
from flask_login import login_required
from .forms import BlogPost


@main.route('/')
def index():
    return render_template('index.html', title = 'Home Page')

@main.route('/blog/new', methods = ['GET', 'POST'])
@login_required
def new_blog():
    # a form to create a blog post
    form = BlogPost()
    
    # flash a message
    # redirect to home
    return render_template('new_blog.html', form = form)
