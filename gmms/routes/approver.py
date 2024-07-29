from flask import Blueprint, render_template

approver_bp = Blueprint('approver', __name__)

@approver_bp.route('/approver')
def approver():
    return render_template("approver.html")
