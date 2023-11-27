from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
import os 

# file_path = os.path.abspath(os.getcwd())+"/todo.db"

app = Flask(__name__) 
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+file_path 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(app) 

with app.app_context():
    from app import models  # or wherever your models are defined
    db.create_all()

from app import routes 
