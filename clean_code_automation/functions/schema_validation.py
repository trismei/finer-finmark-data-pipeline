import pandas as pd
import pandera.pandas as pa
from pandera import Column, DataFrameSchema, Check
from pandera.errors import SchemaError


"""
Functions to validate the schema of the dataframes before passing it to the database.
These functions ensure that the dataframes conform to the expected structure and data types.
This helps in maintaining data integrity and prevents errors during data processing.
"""

def validate_event_log_schema(df):
    """
    Validate the schema of the event log DataFrame.
    """

    for col in df:
        if df[col].dtype == 'object':
            convert_to_datetime(df, col)

    schema = DataFrameSchema({
        "user_id": Column(int, Check.ge(0), nullable=False),
        "event_type": Column(str, Check.isin(["wishlist_add", "login", "checkout","search", "profile_update", "page_view", "add_to_cart"]), nullable=False),
        "product_id": Column(str, nullable=False),
        "amount": Column(int, Check.ge(0), nullable=False),
        "date": Column(pa.DateTime, nullable=False),
        "time": Column(pa.DateTime, nullable=True),
    })

    try:
        schema.validate(df)
        return True
    except SchemaError as e:
        print(f"Schema validation error: {e}")
        return False
    
def validate_marketing_summary_schema(df):
    """
    Validate the schema of the marketing summary DataFrame.
    """
    for col in df:
        if df[col].dtype == 'object':
            convert_to_datetime(df, col)

    schema = DataFrameSchema({
        "date": Column(pa.DateTime, nullable=False),
        "users_active": Column(int, Check.ge(0), nullable=False),
        "total_sales": Column(float, Check.ge(0), nullable=False),
        "new_customers": Column(int, Check.ge(0), nullable=False),
        "report_date": Column(pa.DateTime, nullable=True),
        "report_time": Column(pa.DateTime, nullable=True)
    })

    try:
        schema.validate(df)
        return True
    except SchemaError as e:
        print(f"Schema validation error: {e}")
        return False
    
def validate_trend_report_schema(df):
    """
    Validate the schema of the trend report DataFrame.
    """
    for col in df:
        if df[col].dtype == 'object':
            convert_to_datetime(df, col)

    schema = DataFrameSchema({
        "week_start": Column(pa.DateTime, nullable=False),
        "week_end": Column(pa.DateTime, nullable=False),
        "avg_user": Column(float, Check.ge(0), nullable=False),
        "sales_growth_rate": Column(float, nullable=False),
    })

    try:
        schema.validate(df)
        return True
    except SchemaError as e:
        print(f"Schema validation error: {e}")
        return False
    
def convert_to_datetime(df, column_name):
    """
    Convert column to datetime format
    """

    try:
        df[column_name] = pd.to_datetime(df[column_name], errors='coerce')
    except KeyError:
        print(f"The '{column_name}' column is not present in the DataFrame.")
        return df
    except Exception as e:
        print(f"Error converting '{column_name}' column to datetime: {e}")
        return df
    