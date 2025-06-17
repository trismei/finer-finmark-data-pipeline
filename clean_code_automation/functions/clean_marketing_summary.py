import pandas as pd

def clean_marketing_summary(df, headers):

    df = df[headers]

    # Check if the df is empty
    if df.empty:
        print("The df is empty.")
        return df
    else:
        # Remove rows with all NaN values
        cleaned_df = df.dropna(how='any')

    #Check if 'report_generated' column exists and convert it to datetime
    try:
        cleaned_df['report_generated'] = pd.to_datetime(
    cleaned_df['report_generated'],
    errors='coerce'
)
        cleaned_df['report_date'] = cleaned_df['report_generated'].dt.date
        cleaned_df['report_time'] = cleaned_df['report_generated'].dt.time
        cleaned_df = cleaned_df.drop('report_generated', axis=1)

        print(cleaned_df.head())

    except KeyError:
        print("The 'report_generated' column is not present in the DataFrame.")
        return cleaned_df

    return cleaned_df

#For testing purposes
# clean_marketing_summary('../datasets/marketing_summary.csv')

