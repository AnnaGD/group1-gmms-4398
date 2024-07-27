from flask import Blueprint, render_template, session, flash, redirect, url_for

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template("index.html")

@main_bp.route('/CustomerDashboard')
def customer_dashboard():
    return render_template("CustomerDashboard.html")

@main_bp.route('/WorkRequest')
def WorkRequest():
    return render_template("WorkRequest.html")

@main_bp.route("/logout")
def logout():
    flash("You have been logged out!", "info")
    session.pop("customer", None)
    session.pop("username", None)  # user logged out
    return redirect(url_for("main.index"))
