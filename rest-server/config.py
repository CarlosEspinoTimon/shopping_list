import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # SQLALCHEMY_DATABASE_URI = 'mysql://root:root@127.0.0.1:3306/test'

    # When deployed to App Engine, the `SERVER_SOFTWARE` environment variable
    # will be set to 'Google App Engine/version'.
    connection_name = os.environ.get('CLOUDSQL_CONNECTION_NAME')
    user = os.environ.get('CLOUDSQL_USER')
    password = os.environ.get('CLOUDSQL_PASSWORD')
    database = os.environ.get('CLOUDSQL_DATABASE')
    if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/'):
        # Connect to production Cloud SQL
        # SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://[CLOUDSQL_USER]@[CLOUDSQL_PASSWORD]/[CLOUDSQL_DATABASE]?unix_socket=/cloudsql/[CLOUDSQL_CONNECTION_NAME]'
        
        # SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://{}:{}@/{}?unix_socket=/cloudsql/{}'.format(user, password, database, connection_name)
        SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root@/test?unix_socket=/cloudsql/shopping-list-215005:shopping-list-sql'
    else:                         

        # Connect to through proxy
        # :SQLALCHEMY_DATABASE_URI = 'mysql://[CLOUDSQL_USER]:[CLOUDSQL_PASSWORD]@127.0.0.1:3306/[CLOUDSQL_DATABASE]'
        SQLALCHEMY_DATABASE_URI = 'mysql://{}:{}@127.0.0.1:3306/{}'.format(user, password, database)
    # os.environ.get('DATABASE_URL') or \
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ARTICLES_PER_PAGE = 5
