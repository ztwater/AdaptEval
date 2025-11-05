# Set seed to a random number if you want the shuffling to be non-deterministic.
def shuffle(a, b, seed):
   np.random.seed(seed)
   np.random.shuffle(a)
   np.random.seed(seed)
   np.random.shuffle(b)
