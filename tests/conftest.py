# conftest.py
import pytest
from gmms import create_app
from gmms.models import db

@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app('testing')  # You might need to adjust this based on how your `create_app` is structured

    # Flask provides a way to test your application by exposing the Werkzeug test Client
    testing_client = flask_app.test_client()

    # Establish an application context before running the tests.
    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client  # this is where the testing happens!

    ctx.pop()