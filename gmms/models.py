from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize SQLAlchemy with Flask app
db = SQLAlchemy()

class Customer(db.Model):
    # Define a Customer model with various fields and methods for interaction with customer data

    # Primary key column for customer identification
    id = db.Column(db.Integer, primary_key=True)
    # Username field must be unique and not nullable
    username = db.Column(db.String(80), unique=True, nullable=False)
    # Password hash for storing hashed passwords instead of plain text for security
    password_hash = db.Column(db.String(128), nullable=False)
    # Email field, must be unique and not nullable
    email = db.Column(db.String(120), unique=True, nullable=False)
    # Optional phone field
    phone = db.Column(db.String(20), nullable=True)
    # Optional address field
    address = db.Column(db.String(200), nullable=True)

    def set_password(self, password):
        # Create a hashed password to store in the database
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        # Check if the provided password matches the stored hash
        return check_password_hash(self.password_hash, password)
