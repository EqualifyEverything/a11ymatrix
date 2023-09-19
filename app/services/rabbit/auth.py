"""Module for establishing a connection and declaring a queue in RabbitMQ."""

import pika
from utils.watch import logger


def get_rabbitmq_channel(queue_name: str) -> tuple:
    """Establish a connection to the RabbitMQ server and declare a queue.

    Args:
        queue_name (str): The name of the queue to declare.

    Returns:
        tuple: A tuple containing the channel and connection objects.

    Raises:
        Exception: Any exception raised while establishing the connection or declaring the queue.
    """
    # Connect to the RabbitMQ server
    logger.debug('Connecting to RabbitMQ server...')

    credentials = pika.PlainCredentials('yeeter_in_chief', 'yeet_for_love')
    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters('rabbit', credentials=credentials, virtual_host='gova11y')
        )
        logger.debug('Connected to RabbitMQ server!')

        # Create a channel and declare a queue
        logger.debug(f'Declaring queue: {queue_name}...')
        channel = connection.channel()
        channel.queue_declare(
            queue=queue_name, durable=True, arguments={'x-message-ttl': 7200000}
        )
        logger.debug(f'Queue {queue_name} declared!')
    except Exception as e:
        logger.error(f'Failed to connect or declare queue: {e}')
        raise

    return channel, connection


# Usage example (Uncomment to use)
# if __name__ == "__main__":
#     channel, connection = get_rabbitmq_channel('test_queue')
