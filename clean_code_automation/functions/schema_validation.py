import pandera as pd
from pandera import Column, DataFrameSchema, Check
from pandera.errors import SchemaError

def validate_event_log_schema(df):
    """
    Validate the schema of the event log DataFrame.
    """
    schema = DataFrameSchema({
        "user_id": Column(int, Check.ge(0), nullable=False),
        "event_type": Column(str, Check.isin(["wishlist_add", "login", "checkout","search", "profile_update", "page_view", "add_to_cart"]), nullable=False),
        "product_id": Column(str, nullable=False),
        "amount": Column(int, Check.ge(0), nullable=False),
        "date": Column(str, Check.is_datetime64(), nullable=False),
        "time": Column(str, Check.is_datetime64(), nullable=True),
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
    schema = DataFrameSchema({
        "date": Column(str, nullable=False),
        "users_active": Column(str, Check.is_datetime64(), nullable=False),
        "total_sales": Column(str, Check.is_datetime64(), nullable=False),
        "new_customers": Column(float, Check.ge(0), nullable=False),
        "report_date": Column(int, Check.ge(0), nullable=True),
        "report_time": Column(int, Check.ge(0), nullable=True)
    })

    try:
        schema.validate(df)
        return True
    except SchemaError as e:
        print(f"Schema validation error: {e}")
        return False