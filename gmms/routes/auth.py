from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from gmms.models.customer import Customer, db
from gmms.models.technician import Technician
from gmms.models.approver import Approver

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/auth', methods=["GET", "POST"])
def auth():
    if request.method == "POST":
        form_type = request.form['form_type']
        username = request.form['username']
        password = request.form['password']
        user_role = request.form.get('user_role')  # Added to capture the role

        if form_type == 'login':
            if user_role == 'customer':
                user = Customer.query.filter_by(username=username, password=password).first()
                dashboard = 'main.customer_dashboard'
            elif user_role == 'technician':
                user = Technician.query.filter_by(username=username, password=password).first()
                dashboard = 'main.technician_dashboard'
            elif user_role == 'approver':
                user = Approver.query.filter_by(username=username, password=password).first()
                dashboard = 'main.approver_dashboard'

            if user:
                session[user_role] = user.username
                return redirect(url_for(dashboard))
            else:
                flash("Invalid credentials, please register.")
                return redirect(url_for('auth.auth'))

        elif form_type == 'register':
            fullname = request.form['fullname']
            email = request.form['email']
            phone = request.form['phone']

            if user_role == 'customer':
                existing_user = Customer.query.filter_by(username=username).first()
                if existing_user:
                    flash("Username already exists. Please choose a different one.")
                    return redirect(url_for('auth.auth'))
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

            db.session.add(new_user)
            db.session.commit()
            flash("Registration successful. Please log in.")
            return redirect(url_for('auth.auth'))

    return render_template("auth.html")
