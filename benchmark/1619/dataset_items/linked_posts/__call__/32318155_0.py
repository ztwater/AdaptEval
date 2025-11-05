filename = 'myimage.png'
img = (scipy.misc.imread(filename)).astype(float)

noise_mask = numpy.random.poisson(img)

noisy_img = img + noise_mask
