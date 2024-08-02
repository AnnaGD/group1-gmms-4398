from gmms.models.approver import Approver
from gmms.models.work_request import WorkRequest
from gmms import db

def test_new_approvr_registration(test_client):
    # create test data to assert db after POST
    form_type ='register'
    fullname = 'New User'
    email = 'newuser@example.com'
    username = 'newuser'
    password = 'newpass'
    phone = '1234567890'
    user_role = 'approver'

    # ensure user doesn't exist in db
    user = Approver.query.filter_by(username=username, password=password).first()
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
    
    user = Approver.query.filter_by(username=username, password=password).first()

    # assert user exists
    assert user is not None

    assert user.fullname == fullname
    assert user.email == email
    assert user.username == username
    assert user.password == password
    assert user.phone == phone


# def test_approver_access_control(test_client):
#     # Test access without login
#     response = test_client.get('/approver_dashboard', follow_redirects=True)
#     assert response.status_code == 403  # Checking for unauthorized response
#     print("Response: ", response.headers)
#     assert '/auth' in response.headers['Location']  # Check if redirecting to login

#     # Test access with non-approver session
#     with test_client.session_transaction() as session:
#         session['customer'] = 'customerUser'  # Assuming 'customer' role is for non-approvers
    
#     response = test_client.get('/approver_dashboard', follow_redirects=True)
#     assert response.status_code == 403
#     assert b"Please log in as an approver." in response.data

#     # Test access with approver session
#     with test_client.session_transaction() as session:
#         session['approver'] = 'approverUser'  # Correct role for access
    
#     response = test_client.get('/approver_dashboard')
#     assert response.status_code == 200  # Assumes there is some data or at least a valid template to render


def test_approve_work_order(test_client):
    # Set up a work order with pending status
    new_order = WorkRequest(
        first_name="Harry",
        last_name="Potter",
        email="seeker@mail.com",
        department="Quidditch Equipment",
        equipment_id="Nimbus2000",
        description="Loses speed after 30 minutes of flight",
        status="pending"
    )
    db.session.add(new_order)
    db.session.commit()

    # Set the approver session correctly
    with test_client.session_transaction() as session:
        session['approver'] = 'true'  # Assuming this is the correct key and value

    # Attempt to approve the work order
    response = test_client.post(f'/approver/approve/{new_order.id}', follow_redirects=True)

    # Ensure the response is successful
    assert response.status_code == 200
    assert b"Work order approved successfully" in response.data

    # Refresh the instance to see if it was updated
    db.session.refresh(new_order)
    assert new_order.status == 'approved'

    # Cleanup after test
    db.session.delete(new_order)
    db.session.commit()