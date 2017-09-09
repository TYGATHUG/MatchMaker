from sqlalchemy import *
from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
import sqlite3
import random
from random import randint
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + os.path.join(basedir, 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
conn = sqlite3.connect('app.db')
c = conn.cursor()


class User(UserMixin, db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))
    setup = db.Column(db.Boolean())


class Match(db.Model):
    __tablename__ = 'Match'
    username = db.Column(db.String(15), primary_key=True, unique=True)
    view_count = db.Column(db.Integer())
    image = db.Column(db.String(120))
    name = db.Column(db.String(20))
    gender = db.Column(db.String(20))
    pref_gender = db.Column(db.String(20))
    age = db.Column(db.Integer())
    pref_age_min = db.Column(db.Integer())
    pref_age_max = db.Column(db.Integer())
    height = db.Column(db.Integer())
    location = db.Column(db.String(30))
    pref_location = db.Column(db.String(1200))
    education = db.Column(db.String(30))
    bio = db.Column(db.String(255))
    practicality = db.Column(db.Integer())
    love = db.Column(db.Integer())
    excitment = db.Column(db.Integer())
    challenge = db.Column(db.Integer())
    closeness = db.Column(db.Integer())
    structure = db.Column(db.Integer())
    live_music = db.Column(db.Integer())
    spare_moment_purchases = db.Column(db.Integer())
    gym_member = db.Column(db.Integer())
    outdoors = db.Column(db.Integer())
    volunteering = db.Column(db.Integer())
    entreprenuer = db.Column(db.Integer())
    reading = db.Column(db.Integer())


class Like(db.Model):
    __tablename__ = 'Like'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15))
    liked_user = db.Column(db.String(15))


class Dislike(db.Model):
    __tablename__ = 'Dislike'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15))
    disliked_user = db.Column(db.String(15))



# if current tables exist then drop them
def check_existing_tables():
    c.executescript('DROP TABLE IF EXISTS match')
    c.executescript('DROP TABLE IF EXISTS user')


# main logic for entering randomised data
def data_entry():

    imageExtension = ".jpg"
    emailExtension = "@gmail.com"

    # for user table
    idCounter = 1;
    password = 'password'
    admin_password = 'admin'
    test_passwordHash = generate_password_hash(password, method='sha256')
    admin_passwordHash = generate_password_hash(password, method='sha256')

    usernames = ["Jerrell", "Stan", "Ross", "Cesar", "Fredric", "Henry", "Anderson", "Alec", "Jon", "Noel", "Fidel"
        , "Brady", "Wallace", "Gayle", "Neil", "Horacio", "Florencio", "Hassan", "Raphael", "Jay", "Ali", "Lynn"
        , "Gordon", "Waylon", "Randal", "Emilio", "Fletcher", "Brett", "Emerson", "Lindsey", "Homer", "Blake", "Jarred"
        , "Damian", "Paul", "Issac", "Alvaro", "Terry", "Bryan", "Hong", "Theo", "Les", "Mohamed", "Demetrius"
        , "Benjamin", "Elde", "Christoper", "Jospeh", "Dusty", "Edwardo", "Florance", "Nelly",  "Shanti", "Cristal"
        , "Meghann", "Shelley", "Tessa", "Amada", "Argentina", "Terina", "Karie", "Adriane", "Sarita", "Ofelia", "Mollie"
        , "Shawnda", "Alise", "Chantay", "Verda", "Delmy", "Claire", "Lakeisha", "Carolina", "Hilaria", "Fanny", "Sharon"
        , "Shavonda", "Millicent", "Yan", "Nanci", "Lecia", "Dinah", "Adele", "Mindy", "Tori", "Monica", "Agripina"
        , "Myesha", "Rebecka", "Crista", "Shu", "Kasandra", "Tierra", "Merly", "Evia", "Hae", "Yer", "Sun", "Dahlia", "Marianna"
                 ]

    gender = ["Male", "Female"]

    location = ["Melbourne", "Sydney", "Perth", "ACT", "Adelaide", "Hobart", "ACT", "Darwin", "Brisbane"]
    education = ["Certificate", "Diploma", "Associate Degree", "Bachelor", "Master", "Doctoral"]
    
    bio = ["I like to fly model aircraft.", "I like pizza and walks on beach at sunset.",
           "I like to play minecraft.", "I like horror movies and fast cars.",
           "My ideal date is walk on beach and enjoy the sunset.", "I love to travel and see other cultures.",
           "Duis efficitur diam sit amet augue mollis fermentum.", "Aliquam sed diam at sapien aliquet pellentesque.",
           "Morbi malesuada ipsum sit amet interdum pellentesque.", "Phasellus nec lacus vel elit iaculis ullamcorper at consequat lectus.",
           "Maecenas venenatis urna sed lectus vehicula pellentesque.", "Fusce placerat sem eu quam vestibulum imperdiet.",
           "Maecenas congue mauris id leo volutpat posuere.", "Nullam posuere risus non eros porttitor, quis cursus erat finibus."
           ]

    experienceValues = [0, 0.5, 1]

    initialLengthOfNames = len(usernames)


    for x in range(0,initialLengthOfNames):

        # for Match table
        randName = random.choice(usernames)
        imageName = randName + imageExtension
        randGender = random.choice(gender)
        randLocation = random.choice(location)
        randEducation = random.choice(education)
        randBio = random.choice(bio)

        # for user table
        emailName = randName + emailExtension

        conn.execute('''INSERT INTO Match (username, view_count, image, name, gender, pref_gender,
                     age, pref_age_min, pref_age_max, height, location, pref_location, education,
                     bio, practicality, love, excitment, challenge, closeness, structure, live_music, 
                     spare_moment_purchases, gym_member, outdoors, volunteering, entreprenuer, reading) 
                     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                     (randName.lower(), 0, imageName.lower(), randName, randGender, "", (randint(18, 70)), 0, 0,
                     (randint(145, 213)), randLocation, "", randEducation, randBio, (randint(1, 100)), (randint(1, 100)),
                     (randint(1, 100)), (randint(1, 100)), (randint(1, 100)), (randint(1, 100)), random.choice(experienceValues),
                     random.choice(experienceValues), random.choice(experienceValues), random.choice(experienceValues),
                     random.choice(experienceValues), random.choice(experienceValues), random.choice(experienceValues)))

        conn.execute('''INSERT INTO user (id, username, email, password, setup) VALUES (?, ?, ?, ?, ?)''',
                     (idCounter, randName.lower(), emailName.lower(), test_passwordHash, True))
        conn.commit()

        usernames.remove(randName)
        idCounter += 1;

    conn.execute('''INSERT INTO user (id, username, email, password, setup) VALUES (?, ?, ?, ?, ?)''',
                 (idCounter, "admin", "admin@gmail.com", admin_passwordHash, True))
    conn.commit()

    c.close()
    conn.close()


if __name__ == "__main__":

    check_existing_tables()

    # sqlalchemys database connection object
    engine = create_engine('sqlite:////' + os.path.join(basedir, 'app.db'))
    # create all table database definitions
    db.metadata.create_all(bind=engine)

    data_entry()
