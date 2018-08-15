import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@127.0.0.1:3306/test'
    # os.environ.get('DATABASE_URL') or \
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ARTICLES_PER_PAGE = 5
