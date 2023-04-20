# 3rd Party Imports
from flask import Flask, request
from flask_cors import CORS
# Script Imports
from utils.watch import logger


app = Flask(__name__)
CORS(app)


# Define Endpoints

# Axe Specific
"""
    Endpoints related to Axe Processing
        1. /start
        2. /stop
        3. /status
        4. /health
"""
@app.route('/axe/start', methods=['POST'])
def axe_start():
    # Start the Axe Processing
    logger.info('Start Requested')


# Stop Axe Scans
@app.route('/axe/stop', methods=['POST'])
def axe_stop():


# Get Axe Status
@app.route('/axe/status', methods=['GET'])
def axe_status():


# Check Axe Health
@app.route('/axe/health', methods=['GET'])
def axe_health():


if __name__ == '__endpoints__':
    logger.debug('Starting Endpoints')