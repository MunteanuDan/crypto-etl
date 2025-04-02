# Crypto ETL Pipeline (Python + PostgreSQL)

This project is a complete ETL (Extract, Transform, Load) pipeline that fetches real-time cryptocurrency data from the CoinGecko API, transforms it using pandas, and loads it into a PostgreSQL database. The pipeline is modular, testable, and designed to be extended for automation and visualization.

## Features

- Extracts top 10 cryptocurrencies from CoinGecko public API
- Transforms raw data:
  - Keeps only relevant fields
  - Cleans column names (snake_case)
  - Converts symbols to uppercase
  - Drops rows with missing values
- Loads cleaned data into PostgreSQL using SQLAlchemy
- Includes unit tests for transformation logic with pytest
- Project structured for extensibility (e.g., dashboard, scheduler)

## Tech Stack

- Python 3.12
- Libraries:
  - `pandas`
  - `requests`
  - `sqlalchemy`
  - `psycopg2`
  - `pytest`
- PostgreSQL
- IDE: PyCharm (recommended)