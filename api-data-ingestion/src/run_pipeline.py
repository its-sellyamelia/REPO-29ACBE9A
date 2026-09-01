import os

from dotenv import load_dotenv

from api_client import DummyJsonClient
from extractor import extract_all_products
from validator import validate_product
from transformer import transform_product
from loader import load_products


load_dotenv()


def main():

    # =========================
    # Configuration
    # =========================

    base_url = os.getenv(
        "API_BASE_URL",
        "https://dummyjson.com"
    )

    db_config = {
        "host": os.getenv("DATABASE_HOST"),
        "port": os.getenv("DATABASE_PORT"),
        "database": os.getenv("DATABASE_NAME"),
        "user": os.getenv("DATABASE_USER"),
        "password": os.getenv("DATABASE_PASSWORD"),
    }

    # =========================
    # Extract
    # =========================

    client = DummyJsonClient(base_url)

    products = extract_all_products(
        client,
        batch_size=30
    )

    print(f"\nTotal extracted: {len(products)}")

    # =========================
    # Validate & Transform
    # =========================

    valid_products = []

    for product in products:

        if validate_product(product):
            transformed = transform_product(product)
            valid_products.append(transformed)

    print(f"Valid products: {len(valid_products)}")

    # =========================
    # Load
    # =========================

    affected_rows = load_products(
        valid_products,
        db_config
    )

    print(f"Rows affected: {affected_rows}")


if __name__ == "__main__":
    main()