# reset_db.py
from gmms import db, create_app

app = create_app()
with app.app_context():
    db.drop_all()  # This will drop all tables
    db.create_all()  # This will recreate all tables
    print("Database has been reset.")
