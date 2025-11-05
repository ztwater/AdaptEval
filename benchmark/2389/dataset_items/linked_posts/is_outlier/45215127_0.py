import numpy as np

# Create some random numbers
x = np.random.normal(5, 2, 1000)

# Calculate the statistics
print("Mean= ", np.mean(x))
print("Median= ", np.median(x))
print("Max/Min=", x.max(), " ", x.min())
print("StdDev=", np.std(x))
print("90th Percentile", np.percentile(x, 90))

# Add a few large points
x[10] += 1000
x[20] += 2000
x[30] += 1500

# Recalculate the statistics
print()
print("Mean= ", np.mean(x))
print("Median= ", np.median(x))
print("Max/Min=", x.max(), " ", x.min())
print("StdDev=", np.std(x))
print("90th Percentile", np.percentile(x, 90))

# Measure the percentile intervals and then estimate Standard Deviation of the distribution, both from median to the 90th percentile and from the 10th to 90th percentile
p90 = np.percentile(x, 90)
p10 = np.percentile(x, 10)
p50 = np.median(x)
# p50 to p90 is 1.2815 sigma
rSig = (p90-p50)/1.2815
print("Robust Sigma=", rSig)

rSig = (p90-p10)/(2*1.2815)
print("Robust Sigma=", rSig)
