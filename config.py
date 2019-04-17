import os


# Default config
class BaseConfig(object):
    DEBUG = True
    SECRET_KEY = b'\xfa\xb2X$\x9b\xdf\x8e\r\x8b\xb1L\xd7\xc0\x9d9"R\x81U\xa9Fp\x91\xd6'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'

# Test config
class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

# Production config
class ProductionConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:test@localhost/feature_request'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
