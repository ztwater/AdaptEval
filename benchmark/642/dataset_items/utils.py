#########################################
# Still ugly file with helper functions #
#########################################
import numpy as np
import torch
import cv2

# def get_warp_pyramid(im1, im2, nol, criteria_, warp_mode):
#     """
#     Faster implementation of CMC based on an image pyramid.
#     Code was obtained from:
#     https://stackoverflow.com/questions/45997891/cv2-motion-euclidean-for-the-warp-mode-in-ecc-image-alignment-method
#     """
#
#     # pyr_start_time = timeit.default_timer()
#     init_warp = np.array([[1, 0, 0], [0, 1, 0]], dtype=np.float32)
#
#     warp = init_warp
#     warp = warp * np.array([[1, 1, 2], [1, 1, 2]], dtype=np.float32) ** (1 - nol)
#
#     # construct grayscale pyramid
#     gray1 = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
#     gray2 = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)
#     gray1_pyr = [gray1]
#     gray2_pyr = [gray2]
#
#     for level in range(nol):
#         gray1_pyr.insert(0, cv2.resize(gray1_pyr[0], None, fx=1 / 2, fy=1 / 2,
#                                        interpolation=cv2.INTER_AREA))
#         gray2_pyr.insert(0, cv2.resize(gray2_pyr[0], None, fx=1 / 2, fy=1 / 2,
#                                        interpolation=cv2.INTER_AREA))
#
#     # run pyramid ECC
#     for level in range(nol):
#         # lvl_start_time = timeit.default_timer()
#
#         if level != nol - 1:
#             # if True:
#             cc, warp = cv2.findTransformECC(gray1_pyr[level], gray2_pyr[level],
#                                             warp, warp_mode, criteria_, inputMask=None, gaussFiltSize=1)
#
#         # if level != nol-1:  # scale up for the next pyramid level
#         warp = warp * np.array([[1, 1, 2], [1, 1, 2]], dtype=np.float32)
#
#     # print('Level %i time: '%level, timeit.default_timer() - lvl_start_time)
#     # print('Pyramid time:', timeit.default_timer() - pyr_start_time)
#
#     return torch.from_numpy(warp)

def get_warp_pyramid(im1, im2, nol, criteria_, warp_mode, inputMask=None, gaussFiltSize=1):
    # Initialize warp matrix with a translation component set to zero
    warp = np.array([[1, 0, 0], [0, 1, 0]], dtype=np.float32)

    # Adjust warp matrix for pyramid levels
    warp = warp * np.array([[1, 1, 2], [1, 1, 2]], dtype=np.float32) ** (1 - nol)

    # Construct grayscale pyramid
    gray1 = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)
    gray1_pyr = [gray1]
    gray2_pyr = [gray2]

    for level in range(nol):
        gray1_pyr.insert(0, cv2.resize(gray1_pyr[0], None, fx=1/2, fy=1/2, interpolation=cv2.INTER_AREA))
        gray2_pyr.insert(0, cv2.resize(gray2_pyr[0], None, fx=1/2, fy=1/2, interpolation=cv2.INTER_AREA))

    # Run pyramid ECC
    for level in range(nol):
        warp, _ = cv2.findTransformECC(
            gray1_pyr[level], gray2_pyr[level], warp, warp_mode, criteria_,
            inputMask=inputMask, gaussFiltSize=gaussFiltSize
        )

        if level != nol - 1:  # Scale up for the next pyramid level
            warp = warp * np.array([[1, 1, 2], [1, 1, 2]], dtype=np.float32)

    # Return warp as a PyTorch tensor
    return torch.tensor(warp)



