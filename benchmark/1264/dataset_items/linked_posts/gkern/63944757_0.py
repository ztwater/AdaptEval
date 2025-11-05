import numpy as np
import scipy.stats as st

def gkern(kernlen=21, sig=3):
    """Returns a 2D Gaussian kernel."""

    x = np.linspace(-(kernlen/2)/sig, (kernlen/2)/sig, kernlen+1)
    kern1d = np.diff(st.norm.cdf(x))
    kern2d = np.outer(kern1d, kern1d)
    return kern2d/kern2d.sum()

print(gkern(kernlen=5, sig=1))
