import pandas as pd

def clean_marketing_summary(dataframe):

    slice_column = 5
    headers = ['date', 'users_active', 'total_sales', 'new_customers', 'report_generated']
    df = pd.read_csv(dataframe, header=None, names=headers, usecols=range(slice_column))

    # Check if the df is empty
    if df.empty:
        print("The df is empty.")
        return df
    else:
        # Remove rows with all NaN values
        cleaned_df = df.dropna(how='any')

    #Check if 'report_generated' column exists and convert it to datetime
    try:
        cleaned_df['report_generated'] = pd.to_datetime(cleaned_df['report_generated'], errors='coerce')
        cleaned_df['report_date'] = cleaned_df['report_generated'].dt.date
        cleaned_df['report_time'] = cleaned_df['report_generated'].dt.time
        cleaned_df = cleaned_df.drop('report_generated', axis=1)
    except KeyError:
        print("The 'report_generated' column is not present in the DataFrame.")
        return cleaned_df

    return cleaned_df