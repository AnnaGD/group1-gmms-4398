from gmms.models.technician import Technician
from gmms.models.work_request import WorkRequest

def test_new_approvr_registration(test_client):
    # create test data to assert db after POST
    form_type ='register'
    fullname = 'New User'
    email = 'newuser@example.com'
    username = 'newuser'
    password = 'newpass'
    phone = '1234567890'
    user_role = 'technician'

    # ensure user doesn't exist in db
    user = Technician.query.filter_by(username=username, password=password).first()
    assert user is None

    # register new customer
    response = test_client.post('/auth', data={
        'form_type': form_type,
        'fullname': fullname,
        'email': email,
        'username': username,
        'password': password,
        'phone': phone,
        'user_role': user_role,
    }, follow_redirects=True)
    assert response.status_code == 200

    # Check for registration success message
    assert b"Registration successful. Please log in." in response.data
    
    user = Technician.query.filter_by(username=username, password=password).first()

    # assert user exists
    assert user is not None

    assert user.fullname == fullname
    assert user.email == email
    assert user.username == username
    assert user.password == password
    assert user.phone == phone