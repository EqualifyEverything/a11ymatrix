import json
import os
import requests
from threading import Event
from utils.watch import logger
from data.update import get_uppies

stop_event = Event()

def roll_uppies():
    batch_size = 10
    while True:
        uppers = get_uppies(batch_size=batch_size)
        if not uppers:
            logger.debug('No URLs to process')
            break

        # Format the data as a list of dictionaries
        data = [{'url': up[0], 'url_id': up[1]} for up in uppers]
        logger.debug(f'Data Ready: {data}')

        # Send the POST request to Franklin
        franklin_url = os.environ.get('FRANKLIN_URL')
        url = f'{franklin_url}/uppies/yeet'
        headers = {'Content-Type': 'application/json'}
        logger.debug(f'Sending POST request to {url} with data: {data}')
        response = requests.post(url, headers=headers, json=data)

        # Check the response status code
        if response.status_code == 200:
            logger.info('🚀   📡 POST request sent successfully')
        else:
            logger.error(f'🚀   📡 Error sending POST request: {response.status_code} - {response.reason}')

        # Check if the stop_event is set and break the loop if it is
        if stop_event.is_set():
            break
    else:
        logger.debug('No URLs to process')

