import requests


class DummyJsonClient:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")

    def get_products(self, limit: int = 30, skip: int = 0):
        url = f"{self.base_url}/products"

        params = {
            "limit": limit,
            "skip": skip
        }

        response = requests.get(
            url,
            params=params,
            timeout=10
        )

        response.raise_for_status()

        return response.json()