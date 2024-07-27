from flask import Blueprint, render_template

technician_bp = Blueprint('technician', __name__)

@technician_bp.route('/technician')
def technician():
    return render_template("technician.html")
