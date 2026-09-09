from api_client import DummyJsonClient


def extract_all_products(
    client: DummyJsonClient,
    batch_size: int = 30
):
    all_products = []

    skip = 0

    while True:
        response = client.get_products(
            limit=batch_size,
            skip=skip
        )

        products = response["products"]
        total = response["total"]

        print(
            f"Fetched {len(products)} products "
            f"(skip={skip}, total={total})"
        )

        all_products.extend(products)

        skip += batch_size

        if skip >= total:
            break

    return all_products