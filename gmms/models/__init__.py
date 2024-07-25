from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_app(app):
    db.init_app(app)

# eg: for from .models import WorkRequest  # Assuming WorkRequest is a class in models.py
