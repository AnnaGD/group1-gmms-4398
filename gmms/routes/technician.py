from flask import Blueprint, render_template, jsonify, session, redirect, url_for, flash
from gmms.models.work_request import WorkRequest
from gmms.models import db

technician_bp = Blueprint('technician', __name__)

@technician_bp.route('/technician_dashboard', methods=["GET"])
def technician_dashboard():
    if 'technician' not in session:
        flash("Please log in as a technician.", "danger")
        return redirect(url_for('auth.auth'))

    approved_work_orders = WorkRequest.query.filter_by(status='approved').all()
    return render_template("TechnicianDashboard.html", approved_work_orders=approved_work_orders)

@technician_bp.route('/technician/work_order/<int:work_order_id>', methods=["GET"])
def get_work_order(work_order_id):
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
    work_order = WorkRequest.query.get(work_order_id)
    if work_order:
        work_order.status = 'complete'
        db.session.commit()
        return jsonify({'message': 'Work order completed successfully'})
    return jsonify({'error': 'Work order not found'}), 404