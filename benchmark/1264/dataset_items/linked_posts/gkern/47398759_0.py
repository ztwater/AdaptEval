import numpy as np
def generate_gaussian_mask(shape, sigma, sigma_y=None):
    if sigma_y==None:
        sigma_y=sigma
    rows, cols = shape

    def get_gaussian_fct(size, sigma):
        fct_gaus_x = np.linspace(0,size,size)
        fct_gaus_x = fct_gaus_x-size/2
        fct_gaus_x = fct_gaus_x**2
        fct_gaus_x = fct_gaus_x/(2*sigma**2)
        fct_gaus_x = np.exp(-fct_gaus_x)
        return fct_gaus_x

    mask = np.outer(get_gaussian_fct(rows,sigma), get_gaussian_fct(cols,sigma_y))
    return mask
