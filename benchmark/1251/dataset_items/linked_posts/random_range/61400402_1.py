import jax

minval, maxval, n_samples = -50, 50, 10
key = jax.random.PRNGKey(seed=0)
samples = jax.random.shuffle(key, jax.numpy.arange(minval, maxval))[:n_samples]
