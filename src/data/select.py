from data.access import connection
from utils.watch import logger
from datetime import datetime, timedelta

# Log Emoji: 🗄️🔍


def execute_select(query, params=None, fetchone=True):
    # Connect to the database
    conn = connection()
    conn.open()
    # logger.debug("🗄️🔍 Database connection opened")

    # Create a cursor
    cur = conn.conn.cursor()

    # Execute the query
    cur.execute(query, params)
    conn.conn.commit()
    logger.info("🗄️✏️🟢 Query executed and committed")
    # logger.debug(f"🗄️🔍 Executed select query: {query}")
    #   logger.debug(f"🗄️🔍 Query parameters: {params}")

    # Fetch the results if requested
    result = None
    if fetchone:
        result = cur.fetchone() if cur.rowcount > 0 else None
    else:
        result = cur.fetchall()

    # Close the cursor and connection
    cur.close()
    conn.close()
    logger.debug("🗄️🔍 Cursor and connection closed")

    return result


# Queries

def sync_target_urls():
    query = """
        SELECT processing.update_uppies_at_and_code();
    """
    execute_select(query)
    return True


def add_more_urls():
    query = """
        SELECT processing.add_uppies_urls_to_process();
    """
    execute_select(query)
    return True


def get_axe_url(batch_size=10):
    select_query = """
        SELECT t.id, t.url
        FROM targets.urls t
        INNER JOIN results.scan_uppies s ON t.id = s.url_id AND (s.content_type ILIKE 'text/html' OR s.content_type IS NULL)
        WHERE t.active_main IS TRUE
            AND t.is_objective IS TRUE
            AND (t.uppies_code BETWEEN 100 AND 299 OR t.uppies_code IS NULL)
            AND (t.scanned_at_axe > now() - interval '7 days' OR t.scanned_at_axe IS NULL)
            AND (t.queued_at_axe IS NULL OR t.queued_at_axe < now() - interval '1 hour')
        ORDER BY t.queued_at_axe ASC NULLS FIRST
        LIMIT %s;
    """
    result = execute_select(select_query, (batch_size,), fetchone=False)  # Set fetchone to False
    logger.debug(f'Selected URLs: {result}')
    return result

