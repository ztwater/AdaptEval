def weighted_sample_avg_std(values, weights):
    """
    Return the weighted average and weighted sample standard deviation.

    values, weights -- Numpy ndarrays with the same shape.
    
    Assumes that weights contains only integers (e.g. how many samples in each group).
    
    See also https://en.wikipedia.org/wiki/Weighted_arithmetic_mean#Frequency_weights
    """
    average = np.average(values, weights=weights)
    variance = np.average((values-average)**2, weights=weights)
    variance = variance*sum(weights)/(sum(weights)-1)
    return (average, sqrt(variance))

print(weighted_sample_avg_std(X, n))
