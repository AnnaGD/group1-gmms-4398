# main.py
from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from gmms.models import db
from gmms.models.work_request import WorkRequest

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    """
    Render the main index page of the application.

    This function handles the root URL and simply returns the main index page 
    of the application using Flask's render_template function.

    Returns:
        Rendered template: Returns the 'index.html' template which serves as 
        the landing page of the website.
    """
    return render_template("index.html")