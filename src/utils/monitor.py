import time
import pika
from utils.auth import rabbit
from utils.watch import logger
from send import yeet_axes


def start_rabbit():
    """
    Starts monitoring the queue sizes and sends messages to the queues at the current rate.
    """
    global is_running
    is_running = True

    while is_running:
        # Update queue sizes
        queue_sizes = {}
        for queue_name in QUEUE_NAMES:
            channel, connection = rabbit(queue_name)
            queue_declare_result = channel.queue_declare(queue_name, passive=True)
            queue_sizes[queue_name] = queue_declare_result.method.message_count
            connection.close()

        # Send messages to the queues using yeet_axes()
        for queue_name in QUEUE_NAMES:
            channel, connection = rabbit(queue_name)
            yeet_axes(channel, queue_name)  # add URL to queue
            connection.close()

        # Adjust the send rate based on the queue sizes
        adjust_send_rate()

        # Wait for some time before checking the queues again
        time.sleep(1)




def stop_rabbit():
    """
    Stops the monitoring.
    """
    global is_running
    is_running = False


def whats_up_doc():
    """
    Gets the status of the queues.
    """
    queue_sizes = {}
    for queue_name in QUEUE_NAMES:
        channel, connection = rabbit(queue_name)
        queue_declare_result = channel.queue_declare(queue_name, passive=True)
        queue_sizes[queue_name] = queue_declare_result.method.message_count
        connection.close()
    return queue_sizes, send_rate


def rabbit_checkup():
    """
    Checks the health of RabbitMQ.
    """
    try:
        channel, connection = rabbit(QUEUE_NAMES[0])
        channel.close()
        connection.close()
        return True
    except Exception as e:
        logger.error(f"Error connecting to RabbitMQ: {e}")
        return False


# QUEUE_NAMES = ['urls_scan-axe-1', 'urls_scan-axe-2', 'urls_scan-axe-3', 'urls_scan-axe-4', 'urls_scan-axe-5']
QUEUE_NAMES = ['axes_for_throwing']

MAX_QUEUE_SIZE = 3000
MIN_QUEUE_SIZE = 50
SEND_RATE_INCREMENT = 0.1  # increase send rate by 10% per step
SEND_RATE_DECREMENT = 0.05  # decrease send rate by 5% per step
SEND_RATE_MIN = 0.1
SEND_RATE_MAX = 50.0
SEND_RATE_INITIAL = 1.0

send_rate = SEND_RATE_INITIAL
queue_sizes = {}
is_running = False


def adjust_send_rate():
    """
    Adjusts the send rate based on the queue sizes.
    """
    global send_rate

    # Initialize queue_sizes
    queue_sizes = {}

    # Check each queue size and adjust send rate if necessary
    for queue_name in QUEUE_NAMES:
        channel, connection = rabbit(queue_name)
        queue_declare_result = channel.queue_declare(queue_name, passive=True)
        queue_sizes[queue_name] = queue_declare_result.method.message_count
        connection.close()

    logger.info(f"Queue sizes: {queue_sizes}")

    if all(size > MAX_QUEUE_SIZE for size in queue_sizes.values()):
        send_rate -= SEND_RATE_DECREMENT
    elif all(size < MIN_QUEUE_SIZE for size in queue_sizes.values()):
        send_rate += SEND_RATE_INCREMENT

    send_rate = max(SEND_RATE_MIN, min(SEND_RATE_MAX, send_rate))
