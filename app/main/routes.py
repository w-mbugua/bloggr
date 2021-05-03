from . import main
from flask import render_template, flash, redirect, request, url_for, abort
from flask_login import login_required, current_user
from .forms import BlogPost, CommentForm, UpdateProfile, SubscriptionForm
from .. import db
from ..models import Blog, Comment, Writer, Subscription
import urllib.request, json


@main.route('/')
def index():
    blogposts = Blog.query.order_by(Blog.date_posted.desc()).all()
    quote = random_quote()
    return render_template('index.html', title = 'Home Page', posts = blogposts, quote = quote)

@main.route('/blog/new', methods = ['GET', 'POST'])
@login_required
def new_blog():
    # a form to create a blog post
    form = BlogPost()
    if form.validate_on_submit():
        blog = Blog(title = form.title.data, post = form.body.data, writer = current_user)
        db.session.add(blog)
        db.session.commit()
        flash('Your blog has been posted!', 'success')
        return redirect(url_for('main.index'))
    flash("Check your input!", 'warning')
    return render_template('new_blog.html', form = form)

@main.route('/blog/<int:id>')
def read_blog(id):
    blog = Blog.query.get_or_404(id)
    if blog is None:
        abort(404)
    comment_form = CommentForm()

    comments = Comment.query.filter_by(blog_id = blog.id).all()
    return render_template('blog.html', blog = blog, form = comment_form, comments = comments)

@main.route('/comment/<int:id>', methods = ['GET','POST'])
def comment(id):
   blog = Blog.query.get_or_404(id)
   form = CommentForm()
   if form.validate_on_submit():
       comment = Comment(username = form.username.data, body = form.body.data, blog_id = blog.id)
       db.session.add(comment)
       db.session.commit()
       
   return redirect(url_for('main.read_blog', id = blog.id))

@main.route('/writer/<string:writers_name>')
def profile(writers_name):
    writer = Writer.query.filter_by(username = writers_name).first()
    if writer is None:
        abort(404)
    blogs = Blog.query.order_by(Blog.date_posted.desc()).filter_by(writer_id = writer.id)
    return render_template('profile/profile.html', writer = writer, blogs = blogs)


@main.route('/writer/<name>/update', methods = ['GET', 'POST'])
def update_profile(name):
    form = UpdateProfile()
    writer = Writer.query.filter_by(username = name).first()
    if writer is None:
        abort(404)

    form = UpdateProfile()
    if form.validate_on_submit():
        writer.bio = form.bio.data
        db.session.add(writer)
        db.session.commit()
        flash('Your profile has been updated!')
        return redirect(url_for('.profile', writers_name = writer.username))
    return render_template('profile/update.html', form = form)

@main.route('/blog/<int:id>/update', methods = ['GET','POST'])
@login_required
def blogupdate(id):
   blog = Blog.query.get_or_404(id)
   if blog.writer != current_user:
       abort(403)
   form = BlogPost()
   if form.validate_on_submit():
       blog.post = form.body.data
       blog.title = form.title.data
       db.session.commit()
       return redirect(url_for('main.read_blog', id = blog.id))
    # to populate the edit input with the posted blog text
   form.body.data = blog.post
   form.title.data = blog.title 
   return render_template('new_blog.html', form = form)

@main.route('/blog/<int:id>/delete', methods = ['POST'])
@login_required
def blog_delete(id):
    blog = Blog.query.get_or_404(id)
    if blog.writer != current_user:
       abort(403)
    db.session.delete(blog)
    db.session.commit()
    flash('Blog successfully deleted!', 'success')
    return redirect(url_for('main.index'))

@main.route('/comment/<int:id>/delete', methods = ['POST'])
@login_required
def comment_delete(id):
    comment = Comment.query.get_or_404(id)
    db.session.delete(comment)
    db.session.commit()
    flash('Comment successfully deleted!', 'success')
    return redirect(url_for('main.read_blog'))

def random_quote():
    base_url = 'http://quotes.stormconsultancy.co.uk/random.json'
    with urllib.request.urlopen(base_url) as url:
        data = url.read()
        data = json.loads(data)
    
    quote = None

    if data['quote']:
        quote = data
    return quote

@main.route('/new/subscriber', methods = ['GET','POST'])
def subscribe():
    form = SubscriptionForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            subscription = Subscription(name = form.name.data, email = form.email.data)
            # signup(form.email.data)
            db.session.add(subscription)
            db.session.commit()
            flash("You subscribed!")
            return redirect(url_for('main.index'))
    return render_template('subscribe.html', form = form)


 

