from logging import DEBUG
import os

class Config:
    SECRET_KEY= os.environ.get('SECRET_KEY')

class ProdConfig(Config):
    pass

class TestConfig(Config):
    pass
class DevConfig(Config):
    DEBUG = True

config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}