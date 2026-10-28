import pandas as pd
import numpy as np

statistics = pd.read_csv('data/asset_statistics.csv', index_col=0)
returns = statistics['Annualized Returns']
volatility = statistics['Annualized Volatility']
covariance = pd.read_csv('data/asset_covariance.csv', index_col=0)


number_of_assets = len(returns)
print(f"Number of assets: {number_of_assets}")

w = np.ones(number_of_assets) / number_of_assets  # Equal weights for each asset
print(f"Asset weights: {w}")
total_w = np.sum(w)
print(f"Total weight: {total_w}")

print(returns.index)  # Display the asset names
print(covariance.index)  # Display the asset names in the covariance matrix
print(covariance.columns)  # Display the asset names in the covariance matrix
print(returns.index.equals(covariance.index) and returns.index.equals(covariance.columns)) # Check if the asset names match between returns and covariance matrix

returns_array = returns.to_numpy()  # Convert returns to a NumPy array
covariance_array = covariance.to_numpy()  # Convert covariance matrix to a NumPy array

portfolio_return = w @ returns_array  # Calculate the expected portfolio return
portfolio_variance = w @ covariance_array @ w  # Calculate the portfolio variance
portfolio_volatility = np.sqrt(portfolio_variance)  # Calculate the portfolio volatility

print(f"Expected Portfolio Return: {portfolio_return:.4f}")
print(f"Portfolio Variance: {portfolio_variance:.4f}")
print(f"Portfolio Volatility: {portfolio_volatility:.4f}")


