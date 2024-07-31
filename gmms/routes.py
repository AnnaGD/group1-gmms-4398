from gmms import create_app
from flask import render_template, request, redirect, url_for

# Dummy user data for demonstration purposes.
# NOTE: This should be replaced with a more secure authentication mechanism for production.
users = {
    'username': 'password'  # This is a placeholder. Ideally, passwords should not be stored in plain text.
}

# Route to the main index page
@create_app.route('/')
def index():
    return render_template("index.html")

@create_app.route('/customer')
def customer():
    return render_template("customer.html")

@create_app.route('/technician')
def technician():
    return render_template("technician.html")

@create_app.route('/approver')
def approver():
    return render_template("approver.html")

@create_app.route('/register')
def register():
    return render_template("register.html")

@create_app.route('/CustomerDashboard')
def customer_dashboard():
    return render_template("CustomerDashboard.html")

# Route for handling login functionality, accepts only POST requests
@create_app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # Authenticate the user based on username and password
    # Checks if user exists in the users dictionary and password matches
    if users.get(username) == password:
        return redirect(url_for('customer_dashboard')) # Redirect to dashboard if successful
    else:
        return redirect(url_for('register')) # Redirect to registration if login fails

if __name__ == '__main__':
    create_app.run(debug=True) # Run the server with debug mode enabled
