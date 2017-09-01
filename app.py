from flask import Flask, render_template, url_for, g, redirect, session, request, flash
import os
import sqlite3
import api

app = Flask(__name__)
app.config.from_object(__name__) 


app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'app.db'),
    SECRET_KEY='secretkey',
    USERNAME='admin',
    PASSSWORD='password'
))

app.config.from_envvar('FLASKR_SETTINGS', silent=True)


"""
Database Handlers
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
Routes
"""
@app.route('/') 
def home():
    return render_template('welcome.html')


<<<<<<< HEAD
@app.route('/member') 
def member():

    
    return render_template('member.html')
=======
@app.route('/register')
def register():
    return render_template('register.html')
>>>>>>> 9b2227b5c872dcf5a2cf5c8499851df4efa77354


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/profile')
def profile():

    return render_template('profile.html')


@app.route('/member')
def member():
    return render_template('member.html')


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



if __name__ == "__main__":
    app.run(debug=True)
