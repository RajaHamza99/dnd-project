from application import db, login_manager
from flask_login import UserMixin
from datetime import datetime

class characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=False)
    char_class = db.Column(db.String(100), nullable=False, unique=False)
    char_race = db.Column(db.String(100), nullable=False, unique=False)

