import unittest
from flask import Flask, session, template_rendered, url_for
from flask_testing import TestCase
from contextlib import contextmanager
from gmms import app, db  # Import your Flask app and db object
from gmms.models import WorkRequest  # Import model

class TestFlaskRoutes(TestCase):
    def create_app(self):
        # Configure your Flask app for testing
        # app = create_app('testing')
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Use in-memory database for tests
        app.config['WTF_CSRF_ENABLED'] = False  # Disable CSRF forms protection in testing
        return app

    def login(self):
        with self.client.session_transaction() as sess:
            sess['customer'] = "TestCustomer"  # Simulate customer logged in with username "TestCustomer"

    def test_customer_redirected_ifnot_loggedin(self):
        data={
            'title': 'Test Title',
            'description': 'Test Description'
        }

        response = self.client.post('/customer_dashboard', data, follow_redirects=True)

        self.assertRedirects(response, url_for('auth.auth'))


    def test_post_customer_dashboard(self):
        # Log in before testing POST
        self.login()
        
        # Create Test form data
        data={
            'title': 'Test Title',
            'description': 'Test Description'
        }

        response = self.client.post('/customer_dashboard', data, follow_redirects=True)

        # Check if the response is correct
        self.assertRedirects(response, url_for('main.customer_dashboard'))
        self.assertTrue(b"Work request submitted successfully." in response.data)

        # Verify that data was written to the database
        work_request = WorkRequest.query.first()
        self.assertIsNotNone(work_request)
        self.assertEqual(work_request.title, 'Test Title')
        self.assertEqual(work_request.description, 'Test Description')

if __name__ == '__main__':
    unittest.main()
