import unittest
from flask_testing import TestCase
from app import app, db
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user


class TestUser(UserMixin, db.Model):
    __tablename__ = 'TestUser'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))
    setup = db.Column(db.Boolean())
    activated = db.Column(db.Boolean())


class BaseTestCase(TestCase):
    """A base test  case."""

    # return the flask instance
    def create_app(self):
        # establishes our test configuration
        app.config.from_object('config.TestConfig')
        return app

    # create all our database tables before each test
    def setUp(self):
        db.create_all()
        # db.session.add
        test_user = TestUser(id=1, username='TestUser', email='TestUser@gmail.com', password='password', setup=True, activated=False)
        db.session.add(test_user)
        db.session.commit()

    # delete all tables at the end of every test
    def tearDown(self):
        db.session.remove()
        db.drop_all()


# based on the above, each test will be run on a clean database
class FlaskTestCase(BaseTestCase):

    # ensure that flask was set up correctly
    def test_index(self):

        # what we used to create the test
        # mocking out functionality of current app
        # isolated app to send request to and test the response out of scope of main app


        # test response of login route
        response = self.client.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # ensure that login page loads correctly
    # need to know that the actual data shown is loaded
    def test_login_page_loads(self):

        response = self.client.get('/login', content_type='html/text')
        self.assertTrue(b'LOGIN' in response.data)
        self.assertEqual(response.status_code, 200)

    # test other main pages
    def test_help_page(self):

        response = self.client.get('/help', content_type='html/text')
        self.assertTrue(b'Help' in response.data)
        self.assertEqual(response.status_code, 200)

    def test_tnc_page(self):

        response = self.client.get('/terms', content_type='html/text')
        self.assertTrue(b'Terms' in response.data)
        self.assertEqual(response.status_code, 200)

    def test_privacy_page(self):

        response = self.client.get('/terms', content_type='html/text')
        self.assertTrue(b'Privacy' in response.data)
        self.assertEqual(response.status_code, 200)

    def test_aboutus_page(self):

        response = self.client.get('/about', content_type='html/text')
        self.assertTrue(b'Privacy' in response.data)
        self.assertEqual(response.status_code, 200)

    # ensure that login behaves correctly given the correct credentials
    # def test_correct_login(self):
    #
    #     response = self.client.post('/login', data=dict(username='TestUser', password='password'),
    #                            follow_redirects=True)
    #     self.assertIn(b'Profile', response.data)

    def login(self, username, password):
        return self.client.post('/login', data=dict(username=username,
                                                    password=password
                                                    ), follow_redirects=True)

    def logout(self):
        return self.client.get('/logout', follow_redirects=True)

    def test_login_logout(self):
        rv = login_user('TestUser')
        assert b'Profile' in rv.data
        rv = self.logout()
        assert b'Register' in rv.data
        # rv = self.login('TestUserx', 'password')
        # assert b'Invalid Username' in rv.data
        # rv = self.login('TestUser', 'passwordx')
        assert b'Incorrect Password' in rv.data

    # # ensure that login behaves correctly given the incorrect credentials
    #
    # def test_correct_login(self):
    #
    #     response = self.client.post('/login', data=dict(username="hello", password="password"),
    #                            follow_redirects=True)
    #     self.assertIn(b'Username: Invalid Username', response.data)
    # ensure logout behaves correctly

if __name__ == '__main__':
    unittest.main()