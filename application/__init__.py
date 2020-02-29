from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)

db = SQLAlchemy(app)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI")
#app.config["SQLALCHEMY_DATABASE_URI"] = 

from application import routes
