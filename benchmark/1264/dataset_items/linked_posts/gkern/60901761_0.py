from scipy import signal

def gaussian2D(patchHeight, patchWidth, stdHeight=1, stdWidth=1):
    gaussianWindow = signal.gaussian(patchHeight, stdHeight).reshape(-1, 1)@signal.gaussian(patchWidth, stdWidth).reshape(1, -1)
    return gaussianWindow

print(gaussian2D(3, 5))
