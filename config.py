import os


# default config
class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = b'\xfa\xb2X$\x9b\xdf\x8e\r\x8b\xb1L\xd7\xc0\x9d9"R\x81U\xa9Fp\x91\xd6'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'


class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
    DB_USERNAME = 'root'
    DB_PASSWORD = 'test'
    DATABASE_NAME = 'feature_request'
    DB_HOST = 'mysql:3306'
    DB_URI = "mysql+pymysql://%s:%s@%s/%s" % (DB_USERNAME, DB_PASSWORD, DB_HOST, DATABASE_NAME)
    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = True
