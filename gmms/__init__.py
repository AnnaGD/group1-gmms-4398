from flask import Flask
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=5) #session will expire in 5 minutes, this should be changed after logout button implementation. 

# Import and register blueprints
from gmms.routes.main import main_bp
from gmms.routes.customer import customer_bp
from gmms.routes.technician import technician_bp
from gmms.routes.approver import approver_bp
from gmms.routes.register import register_bp
from gmms.routes.login import login_bp

app.register_blueprint(main_bp)
app.register_blueprint(customer_bp)
app.register_blueprint(technician_bp)
app.register_blueprint(approver_bp)
app.register_blueprint(register_bp)
app.register_blueprint(login_bp)
