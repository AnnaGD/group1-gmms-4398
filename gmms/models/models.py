from flask_sqlalchemy import SQLAlchemy

# Create a SQLAlchemy object to handle database interactions
db = SQLAlchemy()

def init_app(app):
    """
    Initializes the SQLAlchemy app with Flask app settings.
    This function binds the Flask application and its configuration with SQLAlchemy.
    
    Args:
    app (Flask): The Flask application instance to be initialized with SQLAlchemy.
    """
    db.init_app(app)

# Defines the structure of the WorkRequest table in the database using a Python class. 
# Each attribute of the class corresponds to a column in the database table.
class WorkRequest(db.Model):
    # Define the columns of the database table for WorkRequests.

     # Unique identifier for each work request, automatically generated and increments.
    id = db.Column(db.Integer, primary_key=True)

    # Details about the equipment related to the maintenance request. Must be provided.
    equipment_details = db.Column(db.String(255), nullable=False)

     # Personal information of the user submitting the work request. Must be provided.
    personal_info = db.Column(db.String(255), nullable=False)

    # The date and time when the work request was submitted. Automatically set and must be provided.
    date_submitted = db.Column(db.DateTime, nullable=False)

    # The current status of the work request. Defaults to 'draft' and can be changed to 'submitted'.
    status = db.Column(db.String(50), default='draft')  # 'draft', 'submitted'