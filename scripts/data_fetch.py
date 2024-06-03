import sys
import pandas as pd
import yfinance as yf
from sqlalchemy import create_engine

# Database settings
DB_USER = 'user'
DB_PASSWORD = 'password'
DB_HOST = 'postgres_timescaledb'
DB_PORT = '5432'
DB_NAME = 'jessicadb'

# Stock symbols
SP500_SYMBOLS = ['AAPL', 'MSFT', 'GOOGL']  # Example symbols, replace with full list
RUSSELL2000_SYMBOLS = ['AMC', 'GME']  # Example symbols, replace with full list

# Create database connection
engine = create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

def fetch_stock_data(symbols):
    data = yf.download(symbols, start='2020-01-01', end='2024-01-01')
    return data

def store_data_to_db(df, table_name):
    df.to_sql(table_name, engine, if_exists='replace', index=True)

def main():
    # Fetch data for S&P 500 and Russell 2000 symbols
    sp500_data = fetch_stock_data(SP500_SYMBOLS)
    russell2000_data = fetch_stock_data(RUSSELL2000_SYMBOLS)

    # Store data in PostgreSQL
    store_data_to_db(sp500_data, 'sp500_data')
    store_data_to_db(russell2000_data, 'russell2000_data')

    print("Data fetched and stored!")
    sys.exit(0)

if __name__ == "__main__":
    main()
