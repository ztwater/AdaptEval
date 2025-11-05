
pyr_start_time = timeit.default_timer()

nol = 4
warp = init_warp
warp = warp * np.array([[1, 1, 2], [1, 1, 2]], dtype=np.float32)**(1-nol)

# construct grayscale pyramid
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
gray1_pyr = [gray1]
gray2_pyr = [gray2]

for level in range(nol):
    gray1_pyr.insert(0, cv2.resize(gray1_pyr[0], None, fx=1/2, fy=1/2,
                                   interpolation=cv2.INTER_AREA))
    gray2_pyr.insert(0, cv2.resize(gray2_pyr[0], None, fx=1/2, fy=1/2,
                                   interpolation=cv2.INTER_AREA))

# run pyramid ECC
for level in range(nol):
    lvl_start_time = timeit.default_timer()

    cc, warp = cv2.findTransformECC(gray1_pyr[level], gray2_pyr[level],
                                    warp, warp_mode, criteria)

    if level != nol-1:  # scale up for the next pyramid level
        warp = warp * np.array([[1, 1, 2], [1, 1, 2]], dtype=np.float32)

    print('Level %i time: '%level, timeit.default_timer() - lvl_start_time)

print('Pyramid time:', timeit.default_timer() - pyr_start_time)
