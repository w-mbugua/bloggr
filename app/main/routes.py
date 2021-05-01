from . import main
from flask import render_template, flash, redirect, url_for
from flask_login import login_required
from .forms import BlogPost
from .. import db
from ..models import Blog


@main.route('/')
def index():
    blogposts = Blog.query.all()
    return render_template('index.html', title = 'Home Page', posts = blogposts)

@main.route('/blog/new', methods = ['GET', 'POST'])
@login_required
def new_blog():
    # a form to create a blog post
    form = BlogPost()
    if form.validate_on_submit():
        blog = Blog(title = form.title.data, post = form.body.data)
        db.session.add(blog)
        db.session.commit()
        flash('Your blog has been posted!', 'success')
        return redirect(url_for('main.index'))
    flash("Check your input!", 'warning')
    return render_template('new_blog.html', form = form)
