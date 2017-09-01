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


@app.route('/member') 
def member():

    
    return render_template('member.html')


@app.route('/profile') 
def profile():

    input_string = """Have you heard of the principle of least action? It’s the most important idea in physics, and it underlies everything. According to this principle, our reality is optimal in a mathematically exact way: it minimizes a function called the “action.” The universe that we find ourselves in is the one for which the action takes on the smallest value.
    In quantum mechanics, reality isn’t quite that optimal. Quantum fields don’t have to decide on one specific configuration; they can do everything they want, and the action then quantifies the weight of each contribution. The sum of all these contributions – known as the path-integral – describes again what we observe.
    This omniscient action has very little to do with action as action hero. It’s simply an integral, usually denoted S, over another function, called the Lagrangian, usually denoted L. There’s a Lagrangian for the Standard Model and one for General Relativity. Taken together they encode the behavior of everything that we know of, except dark matter and quantum gravity. 
    With a little practice, there’s a lot you can read off directly from the Lagrangian, about the behavior of the theory at low or high energies, about the type of fields and mediator fields, and about the type of interaction. 
    The below figure gives you a rough idea how that works."""

    personality = api.MatchAPI.get_personality(inputstring)
    print personailty

    return render_template('profile.html')


@app.route('/register') 
def register():
    
    return render_template('register.html')


@app.route('/login') 
def login():
    
    return render_template('login.html')

    




if __name__ == "__main__":
    app.run(debug=True)