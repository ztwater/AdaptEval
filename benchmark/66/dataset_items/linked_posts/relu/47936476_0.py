def ReLU(x):
    return x * (x > 0)

def dReLU(x):
    return 1. * (x > 0)
