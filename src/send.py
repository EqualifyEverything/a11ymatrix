import json
import pika
from data.select import get_axe_url, get_uppies_url
from utils.watch import logger
from utils.auth import rabbit
from data.update import execute_update


# Selects and sends a single url to the queue
def yeet_axes(channel, queue_name):
    # Retrieve data from get_axe_url() function with a specified batch size
    batch_size = 10
    data = get_axe_url(batch_size)

    # If data is not empty
    if data:
        for row in data:
            # Get the URL and URL ID values
            url = row[1]
            url_id = row[0]

            # Construct message body as a JSON string
            message_body = json.dumps({"url": url, "url_id": url_id})

            # Publish message to the queue
            channel.basic_publish(exchange='',
                                  routing_key=queue_name,
                                  body=message_body,
                                  properties=pika.BasicProperties(
                                     delivery_mode = 2, # make message persistent
                                  ))

            # Update the queued_at_axe field for the selected URL IDs
            update_query = """
                UPDATE targets.urls
                SET queued_at_axe = now()
                WHERE id IN %s;
            """
            url_ids = tuple(row[0] for row in data)
            execute_update(update_query, (url_ids,))
    else:
        logger.info('No URLs found to send to the Axe queue.')


# Selects and sends url(s) to Uppies Queue
def share_uppies(channel, queue_name):
    # Retrieve data from get_uppies_url() function with a specified batch size
    batch_size = 10
    data = get_uppies_url(batch_size)

    # If data is not empty
    if data:
        for row in data:
            # Get the URL and URL ID values
            url = row[1]
            url_id = row[0]

            # Construct message body as a JSON string
            message_body = json.dumps({"url": url, "url_id": url_id})

            # Publish message to the queue
            channel.basic_publish(exchange='',
                                  routing_key=queue_name,
                                  body=message_body,
                                  properties=pika.BasicProperties(
                                    delivery_mode=2,))

            # Update the queued_at_axe field for the selected URL IDs
            update_query = """
                UPDATE targets.urls
                SET queued_at_uppies = now()
                WHERE id IN %s;
            """
            url_ids = tuple(row[0] for row in data)
            execute_update(update_query, (url_ids,))
    else:
        logger.info('No URLs found to send to the Uppies queue.')