def Gaussian(x,z,sigma,axis=None):
    return np.exp((-(np.linalg.norm(x-z, axis=axis)**2))/(2*sigma**2))

x=np.arange(12).reshape(3,4)
GaussianMatrix(x,1)
