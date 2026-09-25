from src.extract import extract_data


def test_extract_data():
    df = extract_data("data/raw/sales.csv")

    assert not df.empty
    assert len(df) > 0
    assert "order_id" in df.columns