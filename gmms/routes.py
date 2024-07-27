from gmms import app
from flask import render_template, request, redirect, url_for

# Dummy user data for demonstration purposes
users = {
    'username': 'password'  # Replace this with actual user validation logic
}

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/customer')
def customer():
    return render_template("customer.html")

@app.route('/technician')
def technician():
    return render_template("technician.html")

@app.route('/approver')
def approver():
    return render_template("approver.html")

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/CustomerDashboard')
def customer_dashboard():
    return render_template("CustomerDashboard.html")

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # Check if user exists in the users dictionary and password matches
    if users.get(username) == password:
        return redirect(url_for('customer_dashboard'))
    else:
        return redirect(url_for('register'))

if __name__ == '__main__':
    app.run(debug=True)
