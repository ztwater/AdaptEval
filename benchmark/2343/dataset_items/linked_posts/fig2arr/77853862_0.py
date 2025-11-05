import numpy as np 
import cv2
import time
import justpyplot as jplt

xs, ys = [], []
while(cv2.waitKey(1) != 27):
    xt = time.perf_counter() - t0
    yx = np.sin(xt)
    xs.append(xt)
    ys.append(yx)
    
    frame = np.full((500,470,3), (255,255,255), dtype=np.uint8)
    
    vals = np.array(ys)

    plotted_in_array = jplt.just_plot(frame, vals,title="sin() from Clock")
    
    cv2.imshow('np array plot', plotted_in_array)
