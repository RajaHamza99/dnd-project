from flask import Flask
from os import getenv
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + str(getenv('DB_USER')) + ':' + str(getenv('DB_PASS')) + '@dnd_mysql:3306/dnd-db'
app.config['SECRET_KEY'] = getenv('SECRET_KEY')

from application import routes
