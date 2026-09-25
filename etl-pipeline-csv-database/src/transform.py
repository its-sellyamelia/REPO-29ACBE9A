import pandas as pd


def validate_data(df):

    if df.empty:
        raise ValueError("Dataset is empty")

    if df["order_id"].duplicated().any():
        raise ValueError("Duplicate order_id found")

    if (df["quantity"] <= 0).any():
        raise ValueError("Invalid quantity found")

    if (df["price"] < 0).any():
        raise ValueError("Invalid price found")

    return True


def transform_data(df):

    df = df.copy()

    # Convert order_date to datetime
    df["order_date"] = pd.to_datetime(df["order_date"])

    # Remove unnecessary whitespace
    df["customer_name"] = df["customer_name"].str.strip()
    df["product"] = df["product"].str.strip()
    df["category"] = df["category"].str.strip()

    # Calculate total amount
    df["total_amount"] = df["quantity"] * df["price"]

    return df