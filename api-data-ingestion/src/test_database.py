import os

import psycopg2
from dotenv import load_dotenv


load_dotenv()

try:
    connection = psycopg2.connect(
        host=os.getenv("DATABASE_HOST"),
        port=os.getenv("DATABASE_PORT"),
        database=os.getenv("DATABASE_NAME"),
        user=os.getenv("DATABASE_USER"),
        password=os.getenv("DATABASE_PASSWORD"),
    )

    print("Database connection successful!")

    connection.close()

except psycopg2.Error as error:
    print("Database connection failed!")
    print("Error:", error)