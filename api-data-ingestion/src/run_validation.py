from api_client import DummyJsonClient
from extractor import extract_all_products
from validator import validate_product
from transformer import transform_product


BASE_URL = "https://dummyjson.com"

client = DummyJsonClient(BASE_URL)

products = extract_all_products(
    client,
    batch_size=30
)

valid_products = []
invalid_products = []

for product in products:
    if validate_product(product):
        transformed = transform_product(product)
        valid_products.append(transformed)
    else:
        invalid_products.append(product)


print()
print("Validation Result")
print("-----------------")
print(f"Total extracted : {len(products)}")
print(f"Valid products  : {len(valid_products)}")
print(f"Invalid products: {len(invalid_products)}")

if valid_products:
    print()
    print("Sample transformed product:")
    print(valid_products[0])