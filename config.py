# -*- coding: utf-8 -*-
# import os
# basedir = os.path.abspath(os.path.dirname(__file__))

# 是the Flask-SQLAlchemy必需的扩展。这是我们的数据库文件的路径。
# SQLALCHEMY_DATABASE_URI = 'sqlite:///%s' % os.path.join(basedir, 'myrpg.db')
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1234@localhost/rpg'

SQLALCHEMY_TRACK_MODIFICATIONS = True

# 是用来存储SQLAlchemy-migrate数据库文件的文件夹。
# SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
