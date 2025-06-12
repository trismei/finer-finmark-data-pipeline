import pandas as pd
import numpy as np
import sys
import os
import clean_event_logs
import datetime

def import_data(file_path):

    # Read the dataset
    df = pd.read_csv(file_path, header=None)

    #Check file to categorize it
    filename = os.path.basename(file_path)

    if 'event_log' in filename:
        slice_column = 5
        df = df.iloc[:, :slice_column]

        clean_data = clean_event_logs.clean_event_logs(df)
        # Ensure the output directory exists
        output_dir = os.path.join("datasets", "cleaned")
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, f"{os.path.basename(file_path)}_cleaned_{datetime.date.today()}.csv")
        clean_data.to_csv(output_path, index=False, header=False)
    elif 'marketing_summary' in filename:
        slice_column = 5
        df = df.iloc[:, :slice_column]

        output_dir = os.path.join("datasets", "cleaned")
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, f"{os.path.basename(file_path)}_cleaned_{datetime.date.today()}.csv")
        df.to_csv(output_path, index=False, header=False)
    elif 'trend_report' in filename:
        slice_column = 3
        df = df.iloc[:, :slice_column]


        output_dir = os.path.join("datasets", "cleaned")
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, f"{os.path.basename(file_path)}_cleaned_{datetime.date.today()}.csv")
        df.to_csv(output_path, index=False, header=False)

    return df


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python clean_data.py <dataset1>")
        sys.exit(1)
    import_data(sys.argv[1])
