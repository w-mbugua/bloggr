from . import auth
from flask import render_template, url_for, redirect
from .forms import RegistrationForm, LoginForm

@auth.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()

    return render_template('auth/register.html', title='Registration', form = form)

@auth.route('/login', methods = ['GET','POST'])
def login():
    form = LoginForm()

    return render_template('auth/login.html', title='Logged In', form = form)