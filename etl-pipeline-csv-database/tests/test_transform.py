import pandas as pd

from src.transform import transform_data


def test_transform_data():
    df = pd.DataFrame({
        "order_id": [1],
        "order_date": ["2026-01-01"],
        "customer_name": [" Andi "],
        "product": [" Laptop "],
        "category": [" Electronics "],
        "quantity": [2],
        "price": [8500000]
    })

    result = transform_data(df)

    assert pd.api.types.is_datetime64_any_dtype(result["order_date"])
    assert result["customer_name"].iloc[0] == "Andi"
    assert result["product"].iloc[0] == "Laptop"
    assert result["category"].iloc[0] == "Electronics"
    assert result["total_amount"].iloc[0] == 17000000