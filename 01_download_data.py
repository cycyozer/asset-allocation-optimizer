import pandas as pd
import yfinance as yf
import os

def download_stock_data(ticker, start_date, end_date):
    """
    Downloads historical stock data for a given ticker symbol from Yahoo Finance.

    Parameters:
    ticker (str): The stock ticker symbol (e.g., 'AAPL' for Apple).
    start_date (str): The start date for the data in 'YYYY-MM-DD' format.
    end_date (str): The end date for the data in 'YYYY-MM-DD' format.

    Returns:
    pd.DataFrame: A DataFrame containing the historical stock data.
    """
    try:
        # Download historical stock data
        stock_data = yf.download(ticker, start=start_date, end=end_date)["Close"]

        return stock_data
    except Exception as e:
        print(f"An error occurred while downloading data for {ticker}: {e}")
        return None

#In order: Gold, S&P 500, Russell 2000, MSCI EAFE, MSCI Emerging Markets, 20+ Year Treasury Bond, Total Bond Market, 
# Investment Grade Corporate Bonds, High Yield Corporate Bonds, Real Estate Investment Trusts, Commodities
tickers = ['GLD', 'SPY', 'IWM', 'EFA', 'EEM', 'TLT', 'AGG', 'LQD', 'HYG', 'VNQ', 'DBC'   ]  # List of stock tickers to download
start_date = '2007-05-01'
end_date = '2026-06-30'

Data = download_stock_data(tickers, start_date, end_date)

print(Data.head())  # Display the first few rows of the data

print(Data.isna().sum())  # Check for missing values in the data
print(Data.shape)

Data.to_csv('data/historical_stock_data.csv', index=True)  # Save the data to a CSV file

