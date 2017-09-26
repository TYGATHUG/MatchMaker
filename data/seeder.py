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

class PersonalityAnswers(db.Model):
    __tablename__ = 'PersonalityAnswers'
    username = db.Column(db.String(15), primary_key=True, unique=True)
    q1 = db.Column(db.String(255))
    q2 = db.Column(db.String(255))
    q3 = db.Column(db.String(255))
    q4 = db.Column(db.String(255))
    q5 = db.Column(db.String(255))
    q6 = db.Column(db.String(255))
    q7 = db.Column(db.String(255))
    q8 = db.Column(db.String(255))


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
    c.executescript('DROP TABLE IF EXISTS personalityanswers')
    c.executescript('DROP TABLE IF EXISTS Like')
    c.executescript('DROP TABLE IF EXISTS Dislike')


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

    answers = ["I tend to keep to myself and study a lot", "I like to be outside with nature", "I like to go camping with friends",
               "I like to spend time with family doing things", "I like to go on adventures outside from home",
               "I like to sing in the shower", "I like to walk my dog", "I love exercising, particularly running",
               "I would love to go to China and see the history", "I want to go to America and see more pop culture",
               "I want to see the scenery in New Zealand", "I would be happy just going to Sydney for a visit",
               "I have always wanted to see what Africa has to offer", "Europe has been a place I've always wanted to go",
               "I recently splurged a lot of money, I impulse buy a lot", "I just like to window shop",
               "I love trying on clothes at different stores", "I usually just buy only the necessities",
               "I always go just for strength training, my favourite!", "I think people exercising is a great thing",
               "I just do cardio and like to keep fit that way", "I'm a bit intimidated by the thought",
               "It meanns being able to enjoy yourself without a phone", "To keep away from electronics and enjoy yourself",
               "Just enjoying yourself outside of the comfort of your home", "Heading straight into the wilderness",
               "I went camping at Dandenong, good times", "Does the beach count as nature?", "Very, very cold to go during Winter",
               "I invented a new app that no one has done before", "I made my own clothes business",
               "It is something more people should do", "I don't really see the need for it personally"]

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

        conn.execute('''INSERT INTO PersonalityAnswers (username, q1, q2, q3, q4, q5, q6, q7, q8) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                     (randName.lower(), random.choice(answers), random.choice(answers), random.choice(answers),
                      random.choice(answers), random.choice(answers), random.choice(answers), random.choice(answers),
                      random.choice(answers)))

        conn.commit()

        usernames.remove(randName)
        idCounter += 1;

    conn.execute('''INSERT INTO user (id, username, email, password, setup) VALUES (?, ?, ?, ?, ?)''',
                 (idCounter, "admin", "admin@gmail.com", admin_passwordHash, True))

    conn.execute('''INSERT INTO Match (username, view_count, image, name, gender, pref_gender,
                         age, pref_age_min, pref_age_max, height, location, pref_location, education,
                         bio, practicality, love, excitment, challenge, closeness, structure, live_music, 
                         spare_moment_purchases, gym_member, outdoors, volunteering, entreprenuer, reading) 
                         VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                 ("admin", 0, "neil.jpg", "Admin", randGender, "", (randint(18, 70)), 0, 0,
                  (randint(145, 213)), randLocation, "", randEducation, randBio, (randint(1, 100)), (randint(1, 100)),
                  (randint(1, 100)), (randint(1, 100)), (randint(1, 100)), (randint(1, 100)),
                  random.choice(experienceValues),
                  random.choice(experienceValues), random.choice(experienceValues), random.choice(experienceValues),
                  random.choice(experienceValues), random.choice(experienceValues), random.choice(experienceValues)))

    usernames = ["Admin", "Jerrell", "Stan", "Ross", "Cesar", "Fredric", "Henry", "Anderson", "Alec", "Jon", "Noel",
                 "Fidel", "Brady", "Wallace", "Gayle", "Neil", "Horacio", "Florencio", "Hassan", "Raphael", "Jay", "Ali", "Lynn"
                , "Gordon", "Waylon", "Randal", "Emilio", "Fletcher", "Brett", "Emerson", "Lindsey", "Homer", "Blake", "Jarred"
                , "Damian", "Paul", "Issac", "Alvaro", "Terry", "Bryan", "Hong", "Theo", "Les", "Mohamed", "Demetrius"
                , "Benjamin", "Elde", "Christoper", "Jospeh", "Dusty", "Edwardo", "Florance", "Nelly", "Shanti", "Cristal"
                , "Meghann", "Shelley", "Tessa", "Amada", "Argentina", "Terina", "Karie", "Adriane", "Sarita", "Ofelia", "Mollie"
                , "Shawnda", "Alise", "Chantay", "Verda", "Delmy", "Claire", "Lakeisha", "Carolina", "Hilaria", "Fanny", "Sharon"
                , "Shavonda", "Millicent", "Yan", "Nanci", "Lecia", "Dinah", "Adele", "Mindy", "Tori", "Monica", "Agripina"
                , "Myesha", "Rebecka", "Crista", "Shu", "Kasandra", "Tierra", "Merly", "Evia", "Hae", "Yer", "Sun", "Dahlia", "Marianna"]

    # seed like table
    id_count = 0
    for i in range(0, (initialLengthOfNames / 2)):
        username = usernames[i]

        for j in range(0, (initialLengthOfNames - 1)):
            if i != j:
                liked_user = usernames[j]

                conn.execute('''INSERT INTO Like (id, username, liked_user) VALUES (?, ?, ?)''',
                             (id_count, username.lower(), liked_user.lower()))

                id_count += 1

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
