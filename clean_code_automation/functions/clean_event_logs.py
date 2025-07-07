import pandas as pd


# Function to clean event logs data

def clean_event_logs(df, headers):

    # slice_column = 5
    # headers = ['user_id', 'event_type', 'event_time', 'product_id', 'amount']
    # df = pd.read_csv(dataframe, header=None, names=headers, usecols=range(slice_column))
    
    #Clean the dataframe to the required headers
    df = df[headers]

    # Check if the df is empty
    if df.empty:
        print("The df is empty.")
        return df
    else:
        # Remove rows with all NaN values
        cleaned_df = df.dropna(how='any')

    try:
        cleaned_df['event_time'] = pd.to_datetime(cleaned_df['event_time'], errors='coerce')
        #Separating date time into date time
        cleaned_df['date'] = cleaned_df['event_time'].dt.date
        cleaned_df['time'] = cleaned_df['event_time'].dt.time
    except Exception as e:
        print(f"Error: {e}")
        return df

    # Drop the original column that contained both date and time
    cleaned_df = cleaned_df.drop('event_time', axis=1)
    return cleaned_df
