from datetime import datetime, timezone


def transform_product(product: dict) -> dict:
    return {
        "product_id": product["id"],
        "title": product["title"].strip(),
        "price": float(product["price"]),
        "category": product["category"].strip().lower(),
        "rating": float(product["rating"]),
        "stock": int(product["stock"]),
        "source_updated_at": product["meta"]["updatedAt"],
        "ingested_at": datetime.now(timezone.utc),
    }