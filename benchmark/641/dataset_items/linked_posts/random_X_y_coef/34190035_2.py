import numpy as np


def improved(prob_matrix, items):
    # transpose here for better data locality later
    cdf = np.cumsum(prob_matrix.T, axis=1)
    # random numbers are expensive, so we'll get all of them at once
    ridx = np.random.random(size=n)
    # the one loop we can't avoid, made as simple as possible
    idx = np.zeros(n, dtype=int)
    for i, r in enumerate(ridx):
        idx[i] = np.searchsorted(cdf[i], r)
    # fancy indexing all at once is faster than indexing in a loop
    return items[idx]


def original(prob_matrix, items):
    choices = np.zeros((n,))
    # This is slow, because of the loop in Python
    for i in range(n):
        choices[i] = np.random.choice(items, p=prob_matrix[:,i])
    return choices


def vectorized(prob_matrix, items):
    s = prob_matrix.cumsum(axis=0)
    r = np.random.rand(prob_matrix.shape[1])
    k = (s < r).sum(axis=0)
    return items[k]


m = 10
n = 10000 # Or some very large number

items = np.arange(m)
prob_weights = np.random.rand(m, n)
prob_matrix = prob_weights / prob_weights.sum(axis=0, keepdims=True)
