enter code here

import numpy as np

clrs = np.linspace( 0, 1, 18 )  # It will generate 
# color only for 18 for more change the number
np.random.shuffle(clrs)
colors = []
for i in range(0, 72, 4):
    idx = np.arange( 0, 18, 1 )
    np.random.shuffle(idx)
    r = clrs[idx[0]]
    g = clrs[idx[1]]
    b = clrs[idx[2]]
    a = clrs[idx[3]]
    colors.append([r, g, b, a])
