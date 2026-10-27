import pandas as pd
import os
import numpy as np

Data = pd.read_csv('data/historical_stock_data.csv', index_col=0, parse_dates=True)
print(Data.head())  # Display the first few rows of the data

monthly_prices = Data.resample('ME').last()  # Resample to monthly frequency, taking the last price of each month
print(monthly_prices.head())  # Display the first few rows of the monthly prices

# Calculate monthly returns
monthly_returns = monthly_prices.pct_change().dropna()  # Calculate percentage change and drop NaN values
print(monthly_returns.head())  # Display the first few rows of the monthly returns

annualized_volatility = monthly_returns.std() * np.sqrt(12)  # Annualized volatility

annualized_returns = monthly_returns.mean() * 12  # Annualized returns

statistics = pd.DataFrame({
    'Annualized Returns': annualized_returns,
    'Annualized Volatility': annualized_volatility
})
print("Statistics:")
print(statistics.round(3))  # Display the statistics

