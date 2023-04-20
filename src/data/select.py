from data.access import connection
from utils.watch import logger

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
def get_uppies():
    query = """
        UPDATE processing.uppies_urls
        SET processed = true
        WHERE url_id IN (
          SELECT url_id
          FROM processing.uppies_urls
          WHERE processed = false
          LIMIT 10
        )
        RETURNING url, url_id;
    """


def next_tech_url():
    query = """
        SELECT url AS "target",
               id AS "url_id"
        FROM (
          SELECT *
          FROM targets.urls
          WHERE active_main IS TRUE
            AND active_scan_tech IS TRUE
            AND url NOT ilike '%?%'
          ORDER BY created_at DESC
          LIMIT 500
        ) AS subquery
        OFFSET floor(random() * 100)
        LIMIT 1;
    """
    result = execute_select(query)
    if result:
        target, url_id = result
        logger.info(f'🗄️🔍 Next Tech Check URL: {target}')
        return target, url_id
    else:
        logger.error(f'🗄️🔍 Unable to Tech Check URL')
        return None, None