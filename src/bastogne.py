import os
import threading
from utils.watch import logger
from utils.auth import rabbit
from send import yeet_axes, share_uppies, crawl_things


# Function to start axe queue
def start_rabbit():
    channel, connection = rabbit("launch_axe")
    while True:
        try:
            yeet_axes(channel, "launch_axe")
        except Exception as e:
            logger.error(f"Error in start_rabbit: {e}")
            channel, connection = rabbit("launch_axe")


# Function to start crawl queue
def start_crawler():
    channel, connection = rabbit("launch_crawler")
    while True:
        try:
            crawl_things(channel, "launch_crawler")
        except Exception as e:
            logger.error(f"Error in start_crawler: {e}")
            channel, connection = rabbit("launch_crawler")


# Function to start uppies queue
def start_uppies():
    channel, connection = rabbit("launch_uppies")
    while True:
        try:
            share_uppies(channel, "launch_uppies")
        except Exception as e:
            logger.error(f"Error in start_uppies: {e}")
            channel, connection = rabbit("launch_uppies")


# Start parallel threads for queues
rabbit_thread = threading.Thread(target=start_rabbit)
crawler_thread = threading.Thread(target=start_crawler)
uppies_thread = threading.Thread(target=start_uppies)

rabbit_thread.start()
crawler_thread.start()
uppies_thread.start()

rabbit_thread.join()
crawler_thread.join()
uppies_thread.join()