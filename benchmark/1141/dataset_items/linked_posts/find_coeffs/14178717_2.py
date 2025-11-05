coeffs = find_coeffs(
        [(0, 0), (256, 0), (256, 256), (0, 256)],
        [(0, 0), (256, 0), (new_width, height), (xshift, height)])

img.transform((width, height), Image.PERSPECTIVE, coeffs,
        Image.BICUBIC).save(sys.argv[3])
