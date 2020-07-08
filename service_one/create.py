from application import db
from application.models import characters


db.drop_all()
db.create_all()
