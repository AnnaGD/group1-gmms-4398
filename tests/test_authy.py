import pytest

# Test the GET request for the login/registration page
def test_auth_page_get(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/auth' page is accessed via GET
    THEN check that the response is valid and the login form is present
    """
    print("test client?", test_client)

    response = test_client.get('/auth')
    print("response??")
    print(response)

    print("\n\n")
    assert response.status_code == 200
    assert b"Login" in response.data
    assert b"Username" in response.data  # Check for the presence of the form field

# Test the POST request for the login functionality
#def test_auth_page_post_login(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN a POST request to '/auth' is made with valid login credentials
    THEN check that the redirection is to the correct dashboard based on the user role
    """
    """# Create a test user in the database
    test_client = Customer(user_role='customer', username='testuser', password='testpass')
    #db_session.add(test_user)
    #db_session.commit()

    response = test_client.post('/auth', data={
        'form_type': 'login',
        'user_role': 'customer',
        'username': 'testuser',
        'password': 'testpass'
    }, follow_redirects=True)
    
    assert response.status_code == 200
    assert b"Customer Dashboard" in response.data
    print("test_auth_page_post_login:", response.data)"""

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

