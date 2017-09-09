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
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

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

# Admin configurations
admin = Admin(app)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# ---------------------------------------------------------------------------------
#   Classes Databases
# -------------------------------------------------------------------------------*/
class User(UserMixin, db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))
    setup = db.Column(db.Boolean())

admin.add_view(ModelView(User, db.session)) # create User view for current session

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Match(db.Model):
    __tablename__ = 'Match'
    username = db.Column(db.String(15), primary_key=True, unique=True)
    view_count = db.Column(db.Integer())
    image = db.Column(db.String(120))
    name = db.Column(db.String(20))
    gender = db.Column(db.String(20))
    age = db.Column(db.Integer())
    height = db.Column(db.Integer())
    location = db.Column(db.String(30))
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



# ---------------------------------------------------------------------------------
#   Classes Forms
# -------------------------------------------------------------------------------*/
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=3, max=15)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=4, max=80)])
    remember = BooleanField('Remember Me')


class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email(message='Invalid email'), Length(min=3, max=50)])
    username = StringField('Username', validators=[InputRequired(), Length(min=3, max=15)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=4, max=80)])
    unique_user = BooleanField('unique_user')
    unique_email = BooleanField('unique_email')


class MatchForm(FlaskForm):
    image = FileField('Image', validators=[FileRequired(), FileAllowed(ALLOWED_EXTENSIONS)])
    name = StringField('Name', validators=[InputRequired(), Length(min=1, max=20)])
    age = StringField('Age', validators=[InputRequired(), Length(min=1, max=3)])
    gender = StringField('Gender', validators=[InputRequired(), Length(min=1, max=10)])
    height = StringField('Height', validators=[InputRequired(), Length(min=1, max=5)])
    location = StringField('Location', validators=[InputRequired(), Length(min=1)])
    education = StringField('Education', validators=[InputRequired(), Length(min=1, max=20)])
    ethnicity = StringField('Ethnicity', validators=[InputRequired(), Length(min=1, max=20)])
    religion = StringField('Religion', validators=[InputRequired(), Length(min=1, max=20)])
    bio = StringField('Bio', validators=[InputRequired(), Length(min=1, max=255)])
    q1 = StringField('Question 1', validators=[InputRequired(), Length(min=15, max=255)])
    q2 = StringField('Question 2', validators=[InputRequired(), Length(min=15, max=255)])
    q3 = StringField('Question 3', validators=[InputRequired(), Length(min=15, max=255)])
    q4 = StringField('Question 4', validators=[InputRequired(), Length(min=15, max=255)])
    q5 = StringField('Question 5', validators=[InputRequired(), Length(min=15, max=255)])
    q6 = StringField('Question 6', validators=[InputRequired(), Length(min=15, max=255)])
    q7 = StringField('Question 7', validators=[InputRequired(), Length(min=15, max=255)])
    q8 = StringField('Question 8', validators=[InputRequired(), Length(min=15, max=255)])
    setup = BooleanField()


# ---------------------------------------------------------------------------------
#   Page Routes
# -------------------------------------------------------------------------------*/

@app.route('/', methods=['GET', 'POST'])
def home():
    register_form = RegisterForm()
    login_form = LoginForm()
    globals()['PREVIOUS_SAVED_ROUTE'] = "welcome.html"

    if current_user.is_authenticated:
        return member()
    else:
        return render_template('welcome.html', register_form=register_form, login_form=login_form)


@app.route('/member', methods=['GET', 'POST'])
@login_required
def member():
    username = current_user.username.title()    # get session based username
    curr_user = Match.query.filter_by(username=username.lower()).first()    # get current user by matching session and Match DB

    # take care of likes / dislikes
    if request.method == "POST":
        like_dislike = request.form['like_dislike']
        liked_user = request.form['liked_user']

        if "like" in like_dislike:
            like = Like(username=curr_user.username, liked_user=liked_user)
            db.session.add(like)
            db.session.commit()

        if "dislike" in like_dislike:
            dislike = Dislike(username=curr_user.username, disliked_user=liked_user)
            db.session.add(dislike)
            db.session.commit()

    # fetch Recommended using Watson algo
    if curr_user:
        highest_match_users = match_users_watson(curr_user)
    else:
        highest_match_users = ""


    # fetch Matched users (mutual likes)
    if curr_user:
        mutual_likes = fetch_mutual_likes(curr_user)
    else:
        mutual_likes = ""
    print mutual_likes

    # take care of matching
    curr_user_table = User.query.filter_by(username=current_user.username).first()
    curr_match_table = Match.query.filter_by(username=current_user.username).first()


    return render_template('member.html', name=current_user.username, highest_match_users=highest_match_users, curr_user_table=curr_user_table, curr_match_table=curr_match_table, mutual_likes=mutual_likes)


