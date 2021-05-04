import os

class Config:
    SECRET_KEY= os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

    # mail_settings 
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('MAIL_USER')
    MAIL_PASSWORD = os.environ.get('MAIL_PASS')

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgres://mexldstdripdhe:ccd4d838a185c546cb99f43ce7ded2839e567f89af403827f5819a117b7e7ca5@ec2-35-174-35-242.compute-1.amazonaws.com:5432/d20rs9vgivecdj'.replace("://", "ql://", 1)

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://joey:alchemist007@localhost/bloggr_test'

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://joey:alchemist007@localhost/bloggr'

config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}