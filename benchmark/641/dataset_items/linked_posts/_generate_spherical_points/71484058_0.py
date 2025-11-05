import numpy as np
def sample(center, radius, n_samples, seed=None):

    # initial values
    d = center.shape[0]

    # sample n_samples points in d dimensions from a standard normal distribution
    rng = np.random.default_rng(seed)
    samples = rng.normal(size=(n_samples, d))

    # make the samples lie on the surface of the unit hypersphere
    normalize_radii = np.linalg.norm(samples, axis=1)[:, np.newaxis]
    samples /= normalize_radii

    # make the samples lie inside the hypersphere with the correct density
    uniform_points = rng.uniform(size=n_samples)[:, np.newaxis]
    new_radii = np.power(uniform_points, 1/d)
    samples *= new_radii

    # scale the points to have the correct radius and center
    samples = samples * radius + center
    return samples
