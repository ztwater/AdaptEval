try:
    exif = im._getexif()
except Exception:
    exif = None

# ...
# im = im.copy() somewhere
# ...

if exif:
    im = transpose_im(im, exif)
