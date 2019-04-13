import unittest

from datetime import datetime

from flask_testing import TestCase
from flask_login import current_user

from project import app, db
from project.models import User, FeatureRequest


class BaseTestCase(TestCase):
    """A base test case."""

    def create_app(self):
        app.config.from_object('config.TestConfig')
        return app

    def setUp(self):
        db.create_all()
        request = FeatureRequest("Test request", "This is a test request",
                                 "Client A", 1, datetime.utcnow(), "Billing", "stevejobs")
        user = User("stevejobs", "stevejobs@iws.com", "stevejobs")
        db.session.add(request)
        db.session.add(user)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class AppTestCase(BaseTestCase):

    # Ensure that FlaskApp was set up correctly
    def test_home(self):
        response = self.client.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure that main page requires user login
    def test_main_route_requires_login(self):
        response = self.client.get('/', follow_redirects=True)
        self.assertIn(b'Please sign in', response.data)

    # Ensure that feature request title show up on the home page
    def test_request_title_show_up_on_home_page(self):
        response = self.client.post(
            '/login',
            data=dict(username="stevejobs", password="stevejobs"),
            follow_redirects=True
        )
        self.assertIn(b'Test request', response.data)


class UserViewsTests(BaseTestCase):

    # Ensure that the login page loads correctly
    def test_login_page_loads(self):
        response = self.client.get('/login')
        self.assertIn(b'Please sign in', response.data)

    # Ensure login behaves correctly with correct credentials
    def test_correct_login(self):
        with self.client:
            response = self.client.post(
                '/login',
                data=dict(username="stevejobs", password="stevejobs"),
                follow_redirects=True
            )
            self.assertIn(b'Login successful', response.data)
            self.assertTrue(current_user.username == "stevejobs")
            self.assertTrue(current_user.is_active())

    # Ensure login behaves correctly with incorrect credentials
    def test_incorrect_login(self):
        response = self.client.post(
            '/login',
            data=dict(username="wrong", password="wrong"),
            follow_redirects=True
        )
        self.assertIn(b'Invalid username or password.', response.data)

    # Ensure logout behaves correctly
    def test_logout(self):
        with self.client:
            self.client.post(
                '/login',
                data=dict(username="stevejobs", password="stevejobs"),
                follow_redirects=True
            )
            response = self.client.get('/logout', follow_redirects=True)
            self.assertIn(b'Please sign in', response.data)
            self.assertFalse(current_user.is_active)

    # Ensure that logout page requires user login
    def test_logout_route_requires_login(self):
        response = self.client.get('/logout', follow_redirects=True)
        self.assertIn(b'Please sign in', response.data)


if __name__ == '__main__':
    unittest.main()
