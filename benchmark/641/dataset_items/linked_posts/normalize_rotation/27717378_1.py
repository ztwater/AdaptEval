from PIL import Image, ExifTags

# Open file with Pillow
image = Image.open('IMG_0002.jpg')

#If no ExifTags, no rotating needed.
try:
# Grab orientation value.
    image_exif = image._getexif()
    image_orientation = image_exif[274]

# Rotate depending on orientation.
    if image_orientation == 3:
        rotated = image.rotate(180)
    if image_orientation == 6:
        rotated = image.rotate(-90)
    if image_orientation == 8:
        rotated = image.rotate(90)

# Save rotated image.
    rotated.save('rotated.jpg')
except:
    pass
