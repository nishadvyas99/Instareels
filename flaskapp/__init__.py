import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask import Flask
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SECRET_KEY'] = '2951b9d5bb58fe1fac16d872533168aa'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ig_clone.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['FLASK_APP'] = os.getenv('FLASK_APP')
app.config['FLASK_ENV'] = os.getenv('FLASK_ENV')

from flaskapp import routes