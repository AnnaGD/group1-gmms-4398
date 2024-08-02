from gmms.models import db

class Technician(db.Model):

    """
    Represents the technician in the system.

    An technician is responsible for completing work orders.

    :param id: The unique identifier for the Technician.
    :param fullname: The full name of the Technician.
    :param email: The email address of the Technician. Must be unique.
    :param username: The username for the Technician's account. Must be unique.
    :param password: The hashed password for the Technician's account.
    :param phone: The phone number of the Technician (optional).
    """


    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(20))
