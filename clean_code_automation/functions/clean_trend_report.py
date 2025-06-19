import pandas as pd
from datetime import datetime, timedelta

def clean_trend_report(df, headers):
    # Initially clean the DataFrame to the required headers
    df = df[headers]

    # Check if the DataFrame is empty
    if df.empty:
        print("The DataFrame is empty.")
        return df
    else:
        # Remove rows with any NaN values
        df = df.dropna(how='any')
    try:
        df[['week_start', 'week_end']] = df['week'].apply(lambda x: pd.Series(weeks_to_date(x)))
        df = df.drop('week', axis=1)
        #Position the new columns at the beginning
        df = df[['week_start', 'week_end'] + [col for col in df.columns if col not in ['week_start', 'week_end']]]
    except Exception as e:
        print(f"Error processing 'week' column: {e}")
        return df
    
    return df

def weeks_to_date(week_str):
    """
    Convert a week string in the format 'YYYY-Www' to a tuple of start and end dates.
    """
    week_str = week_str.strip()
    try:
        monday = datetime.strptime(week_str + '-1', "%Y-W%W-%w")
        sunday = monday + timedelta(days=6)
        return monday.strftime('%m/%d/%Y'), sunday.strftime('%m/%d/%Y')
    except Exception:
        return None, None
