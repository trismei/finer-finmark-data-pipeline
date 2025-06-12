import pandas as pd
import os
import sys

def clean_event_logs(dataframe):

    cleaned_df = dataframe.copy()

    # Check if the dataframe is empty
    if dataframe.empty:
        print("The dataframe is empty.")
        return cleaned_df
    else:
        # Remove rows with all NaN values
        cleaned_df = dataframe.dropna(how='any')

    return cleaned_df