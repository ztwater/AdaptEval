def crop_image(image, angle):
    h, w = image.shape
    tan_a = abs(np.tan(angle * np.pi / 180))
    b = int(tan_a / (1 - tan_a ** 2) * (h - w * tan_a))
    d = int(tan_a / (1 - tan_a ** 2) * (w - h * tan_a))
    return image[d:h - d, b:w - b]
