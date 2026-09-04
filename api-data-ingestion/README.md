# API Data Ingestion Pipeline

A Python-based data ingestion pipeline that retrieves product data from a REST API, handles pagination, validates and transforms the data, and loads it into PostgreSQL.

This project was developed as part of the Data Engineering Internship Program at InternCareerPath.

---

## Project Overview

External APIs are commonly used as data sources in modern data engineering systems. However, API data cannot always be retrieved through a single request and may require pagination, validation, transformation, incremental processing, and error handling.

This project implements a simple but structured ETL-style pipeline that:

1. Extracts product data from DummyJSON REST API
2. Handles API pagination
3. Validates incoming data
4. Transforms API fields into a database-friendly structure
5. Loads data into PostgreSQL
6. Performs incremental updates using source timestamps
7. Handles API failures using retry and exponential backoff
8. Tracks pipeline execution status using `pipeline_state`

---

## Architecture

```text
                  DummyJSON REST API
                         |
                         v
                  +--------------+
                  | API Client   |
                  |              |
                  | Timeout      |
                  | Retry        |
                  | Backoff      |
                  +------+-------+
                         |
                         v
                  +--------------+
                  |  Extractor   |
                  |              |
                  | Pagination   |
                  +------+-------+
                         |
                         v
                  +--------------+
                  |  Validator   |
                  +------+-------+
                         |
                         v
                  +--------------+
                  | Transformer  |
                  +------+-------+
                         |
                         v
                  +--------------+
                  |    Loader    |
                  |              |
                  | PostgreSQL   |
                  | UPSERT       |
                  +------+-------+
                         |
              +----------+----------+
              |                     |
              v                     v
        +-----------+       +---------------+
        | products  |       | pipeline_state|
        +-----------+       +---------------+
              |
              v
       Incremental Load

## Pipeline Flow
Extract → Paginate → Validate → Transform → Incremental Load → PostgreSQL → Pipeline State

## Data Source
This project uses the DummyJSON Products API as the external data source.

- API Base URL: https://dummyjson.com

Endpoint:
https://dummyjson.com/products

The API provides product information such as:
- Product ID
- Product title
- Price
- Category
- Rating
- Stock
- Product metadata
- Last updated timestamp

The API response contains pagination information including:
- total
- skip
- limit
```
