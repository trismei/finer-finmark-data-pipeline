import pandas as pd
import numpy as np
import sys
import os
import functions.clean_event_logs as clean_event_logs
import functions.clean_marketing_summary as clean_marketing_summary
import functions.clean_trend_report as clean_trend_report
import datetime
from sqlalchemy import create_engine

def import_data(file_path):

    dataframe = sys.argv[1]
    #Initialize the Database connection
    engine = create_engine('sqlite:///finmark_database.db')

    #Check file to categorize it
    filename = os.path.basename(file_path)

    if 'event_log' in filename:
        try:
            #Read the CSV file into a dataframe and validate if the columns noted are present
            present_columns = ['user_id', 'event_type', 'event_time', 'product_id', 'amount']
            dataframe = pd.read_csv(file_path)
            validate_columns(dataframe, present_columns)
        except pd.errors.EmptyDataError:
            raise ValueError(f"File {filename} is empty or does not contain valid data.")
        # Clean the event logs data
        clean_data = clean_event_logs.clean_event_logs(dataframe, present_columns)[1:]
        
        # Uncomment the following lines if you want to save the cleaned data to a CSV file

        output_path = standardize_output_filename(file_path)
        clean_data.to_csv(output_path, index=False, header=True)

        # # Save the cleaned data to the database
        # clean_data.to_sql(filename, con=engine, if_exists='append', index=False)

    elif 'marketing_summary' in filename:
        try:
            # Read the CSV file into a dataframe and validate if the columns noted are present
            present_columns = ['date', 'users_active', 'total_sales', 'new_customers', 'report_generated']
            dataframe = pd.read_csv(file_path)
            # Validate if the required columns are present
            validate_columns(dataframe, present_columns)
            # if not all(col in dataframe.columns for col in present_columns):
            #     raise ValueError(f"File {filename} does not contain the required columns: {present_columns}")
        except pd.errors.EmptyDataError:
            raise ValueError(f"File {filename} is empty or does not contain valid data.")
        
        # Clean the marketing summary data
        clean_data = clean_marketing_summary.clean_marketing_summary(dataframe, present_columns)[1:]
        
        # output_path = standardize_output_filename(file_path)
        # clean_data.to_csv(output_path, index=False, header=True)

        clean_data.to_sql(filename, con=engine, if_exists='append', index=False)

    elif 'trend_report' in filename:
        try:
            # Read the CSV file into a dataframe and validate if the columns noted are present
            present_columns = ['weeks', 'avg_user', 'sales_growth_rate']
            dataframe = pd.read_csv(file_path)
            # Validate if the required columns are present
            validate_columns(dataframe, present_columns)
        except pd.errors.EmptyDataError:
            raise ValueError(f"File {filename} is empty or does not contain valid data.")

        clean_data = clean_trend_report.clean_trend_report(dataframe)[1:]
        
        # output_path = standardize_output_filename(file_path)
        # clean_data.to_csv(output_path, index=False, header=True)

        clean_data.to_sql(filename, con=engine, if_exists='append', index=False)

    return FileExistsError(f"File {filename} already exists. Please choose a different name or delete the existing file.")

def standardize_output_filename(file_path):
    """
    Standardizes the output filename by removing special characters and replacing spaces with underscores.
    """
    output_dir = os.path.join("datasets", "cleaned")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"{os.path.basename(file_path)}_cleaned_{datetime.date.today()}.csv")

    return output_path

def validate_columns(dataframe, required_columns):
    """
    Validates if the required columns are present in the dataframe.
    """
    for col in required_columns:
        if col not in dataframe.columns:
            raise ValueError(f"File does not contain the required column: {col}")
    return True

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: py clean_data.py <dataset1>")
        sys.exit(1)
    import_data(sys.argv[1])
