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

#SPY is equity and AGG is bond, so the utility values for these two assets can be compared to see which one is more attractive for a given risk aversion level.
#And thus see at which risk aversion level the investor would prefer to invest in equity or bond.

breakeven_aversion = 2*(returns["SPY"] - returns["AGG"])/(variance["SPY"] - variance["AGG"])
print(f"Breakeven risk aversion level: {breakeven_aversion:.2f}")

#For risk aversion below 7.41, an investor would prefer to invest in equity (SPY) over bond (AGG), 
# while for risk aversion above 7.41, the investor would prefer to invest in bond (AGG) over equity (SPY).