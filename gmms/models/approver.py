from gmms.models import db

class Approver(db.Model):

    """
    Represents an approver in the system.

    An approver is responsible for reviewing and approving maintenance requests.

    :param id: The unique identifier for the approver.
    :param fullname: The full name of the approver.
    :param email: The email address of the approver. Must be unique.
    :param username: The username for the approver's account. Must be unique.
    :param password: The hashed password for the approver's account.
    :param phone: The phone number of the approver (optional).
    """

    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(20))
