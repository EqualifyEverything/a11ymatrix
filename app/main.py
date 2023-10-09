# main.py
import os
from services.postgres import auth, execute_select
from utils import logger

def get_targets():
    # Define the queue
    queue = define_queue()
    logger.info('%s queue declared!', queue)

    # Create a database connection
    db_conn = auth.PostgreSQLConnection()
    db_conn.open()

    # Determine the SQL file to execute based on the queue
    sql_filename = "get_uppies.sql" if queue == "uppies" else "get_em.sql"
    sql_filepath = os.path.join("services", "postgres", "queries", sql_filename)

    # Execute the SQL query and get the results
    targets = execute_select.execute_sql_from_file(db_conn.conn, sql_filepath, queue)

    # Close the database connection
    db_conn.close()

    # Send the targets to the appropriate RabbitMQ queue
    # ...

def define_queue():
    queue = "crawl"
    logger.info('%s queue declared!', queue)
    return queue

get_targets()
