# import os

# class Config(object):
#     """
#     Common configurations
#     """
#     SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
#     SECRET_KEY = os.environ.get("SECRET_KEY")

#     # Put any configurations here that are common across all environments


# class DevelopmentConfig(Config):
#     """
#     Development configurations
#     """

#     DEBUG = True
#     SQLALCHEMY_ECHO = True


# class ProductionConfig(Config):
#     """
#     Production configurations
#     """

#     DEBUG = False

# app_config = {
#     'development': DevelopmentConfig,
#     'production': ProductionConfig
# }


import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
