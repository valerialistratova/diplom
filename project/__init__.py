# -*- coding: utf-8 -*-
__version__ = '0.1'
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import locale
locale.setlocale(locale.LC_ALL, 'rus_rus')
from flask_debugtoolbar import DebugToolbarExtension
app = Flask('project')
app.config['SECRET_KEY'] = 'random'
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost:3306/lectio'
db = SQLAlchemy(app)
# toolbar = DebugToolbarExtension(app)
from project.controllers import *
