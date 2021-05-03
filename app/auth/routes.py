from flask_login.utils import login_required
from . import auth
from flask import render_template, url_for, redirect, flash, request
from .forms import RegistrationForm, LoginForm
from .. import db
from ..models import Writer
from flask_login import login_user, logout_user
from flask_mail import Message
from .. import mail

@auth.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        writer = Writer(username = form.username.data, email = form.email.data, password = form.password.data)
        db.session.add(writer)
        db.session.commit()
        msg = Message(subject="Welcome To The Code Savvy Blog",
                          sender="itsjoymbugua@gmail.com",
                          recipients=[form.email.data],
                          body=f"Hey {writer.username}\nThank you for signing up. If you have any queries, don't hesitate to contact me!\nJoy Mbugua")
        mail.send(msg)
        flash('Your account has been created!', 'success')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', title='Registration', form = form)

@auth.route('/login', methods = ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        writer = Writer.query.filter_by(email = form.email.data).first()
        if writer is not None and writer.verify_password(form.password.data):
            login_user(writer, form.remember.data)
            return redirect(request.args.get(next) or url_for('main.index'))
        flash('Invalid username or password')
    return render_template('auth/login.html', title='Logged In', form = form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))