# work_request.py
from gmms.models import db

class WorkRequest(db.Model):

    """
    Represents an approver in the system.

    An approver is responsible for reviewing and approving maintenance requests.

    :param id: The unique identifier for the work request.
    :param first_name: The first name of the requester.
    :param last_name: The last name of the requester.
    :param email: The email address of the requester.
    :param department: The name of the department.
    :param equipment_id: The equipment id for this work request.
    :param description: Description of the issue.
    :param comment_section: Comments returns from work order.
    :param status: Status for the work request, pending, approved, denied, completed.
    """
        
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    department = db.Column(db.String(255), nullable=True)
    equipment_id = db.Column(db.String(255), nullable=True)
    description = db.Column(db.Text, nullable=False)
    comment_section = db.Column(db.Text, nullable=False, default="")
    status = db.Column(db.String(50), nullable=False, default="pending")  # Add this line
    
