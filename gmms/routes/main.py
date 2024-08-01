# main.py
from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from gmms.models import db
from gmms.models.work_request import WorkRequest

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template("index.html")
