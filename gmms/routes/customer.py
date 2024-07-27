from flask import Blueprint, render_template, request, session, flash, redirect, url_for

customer_bp = Blueprint('customer', __name__)

@customer_bp.route('/customer', methods=["POST", "GET"])
def customer():
    if "customer" in session:
        return render_template("WorkRequest.html")
    else:
        flash("You are not logged in!")
        return redirect(url_for("login.login"))
