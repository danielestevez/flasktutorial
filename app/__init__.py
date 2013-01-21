import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from config import basedir
import logging



''' Creates the application object instancing Flask and imports 'views' module '''
app = Flask(__name__)
app.config.from_object('config')

file_handler = logging.FileHandler('app.log')
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)


db = SQLAlchemy(app)

lm = LoginManager()
lm.setup_app(app)
oid = OpenID(app, os.path.join(basedir, 'tmp'))

app.logger.info('Flask Tutorial app initialized')

