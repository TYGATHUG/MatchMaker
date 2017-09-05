# ---------------------------------------------------------------------------------
#   Imports
# -------------------------------------------------------------------------------*/
# encoding=utf8
import os
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
from werkzeug.utils import secure_filename


# ---------------------------------------------------------------------------------
#   Initialisation / Settings
# -------------------------------------------------------------------------------*/
# Create app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
###### get pwd function
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + os.path.join(basedir, 'data/app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Database Properties
Bootstrap(app)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Upload Image Properties
UPLOAD_FOLDER = "./static/images/profiles"
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# ---------------------------------------------------------------------------------
#   Classes
# -------------------------------------------------------------------------------*/
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
    image = FileField('image', validators=[FileRequired(), FileAllowed(ALLOWED_EXTENSIONS)])
    name = StringField('name', validators=[InputRequired(), Length(min=1, max=20)])
    age = StringField('age', validators=[InputRequired(), Length(min=1, max=3)])
    gender = StringField('gender', validators=[InputRequired(), Length(min=1, max =10)])
    height = StringField('height', validators=[InputRequired(), Length(min=1, max=5)])
    location = StringField('location', validators=[InputRequired(), Length(min=1)])
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


# ---------------------------------------------------------------------------------
#   Page Routes
# -------------------------------------------------------------------------------*/

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
    # instatiate API for getting Watson data
    personality_results = api.MatchAPI()

    # validate form and upload to match data to DB
    if match_form.validate_on_submit():

        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['image']

        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print "Filename: " + filename
            print "Filepath: " + UPLOAD_FOLDER + "/" + filename

            print "Filepath: " + UPLOAD_FOLDER + "/" + filename
            
        print filename

        print"$$$ DATA $$$"
        print"cunt"
        q1 = str(match_form.q1.data)
        q2 = str(match_form.q2.data)
        q3 = str(match_form.q3.data)
        q4 = str(match_form.q4.data)
        q5 = str(match_form.q5.data)
        q6 = str(match_form.q6.data)
        q7 = str(match_form.q7.data)
        q8 = str(match_form.q8.data)
        personality = q1 + q2 + q3 + q4 + q5 + q6 + q7 + q8

        # call the Watson API and pass in the 8 questions
        results = personality_results.get_personality('test')

        # extract traits: 0 - 100 scale
        practicality = results['needs'][0]['practicality']
        love = results['needs'][0]['love']
        challenge = results['needs'][0]['challenge']
        closeness = results['needs'][0]['closeness']
        excitment = results['needs'][0]['excitment']
        structure = results['needs'][0]['structure']

        # extract traits: 1 - 3 scale
        live_music = results['live_music']
        volunteering = results['volunteering']['score']
        entreprenuer = results['entreprenuer']
        reading = results['reading']

        new_match = Match(username=user, name=match_form.name.data, gender=match_form.gender.data, \
                          age=match_form.age.data, height=match_form.height.data, suburb=match_form.suburb.data, \
                          education=match_form.education.data, ethnicity=match_form.ethnicity.data, \
                          religion=match_form.religion.data)

        new_user = User(username=register_form.username.data, email=register_form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()


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


# ---------------------------------------------------------------------------------
#   Routes for user authentication
# -------------------------------------------------------------------------------*/
# Global Variables
PREVIOUS_SAVED_ROUTE = "welcome.html"

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
        previous_route = PREVIOUS_SAVED_ROUTE
    elif previous_route == "register.html":
        previous_route = PREVIOUS_SAVED_ROUTE
    elif previous_route == "login.html":
        previous_route = PREVIOUS_SAVED_ROUTE
    else:
        globals()['PREVIOUS_SAVED_ROUTE'] = previous_route

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
        previous_route = PREVIOUS_SAVED_ROUTE
    elif previous_route == "register.html":
        previous_route = PREVIOUS_SAVED_ROUTE
    elif previous_route == "login.html":
        previous_route = PREVIOUS_SAVED_ROUTE
    else:
        globals()['PREVIOUS_SAVED_ROUTE'] = previous_route

    return render_template(previous_route, register_form=register_form, login_form=login_form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
