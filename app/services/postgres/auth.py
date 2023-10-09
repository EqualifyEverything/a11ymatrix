# app/services/postgres/auth.py
"""Module for managing PostgreSQL database connections.

This module provides a class for managing PostgreSQL database connections
with support for setting connection parameters through environment variables.

"""

import os
import psycopg2
from psycopg2 import sql


class PostgreSQLConnection:
    """A class to manage PostgreSQL database connections.

    Attributes:
        host: Database host address.
        port: Database connection port.
        user: Database user.
        password: Database user password.
        db_name: Database name.
        conn: The psycopg2 connection object.
        cur: The psycopg2 cursor object.
    """

    def __init__(self) -> None:
        """Initialize a new PostgreSQL connection object with default or environment-specified parameters."""
        self.host = os.environ.get("POSTGRES_HOST", "db_postgres")
        self.port = int(os.environ.get("POSTGRES_PORT", "5432"))
        self.user = os.environ.get("POSTGRES_USER", "gova11y_root")
        self.password = os.environ.get("POSTGRES_PASSWORD", "a11yAllTheThings!")
        self.db_name = os.environ.get("POSTGRES_DB_NAME", "gova11y")
        self.conn = None
        self.cur = None

    def open(self) -> None:
        """Open a new database connection using the specified parameters."""
        self.conn = psycopg2.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.db_name,
        )
        self.cur = self.conn.cursor()

    def close(self) -> None:
        """Close the current database connection and cursor."""
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()

    def test(self) -> bool:
        """Test the database connection by executing a sample query.

        Returns:
            bool: True if the query executes successfully, False otherwise.
        """
        try:
            self.open()
            self.cur.execute(sql.SQL("SELECT name FROM meta.orgs WHERE id = 1"))
            result = self.cur.fetchone()
            self.close()
            return result[0] == "1"
        except Exception as e:
            print(f"Error during test: {e}")
            return False

    def get_connection_params(self) -> dict:
        """Get the connection parameters as a dictionary.

        Returns:
            dict: A dictionary containing the connection parameters.
        """
        return {
            'host': self.host,
            'port': self.port,
            'database': self.db_name,
            'user': self.user,
            'password': self.password,
        }


if __name__ == "__main__":
    # Demonstration of usage
    db_conn = PostgreSQLConnection()
    print(db_conn.test())
