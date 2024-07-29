import pytest

# Test the GET request for the login/registration page
def test_auth_page_get(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/auth' page is accessed via GET
    THEN check that the response is valid and the login form is present
    """
    print("!!!!!!!!!!\n\n")
    print("test client?", test_client)
    print("!!!!!!!!!!\n\n")

    response = test_client.get('/auth')
    print("response??")
    print(response)

    print("\n\n")
    assert response.status_code == 200
    assert b"Login" in response.data
    assert b"Username" in response.data  # Check for the presence of the form field

# Test the POST request for the login functionality
def test_auth_page_post_login(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN a POST request to '/auth' is made with valid login credentials
    THEN check that the redirection is to the correct dashboard based on the user role
    """
    # Assuming default role handling for this example, modify as needed
    response = test_client.post('/auth', data={
        'form_type': 'login',
        'username': 'testuser',
        'password': 'testpass',
        'user_role': 'customer'
    }, follow_redirects=True)
    assert response.status_code == 200
    # Check redirection to the correct dashboard; adjust expected redirect response as necessary
    assert b"Customer Dashboard" in response.data

# Test the POST request for the registration functionality
def test_auth_page_post_register(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN a POST request to '/auth' is made with valid registration data
    THEN check that the user is registered and redirected appropriately
    """
    response = test_client.post('/auth', data={
        'form_type': 'register',
        'fullname': 'New User',
        'email': 'newuser@example.com',
        'username': 'newuser',
        'password': 'newpass',
        'phone': '1234567890',
        'user_role': 'customer'
    }, follow_redirects=True)
    assert response.status_code == 200
    # Check for registration success message
    assert b"Registration successful. Please log in." in response.data

