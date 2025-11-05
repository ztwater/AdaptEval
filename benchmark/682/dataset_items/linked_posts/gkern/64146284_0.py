indicatrice = np.zeros((5,5))
indicatrice[2,2] = 1
gaussian_kernel = gaussian_filter(indicatrice, sigma=1)
gaussian_kernel/=gaussian_kernel[2,2]
