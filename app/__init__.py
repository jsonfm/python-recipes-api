import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

dbdir = os.path.join(os.path.abspath(os.path.dirname(__file__)), "database")
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(dbdir, 'recipes.sqlite')
db = SQLAlchemy()

db.init_app(app)

with app.app_context():
    db.create_all()
