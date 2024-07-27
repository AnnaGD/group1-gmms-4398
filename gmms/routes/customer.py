from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from gmms.models.customer import Customer, db

customer_bp = Blueprint('customer', __name__)

@customer_bp.route('/customer', methods=["POST", "GET"])
def customer():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        
        customer = Customer.query.filter_by(username=username, password=password).first()
        if customer:
            session['customer'] = customer.username
            return redirect(url_for('main.WorkRequest'))
        else:
            flash("Invalid credentials, please register.")
            return redirect(url_for('register.register'))
    return render_template("customer.html")
