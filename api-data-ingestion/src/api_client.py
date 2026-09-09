import time
import requests


class DummyJsonClient:

    def __init__(
        self,
        base_url: str,
        max_retries: int = 3,
        timeout: int = 10
    ):
        self.base_url = base_url.rstrip("/")
        self.max_retries = max_retries
        self.timeout = timeout

    def get_products(
        self,
        limit: int = 30,
        skip: int = 0
    ):

        url = f"{self.base_url}/products"

        params = {
            "limit": limit,
            "skip": skip
        }

        for attempt in range(1, self.max_retries + 1):

            try:

                print(
                    f"Requesting products "
                    f"(skip={skip}, limit={limit}) "
                    f"[attempt {attempt}/{self.max_retries}]"
                )

                response = requests.get(
                    url,
                    params=params,
                    timeout=self.timeout
                )

                # Retry untuk error server / rate limit
                if response.status_code in {
                    429,
                    500,
                    502,
                    503,
                    504
                }:

                    if attempt == self.max_retries:
                        response.raise_for_status()

                    wait_time = 2 ** (attempt - 1)

                    print(
                        f"API returned {response.status_code}. "
                        f"Retrying in {wait_time}s..."
                    )

                    time.sleep(wait_time)

                    continue

                # Error lain yang tidak perlu retry
                response.raise_for_status()

                return response.json()

            except requests.exceptions.Timeout:

                if attempt == self.max_retries:
                    raise

                wait_time = 2 ** (attempt - 1)

                print(
                    f"Request timeout. "
                    f"Retrying in {wait_time}s..."
                )

                time.sleep(wait_time)

            except requests.exceptions.ConnectionError:

                if attempt == self.max_retries:
                    raise

                wait_time = 2 ** (attempt - 1)

                print(
                    f"Connection error. "
                    f"Retrying in {wait_time}s..."
                )

                time.sleep(wait_time)

        raise RuntimeError(
            "Failed to retrieve products after retries."
        )