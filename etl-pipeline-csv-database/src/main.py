from extract import extract_data
from transform import transform_data, validate_data
from load import load_data


def main():

    file_path = "data/raw/sales.csv"

    print("=" * 50)
    print("ETL PIPELINE STARTED")
    print("=" * 50)

    # Extract
    df = extract_data(file_path)

    # Validate
    validate_data(df)
    print("Data validation: PASSED")

    # Transform
    df = transform_data(df)
    print("Data transformation: PASSED")

    # Load
    load_data(df, "sales")

    print("\nETL PIPELINE SUCCESS")


if __name__ == "__main__":
    main()