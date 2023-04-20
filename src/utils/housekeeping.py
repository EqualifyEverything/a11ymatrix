import time
from utils.watch import logger
from data.select import add_more_urls, sync_target_urls


def sync_those_urls(run_wild):
    if run_wild:
        if sync_target_urls():
            logger.info('Synced URL Uppy Activity to Targets')
        else:
            logger.info('URL Sync Issue')

        # Run add_more_urls() every 15 minutes
        if int(time.time()) % 900 == 0:
            add_more_urls()
            logger.info('Adding more URLs')