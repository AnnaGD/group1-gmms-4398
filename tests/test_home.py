# test_home.py

def test_redirect_to_login(test_client):
    """
    GIVEN a Flask application
    WHEN the URL '/auth?form_type=login' is accessed directly (simulating a click)
    THEN check that the response is the expected login page
    """
    response = test_client.get('/auth?form_type=login', follow_redirects=True)
    assert response.status_code == 200
    assert b"Login" in response.data  # Assuming 'Login' is prominently featured on the page
    print(response.data)