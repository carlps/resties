# project/_config.py


import os
from binascii import hexlify

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    CSRF_ENABLED = True
    SECRET_KEY = hexlify(os.urandom(24))
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.environ['RESTIES_DB_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = os.environ['TEST_DB_URL']


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
