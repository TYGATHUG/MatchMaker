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
    
    personality = api.MatchAPI().get_personality('test')
    print personality

    return render_template('member.html')


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    
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



if __name__ == "__main__":
    app.run(debug=True)
