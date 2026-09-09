from src.validator import validate_product


def test_valid_product():

    product = {
        "id": 1,
        "title": "Test Product",
        "price": 10.5,
        "category": "beauty",
        "rating": 4.5,
        "stock": 100,
        "meta": {
            "updatedAt": "2025-04-30T09:41:02.053Z"
        }
    }

    assert validate_product(product) is True


def test_invalid_product():

    product = {
        "id": 1,
        "title": "",
        "price": 10.5,
        "category": "beauty",
        "rating": 4.5,
        "stock": 100,
        "meta": {
            "updatedAt": "2025-04-30T09:41:02.053Z"
        }
    }

    assert validate_product(product) is False
