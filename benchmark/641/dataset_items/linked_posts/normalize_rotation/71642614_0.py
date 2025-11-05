from PIL import Image, ImageOps

img = Image.open(filename)
img = ImageOps.exif_transpose(img)
img.thumbnail((1000,1000), Image.ANTIALIAS)
img.save(output_fname, "JPEG")
