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
    SQLALCHEMY_DATABASE_URI = 'postgres://oifoekteswjcdo:64181d4f3f4ed77bfd5e56868642eca89d701e75cbf39a6f2f83a20f625c348c@ec2-50-16-108-41.compute-1.amazonaws.com:5432/d6fdke2sffeg9o'.replace("://", "ql://", 1)
    DEBUG = True

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