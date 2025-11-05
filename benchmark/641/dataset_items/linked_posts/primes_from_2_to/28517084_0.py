import numpy as np
def ajs_primes3a(upto):
    mat = np.ones((upto), dtype=bool)
    mat[0] = False
    mat[1] = False
    mat[4::2] = False
    for idx in range(3, int(upto ** 0.5)+1, 2):
        mat[idx*2::idx] = False
    return np.where(mat == True)[0]
