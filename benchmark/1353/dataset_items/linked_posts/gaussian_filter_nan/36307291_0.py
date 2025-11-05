import numpy as np
import scipy as sp
import scipy.ndimage

sigma=2.0                  # standard deviation for Gaussian kernel
truncate=4.0               # truncate filter at this many sigmas

U=sp.randn(10,10)          # random array...
U[U>2]=np.nan              # ...with NaNs for testing

V=U.copy()
V[np.isnan(U)]=0
VV=sp.ndimage.gaussian_filter(V,sigma=sigma,truncate=truncate)

W=0*U.copy()+1
W[np.isnan(U)]=0
WW=sp.ndimage.gaussian_filter(W,sigma=sigma,truncate=truncate)

Z=VV/WW
