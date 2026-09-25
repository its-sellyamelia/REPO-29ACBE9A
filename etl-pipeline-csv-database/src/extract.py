import pandas as pd

def extract_data(file_path):
    df = pd.read_csv(file_path)

    print(f"Data extracted: {len(df)} rows")

    return df