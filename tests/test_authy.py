# test_auth.py
def test_login_page(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/auth' page is accessed
    THEN check that the response is valid and the login form is present
    """
    response = test_client.get('/auth')
    assert response.status_code == 200
    assert b"Login" in response.data
    assert b"Username" in response.data  # Check for form fields