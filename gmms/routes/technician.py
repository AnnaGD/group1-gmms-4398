from flask import Blueprint, render_template, session, redirect, url_for, flash
from gmms.models.work_request import WorkRequest

technician_bp = Blueprint('technician', __name__)

@technician_bp.route('/technician', methods=["GET"])
def technician_dashboard():
    if 'technician' not in session:
        flash("Please log in as a technician.", "danger")
        return redirect(url_for('auth.auth'))

    approved_work_orders = WorkRequest.query.filter_by(status='approved').all()
    return render_template("TechnicianDashboard.html", approved_work_orders=approved_work_orders)
