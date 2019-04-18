import unittest

from datetime import date

from flask_testing import TestCase
from flask_login import current_user

from project import app, db
from project.models import User, FeatureRequest




class BaseTestCase(TestCase):
    """A base test case."""


    def create_app(self):
        app.config["DEBUG"] = True
        app.config["TESTING"] = True
        app.config["WTF_CSRF_ENABLED"] = False
        app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///:memory:'
        return app

    def setUp(self):
        db.create_all()
        user = User("stevejobs", "stevejobs@iws.com", "stevejobs")
        request = FeatureRequest("Test request 1", "This is a test request",
                                 "Client A", 1, date.today(), "Billing", "1")
        db.session.add(user)
        db.session.add(request)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class AppTestCase(BaseTestCase):

    # Ensure that FlaskApp was set up correctly
    def test_app_load(self):
        response = self.client.get('/', content_type='html/text')
        assert response.status_code == 200

class UserAuthenticationTests(BaseTestCase):

    # Ensure that the login page loads correctly
    def test_login_page_loads(self):
        response = self.client.get('/')
        assert b'Please sign in' in response.data

    # Ensure login behaves correctly with correct credentials
    def test_correct_login(self):
        with self.client:
            response = self.client.post(
                '/',
                data=dict(username="stevejobs", password="stevejobs"),
                follow_redirects=True
            )
            assert response.status_code == 200
            assert b'Login successful' in response.data
            assert current_user.username == "stevejobs"
            assert current_user.is_active()

    # Ensure login behaves correctly with incorrect credentials
    def test_incorrect_login(self):
        response = self.client.post(
            '/',
            data=dict(username="wrong", password="wrong"),
            follow_redirects=True
        )
        assert b'Invalid username or password.' in response.data

    # Ensure logout behaves correctly
    def test_logout(self):
        with self.client:
            self.client.post(
                '/',
                data=dict(username="stevejobs", password="stevejobs"),
                follow_redirects=True
            )
            response = self.client.get('/logout', follow_redirects=True)
            assert b'Please sign in' in response.data
            assert current_user.is_active is False

    # Ensure that logout page requires user login
    def test_logout_route_requires_login(self):
        response = self.client.get('/logout', follow_redirects=True)
        assert b'Please sign in' in response.data


class HomeViewsTests(BaseTestCase):

    # Ensure that homepage requires user login
    def test_homepage_requires_login(self):
        response = self.client.get('/home', follow_redirects=True)
        assert b'Please sign in' in response.data

    # Ensure that homepage deplays feature request form and list
    def test_home_page_displays_form_and_list(self):
        self.client.post(
            '/',
            data=dict(username="stevejobs", password="stevejobs"),
            follow_redirects=True
        )
        response = self.client.get('/home')
        assert b'Feature Request Form' in response.data
        assert b'Test request' in response.data

    # Ensure that homepage form captures data and display list correctly
    def test_request_form_captures_data(self):
        self.client.post(
            '/',
            data=dict(username="stevejobs", password="stevejobs"),
            follow_redirects=True
        )
        response = self.client.post(
            '/home',
            data= dict(title="Test request 2", description="This is a test request",
                                     client="Client A", client_priority=1, target_date=date.today(),product_area="Billing"),
            follow_redirects=True
        )
        assert b"Test request 1" in response.data
        assert b"Your Feature Request has been Added!" in response.data
        assert FeatureRequest.query.filter_by(id=1).first().client_priority == 2
        assert response.status == "200 OK"

    def test_target_date_validates(self):
        self.client.post(
            '/',
            data=dict(username="stevejobs", password="stevejobs"),
            follow_redirects=True
        )
        response = self.client.post(
            '/home',
            data=dict(title="Test request 2", description="This is a test request",
                                     client="Client A", client_priority=1, target_date=date(2019, 1, 1),product_area="Billing"),
            follow_redirects=True
        )
        assert b'Date should be greater than today' in response.data

class DetailViewsTests(BaseTestCase):
    # Ensure that Detail View functions
    def test_detail_view(self):
        self.client.post(
            '/',
            data=dict(username="stevejobs", password="stevejobs"),
            follow_redirects=True
        )
        self.client.post(
            '/home',
            data= dict(title="Test request 2", description="This is a test request",
                                     client="Client A", client_priority=1, target_date=date.today(),product_area="Billing"),
            follow_redirects=True
        )
        response = self.client.get('/request/2')
        assert response.status == "200 OK"
        assert b"Test request 2" in response.data


    # Ensure that Detail View updates
    def test_detail_view_updates(self):
        self.client.post(
            '/',
            data=dict(username="stevejobs", password="stevejobs"),
            follow_redirects=True
        )
        self.client.post(
            '/home',
            data= dict(title="Test request 2", description="This is a test request",
                                     client="Client A", client_priority=1, target_date=date.today(),product_area="Billing"),
            follow_redirects=True
        )
        response = self.client.post('/request/2', data= dict(title="Test request Updated", description="This is a test request",
                                 client="Client A", client_priority=1, target_date=date.today(),product_area="Billing"),
        follow_redirects=True)
        assert response.status == "200 OK"
        assert b"Your Feature Request has been updated!" in response.data
        assert b"Test request Updated" in response.data

    # Ensure that Detail View deletes
    def test_detail_view_delete(self):
        self.client.post(
            '/',
            data=dict(username="stevejobs", password="stevejobs"),
            follow_redirects=True
        )
        self.client.post(
            '/home',
            data= dict(title="Test request 2", description="This is a test request",
                                     client="Client A", client_priority=1, target_date=date.today(),product_area="Billing"),
            follow_redirects=True
        )
        response = self.client.post('/request/2/delete', follow_redirects=True)
        assert response.status == "200 OK"
        assert b"Your request has been deleted!" in response.data
        assert b"Test request 2" not in response.data


if __name__ == '__main__':
    unittest.main()
