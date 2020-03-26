from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

comp_app = Flask(__name__)
comp_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./comp.db'
db = SQLAlchemy(comp_app)
migrate = Migrate(comp_app, db)

from .models import Member, BlogPost

from . import routes
