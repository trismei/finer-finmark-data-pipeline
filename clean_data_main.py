import pandas as pd
import numpy as np
import sys
import os
import functions.clean_event_logs as clean_event_logs
import functions.clean_marketing_summary as clean_marketing_summary
import functions.clean_trend_report as clean_trend_report
import datetime

def import_data(file_path):

    dataframe = sys.argv[1]

    #Check file to categorize it
    filename = os.path.basename(file_path)

    if 'event_log' in filename:
        clean_data = clean_event_logs.clean_event_logs(dataframe)[1:]
        # Ensure the output directory exists
        output_path = standardize_output_filename(file_path)
        clean_data.to_csv(output_path, index=False, header=True)
    elif 'marketing_summary' in filename:
        clean_data = clean_marketing_summary.clean_marketing_summary(dataframe)[1:]
        output_path = standardize_output_filename(file_path)
        clean_data.to_csv(output_path, index=False, header=True)
    elif 'trend_report' in filename:
        clean_data = clean_trend_report.clean_trend_report(dataframe)[1:]
        output_path = standardize_output_filename(file_path)
        clean_data.to_csv(output_path, index=False, header=True)

    return FileExistsError(f"File {output_path} already exists. Please choose a different name or delete the existing file.")

def standardize_output_filename(file_path):
    """
    Standardizes the output filename by removing special characters and replacing spaces with underscores.
    """
    output_dir = os.path.join("datasets", "cleaned")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"{os.path.basename(file_path)}_cleaned_{datetime.date.today()}.csv")

    return output_path


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python clean_data.py <dataset1>")
        sys.exit(1)
    import_data(sys.argv[1])
