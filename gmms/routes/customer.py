# customer.py
from flask import Blueprint, render_template, request, flash, redirect, url_for
from gmms.models import db
from gmms.models.work_request import WorkRequest

customer_bp = Blueprint('customer', __name__)

@customer_bp.route('/customer', methods=["GET"])
def customer_dashboard():
    return render_template("CustomerDashboard.html")

@customer_bp.route('/customer/submit_request', methods=["POST"])
def submit_request():
    if request.method == "POST":
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        department = request.form['department']
        equipment_id = request.form['equipment_id']
        description = request.form['description']

        # Create a new WorkRequest entry
        work_request = WorkRequest(
            first_name=first_name,
            last_name=last_name,
            email=email,
            department=department,
            equipment_id=equipment_id,
            description=description
        )
        db.session.add(work_request)
        db.session.commit()

        flash("Your request has been submitted!", "success")
        return redirect(url_for('customer.customer_dashboard'))
