from flask import Flask
from datetime import timedelta
from gmms.models import db, init_app as init_db
from gmms.routes.main import main_bp
from gmms.routes.auth import auth_bp
from gmms.routes.technician import technician_bp
from gmms.routes.approver import approver_bp

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=5)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yourdatabase.db'

# Initialize the database
init_db(app)

# Register blueprints
app.register_blueprint(main_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(technician_bp)
app.register_blueprint(approver_bp)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
