import pandas as pd
import pytest

from src.transform import validate_data


def test_validate_valid_data():
    df = pd.DataFrame({
        "order_id": [1, 2],
        "order_date": ["2026-01-01", "2026-01-02"],
        "customer_name": ["Andi", "Budi"],
        "product": ["Laptop", "Mouse"],
        "category": ["Electronics", "Accessories"],
        "quantity": [1, 2],
        "price": [8500000, 150000]
    })

    assert validate_data(df) is True


def test_validate_duplicate_order_id():
    df = pd.DataFrame({
        "order_id": [1, 1],
        "quantity": [1, 2],
        "price": [100000, 200000]
    })

    with pytest.raises(ValueError):
        validate_data(df)


def test_validate_invalid_quantity():
    df = pd.DataFrame({
        "order_id": [1],
        "quantity": [0],
        "price": [100000]
    })

    with pytest.raises(ValueError):
        validate_data(df)


def test_validate_invalid_price():
    df = pd.DataFrame({
        "order_id": [1],
        "quantity": [1],
        "price": [-100000]
    })

    with pytest.raises(ValueError):
        validate_data(df)