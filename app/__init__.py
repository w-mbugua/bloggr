import os
from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_manager
from flask_bootstrap import Bootstrap
from flask_simplemde import SimpleMDE
from mailchimp_marketing import Client
from mailchimp3 import MailChimp
from flask_mail import Mail

db = SQLAlchemy()
simple = SimpleMDE()
bootstrap = Bootstrap()
mailchimp = Client()
mail = Mail()


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

MAILCHIMP_API_KEY = os.environ.get('MAILCHIMP_API_KEY')

client = MailChimp(mc_api=MAILCHIMP_API_KEY, mc_user='mbugua_j')

def create_app(config_name):

    app = Flask(__name__, static_url_path='/static')

    app.config.from_object(config_options[config_name])

    db.init_app(app)
    login_manager.init_app(app)
    simple.init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)


    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    return app
