# encoding=utf8
from flask import Flask, render_template, url_for, g, redirect, session, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_user import login_required, UserManager, UserMixin, SQLAlchemyAdapter
import sqlite3
import os
import api

# Create app
app = Flask(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/damontoumbourou/Code/match-maker/data/app.db'
app.config['SECRET_KEY'] = 'secret'
app.config['CSRF_ENABLED'] = True
app.config['USER_ENABLE_EMAIL'] = False

db = SQLAlchemy(app)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False, server_default='')
    active = db.Column(db.Boolean(), nullable=False, server_default='0')

db_adapter = SQLAlchemyAdapter(db, User)
user_manager = UserManager(db_adapter, app)


"""
Database handlers
"""
"""
def connect_db():
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

@app.cli.command('initdb')
def initdb_command():
    init_db()
    print('init the database')


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

"""
"""
Page Routes
"""
@app.route('/', methods=['GET', 'POST']) 
def home():

    return render_template('welcome.html')


@app.route('/member')
def member():
    
    personality = api.MatchAPI().get_personality('test')
    print personality

    return render_template('member.html')


@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():

    """
    q1 = str(request.args.get('q1'))
    q2 = str(request.args.get('q2'))
    q3 = str(request.args.get('q3'))
    q4 = str(request.args.get('q4'))
    q5 = str(request.args.get('q5'))
    q6 = str(request.args.get('q6'))
    q7 = str(request.args.get('q7'))
    q8 = str(request.args.get('q8'))


    personality = q1 + q2 + q3 + q4 + q5 + q6 + q7 + q8
    
  
    results = api.MatchAPI().get_personality(personality)
    
    
    db_write = get_db()
    practicality = results['needs'][0]['practicality']
    love = results['needs'][0]['love']
    excitement = results['needs'][0]['excitment']
    
    print practicality
    #db_write.execute('insert into MATCH (')

    """    
    return render_template('profile.html')


@app.route('/terms')
def terms():
    return render_template('terms.html')


@app.route('/privacy')
def privacy():
    return render_template('privacy.html')


@app.route('/help')
def help():
    return render_template('help.html')


@app.route('/about')
def about():
    return render_template('about.html')


"""
Routes for user authentication
"""


if __name__ == "__main__":

    app.run(debug=True)
