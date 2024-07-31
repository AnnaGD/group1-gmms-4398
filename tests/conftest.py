# conftest.py
import pytest
from gmms import create_app
from gmms.models import db

@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app('testing') 

    # Flask provides a way to test the application by exposing the Werkzeug test Client
    testing_client = flask_app.test_client()

    # Establish an application context before running the tests.
    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client

    ctx.pop()