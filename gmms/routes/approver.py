from flask import Blueprint, render_template, jsonify, session, redirect, url_for, flash
from gmms.models.work_request import WorkRequest

approver_bp = Blueprint('approver', __name__)

@approver_bp.route('/approver', methods=["GET"])
def approver_dashboard():
    if 'approver' not in session:
        flash("Please log in as an approver.", "danger")
        return redirect(url_for('auth.auth'))

    pending_work_orders = WorkRequest.query.all()  # Fetch all work orders
    return render_template("ApproverDashboard.html", pending_work_orders=pending_work_orders)

@approver_bp.route('/approver/work_order/<int:work_order_id>', methods=["GET"])
def get_work_order(work_order_id):
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
