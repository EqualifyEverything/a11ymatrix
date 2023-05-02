from utils.watch import logger
from utils.auth import rabbit

QUEUE_NAMES = [
    'am_i_up', 'axe_scan_error', 'axe_speed',
    'axes_for_throwing', 'i_am_down', 'i_am_up',
    'sharp_axes'
    ]


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
