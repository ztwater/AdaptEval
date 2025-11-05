import numpy as np

def ecdf(var_0):

    # convert sample to a numpy array, if it isn't already
    var_0 = np.atleast_1d(var_0)

    # find the unique values and their corresponding counts
    quantiles, counts = np.unique(var_0, return_counts=True)

    # take the cumulative sum of the counts and divide by the sample size to
    # get the cumulative probabilities between 0 and 1
    var_1 = np.cumsum(counts).astype(np.double) / var_0.size

    return quantiles, var_1
