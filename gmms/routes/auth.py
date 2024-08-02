from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from gmms.models.customer import Customer, db
from gmms.models.technician import Technician
from gmms.models.approver import Approver

# Create a Blueprint named 'auth' for the authentication part of the application
auth_bp = Blueprint('auth', __name__)

# Define a route for authentication which handles both GET and POST requests
@auth_bp.route('/auth', methods=["GET", "POST"])
def auth():
    """
    Handle user authentication, including both login and registration.

    This endpoint supports both GET and POST requests. GET requests return
    the authentication page, whereas POST requests process submitted forms
    for either logging in or registering new users.

    Returns:
        On POST:
            Redirects to the appropriate dashboard if login is successful.
            Returns an error message and redirects back to the auth page if login or registration fails.
        On GET:
            Renders and returns the authentication page template.

    Raises:
        HTTP 403: Returns an HTTP Forbidden status if login credentials are invalid.
        HTTP 409: Returns an HTTP Conflict status if the registration username is already taken.
    """
    if request.method == "POST": # Check if the current request is a POST request
        form_type = request.form['form_type'] # Get the type of form submitted ('login' or 'register')
        username = request.form['username'] # Retrieve username from form data
        password = request.form['password'] # Retrieve password from form data
        user_role = request.form.get('user_role')  # Retrieve the role of the user (customer, technician, approver)

        if form_type == 'login':
            # Login logic: Depending on the user role, query the appropriate table
            if user_role == 'customer':
                user = Customer.query.filter_by(username=username, password=password).first()
                dashboard = 'customer.customer_dashboard'
            elif user_role == 'technician':
                user = Technician.query.filter_by(username=username, password=password).first()
                dashboard = 'technician.technician_dashboard'
            elif user_role == 'approver':
                user = Approver.query.filter_by(username=username, password=password).first()
                dashboard = 'approver.approver_dashboard'

            if user:
                session[user_role] = user.username # Store user info in session for persistence across requests
                return redirect(url_for(dashboard)) # Redirect to the appropriate dashboard
            else:
                flash("Invalid credentials, please register.")
                return redirect(url_for('auth.auth'))

        elif form_type == 'register':
            # Registration logic: Check if the username already exists and handle new user registration
            fullname = request.form['fullname']
            email = request.form['email']
            phone = request.form['phone']

            # Similar logic for different user roles
            if user_role == 'customer':
                existing_user = Customer.query.filter_by(username=username).first()
                if existing_user:
                    flash("Username already exists. Please choose a different one.")
                    return redirect(url_for('auth.auth'), 409)
                new_user = Customer(fullname=fullname, email=email, username=username, password=password, phone=phone)
            elif user_role == 'technician':
                existing_user = Technician.query.filter_by(username=username).first()
                if existing_user:
                    flash("Username already exists. Please choose a different one.")
                    return redirect(url_for('auth.auth'))
                new_user = Technician(fullname=fullname, email=email, username=username, password=password, phone=phone)
            elif user_role == 'approver':
                existing_user = Approver.query.filter_by(username=username).first()
                if existing_user:
                    flash("Username already exists. Please choose a different one.")
                    return redirect(url_for('auth.auth'))
                new_user = Approver(fullname=fullname, email=email, username=username, password=password, phone=phone)

            db.session.add(new_user) # Add new user to the database
            db.session.commit() # Commit changes to the database
            flash("Registration successful. Please log in.") # Show success message
            return redirect(url_for('auth.auth'))

    return render_template("auth.html") # Render the authentication template for GET requests
