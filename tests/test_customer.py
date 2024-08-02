import pytest
from gmms.models.customer import Customer
from gmms.models.work_request import WorkRequest

def test_new_customer_registration(test_client):
    # create test data to assert db after POST
    form_type ='register'
    fullname = 'New User'
    email = 'newuser@example.com'
    username = 'newuser'
    password = 'newpass'
    phone = '1234567890'
    user_role = 'customer'

    # ensure user doesn't exist in db
    user = Customer.query.filter_by(username=username, password=password).first()
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
    
    user = Customer.query.filter_by(username=username, password=password).first()

    # assert user exists
    assert user is not None

    assert user.fullname == fullname
    assert user.email == email
    assert user.username == username
    assert user.password == password
    assert user.phone == phone

def test_duplicate_customer_registration_fails(test_client):
    # retrieve customer from db
    form_type ='register'
    username = 'newuser'
    password = 'newpass'
    user_role = 'customer'
    user = Customer.query.filter_by(username=username, password=password).first()
    assert user is not None

    # register duplicate customer
    response = test_client.post('/auth', data={
        'form_type': form_type,
        'fullname': user.fullname,
        'email': user.email,
        'username': user.username,
        'password': user.password,
        'phone': user.phone,
        'user_role': user_role,
    }, follow_redirects=True)
    assert response.status_code == 409



def test_customer_submits_ticket(test_client):

    # create test data to assert db after POST
    first_name = "Harry"
    last_name = "Potter"
    email = "seeker@mail.com"
    department = "Quidditch Equipment"
    equipment_id = "Nimbus200"
    description = "Looses speed after 30 minutes of flight"

    # ensure no existing order with the same details
    order = WorkRequest.query.filter_by(email=email, equipment_id=equipment_id).first()
    assert order is None

    # simulate user login
    with test_client.session_transaction() as session:
        session['customer'] = 'HarryPotter'  # assuming a session key for logged in customers

    # submit a new work request
    response = test_client.post('/customer_dashboard', data={
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'department': department,
        'equipment_id': equipment_id,
        'description': description,
    }, follow_redirects=True)
    
    assert response.status_code == 200

    # Check for success message in response
    assert b"Work request submitted successfully." in response.data

    # validate that the order has been added to the database
    order = WorkRequest.query.filter_by(email=email, equipment_id=equipment_id).first()
    assert order is not None
    assert order.first_name == first_name
    assert order.last_name == last_name
    assert order.department == department
    assert order.description == description
    assert order.status == "pending"  # Ensuring the default status is set correctly