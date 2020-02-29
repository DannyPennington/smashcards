from application import db
from application.models import Character


db.drop_all()

db.create_all()

values = [Character(char_id=1,name="Mario",HP=170,ATK=60,DEF=60,SPD=60),Character(char_id=2,name="Luigi",HP=170,ATK=60,DEF=50,SPD=70),Character(char_id=3,name="Donkey Kong",HP=190,ATK=60,DEF=80,SPD=20),Character(char_id=4,name="Link",HP=175,ATK=60,DEF=70,SPD=40),Character(char_id=5,name="Samus",HP=185,ATK=55,DEF=80,SPD=30),Character(char_id=6,name="Yoshi",HP=185,ATK=55,DEF=70,SPD=40),Character(char_id=7,name="Kirby",HP=115,ATK=80,DEF=50,SPD=80),Character(char_id=8,name="Fox",HP=130,ATK=80,DEF=45,SPD=95),Character(char_id=9,name="Pikachu",HP=140,ATK=70,DEF=50,SPD=90),Character(char_id=10,name="Jigglypuff",HP=120,ATK=140,DEF=20,SPD=60),Character(char_id=11,name="Captain Falcon",HP=175,ATK=40,DEF=40,SPD=100),Character(char_id=12,name="Ness",HP=150,ATK=70,DEF=50,SPD=50),Character(char_id=13,name="Peach",HP=150,ATK=60,DEF=80,SPD=60),Character(char_id=14,name="Bowser",HP=200,ATK=50,DEF=90,SPD=20),Character(char_id=15,name="Dr Mario",HP=170,ATK=60,DEF=70,SPD=50),Character(char_id=16,name="Zelda",HP=150,ATK=40,DEF=60,SPD=60),Character(char_id=17,name="Shiek",HP=150,ATK=80,DEF=50,SPD=80),Character(char_id=18,name="Young Link",HP=145,ATK=50,DEF=70,SPD=50),Character(char_id=19,name="Ganondorf",HP=185,ATK=100,DEF=60,SPD=25),Character(char_id=20,name="Falco",HP=140,ATK=90,DEF=50,SPD=80),Character(char_id=21,name="Pichu",HP=110,ATK=110,DEF=20,SPD=80),Character(char_id=22,name="Mewtwo",HP=145,ATK=70,DEF=60,SPD=60),Character(char_id=23,name="Ice Climbers",HP=145,ATK=60,DEF=50,SPD=50),Character(char_id=24,name="Marth",HP=145,ATK=90,DEF=40,SPD=80),Character(char_id=25,name="Roy",HP=145,ATK=70,DEF=60,SPD=60),Character(char_id=26,name="Mr. Game and Watch",HP=120,ATK=70,DEF=30,SPD=70),]

db.session.add_all(values)
db.session.commit()
