# run.py
import os
from dotenv import load_dotenv
from app import app

# Load environment variables from .env file
load_dotenv()

# Set Flask-related environment variables programmatically
os.environ['FLASK_APP'] = 'run.py'
os.environ['FLASK_ENV'] = 'development'
os.environ['FLASK_DEBUG'] = '1'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
