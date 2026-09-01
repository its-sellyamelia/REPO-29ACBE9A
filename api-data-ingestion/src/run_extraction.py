from api_client import DummyJsonClient
from extractor import extract_all_products


BASE_URL = "https://dummyjson.com"

client = DummyJsonClient(BASE_URL)


products = extract_all_products(
    client,
    batch_size=30
)

print(products[0])
print()
print(f"Total products extracted: {len(products)}")