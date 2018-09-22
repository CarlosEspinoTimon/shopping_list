import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # These environment variables are configured in app.yaml.
    MYSQL_HOST = os.environ.get('MYSQL_HOST')
    MYSQL_USER = os.environ.get('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD')
    MYSQL_PASSWORD_DEVELOP = os.environ.get('MYSQL_PASSWORD_DEVELOP', 'root')
    MYSQL_DATABASE = os.environ.get('MYSQL_DATABASE', 'test')


    # When deployed to App Engine, the `SERVER_SOFTWARE` environment variable
    # will be set to 'Google App Engine/version'.
    if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/'):
        SQLALCHEMY_DATABASE_URI = ('mysql://{username}:{password}@{host}:3306/{database}').format(
                    username=MYSQL_USER, password=MYSQL_PASSWORD, database=MYSQL_DATABASE,
                    host=MYSQL_HOST)
    else:
        SQLALCHEMY_DATABASE_URI = (
            'mysql://{user}:{password}@127.0.0.1:3306/{database}').format(
            user=MYSQL_USER, password=MYSQL_PASSWORD_DEVELOP,
            database=MYSQL_DATABASE)

    
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ARTICLES_PER_PAGE = 5
