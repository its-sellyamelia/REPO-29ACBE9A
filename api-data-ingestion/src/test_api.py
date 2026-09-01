import requests

url = "https://dummyjson.com/products?limit=10&skip10"

response = requests.get(url, timeout=10)

print("Status:", response.status_code)

data = response.json()

print("Total:", data["total"])
print("Data received:", len(data["products"]))

