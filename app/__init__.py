from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

''' Creates the application object instancing Flask and imports 'views' module '''
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)


from app import views, models