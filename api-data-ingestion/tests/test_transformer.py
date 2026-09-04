from src.transformer import transform_product


def test_transform_product():

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

    result = transform_product(product)

    assert result["product_id"] == 1
    assert result["title"] == "Test Product"
    assert result["price"] == 10.5
    assert result["category"] == "beauty"
    assert result["rating"] == 4.5
    assert result["stock"] == 100
    assert result["source_updated_at"] is not None
    assert result["ingested_at"] is not None