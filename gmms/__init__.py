from flask import Flask
from datetime import timedelta
from gmms.models import db, init_app as init_db
from gmms.routes.main import main_bp
from gmms.routes.auth import auth_bp
from gmms.routes.technician import technician_bp
from gmms.routes.approver import approver_bp

# Create an instance of the Flask class. This is the WSGI application.
app = Flask(__name__)

# Set a secret key for session management and security.
# IMPORTANT: In production, make sure to use a secure, random secret key!
app.secret_key = 'temp_secret_key'

# Configure the duration of a permanent session to be 5 minutes. Session data is deleted after this period of inactivity.
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=5)

# Configure the application to use a SQLite database.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gmms.db'

# Initialize the database
init_db(app)

# Registering blueprints for different sections of the application.
# Each blueprint handles routing for its respective functional area.
app.register_blueprint(main_bp) # Routes for main application functionality
app.register_blueprint(auth_bp) # Routes for user authentication
app.register_blueprint(technician_bp) # Routes for technician-specific features
app.register_blueprint(approver_bp) # Routes for approval-related features

# Ensure all database tables are created at startup. This is done within the app context.
with app.app_context():
    db.create_all()

# Condition to check if the run.py is executed as the main program and not imported as a module.
if __name__ == '__main__':
    # Run the application with debugging enabled to facilitate development.
    # Debug mode allows for live reloading and better error tracking.
    app.run(debug=True)
