import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True
    # Sets the URI of the SQLite database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///development.db'
    # Disables object change tracking
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
