from src.extractor import extract_all_products


class MockClient:

    def get_products(self, limit, skip):

        if skip == 0:
            return {
                "products": [
                    {"id": 1},
                    {"id": 2},
                    {"id": 3}
                ],
                "total": 5
            }

        return {
            "products": [
                {"id": 4},
                {"id": 5}
            ],
            "total": 5
        }


def test_extract_all_products():

    client = MockClient()

    products = extract_all_products(
        client,
        batch_size=3
    )

    assert len(products) == 5
    assert products[0]["id"] == 1
    assert products[-1]["id"] == 5