import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flaskext.login import LoginManager
from flaskext.openid import OpenID
from config import basedir

''' Creates the application object instancing Flask and imports 'views' module '''
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

lm = LoginManager()
lm.setup_app(app)
oid = OpenID(app, os.path.join(basedir, 'tmp'))

