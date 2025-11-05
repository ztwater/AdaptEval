import numpy as np
import torch
import scipy.stats as st


def gkern(kernlen=5, nsig=1.0):
    """Returns a 2D Gaussian kernel array."""
    """https://stackoverflow.com/a/29731818"""
    interval = (2 * nsig + 1.) / (kernlen)
    x = np.linspace(-nsig - interval / 2., nsig + interval / 2., kernlen + 1)
    kern1d = np.diff(st.norm.cdf(x))
    kernel_raw = np.sqrt(np.outer(kern1d, kern1d))
    kernel = kernel_raw / kernel_raw.sum()
    return torch.from_numpy(kernel).float()