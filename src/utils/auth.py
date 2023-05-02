import pika


def rabbit(queue_name):
    # Connect to the RabbitMQ server
    credentials = pika.PlainCredentials('yeeter_in_chief', 'time_2_rumble')
    connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.1.29', credentials=credentials, virtual_host='gova11y'))

    # Create a channel and declare a queue
    channel = connection.channel()
    channel.queue_declare(queue=queue_name, durable=True, arguments={'x-message-ttl': 7200000})

    return channel, connection
