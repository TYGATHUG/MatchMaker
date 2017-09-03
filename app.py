# encoding=utf8
from flask import Flask, render_template, url_for, g, redirect, session, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_wtf.file import FileField, FileAllowed, FileRequired
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import UploadSet, IMAGES
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import sqlite3
import os
import api
from werkzeug.security import generate_password_hash, check_password_hash

# Create app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
###### get pwd function
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/bendiep/Github/MatchMaker/data/app.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/damontoumbourou/Code/match-maker/data/app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#app.config.from_envvar('FLASKR_SETTINGS', silent=True)
Bootstrap(app)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
images = UploadSet('images', IMAGES)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')

class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(min=3, max=50)])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    unique = BooleanField('unique')

class MatchForm(FlaskForm):
    age = StringField('age', validators=[InputRequired(), Length(min=1)])
    pref_age = StringField('pref_age', validators=[InputRequired(), Length(min=1)])
    gender = StringField('gender', validators=[InputRequired(), Length(min=1)])
    pref_gender = StringField('pref_gender', validators=[InputRequired(), Length(min=1)])
    image = FileField('image', validators=[FileRequired(), FileAllowed(images, 'Images only!')])
    q1 = StringField('q1', validators=[InputRequired(), Length(min=15, max=255)])
    q2 = StringField('q2', validators=[InputRequired(), Length(min=15, max=255)])
    q3 = StringField('q3', validators=[InputRequired(), Length(min=15, max=255)])
    q4 = StringField('q4', validators=[InputRequired(), Length(min=15, max=255)])
    q5 = StringField('q5', validators=[InputRequired(), Length(min=15, max=255)])
    q6 = StringField('q6', validators=[InputRequired(), Length(min=15, max=255)])
    q7 = StringField('q7', validators=[InputRequired(), Length(min=15, max=255)])
    q8 = StringField('q8', validators=[InputRequired(), Length(min=15, max=255)])

"""
class Match(db.Model):
    username = db.Column(db.String(15), unique=True)
    gender = db.Column(db.String(20))
    pref_gender = db.Column(db.String(20))
    age = db.Column(db.Integer(10))
    password = db.Column(db.String(80))
    password = db.Column(db.String(80))
    password = db.Column(db.String(80))
    password = db.Column(db.String(80))
"""

"""
Page Routes
"""
@app.route('/', methods=['GET', 'POST']) 
def home():
    register_form = RegisterForm()
    login_form = LoginForm()

    return render_template('welcome.html', register_form=register_form, login_form=login_form)


@app.route('/member')
@login_required
def member():
    personality = api.MatchAPI().get_personality('test')
    print personality

    return render_template('member.html', name=current_user.username)


@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():

    
    return render_template('profile.html', name=current_user.username)


@app.route('/match', methods=['GET', 'POST'])
@login_required
def match():
    form = MatchForm()


    print "here : "  
    print form.gender.data

    """
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
    """

    return render_template('match.html', name=current_user.username, form=form)


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
@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    register_form = RegisterForm()

    if login_form.validate_on_submit():
        user = User.query.filter_by(username=login_form.username.data).first()

        if user:
            if check_password_hash(user.password, login_form.password.data):
                login_user(user, remember=login_form.remember.data)
                flash("Login Successful!")
                return redirect(url_for('member'))

    return render_template('login.html', form=form) 
    
    # return error 'username does not exist'
    return render_template('welcome.html', register_form=register_form, login_form=login_form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    login_form = LoginForm()
    register_form = RegisterForm()

    user = User.query.filter_by(username=login_form.username.data).first()
    if not user:
        if register_form.validate_on_submit():
            hashed_password = generate_password_hash(register_form.password.data, method='sha256')
            new_user = User(username=register_form.username.data, email=register_form.email.data, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            flash("Register Successful!")
            register_form.unique = True
            return redirect(url_for('member'))
    else:
        hashed_password = generate_password_hash(register_form.password.data, method='sha256')
        new_user = User(username=register_form.username.data, email=register_form.email.data, password=hashed_password)
        register_form.unique = False

    return render_template('welcome.html', register_form=register_form, login_form=login_form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


if __name__ == "__main__":

    app.run(debug=True)
