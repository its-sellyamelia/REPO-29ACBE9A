import os

from dotenv import load_dotenv

from api_client import DummyJsonClient
from extractor import extract_all_products
from validator import validate_product
from transformer import transform_product
from loader import load_products
from incremental import update_pipeline_state


load_dotenv()


def main():

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

    # Database connection
    import psycopg2

    connection = psycopg2.connect(
        host=db_config["host"],
        port=db_config["port"],
        database=db_config["database"],
        user=db_config["user"],
        password=db_config["password"],
    )

    try:

        print("=" * 50)
        print("DATA INGESTION PIPELINE STARTED")
        print("=" * 50)

        # =========================
        # EXTRACT
        # =========================

        client = DummyJsonClient(
            base_url,
            max_retries=3,
            timeout=10
        )

        products = extract_all_products(
            client,
            batch_size=30
        )

        print(f"\nTotal extracted: {len(products)}")

        # =========================
        # VALIDATE + TRANSFORM
        # =========================

        valid_products = []

        for product in products:

            if validate_product(product):

                transformed = transform_product(product)

                valid_products.append(transformed)

        print(f"Valid products: {len(valid_products)}")

        # =========================
        # LOAD
        # =========================

        affected_rows = load_products(
            valid_products,
            db_config
        )

        print(f"Rows affected: {affected_rows}")

        # =========================
        # PIPELINE STATE
        # =========================

        last_processed_id = max(
            product["product_id"]
            for product in valid_products
        )

        update_pipeline_state(
            connection,
            last_processed_id=last_processed_id,
            status="SUCCESS"
        )

        connection.commit()

        print("\nPipeline status: SUCCESS")

    except Exception as error:

        connection.rollback()

        print("\nPipeline status: FAILED")
        print(f"Error: {error}")

        try:

            update_pipeline_state(
                connection,
                status="FAILED"
            )

            connection.commit()

        except Exception:

            connection.rollback()

        raise

    finally:

        connection.close()


if __name__ == "__main__":
    main()