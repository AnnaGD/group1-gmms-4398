from flask import url_for
from flask.testing import FlaskClient
from flask_sqlalchemy import SQLAlchemy
from gmms import app
from gmms.models import db as database
import unittest

class TestCustomer(unittest.TestCase):
    #TESTING = True
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    #SQLALCHEMY_TRACK_MODIFICATIONS = False

    def setUp(self):
        self.ctx = app.app_context()
        self.ctx.push()
        self.client = app.test_client()

    def tearDown(self):
        self.ctx.pop()

    def test_customer_redirected_ifnot_loggedin(self):
        data={
            'title': 'Test Title',
            'description': 'Test Description'
        }

        response = self.client.post('/customer_dashboard', data, follow_redirects=True)

        self.assertRedirects(response, url_for('auth.auth'))
        assert response.status_code == 200
        assert "POST method called" == response.get_data(as_text=True)

if __name__ == "__main__":
    TestCustomer.setUp()