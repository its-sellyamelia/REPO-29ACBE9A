from typing import Any


def validate_product(product: dict[str, Any]) -> bool:
    required_fields = [
        "id",
        "title",
        "price",
        "category",
        "rating",
        "stock",
    ]

    # Check required fields
    for field in required_fields:
        if field not in product:
            return False

    # Validate ID
    if not isinstance(product["id"], int) or product["id"] <= 0:
        return False

    # Validate title
    if not isinstance(product["title"], str) or not product["title"].strip():
        return False

    # Validate price
    if not isinstance(product["price"], (int, float)) or product["price"] < 0:
        return False

    # Validate category
    if (
        not isinstance(product["category"], str)
        or not product["category"].strip()
    ):
        return False

    # Validate rating
    if (
        not isinstance(product["rating"], (int, float))
        or not 0 <= product["rating"] <= 5
    ):
        return False

    # Validate stock
    if not isinstance(product["stock"], int) or product["stock"] < 0:
        return False

    return True