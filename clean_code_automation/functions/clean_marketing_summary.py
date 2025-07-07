import pandas as pd

def clean_marketing_summary(df, headers):

    # Initially clean the DataFrame to the required headers
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
    errors='coerce')
        cleaned_df['report_date'] = cleaned_df['report_generated'].dt.date
        cleaned_df['report_time'] = cleaned_df['report_generated'].dt.time
        cleaned_df = cleaned_df.drop('report_generated', axis=1)
    except Exception as e:
        print(f"Error: {e}")
        return df
    
    # Calculate, convert to percentage, and round to 2 decimal places in one line
    cleaned_df['percent_customer_change_per_day(%)'] = (cleaned_df['users_active'].pct_change() * 100).round(2)
    # Calculate total sales growth rate
    cleaned_df['sales_growth_rate(%)'] = (cleaned_df['total_sales'].pct_change() * 100).round(2)
    # Calculate average sales per user
    cleaned_df['avg_sales_per_user($)'] = (cleaned_df['total_sales'] / cleaned_df['users_active']).round(2)

    # The first value will be NaN (Not a Number), so we can fill it with 0
    cleaned_df.fillna(0, inplace=True)

    return cleaned_df

#For testing purposes
# clean_marketing_summary('../datasets/marketing_summary.csv')

