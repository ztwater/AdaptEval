def relu_backward(dout, cache):
    x = cache
    dx = np.where(x > 0, dout, 0)
    return dx
