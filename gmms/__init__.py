#Contains Flask app initialization, configuration loading, and imports for models and routes.

import sys
sys.dont_write_bytecode = True
from flask import Flask
#from .config import Config

app = Flask(__name__)
#app.config.from_object(Config)

# Initialize DB with app
#from .models import db, init_app
#init_app(app)

# Import routes after app is created to avoid circular imports
from gmms import routes
