from gmms.models import db

class WorkRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    department = db.Column(db.String(255), nullable=True)
    equipment_id = db.Column(db.String(255), nullable=True)
    description = db.Column(db.Text, nullable=False)
