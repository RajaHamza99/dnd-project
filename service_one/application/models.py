from application import db

class characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=False)
    char_class = db.Column(db.String(100), nullable=False, unique=False)
    char_race = db.Column(db.String(100), nullable=False, unique=False)
    def __repr__(self):
        return ''.join(['ID: ', str(self.id), 'Character Name: ', self.name, 'Character Class', self.char_class, 'Character Race', self.char_class])
