from flask import Blueprint, render_template, jsonify, session, redirect, url_for, flash
from gmms.models.work_request import WorkRequest
from gmms.models import db

technician_bp = Blueprint('technician', __name__)

@technician_bp.route('/technician_dashboard', methods=["GET"])
def technician_dashboard():
    """
    Display the technician dashboard with all approved work orders.

    This endpoint checks if a user is logged in as a technician and displays their dashboard.
    If not logged in, it redirects to the login page.

    Returns:
        Rendered template: 'TechnicianDashboard.html' with a list of approved work orders if logged in.
        Redirect: to the authentication page if the user is not logged in as a technician.
    """
    if 'technician' not in session:
        flash("Please log in as a technician.", "danger")
        return redirect(url_for('auth.auth'))

    approved_work_orders = WorkRequest.query.filter_by(status='approved').all()
    return render_template("TechnicianDashboard.html", approved_work_orders=approved_work_orders)

@technician_bp.route('/technician/work_order/<int:work_order_id>', methods=["GET"])
def get_work_order(work_order_id):
    """
    Fetch and return JSON data for a specific work order based on its ID.

    Args:
        work_order_id (int): The ID of the work order to retrieve.

    Returns:
        JSON response: Details of the work order if found, including first name, last name, email, etc.
        JSON response: Error message with a status code of 404 if the work order is not found.
    """
    work_order = WorkRequest.query.get(work_order_id)
    if work_order:
        return jsonify({
            'first_name': work_order.first_name,
            'last_name': work_order.last_name,
            'email': work_order.email,
            'department': work_order.department,
            'equipment_id': work_order.equipment_id,
            'description': work_order.description,
            'comment_section': work_order.comment_section
        })
    else:
        return jsonify({'error': 'Work order not found'}), 404
    
@technician_bp.route('/technician/complete/<int:work_order_id>', methods=["POST"])
def approve_work_order(work_order_id):
    """
    Complete a specified work order by its ID and update its status in the database.

    Args:
        work_order_id (int): The ID of the work order to mark as complete.

    Returns:
        JSON response: Success message if the work order is marked as complete.
        JSON response: Error message with a status code of 404 if the work order is not found.
    """
    work_order = WorkRequest.query.get(work_order_id)
    if work_order:
        work_order.status = 'complete'
        db.session.commit()
        return jsonify({'message': 'Work order completed successfully'})
    return jsonify({'error': 'Work order not found'}), 404