import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db') #2bechanged with mysql/mariadb1
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
