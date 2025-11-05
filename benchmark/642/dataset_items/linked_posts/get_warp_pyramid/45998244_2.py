nol = 5 # nol: number of levels
# maybe do some calculation to decide the nol based on h, w

# initial guess may not be the identity warp, so scale to smallest level
warp = initWarp
warp = warp * np.array([[1, 1, 2], [1, 1, 2], [1/2, 1/2, 1]])**(1-nol)

for level in range(nol):

    scale = 1/2**(nol-1-level)
    rszImg = cv2.resize(img, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA)
    rszTmp = cv2.resize(tmp, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA)

    warp = your_warping_algorithm(rszImg, rszTmp, warp, ...)

    if level != nol-1:
        # might want some error catching here to reset initial guess
        # if your algorithm fails at some level of the pyramid

        # scale up for the next pyramid level
        warp = warp * np.array([[1, 1, 2], [1, 1, 2], [1/2, 1/2, 1]])

return warp
