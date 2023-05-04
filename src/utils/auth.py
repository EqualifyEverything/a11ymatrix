import pika
from utils.watch import logger


def rabbit(queue_name):
    # Connect to the RabbitMQ server
    logger.debug('Connecting to RabbitMQ server...')
    credentials = pika.PlainCredentials('yeeter_in_chief', 'yeet_for_love')
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbit', credentials=credentials, virtual_host='gova11y'))
    logger.debug('Connected to RabbitMQ server!')

    # connection = pika.BlockingConnection(
    #    pika.ConnectionParameters(
    #        'rabbit', credentials=credentials, virtual_host='gova11y'))

    # Create a channel and declare a queue
    logger.debug(f'Declaring queue: {queue_name}...')
    channel = connection.channel()
    channel.queue_declare(
        queue=queue_name, durable=True, arguments={'x-message-ttl': 7200000})
    logger.debug(f'Queue {queue_name} declared!')

    return channel, connection
