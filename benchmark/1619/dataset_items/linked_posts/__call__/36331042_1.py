import numpy as np
image = read_image("YOUR_IMAGE") 
noisemap = create_noisemap() 
noisy = image + np.random.poisson(noisemap)  
