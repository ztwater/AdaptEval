
var_0 = timeit.default_timer()

var_1 = 4
var_2 = init_warp
var_2 = var_2 * np.array([[1, 1, 2], [1, 1, 2]], dtype=np.float32)**(1-var_1)

# construct grayscale pyramid
var_3 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
var_4 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
var_5 = [var_3]
var_6 = [var_4]

for level in range(var_1):
    var_5.insert(0, cv2.resize(var_5[0], None, fx=1/2, fy=1/2,
                                   interpolation=cv2.INTER_AREA))
    var_6.insert(0, cv2.resize(var_6[0], None, fx=1/2, fy=1/2,
                                   interpolation=cv2.INTER_AREA))

# run pyramid ECC
for level in range(var_1):
    var_7 = timeit.default_timer()

    cc, var_2 = cv2.findTransformECC(var_5[level], var_6[level],
                                    var_2, warp_mode, criteria)

    if level != var_1-1:  # scale up for the next pyramid level
        var_2 = var_2 * np.array([[1, 1, 2], [1, 1, 2]], dtype=np.float32)

    print('Level %i time: '%level, timeit.default_timer() - var_7)

print('Pyramid time:', timeit.default_timer() - var_0)
