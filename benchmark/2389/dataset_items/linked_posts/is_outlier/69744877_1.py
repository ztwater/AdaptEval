# Imports
from hampel import hampel
import pandas as pd

list_d = [2, 4, 5, 1, 6, 5, 40]

# List to Series
time_series = pd.Series(list_d)

# Outlier detection with Hampel filter
# Returns the Outlier indices
outlier_indices = hampel(ts = time_series, window_size = 3)

# Drop Outliers indices from Series
filtered_d = time_series.drop(outlier_indices)

filtered_d.values.tolist()

print(f'filtered_d: {filtered_d.values.tolist()}')
