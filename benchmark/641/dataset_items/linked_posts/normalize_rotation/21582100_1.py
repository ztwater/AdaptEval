>>> img = Image.open('/path/to/image.jpeg')
>>> rotation_code = get_rotation_code(img)
>>> if rotation_code is not None:
...     img = rotate_image(img, rotation_code)
...     img.save('/path/to/image.jpeg')
...
