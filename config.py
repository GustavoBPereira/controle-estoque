import os
from flask import Flask

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + os.path.join(basedir, 'estoque.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

import views