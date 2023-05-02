from utils.auth import rabbit
from utils.watch import logger
from send import share_uppies

queue_name = 'launch_uppies'


def start_the_uppies():
    logger.info('Start Requested')

    global uppies_up
    uppies_up = True

    while uppies_up:
        # Send messages to the queues using yeet_axes()
        channel, connection = rabbit(queue_name)
        share_uppies(channel, queue_name)  # add URL to queue
        connection.close()


def stop_the_uppies():
    logger.info('Stop Requested')
    global is_running
    is_running = False
