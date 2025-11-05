 
import numpy as np 
from scipy.signal import convolve2d 


def estimate_noise(data):
    """ Estimate the RMS noise of an image

    Taked from https://stackoverflow.com/questions/2440504/noise-estimation-noise-measurement-in-image
    Reference: J. Immerkaer, “Fast Noise Variance Estimation”, Computer Vision and Image Understanding,
    Vol. 64, No. 2, pp. 300-302, Sep. 1996 [PDF]
    """
    H, W = data.shape
    data = np.nan_to_num(data)
    M = [[1, -2, 1],
         [-2, 4, -2],
         [1, -2, 1]]
    sigma = np.sum(np.sum(np.abs(convolve2d(data, M))))
    sigma = sigma * np.sqrt(0.5 * np.pi) / (6 * (W - 2) * (H - 2))
    return sigma
 
