import cv2
import numpy as np
import timeit


"""Inits"""


img1 = cv2.imread('IMG_1770_1.png')
img2 = cv2.imread('IMG_1868_1.png')
h, w = img1.shape[:2]

# ECC params
init_warp = np.array([[1, 0, 0], [0, 1, 0]], dtype=np.float32)
n_iters = 1000
e_thresh = 1e-6
warp_mode = cv2.MOTION_EUCLIDEAN
criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, n_iters, e_thresh)


"""Full scale ECC algorithm"""


full_scale_start_time = timeit.default_timer()

gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
cc, warp = cv2.findTransformECC(gray1, gray2, init_warp, warp_mode, criteria)
print('Non-pyramid time:', timeit.default_timer() - full_scale_start_time)

# write blended warp and diff
img2_aligned = cv2.warpAffine(img2, warp, (w, h), flags=cv2.WARP_INVERSE_MAP)
blended = cv2.addWeighted(img1, 0.5, img2_aligned, 0.5, 0)
cv2.imwrite('full_scale_blended.png', blended)
warp_diff = cv2.absdiff(img2_aligned, img1)
cv2.imwrite('full_scale_diff.png', warp_diff)


"""Pyramid ECC algorithm"""


pyr_start_time = timeit.default_timer()

# initial guess may not be the identity warp, so scale to smallest level
nol = 4
warp = init_warp
warp = warp * np.array([[1, 1, 2], [1, 1, 2]], dtype=np.float32)**(1-nol)

for level in range(nol):
    lvl_start_time = timeit.default_timer()

    # resize images
    scale = 1/2**(nol-1-level)
    rszImg1 = cv2.resize(img1, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA)
    rszImg2 = cv2.resize(img2, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA)
    rszGray1 = cv2.cvtColor(rszImg1, cv2.COLOR_BGR2GRAY)
    rszGray2 = cv2.cvtColor(rszImg2, cv2.COLOR_BGR2GRAY)

    cc, warp = cv2.findTransformECC(rszGray1, rszGray2, warp, warp_mode, criteria)

    if level != nol-1:  # scale up for the next pyramid level
        warp = warp * np.array([[1, 1, 2], [1, 1, 2]], dtype=np.float32)

    print('Level %i time: '%level, timeit.default_timer() - lvl_start_time)

print('Pyramid time:', timeit.default_timer() - pyr_start_time)

# write blended warp and diff
img2_aligned = cv2.warpAffine(img2, warp, (w, h), flags=cv2.WARP_INVERSE_MAP)
blended = cv2.addWeighted(img1, 0.5, img2_aligned, 0.5, 0)
cv2.imwrite('pyr_blended.png', blended)
warp_diff = cv2.absdiff(img2_aligned, img1)
cv2.imwrite('pyr_diff.png', warp_diff)
