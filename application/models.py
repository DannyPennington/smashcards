from application import db
import sqlalchemy


class Character(db.Model):
    char_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    HP = db.Column(db.Integer, nullable=False)
    ATK = db.Column(db.Integer, nullable=False)
    DEF = db.Column(db.Integer, nullable=False)
    SPD = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return ''.join(["ID: ", self.char_id, "Name: ", self.name])

