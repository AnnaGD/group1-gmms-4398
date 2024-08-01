# main.py
from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from gmms.models import db
from gmms.models.work_request import WorkRequest

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template("index.html")

@main_bp.route('/customer_dashboard', methods=["GET", "POST"])
def customer_dashboard():
    # Check if the user is logged in by examining session data
    if "customer" not in session:
        flash("Please log in to access the dashboard.")
        return redirect(url_for('auth.auth'))
    
    # Handle POST request: when a user submits a new work request via the dashboard form
    if request.method == "POST":
        # Extract data from form fields based on the model definition in work_request.py
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        department = request.form.get('department', '')  # Optional, provide default as empty string
        equipment_id = request.form.get('equipment_id', '')  # Optional, provide default as empty string
        description = request.form['description']

        # Create a new WorkRequest object and populate it with data from the form
        new_request = WorkRequest(
            first_name=first_name,
            last_name=last_name,
            email=email,
            department=department,
            equipment_id=equipment_id,
            description=description
        )
        db.session.add(new_request)  # Add the new request to the database session
        db.session.commit()  # Commit the transaction to save it to the database
        
        # Notify the user that their request was submitted successfully
        flash("Work request submitted successfully.")
        return redirect(url_for('main.customer_dashboard'))
    
    # For GET requests or after handling POST, render the customer dashboard template
    return render_template("CustomerDashboard.html")

@main_bp.route('/technician_dashboard')
def technician_dashboard():
    if "technician" not in session:
        flash("Please log in to access the dashboard.")
        return redirect(url_for('auth.auth'))
    return render_template("TechnicianDashboard.html")

@main_bp.route('/approver_dashboard')
def approver_dashboard():
    if "approver" not in session:
        flash("Please log in to access the dashboard.")
        return redirect(url_for('auth.auth'))
        # retreive from the db
    pending_work_orders = WorkRequest.query.all()
    print("Workorder: ", pending_work_orders)
    return render_template("ApproverDashboard.html", pending_work_orders=pending_work_orders)
