import pandas as pd
from sqlalchemy import create_engine
from src.db.connection import get_connection

def load_data(file_path, table_name):
    # Establish a database connection
    engine = get_connection()
    
    # Read data from the specified file
    data = pd.read_csv(file_path)
    
    # Load data into the specified table
    data.to_sql(table_name, con=engine, if_exists='append', index=False)
    
    # Close the database connection
    engine.dispose()