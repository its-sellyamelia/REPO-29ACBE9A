import os

from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

def load_data(df, table_name):

    database_url = (
        f"postgresql+psycopg2://"
        f"{os.getenv('DATABASE_USER')}:"
        f"{os.getenv('DATABASE_PASSWORD')}@"
        f"{os.getenv('DATABASE_HOST')}:"
        f"{os.getenv('DATABASE_PORT')}/"
        f"{os.getenv('DATABASE_NAME')}"
    )

    engine = create_engine(database_url)

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

    print(f"Loaded {len(df)} rows into {table_name}")