@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    match_form = MatchForm()

    # instatiate API for getting Watson data
    personality_results = api.MatchAPI()

    # validate form and upload to match data to DB
    if match_form.validate_on_submit():
        """
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        

        # if user does not select file, browser also
        # submit a empty part without filename
    
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        """
        filename = ""
        file = request.files['image']
        if file and allowed_file(file.filename):
            filename_temp = file.filename.split('.')[1]
            filename = secure_filename(current_user.username + "." + filename_temp)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

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
        results = personality_results.get_personality(personality)

        # extract traits: 0 - 100 scale
        practicality = results['needs'][0]['practicality']
        love = results['needs'][0]['love']
        challenge = results['needs'][0]['challenge']
        challenge = results['needs'][0]['challenge']
        closeness = results['needs'][0]['closeness']
        excitment = results['needs'][0]['excitment']
        structure = results['needs'][0]['structure']

        # extract traits: 1 - 3 scale
        live_music = results['live_music']
        volunteering = results['volunteering']['score']
        entreprenuer = results['entreprenuer']
        gym_member = results['consumption'][0]['gym_member']
        spare_moment_purchases = results['consumption'][0]['spare_of_moment_purchase']
        outdoors = results['consumption'][0]['outdoors']
        reading = results['reading']

        username = current_user.username
        new_match = Match(username=username, view_count=0, name=match_form.name.data, image=filename, \
                          gender=match_form.gender.data, age=match_form.age.data, height=match_form.height.data, \
                          location=match_form.location.data, education=match_form.education.data,
                          ethnicity=match_form.ethnicity.data, \
                          religion=match_form.religion.data, bio=match_form.bio.data, practicality=practicality, \
                          love=love, excitment=excitment, challenge=challenge, \
                          closeness=closeness, structure=structure, live_music=live_music, \
                          spare_moment_purchases=spare_moment_purchases, gym_member=gym_member, \
                          outdoors=outdoors, volunteering=volunteering, \
                          entreprenuer=entreprenuer, reading=reading \
                          )

        db.session.add(new_match)
        db.session.commit()

        # update the setup value
        update = User.query.filter_by(username=username).first()
        update.setup = True
        db.session.merge(update)
        db.session.commit()

        return redirect(url_for('member'))

    # partially repopulate fields
    curr_user_table = User.query.filter_by(username=current_user.username).first()
    if curr_user_table.setup == True:
        curr_match_table = Match.query.filter_by(username=current_user.username).first()
        return render_template('profile.html', name=current_user.username, match_form=match_form, curr_user_table=curr_user_table, curr_match_table=curr_match_table)
    else:
        return render_template('profile.html', name=current_user.username, match_form=match_form, curr_user_table=curr_user_table)


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

@app.route('/admin')
def admin():

    return render_template('admin.html')



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
                flash("Login Successful !")
                return redirect(url_for('member'))
            else:
                login_form.password.errors.append('Incorrect Password')
        else:
            login_form.username.errors.append('Invalid Username')


    previous_route = str(request.referrer.split("/", 2)[2].split('/')[1]) + ".html"

    if previous_route == ".html":
        previous_route = PREVIOUS_SAVED_ROUTE
    elif previous_route == "#.html":
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

    user = User.query.filter_by(username=register_form.username.data).first()
    # email = User.query.filter_by(email=register_form.email.data).first()
    email = User.query.filter_by(email=register_form.email.data.lower()).first()
    print user
    if not user:
        if not email:
            if register_form.validate_on_submit():
                hashed_password = generate_password_hash(register_form.password.data, method='sha256')
                new_user = User(username=register_form.username.data.lower(), email=register_form.email.data.lower(),
                                password=hashed_password, setup=False)
                db.session.add(new_user)
                db.session.commit()

                login_user(new_user)
                flash("Registration Successful !")
                register_form.unique_user = True
                register_form.unique_email = True
                return redirect(url_for('member'))

        else:
            register_form.unique_email = False

    else:
        hashed_password = generate_password_hash(register_form.password.data, method='sha256')
        new_user = User(username=register_form.username.data, email=register_form.email.data, password=hashed_password)
        register_form.unique_user = False

    previous_route = str(request.referrer.split("/", 2)[2].split('/')[1]) + ".html"
    if previous_route == ".html":
        previous_route = PREVIOUS_SAVED_ROUTE
    elif previous_route == "#.html":
        previous_route = PREVIOUS_SAVED_ROUTE
    elif previous_route == "register.html":
        previous_route = PREVIOUS_SAVED_ROUTE
    elif previous_route == "login.html":
        previous_route = PREVIOUS_SAVED_ROUTE
    else:
        globals()['PREVIOUS_SAVED_ROUTE'] = previous_route

    print previous_route
    print PREVIOUS_SAVED_ROUTE

    return render_template(previous_route, register_form=register_form, login_form=login_form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))



