from flask import Flask, app
from flask_sqlalchemy import SQLAlchemy
from .models import User, Note
from .views import views
from .auth import auth

db = SQLAlchemy()
DB_NAME = 'database.db'

def create_app():
  app = Flask(__name__)
  app.config['SECRET_KEY'] = 'Zwjpws6Met'
  app.config['SQLALCHEMY_DATABASE_URL'] = f'sqlite:///{DB_NAME}'
  db.init_app(app)


  app.register_blueprint(views, url_prefix='/')
  app.register_blueprint(auth, url_prefix='/')

  return app