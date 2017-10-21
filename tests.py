from app import app
import unittest


class FlaskTestCase(unittest.TestCase):

    # ensure that flask was set up correctly
    def test_index(self):

        # what we used to create the test
        # mocking out functionality of current app
        # isolated app to send request to and test the response out of scope of main app
        tester = app.test_client(self)

        # test response of login route
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # ensure that login page loads correctly
    # need to know that the actual data shown is loaded
    def test_login_page_loads(self):

        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertTrue(b'LOGIN' in response.data)



    # ensure that login behaves correctly given the correct credentials
    # def test_correct_login(self):
    #     tester = app.test_client(self)
    #     response = tester.post('/login', data=dict(username="hello", password="password"),
    #                            follow_redirects=True)
    #     self.assertIn(b'ADMIN', response.data)
    #
    # # ensure that login behaves correctly given the incorrect credentials
    #
    # def test_correct_login(self):
    #     tester = app.test_client(self)
    #     response = tester.post('/login', data=dict(username="hello", password="password"),
    #                            follow_redirects=True)
    #     self.assertIn(b'Username: Invalid Username', response.data)
    # ensure logout behaves correctly

if __name__ == '__main__':
    unittest.main()