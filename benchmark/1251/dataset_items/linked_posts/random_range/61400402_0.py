import numpy as np

minval, maxval, n_samples = -50, 50, 10
generator = np.random.default_rng(seed=0)
samples = generator.permutation(np.arange(minval, maxval))[:n_samples]

# or, if minval is 0,
samples = generator.permutation(maxval)[:n_samples]
