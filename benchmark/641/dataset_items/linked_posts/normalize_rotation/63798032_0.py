from PIL import Image, ImageOps

original_image = Image.open(filename)

fixed_image = ImageOps.exif_transpose(original_image)
