import os
import time
import threading
from multiprocessing import Event, Process
from flask import Flask, jsonify, request
from flask_cors import CORS
from utils.process import roll_uppies
from utils.watch import logger


app = Flask(__name__)
CORS(app)

# Initialize number of workers to 1
num_workers = 1

# Set initial delay to 1 second
delay = 1

# Initialize response time
response_time = 0

# Flag variable to indicate whether the check_response_time function should run
run_wild = False

# Create a shared event object
stop_event = Event()


# Manage Uppies
@app.route('/uppies/start', methods=['POST'])
def starty_uppies():
    logger.info('Start Requested')
    global run_wild

    # Start roll_uppies process
    Process(target=roll_uppies, args=(stop_event,)).start()

    # Set the flag to True
    run_wild = True

    # Return empty response
    return '', 200

@app.route('/uppies/stop', methods=['POST'])
def stopy_uppies():
    logger.info('Stop Requested')
    global run_wild

    # Set the flag to False
    run_wild = False

    # Set the stop event to signal all threads and processes to stop
    stop_event.set()

    # Return empty response
    return '', 200


@app.route('/status', methods=['GET'])
def get_status():
    logger.info('Status Requested')
    # Return the status as a JSON object
    return jsonify({'num_workers': num_workers, 'response_time': response_time, 'delay': delay, 'run_wild': run_wild})


def check_response_time():
    global num_workers, delay, response_time, run_wild, stop_event

    while True:
        # Check if the flag is set
        if run_wild:
            # Measure response time for roll_uppies() function
            start_time = time.time()
            threading.Event().wait(1)
            response_time = time.time() - start_time

            # If response time is less than 2 seconds, add one worker
            if response_time < 2 and num_workers < 16:
                num_workers += 1
                logger.info(f"Increasing number of workers to {num_workers}")

            # If response time is greater than 2 seconds, remove one worker
            elif response_time > 2 and num_workers > 1:
                num_workers -= 1
                logger.info(f"Decreasing number of workers to {num_workers}")

            # Sleep for delay time
            time.sleep(delay)

            # If delay is greater than 60 seconds, reset delay and check again
            if delay > 60:
                delay = 1
            else:
                delay += 1

        else:
            # If the flag is not set, set the stop event to signal all threads and processes to stop
            stop_event.set()

            # Wait for all threads and processes to stop
            stop_event.wait()

            # Reset number of workers to 1
            num_workers = 1

            # Reset delay to 1 second
            delay = 1

            # Reset response time to 0
            response_time = 0

            # Clear the stop event
            stop_event.clear()

            # Sleep for 1 second before checking the flag again
            time.sleep(1)

if __name__ == '__main__':
    # Start check_response_time() function as a separate thread
    threading.Thread(target=check_response_time).start()

    # Start Flask app
    app_port = int(os.environ.get('APP_PORT', 8887))
    app.run(debug=True, host='0.0.0.0', port=app_port)

