import json
import pika
from data.select import get_axe_url
from utils.watch import logger
from utils.auth import rabbit


# Selects and sends a single url to the queue
def yeet_axes(channel, queue_name):
    # Retrieve data from get_axe_url() function
    data = get_axe_url()

    # If data is not empty
    if data:
        # Get the URL and URL ID values
        url = data[0]
        url_id = data[1]

        # Construct message body as a JSON string
        message_body = json.dumps({"url": url, "url_id": url_id})

        # Publish message to the queue
        channel.basic_publish(exchange='',
                              routing_key=queue_name,
                              body=message_body,
                              properties=pika.BasicProperties(
                                 delivery_mode = 2, # make message persistent
                              ))
    else:
        logger.info('No URLs found to send to the queue.')
