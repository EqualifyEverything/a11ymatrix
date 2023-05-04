import psycopg2
import json
import traceback
from data.access import connection
from utils.watch import logger
from psycopg2.pool import SimpleConnectionPool
from datetime import datetime, timezone

# Set use_pooling to True to enable connection pooling
use_pooling = True

# Connection pool
pool = None

if use_pooling:
    conn_params = connection().get_connection_params()
    pool = SimpleConnectionPool(
        minconn=1,
        maxconn=25,
        **conn_params
    )


def connection_pooling():
    return pool.getconn()


def release_pooling(conn):
    pool.putconn(conn)

# Singular Updates


def execute_update(query, params=None, fetchone=True):
    # logger.debug(f'🗄️   🔧 Executing query: {query}')
    # logger.debug(f'🗄️   🔧 Query parameters: {params}... ')

    # Connect to the database
    conn = connection()
    conn.open()
    logger.debug('🗄️   🔧 Database connection opened')

    # Create a cursor
    cur = conn.conn.cursor()

    try:
        # Execute the query
        cur.execute(query, params)
        conn.conn.commit()
        logger.info('🗄️   🔧 Query executed and committed')

        # Fetch the results if requested
        result = None
        if fetchone:
            result = cur.fetchone() or ()
        else:
            result = cur.fetchall() or []
            logger.debug(f'🗄️   🔧 Fetched results: {result}')
    except Exception as e:
        logger.error(f'🗄️   🔧 Error executing update query: {e}')
        result = None

    # Close the cursor and connection
    cur.close()
    conn.close()
    logger.debug('🗄️   🔧 Cursor and connection closed')

    return result


# # # # # # # # # #

# Bulk Updates

def execute_bulk_update(query, params_list):
    # Connect to the database
    if use_pooling:
        conn = connection_pooling()
    else:
        conn = connection()
        conn.open()

    # Create a cursor
    cur = conn.cursor()

    try:
        # Execute the query
        with conn:
            cur.executemany(query, params_list)
            logger.info("🗄️✏️🟢 Query executed and committed")
    except Exception as e:
        logger.error(f"🗄️✏️ Error executing bulk insert query: {e}\n{traceback.format_exc()}")

    # Close the cursor and connection
    cur.close()
    if use_pooling:
        release_pooling(conn)
    else:
        conn.close()


#########################################################
# Queries


# Queries
def get_uppies(batch_size=10):
    query = """
        UPDATE processing.uppies_urls
        SET processed = true
        WHERE url_id IN (
            SELECT url_id
            FROM processing.uppies_urls
            WHERE processed = false
            LIMIT %s
        )
        RETURNING url, url_id;
    """
    result = execute_update(query, (batch_size,), fetchone=False)
    if result:
        urls = [(row[0], row[1]) for row in result]
        logger.info(f'Got {len(urls)} URLs')
        return urls
    else:
        logger.critical('No URLs to process')
        return []
