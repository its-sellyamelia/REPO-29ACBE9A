import psycopg2
from psycopg2.extras import execute_values


def get_connection(db_config: dict):
    return psycopg2.connect(
        host=db_config["host"],
        port=db_config["port"],
        database=db_config["database"],
        user=db_config["user"],
        password=db_config["password"],
    )


def load_products(products: list[dict], db_config: dict):
    if not products:
        return 0

    connection = get_connection(db_config)

    try:
        with connection.cursor() as cursor:

            query = """
                INSERT INTO products (
                    product_id,
                    title,
                    price,
                    category,
                    rating,
                    stock,
                    source_updated_at,
                    ingested_at,
                    updated_at
                )
                VALUES %s
                ON CONFLICT (product_id)
                DO UPDATE SET
                    title = EXCLUDED.title,
                    price = EXCLUDED.price,
                    category = EXCLUDED.category,
                    rating = EXCLUDED.rating,
                    stock = EXCLUDED.stock,
                    source_updated_at = EXCLUDED.source_updated_at,
                    ingested_at = EXCLUDED.ingested_at,
                    updated_at = CURRENT_TIMESTAMP
                WHERE EXCLUDED.source_updated_at > products.source_updated_at
            """

            values = [
                (
                    product["product_id"],
                    product["title"],
                    product["price"],
                    product["category"],
                    product["rating"],
                    product["stock"],
                    product["source_updated_at"],
                    product["ingested_at"],
                    product["ingested_at"],
                )
                for product in products
            ]

            execute_values(cursor, query, values)

            affected_rows = cursor.rowcount

        connection.commit()

        return affected_rows

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()