# -*- coding: utf-8 -*-
#!flask/bin/python
# This had to be fixed with  'pip install SQLAlchemy==0.7.2' since there are compatibility problems with SQLAlchemy-migrate
from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO
from app import db
import os.path
db.create_all()
print SQLALCHEMY_MIGRATE_REPO
print SQLALCHEMY_DATABASE_URI
if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
    api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
else:
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, api.version(SQLALCHEMY_MIGRATE_REPO))