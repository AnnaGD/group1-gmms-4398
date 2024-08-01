from flask import Blueprint, render_template
from gmms.models.work_request import WorkRequest

approver_bp = Blueprint('approver', __name__)

@approver_bp.route('/approver', methods=["POST", "GET"])
def approver():

    # retreive from the db
    pending_work_orders = WorkRequest.query.all()
    print("Workorder: ", pending_work_orders)
    #user = Customer.query.filter_by(username=username, password=password)
    return render_template("approver_dashboard.html", pending_work_orders=pending_work_orders)
