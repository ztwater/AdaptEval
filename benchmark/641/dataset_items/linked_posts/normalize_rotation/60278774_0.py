    from PIL import image
    im1 = Image.open(path_to_image)
    im1.thumbnail(size1, Image.ANTIALIAS)
    y, z = im1.size
    d = z * 1.5
    if y > d:
         im1.rotate(90, expand=1)
