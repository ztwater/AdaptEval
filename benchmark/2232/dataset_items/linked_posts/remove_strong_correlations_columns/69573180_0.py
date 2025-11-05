
# Get correlation matrix 
corr = X.corr()

# Create a mask for values above 90% 
# But also below 100% since it variables correlated with the same one
mask = (X.corr() > 0.9) & (X.corr() < 1.0)
high_corr = corr[mask]

# Create a new column mask using any() and ~
col_to_filter_out = ~high_corr[mask].any()

# Apply new mask
X_clean = X[high_corr.columns[col_to_filter_out]]

# Visualize cleaned dataset
X_clean
