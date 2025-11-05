import numpy as np
image = read_image("YOUR_IMAGE")  # need a rescale to be more realistic
noisy = np.random.poisson(image / 255.0 * PEAK) / PEAK * 255  # noisy image
