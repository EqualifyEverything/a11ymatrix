# 3rd Party Imports
import os
import pika
from flask import Flask, request, jsonify
from flask_cors import CORS
import threading
from prometheus_client import Counter, Histogram, generate_latest
# Script Imports
from utils.watch import logger
from utils.auth import rabbit
from utils.monitor import start_rabbit, stop_rabbit, whats_up_doc, rabbit_checkup


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

        start_rabbit
        stop_rabbit
        whats_rabbit_doing
        rabbit_checkup
"""


# Rabbit Monitor - Start
@app.route('/rabbit/ears/start', methods=['POST'])
def start_rabbits():
    # Start the RabbitMQ monitoring
    rabbit_thread = threading.Thread(target=start_rabbit)
    rabbit_thread.start()
    return jsonify({'status': 'started'}), 200


# Rabbit Monitor - Stop
@app.route('/rabbit/ears/stop', methods=['POST'])
def stop_rabbits():
    # Stop the RabbitMQ monitoring
    stop_rabbit()
    return jsonify({'status': 'stopped'}), 200


# Rabbit Monitor - Health Check
@app.route('/rabbit/health', methods=['GET'])
def rabbit_healthy():
    # Perform a RabbitMQ health check
    status = rabbit_checkup()
    return jsonify(status), 200


# Rabbit Monitor - Queue Status
@app.route('/rabbit/ears', methods=['GET'])
def rabbit_ears():
    # Get the current queue status
    status = whats_up_doc()
    return jsonify(status), 200


@app.route('/rabbit/clear', methods=['POST'])
def clear_rabbit():
    # Get the queue name from the request body
    queue_name = request.json.get('queue_name')

    # Connect to the queue
    channel, connection = rabbit(queue_name)

    # Purge the ready queue
    channel.queue_purge(queue=queue_name)

    # Check if the unacked queue exists
    try:
        channel.queue_declare(queue=f"{queue_name}-unacked")
    except pika.exceptions.ChannelClosedByBroker as e:
        # The queue does not exist, so there is nothing to clear
        pass
    else:
        # The queue exists, so purge it
        channel.queue_purge(queue=f"{queue_name}-unacked")

    # Close the connection and channel
    channel.close()
    connection.close()

    return jsonify({'status': 'cleared'}), 200


# End Rabbit


@app.route('/axe/start', methods=['POST'])
def axe_start():
    # Start the Axe Processing
    logger.info('Start Requested')


# Stop Axe Scans
@app.route('/axe/stop', methods=['POST'])
def axe_stop():
    # Start the Axe Processing
    logger.info('Start Requested')


# Get Axe Status
@app.route('/axe/status', methods=['GET'])
def axe_status():
    # Start the Axe Processing
    logger.info('Start Requested')


# Check Axe Health
@app.route('/axe/health', methods=['GET'])
def axe_health():
    # Start the Axe Processing
    logger.info('Start Requested')


# Prometheus
# Define metrics
REQUESTS = Counter('requests_total', 'Total number of requests')
LATENCY = Histogram('request_latency_seconds', 'Request latency in seconds')


@app.route('/metrics')
def metrics():
    # Collect and return the metrics as a Prometheus-formatted response
    response = Response(generate_latest(), mimetype='text/plain')
    response.headers['Content-Type'] = 'text/plain; charset=utf-8'
    return response



if __name__ == '__main__':
    logger.debug('Starting Endpoints')
    app_port = int(os.environ.get('APP_PORT', 8888))
    app.run(debug=True, host='0.0.0.0', port=app_port)