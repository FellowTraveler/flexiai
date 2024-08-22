# app.py
import os
import logging
import pypandoc
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
    enable_file_logging=True,
    enable_console_logging=True
)

app = Flask(__name__, static_folder='static', template_folder='templates')

app.secret_key = os.urandom(24)

app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'

app.register_blueprint(api_bp, url_prefix='/api')

flexiai = FlexiAI()


# Check if Pandoc is installed on the system and log an instruction if it's missing
try:
    pypandoc.get_pandoc_version()
    app.logger.info("Pandoc is installed and available.")
except OSError:
    app.logger.info("Pandoc is not installed. Please install Pandoc manually on your system for full functionality.")
    # Instructions for installation
    app.logger.info("To install Pandoc, visit https://pandoc.org/installing.html or run 'sudo apt-get install pandoc' on Debian-based systems.")


@app.before_request
def before_request():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=60)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    
    if root_logger.hasHandlers():
        root_logger.handlers.clear()

    loggers = ['werkzeug', 'httpx', 'flexiai', 'user_function_mapping']
    for logger_name in loggers:
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.INFO)
        logger.propagate = False
        if logger.hasHandlers():
            logger.handlers.clear()

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    root_logger.addHandler(console_handler)

    app.run(host='127.0.0.1', port=5000, debug=False)