# ---------------------------------------------------------------------------------
#   Handling Functions: put in seperate file later for tidyness
# -------------------------------------------------------------------------------*/
def match_users_watson(curr_user):
    highest_match_users = ""
    if curr_user:    # if curr user has made a profile we can match them

        matched_users = {}
        users = Match.query.all()  # get all the match profiles


        for user in users:   # get all uses usernames to store in dict
            username = user.username
            matched_users.update({user.username: []})

        for user in users:   # get all the matches within a range and store in dict against name

            up = user.practicality + 10
            down = user.practicality - 10
            if not curr_user.practicality > up:
                if not curr_user.practicality < down:
                    matched_users[user.username].append({'practicality': user.practicality})

            up = user.love + 10
            down = user.love - 10
            if not curr_user.love > up:
                if not curr_user.love < down:
                    matched_users[user.username].append({'love': user.love})

            up = user.excitment + 10
            down = user.excitment - 10
            if not curr_user.excitment > up:
                if not curr_user.excitment < down:
                    matched_users[user.username].append({'excitment': user.excitment})

            up = user.challenge + 10
            down = user.challenge - 10
            if not curr_user.challenge > up:
                if not curr_user.challenge < down:
                    matched_users[user.username].append({'challenge': user.challenge})

            up = user.closeness + 10
            down = user.closeness - 10
            if not curr_user.closeness > up:
                if not curr_user.closeness < down:
                    matched_users[user.username].append({'closeness': user.closeness})

            up = user.structure + 10
            down = user.structure - 10
            if not curr_user.structure > up:
                if not curr_user.structure < down:
                    matched_users[user.username].append({'structure': user.structure})

            if not curr_user.live_music == 0:
                if not user.live_music == 0:
                   matched_users[user.username].append({'structure': user.live_music})

        # get the number of fields that match for each user
        up = 0
        down = 1000
        for match in matched_users:
            num_match = len(matched_users[match])
            matched_users[match].append({'num_match': num_match})
            if num_match > up:
                up = num_match
            if num_match < down:
                down = num_match


        # return the highest matched users currently set to half of num items that match / 2 + 1
        highest_match_users = []
        match_level = up / 2 -2

        for match in matched_users:    # get the match data to return to member page
            for data in matched_users[match]:

                user_match = 0
                try:
                    user_match = data['num_match']
                except:
                    user_match = 0

                if (user_match >= match_level) & (user_match != curr_user.username):
                    #highest_match_users.append(matched_users[match])

                    user = Match.query.filter_by(username=match).first()

                    highest_match_users.append([
                        {'username': user.username},
                        {'image': user.image},
                        {'name': user.name},
                        {'gender': user.gender},
                        {'age': user.age},
                        {'height': user.height},
                        {'location': user.location},
                        {'education': user.education},
                        {'bio': user.bio}
                    ])
                    break;

    return highest_match_users


def fetch_mutual_likes(curr_user):

    # fetch Matched users (mutual likes)
    mutual_liked_users = {}
    if curr_user:
        likes = Like.query.filter_by(username=curr_user.username)

        if likes:
            for like in likes:
                mutual_likes = Like.query.filter_by(username=like.liked_user)

                if mutual_likes:
                    for mutual in mutual_likes:
                        if curr_user.username in mutual.liked_user:
                            if mutual.username != curr_user.username:
                                mutual_liked_users.update({mutual.username: ""})

    mutual_liked_user_details = []
    for user in mutual_liked_users:
        liked_user_details = Match.query.filter_by(username=user).first()

        mutual_liked_user_details.append([
            {
            'username': user,
            'image': liked_user_details.image,
            'bio': liked_user_details.bio,
            'height': liked_user_details.height,
            'location': liked_user_details.location,
            'education': liked_user_details.education
            }
        ])


    return mutual_liked_user_details



if __name__ == "__main__":
    app.run(debug=True)
