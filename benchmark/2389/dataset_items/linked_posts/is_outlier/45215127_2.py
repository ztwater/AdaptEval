y = x[abs(x - p50) < rSig*5]

# Print the statistics again
print("Mean= ", np.mean(y))
print("Median= ", np.median(y))
print("Max/Min=", y.max(), " ", y.min())
print("StdDev=", np.std(y))
