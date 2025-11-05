create a pyramid of image resolutions, halving the h, w each time
warp = np.eye(3)
for each image in the pyramid from smallest to second to largest
    warp = findTransformECC(..., warp, ...)
    warp = warp * np.array([[1, 1, 2], [1, 1, 2], [1/2, 1/2, 1]])
warp = findTransformECC(full resolution images, warp, ...)
