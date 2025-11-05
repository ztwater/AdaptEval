import scipy.ndimage as scim

def gaussian_kernel(dimension: int, sigma: float, ones_in_the_middle=False):
    dirac = np.zeros((dimension,dimension))
    dirac[(dimension-1)//2:dimension//2+1, (dimension-1)//2:dimension//2+1] = 1.0
    kernel = scim.gaussian_filter(dirac, sigma=sigma)
    divisor = kernel[(dimension-1)//2, (dimension-1)//2] if ones_in_the_middle else 1 + 3 * ((dimension + 1) % 2)
    return kernel/divisor
