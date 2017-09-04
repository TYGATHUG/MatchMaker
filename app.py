# encoding=utf8
from flask import Flask, render_template, url_for, g, redirect, request, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_wtf.file import FileField, FileAllowed, FileRequired
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import UploadSet, IMAGES
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import api
from werkzeug.security import generate_password_hash, check_password_hash

# Create app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
###### get pwd function
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/bendiep/Github/MatchMaker/data/app.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/damontoumbourou/Code/match-maker/data/app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


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
    name = StringField('name', validators=[InputRequired(), Length(min=1, max=20)])
    age = StringField('age', validators=[InputRequired(), Length(min=1, max=3)])
    gender = StringField('gender', validators=[InputRequired(), Length(min=1, max =10)])
    height = StringField('height', validators=[InputRequired(), Length(min=1, max=5)])
    suburb = StringField('suburb', validators=[InputRequired(), Length(min=1)])
    education = StringField('education', validators=[InputRequired(), Length(min=1, max=20)])
    ethnicity = StringField('ethnicity', validators=[InputRequired(), Length(min=1, max=20)])
    religion = StringField('religion', validators=[InputRequired(), Length(min=1, max=20)])
    bio = StringField('bio', validators=[InputRequired(), Length(min=1, max=255)])
    q1 = StringField('q1', validators=[InputRequired(), Length(min=15, max=255)])
    q2 = StringField('q2', validators=[InputRequired(), Length(min=15, max=255)])
    q3 = StringField('q3', validators=[InputRequired(), Length(min=15, max=255)])
    q4 = StringField('q4', validators=[InputRequired(), Length(min=15, max=255)])
    q5 = StringField('q5', validators=[InputRequired(), Length(min=15, max=255)])
    q6 = StringField('q6', validators=[InputRequired(), Length(min=15, max=255)])
    q7 = StringField('q7', validators=[InputRequired(), Length(min=15, max=255)])
    q8 = StringField('q8', validators=[InputRequired(), Length(min=15, max=255)])


class Match(db.Model):
    __tablename__ = 'Match'
    username = db.Column(db.String(15), primary_key=True, unique=True)
    name = db.Column(db.String(20))
    gender = db.Column(db.String(20))
    age = db.Column(db.Integer())
    height = db.Column(db.Integer())
    suburb = db.Column(db.String(30))
    education = db.Column(db.String(30))
    ethnicity = db.Column(db.String(30))
    religion = db.Column(db.String(30))
    bio = db.Column(db.String(255))
    personality = db.Column(db.Integer())
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


"""
Page Routes
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    register_form = RegisterForm()
    login_form = LoginForm()
    globals()['previous_saved_route'] = "welcome.html"

    if current_user.is_authenticated:
        return render_template('member.html')
    else:
        return render_template('welcome.html', register_form=register_form, login_form=login_form)


@app.route('/member')
@login_required
def member():



    return render_template('member.html', name=current_user.username)


@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    match_form = MatchForm()
    """
    personality = api.MatchAPI().get_personality('test')
    """

    print"profile route"

    if match_form.validate_on_submit():
        print"$$$ DATA $$$"

        personality = str(match_form.q1.data) + str(match_form.q2.object_data)
        print personality



        """
        new_user = User(username=register_form.username.data, email=register_form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        """

        return redirect(url_for('member'))


    return render_template('profile.html', name=current_user.username, match_form=match_form)


@app.route('/terms', methods=['GET', 'POST'])
def terms():
    register_form = RegisterForm()
    login_form = LoginForm()

    return render_template('terms.html', register_form=register_form, login_form=login_form)


@app.route('/privacy', methods=['GET', 'POST'])
def privacy():
    register_form = RegisterForm()
    login_form = LoginForm()

    return render_template('privacy.html', register_form=register_form, login_form=login_form)


@app.route('/help', methods=['GET', 'POST'])
def help():
    register_form = RegisterForm()
    login_form = LoginForm()

    return render_template('help.html', register_form=register_form, login_form=login_form)


@app.route('/about', methods=['GET', 'POST'])
def about():
    register_form = RegisterForm()
    login_form = LoginForm()

    return render_template('about.html', register_form=register_form, login_form=login_form)


"""
Routes for user authentication
"""
# Global Variables
previous_saved_route = "welcome.html"

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

    previous_route = str(request.referrer.split("/", 2)[2].split('/')[1]) + ".html"
    if previous_route == ".html":
        previous_route = previous_saved_route
    elif previous_route == "register.html":
        previous_route = previous_saved_route
    elif previous_route == "login.html":
        previous_route = previous_saved_route
    else:
        globals()['previous_saved_route'] = previous_route

    return render_template(previous_route, register_form=register_form, login_form=login_form)


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

    previous_route = str(request.referrer.split("/",2)[2].split('/')[1]) + ".html"
    if previous_route == ".html":
        previous_route = previous_saved_route
    elif previous_route == "register.html":
        previous_route = previous_saved_route
    elif previous_route == "login.html":
        previous_route = previous_saved_route
    else:
        globals()['previous_saved_route'] = previous_route

    return render_template(previous_route, register_form=register_form, login_form=login_form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


if __name__ == "__main__":

    app.run(debug=True)
