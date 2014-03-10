import os
basedir = os.path.abspath(os.path.dirname(__file__))

# Set Database URI for flask-sqlalchemy
##Change app.db to test.db to run unittests
if os.environ.get('DATABASE_URL') is None:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
else:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')