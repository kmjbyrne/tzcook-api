import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    RUN_PORT = 5000
    TESTING = False
    # SQLALCHEMY_POOL_SIZE = 100
    # SQLALCHEMY_POOL_RECYCLE = 3600


class StagingConfig(Config):
    DEBUG = True
    TESTING = False


class ReleaseConfig(Config):
    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join('/tmp', 'store.db')
    DEBUG = True
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join('/tmp', 'store.db')
    DEBUG = True
    TESTING = True
