import numpy as np
m = 51
# Generate intervals
epts = np.linspace(0,360,m+1,endpoint=True)
# Create the halfsteps between intervals (One would have sufficed)
halfsteps = (epts[1:] - epts[:-1]) / 2
# Find the midpoints
midpoints = epts[:-1] + halfsteps
# Make an unbiased rounding
results = np.around(midpoints, decimals=0)
