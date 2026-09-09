from unittest.mock import Mock, patch

from src.api_client import DummyJsonClient


@patch("src.api_client.requests.get")
def test_get_products_success(mock_get):

    mock_response = Mock()

    mock_response.status_code = 200

    mock_response.json.return_value = {
        "products": [
            {
                "id": 1,
                "title": "Test Product"
            }
        ],
        "total": 1,
        "skip": 0,
        "limit": 30
    }

    mock_get.return_value = mock_response

    client = DummyJsonClient(
        "https://dummyjson.com"
    )

    result = client.get_products(
        limit=30,
        skip=0
    )

    assert result["total"] == 1
    assert len(result["products"]) == 1

    mock_get.assert_called_once()