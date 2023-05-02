import pika


def rabbit(queue_name):
    # Connect to the RabbitMQ server
    credentials = pika.PlainCredentials('yeeter_in_chief', 'yeet_for_love')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            'rabbit', credentials=credentials, virtual_host='gova11y'))

    # Create a channel and declare a queue
    channel = connection.channel()
    channel.queue_declare(
        queue=queue_name, durable=True, arguments={'x-message-ttl': 7200000})

    return channel, connection
