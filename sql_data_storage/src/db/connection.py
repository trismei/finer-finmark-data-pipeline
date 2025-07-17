import psycopg2
from psycopg2 import sql

def connect_to_db(host, database, user, password):
    """Establish a connection to the SQL database."""
    try:
        connection = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )
        print("Connection to the database established successfully.")
        return connection
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None

def disconnect_from_db(connection):
    """Close the connection to the SQL database."""
    if connection:
        connection.close()
        print("Database connection closed.")