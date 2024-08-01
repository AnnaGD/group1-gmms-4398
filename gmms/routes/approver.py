from flask import Blueprint, render_template, jsonify, session, redirect, url_for, flash, request
from gmms.models.work_request import WorkRequest
from gmms.models import db

approver_bp = Blueprint('approver', __name__)

@approver_bp.route('/approver', methods=["GET"])
def approver_dashboard():
    if 'approver' not in session:
        flash("Please log in as an approver.", "danger")
        return redirect(url_for('auth.auth'))

    pending_work_orders = WorkRequest.query.filter_by(status='pending').all()  # Fetch only pending work orders
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

@approver_bp.route('/approver/approve/<int:work_order_id>', methods=["POST"])
def approve_work_order(work_order_id):
    work_order = WorkRequest.query.get(work_order_id)
    if work_order:
        work_order.status = 'approved'
        db.session.commit()
        return jsonify({'message': 'Work order approved successfully'})
    return jsonify({'error': 'Work order not found'}), 404

@approver_bp.route('/approver/reject/<int:work_order_id>', methods=["POST"])
def reject_work_order(work_order_id):
    work_order = WorkRequest.query.get(work_order_id)
    if work_order:
        work_order.status = 'rejected'
        db.session.commit()
        return jsonify({'message': 'Work order rejected successfully'})
    return jsonify({'error': 'Work order not found'}), 404
