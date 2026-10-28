import pandas as pd
import numpy as np

aversion = [2, 4, 6, 7, 8, 9, 10]  # Example risk aversion levels

statistics = pd.read_csv('data/asset_statistics.csv', index_col=0)

covariance_matrix = pd.read_csv('data/asset_covariance.csv', index_col=0)

#Utility = Returns - 0.5 * Risk Aversion * Variance

returns = statistics['Annualized Returns']
variance = statistics['Annualized Volatility'] ** 2 #or Covariance matrix diagonal elements np.diag(covariance_matrix)

print(np.allclose(variance, np.diag(covariance_matrix)))  # Check if variance matches the diagonal of the covariance matrix

utility = pd.DataFrame(index=statistics.index)

for a in aversion:
    utility_a = returns - 0.5 * a * variance
    utility[a] = utility_a

print(utility.round(3))  # Display the utility values for the given risk aversion level

print(utility.idxmax())  # Display the asset with the highest utility for each risk aversion level
print(utility[2].sort_values(ascending=False))
