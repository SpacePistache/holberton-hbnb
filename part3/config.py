import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'super-secret-jwt-key')
    JWT_ACCESS_TOKEN_EXPIRES = 3600
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///development.dbe')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
