import os


class Config(object):
    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    DEBUG = False


class StageConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

