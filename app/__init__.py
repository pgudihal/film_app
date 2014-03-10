import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
##Initialize all the Flask stuff
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

#A solution for logging data on Heroku from my flask App
# Also from Miguel Grinberg's Mega Tutorials
if not app.debug and os.environ.get('HEROKU') is None:
    import logging
    from logging.handlers import RotatingFileHandler
    file_handler = RotatingFileHandler('tmp/sfilm.log', 'a', 1 * 1024 * 1024, 10)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('SFILM startup')

if os.environ.get('HEROKU') is not None:
    import logging
    stream_handler = logging.StreamHandler()
    app.logger.addHandler(stream_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('SFILM startup')

from app import models,views