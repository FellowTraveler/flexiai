# app.py
import os
from flask import Flask, session, render_template
from datetime import timedelta
from routes.api import api_bp
from flexiai import FlexiAI

app = Flask(__name__, static_folder='static', template_folder='templates')
app.secret_key = os.urandom(24)  # Secure the session with a secret key
app.register_blueprint(api_bp, url_prefix='/api')

flexiai = FlexiAI()

@app.before_request
def before_request():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=30)  # Set session lifetime

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
