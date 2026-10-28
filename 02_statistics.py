import pandas as pd
import os
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

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

correlation_matrix = monthly_returns.corr()  # Calculate the correlation matrix
print("Correlation Matrix:")
print(correlation_matrix.round(3))  # Display the correlation matrix

covariance_matrix = monthly_returns.cov()*12  # Calculate the annualized covariance matrix
print("Covariance Matrix:")
print(covariance_matrix.round(4))  # Display the covariance matrix

#Negative covariance values indicate that the two assets tend to move in opposite directions, which can be beneficial for diversification. 
# Positive covariance values indicate that the two assets tend to move in the same direction, which may increase risk in a portfolio.

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f",vmin=-1, vmax=1)
plt.title('Correlation Matrix of Monthly Returns')
plt.savefig('figures/correlation_matrix_heatmap.png', dpi=150)  # Save the heatmap as a PNG file
plt.show()

statistics.to_csv('data/asset_statistics.csv', index=True)  # Save the statistics to a CSV file
covariance_matrix.to_csv('data/asset_covariance.csv', index=True)  # Save the covariance matrix to a CSV file