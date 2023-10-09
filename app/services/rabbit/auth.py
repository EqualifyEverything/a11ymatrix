# app/services/rabbit/auth.py
"""Module for establishing a connection to RabbitMQ."""

import pika
from app import logger


def get_rabbitmq_channel() -> tuple:
    """Establish a connection to the RabbitMQ server.

    Returns:
        tuple: A tuple containing the channel and connection objects.

    Raises:
        Exception: Any exception raised while establishing the connection.
    """
    # Connect to the RabbitMQ server
    logger.debug('Connecting to RabbitMQ server...')

    credentials = pika.PlainCredentials('yeeter_in_chief', 'yeet_for_love')
    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters('rabbit', credentials=credentials, virtual_host='gova11y')
        )
        logger.debug('Connected to RabbitMQ server!')

        # Create a channel
        channel = connection.channel()

    except Exception as e:
        logger.error(f'Failed to connect to RabbitMQ server: {e}')
        raise

    return channel, connection
