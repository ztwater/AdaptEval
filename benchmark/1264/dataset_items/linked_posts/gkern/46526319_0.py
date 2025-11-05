def gaussian_kernel(size=21, sigma=3):
    """Returns a 2D Gaussian kernel.
    Parameters
    ----------
    size : float, the kernel size (will be square)

    sigma : float, the sigma Gaussian parameter

    Returns
    -------
    out : array, shape = (size, size)
      an array with the centered gaussian kernel
    """
    x = np.linspace(- (size // 2), size // 2)
    x /= np.sqrt(2)*sigma
    x2 = x**2
    kernel = np.exp(- x2[:, None] - x2[None, :])
    return kernel / kernel.sum()
