import scipy.ndimage as scim

def gaussian_kernel(dimension: int, sigma: float):
    dirac = np.zeros((dimension,dimension))
    dirac[(dimension-1)//2:dimension//2+1, (dimension-1)//2:dimension//2+1] = 1.0 / (1 + 3 * ((dimension + 1) % 2))
    return scim.gaussian_filter(dirac, sigma=sigma)
