# app/services/postgres/execute_select.py
import psycopg2
import os

def execute_sql_from_file(conn: psycopg2.extensions.connection, filename: str, domain: str):
    with open(filename, 'r') as fd:
        sql_file = fd.read()

    formatted_sql_file = sql_file % domain

    with conn.cursor() as cur:
        cur.execute(formatted_sql_file)
        result = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]

    return result
