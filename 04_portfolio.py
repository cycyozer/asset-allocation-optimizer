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

#We can compute the utility for the portfolio using the formula: Utility = Expected Return - 0.5 * Risk Aversion * Variance 
# for a given risk aversion level. This will help us understand how attractive the equally weighted portfolio is for different levels of risk aversion.

aversion = [2, 4, 6, 7, 8, 9, 10]  # Risk aversion levels

comparison = pd.DataFrame(index=aversion, columns=["Equal-weight portfolio", "SPY", "AGG"], dtype=float)
comparison.index.name = "Risk aversion"

for a in aversion:
    comparison.loc[a, "Equal-weight portfolio"] = portfolio_return - 0.5 * a * portfolio_variance
    comparison.loc[a, "SPY"] = returns["SPY"] - 0.5 * a * volatility["SPY"] ** 2
    comparison.loc[a, "AGG"] = returns["AGG"] - 0.5 * a * volatility["AGG"] ** 2

print(comparison.round(3))
print(comparison.idxmax(axis=1))  # Best option for each risk aversion level

#The utility values for the equal-weighted portfolio, SPY, and AGG can be compared to see which one is more attractive for a given risk aversion level.
#We can see that the utility of the equally weighted portfolio is always lower than that of SPY and AGG, indicating that the equally weighted portfolio is not as attractive as investing in either SPY or AGG for any level of risk aversion.
