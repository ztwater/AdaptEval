import numpy
def get_grids(N_X, N_Y):
    from numpy import mgrid
    return mgrid[-1:1:1j*N_X, -1:1:1j*N_Y]

def frequency_radius(fx, fy):
    R2 = fx**2 + fy**2
    (N_X, N_Y) = fx.shape
    R2[N_X/2, N_Y/2]= numpy.inf

    return numpy.sqrt(R2)

def enveloppe_color(fx, fy, alpha=1.0):
    # 0.0, 0.5, 1.0, 2.0 are resp. white, pink, red, brown noise
    # (see http://en.wikipedia.org/wiki/1/f_noise )
    # enveloppe
    return 1. / frequency_radius(fx, fy)**alpha #

import scipy
image = scipy.lena()
N_X, N_Y = image.shape
fx, fy = get_grids(N_X, N_Y)
pink_spectrum = enveloppe_color(fx, fy)

from scipy.fftpack import fft2
power_spectrum = numpy.abs(fft2(image))**2
