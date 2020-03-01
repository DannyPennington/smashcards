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
        return ''.join(["ID: ", str(self.char_id), "Name: ", self.name])

class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    forename = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return ''.join(["UserID: ", str(self.user_id), "\r\n", "Email: ", self.email, "Name: ",self.forename, " ", self.surname])


