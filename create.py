from application import db
from application.models import Character


db.drop_all()

db.create_all()

values = [Character(char_id=1,name="Mario",HP=170,ATK=60,DEF=60,SPD=60),Character(char_id=2,name="Luigi",HP=170,ATK=60,DEF=50,SPD=70)]

db.session.add_all(values)
db.session.commit()
