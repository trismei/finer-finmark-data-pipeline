import sys
from db.connection import create_connection, close_connection
from ingest.load_data import load_data_to_db

def main():
    # Establish a database connection
    connection = create_connection()
    
    if connection is None:
        print("Error! Cannot create the database connection.")
        sys.exit(1)

    try:
        # Load data into the database
        load_data_to_db(connection)
        print("Data loaded successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the database connection
        close_connection(connection)

if __name__ == "__main__":
    main()