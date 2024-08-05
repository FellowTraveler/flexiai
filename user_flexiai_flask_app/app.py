# app.py
import os
import logging
from flask import Flask, session, render_template
from datetime import timedelta
from routes.api import api_bp
from flexiai import FlexiAI
from flexiai.config.logging_config import setup_logging


# Initialize application-specific logging
setup_logging(
    root_level=logging.INFO,
    file_level=logging.INFO,
    console_level=logging.INFO,
    enable_file_logging=True,       # Set to False to disable file logging
    enable_console_logging=False    # Set to False to disable console logging
)

# Initialize Flask application with static and template folders
app = Flask(__name__, static_folder='static', template_folder='templates')

# Secure the session with a secret key
app.secret_key = os.urandom(24)

# Set session cookie attributes
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'  # or 'Strict'

# Register the API blueprint with a URL prefix
app.register_blueprint(api_bp, url_prefix='/api')

# Initialize FlexiAI instance
flexiai = FlexiAI()


@app.before_request
def before_request():
    """
    Function to run before each request to ensure sessions are permanent
    and set the session lifetime to 60 minutes.
    """
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=60)


@app.route('/')
def index():
    """
    Route for the index page, rendering the index.html template.
    """
    return render_template('index.html')

if __name__ == '__main__':
    # Configure the root logger to log at INFO level
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    
    # Clear existing handlers from the root logger to prevent duplicate logs
    if root_logger.hasHandlers():
        root_logger.handlers.clear()

    # Configure specific loggers to log at INFO level
    loggers = ['werkzeug', 'httpx', 'flexiai', 'user_function_mapping']
    for logger_name in loggers:
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.INFO)
        logger.propagate = False
        if logger.hasHandlers():
            logger.handlers.clear()

    # Add console handler to the root logger
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    root_logger.addHandler(console_handler)

    # Run the Flask application on host 0.0.0.0 and port 5000
    app.run(host='0.0.0.0', port=5000, debug=False)
