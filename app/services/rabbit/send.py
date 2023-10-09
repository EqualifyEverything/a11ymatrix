# app/services/rabbit/send.py
from app.services.rabbit import auth
from app import logger


def send_message(url: str, url_id: str, binding_key: str):
    """Send a message to the RabbitMQ server.

    Args:
        url (str): The URL to be sent.
        url_id (str): The URL ID to be sent.
        binding_key (str): The binding key for the exchange.
    """
    exchange_name = 'launch'

    # Get the channel and connection objects from the auth module
    channel, connection = auth.get_rabbitmq_channel()

    # Prepare the message
    message = {
        'url_id': url_id,
        'url': url
    }

    # Send the message to the specified exchange with the specified binding key
    try:
        logger.debug(f'Sending message: {message} to exchange {exchange_name} with binding key {binding_key}...')
        channel.basic_publish(exchange=exchange_name, routing_key=binding_key, body=str(message))
        logger.debug('Message sent successfully!')
    except Exception as e:
        logger.error(f'Failed to send message: {e}')
        raise
    finally:
        # Close the connection
        connection.close()
