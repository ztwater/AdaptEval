import numpy as np
import bisect
xarr = np.random.rand(int(1e7))

srt_ind = xarr.argsort()
xar = xarr.copy()[srt_ind]
xlist = xar.tolist()
bisect.bisect_left(xlist, 0.3)
