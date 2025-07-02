import yfinance as yf
import os

def download_yahoo_data(symbol, start, end, filename):
    """
    Download historical data from Yahoo Finance and save it as a CSV file.
    
    Parameters:
        symbol (str): e.g., "AAPL"
        start (str): e.g., "2022-01-01"
        end (str): e.g., "2023-12-31"
        filename (str): e.g., "data/aapl_sample.csv"
    """
    df = yf.download(symbol, start=start, end=end)
    df.to_csv(filename)
    print(f"save {symbol} data to {filename}")
