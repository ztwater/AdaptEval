def test_fill(s,d):
     # s is size of one dimension, d is the number of dimension
    data = np.arange(s**d).reshape((s,)*d)
    seed = np.zeros(data.shape,dtype=bool)
    seed.flat[np.random.randint(0,seed.size,int(data.size/20**d))] = True

    return fill(data,-seed), seed

import matplotlib.pyplot as plt
data,seed  = test_fill(500,2)
data[nd.binary_dilation(seed,iterations=2)] = 0   # draw (dilated) seeds in black
plt.imshow(np.mod(data,42))                       # show cluster
