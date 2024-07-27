from flask import Blueprint, render_template, request, redirect, url_for, session, flash

login_bp = Blueprint('login', __name__)

users = {
    'customer': 'password',  # Replace with actual validation logic
    'approver': 'password',
    'technician': 'password'
}

@login_bp.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        if users.get(username) == password:
            session.permanent = True  # Set the session as permanent
            session["customer"] = username
            return redirect(url_for('customer.customer'))
        else:
            flash("Invalid credentials, please register.")
            return redirect(url_for('register.register'))
    return render_template("login.html")
