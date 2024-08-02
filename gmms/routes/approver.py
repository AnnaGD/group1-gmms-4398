from flask import Blueprint, render_template, jsonify, session, redirect, url_for, flash, request
from gmms.models.work_request import WorkRequest
from gmms.models import db

approver_bp = Blueprint('approver', __name__)

@approver_bp.route('/approver_dashboard', methods=["GET"])
def approver_dashboard():
    """
    Serve the dashboard page to approvers showing all pending work orders.

    Requires the user to be logged in as an approver. Redirects to the authentication
    page if not authenticated.

    Returns:
        - Redirect to login: If user is not logged in as approver.
        - HTML template: The approver dashboard page with pending work orders listed.
    """
    if 'approver' not in session:
        flash("Please log in as an approver.", "danger")
        return redirect(url_for('auth.auth'), 403)

    pending_work_orders = WorkRequest.query.filter_by(status='pending').all()  # Fetch only pending work orders
    return render_template("ApproverDashboard.html", pending_work_orders=pending_work_orders)

@approver_bp.route('/approver/work_order/<int:work_order_id>', methods=["GET"])
def get_work_order(work_order_id):
    """
    Fetch and return JSON data for a specific work order based on its ID.

    Args:
        work_order_id (int): The ID of the work order to fetch.

    Returns:
        - JSON response: Details of the work order if found.
        - JSON response: Error message if the work order is not found.
    """
    work_order = WorkRequest.query.get(work_order_id)
    if work_order:
        return jsonify({
            'first_name': work_order.first_name,
            'last_name': work_order.last_name,
            'email': work_order.email,
            'department': work_order.department,
            'equipment_id': work_order.equipment_id,
            'description': work_order.description
        })
    else:
        return jsonify({'error': 'Work order not found'}), 404

@approver_bp.route('/approver/approve/<int:work_order_id>', methods=["POST"])
def approve_work_order(work_order_id):
    """
    Approve a specified work order by its ID and update its status in the database.

    Args:
        work_order_id (int): The ID of the work order to approve.

    Returns:
        - JSON response: Success message if the work order is approved.
        - JSON response: Error message if the work order is not found.
    """
    work_order = WorkRequest.query.get(work_order_id)
    if work_order:
        work_order.status = 'approved'
        db.session.commit()
        return jsonify({'message': 'Work order approved successfully'})
    return jsonify({'error': 'Work order not found'}), 404

@approver_bp.route('/approver/reject/<int:work_order_id>', methods=["POST"])
def reject_work_order(work_order_id):
    """
    Reject a specified work order by its ID and update its status in the database.

    Args:
        work_order_id (int): The ID of the work order to reject.

    Returns:
        - JSON response: Success message if the work order is rejected.
        - JSON response: Error message if the work order is not found.
    """
    work_order = WorkRequest.query.get(work_order_id)
    if work_order:
        work_order.status = 'rejected'
        db.session.commit()
        return jsonify({'message': 'Work order rejected successfully'})
    return jsonify({'error': 'Work order not found'}), 404
