def find_nearest(array, values):
    array = np.asarray(array)

    # the last dim must be 1 to broadcast in (array - values) below.
    values = np.expand_dims(values, axis=-1) 

    indices = np.abs(array - values).argmin(axis=-1)

    return array[indices]


image = plt.imread('example_3_band_image.jpg')

print(image.shape) # should be (nrows, ncols, 3)

quantiles = np.linspace(0, 255, num=2 ** 2, dtype=np.uint8)

quantiled_image = find_nearest(quantiles, image)

print(quantiled_image.shape) # should be (nrows, ncols, 3)
