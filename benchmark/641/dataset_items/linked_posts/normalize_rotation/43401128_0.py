def _fix_image_rotation(image):
 orientation_to_rotation_map = {
     3: Image.ROTATE_180,
     6: Image.ROTATE_270,
     8: Image.ROTATE_90,
 }
 try:
     exif = _get_exif_from_image(image)
     orientation = _get_orientation_from_exif(exif)
     rotation = orientation_to_rotation_map.get(orientation)
     if rotation:
         image = image.transpose(rotation)

 except Exception as e:
     # Would like to catch specific exceptions, but PIL library is poorly documented on Exceptions thrown
     # Log error here

 finally:
     return image


def _get_exif_from_image(image):
 exif = {}

 if hasattr(image, '_getexif'):  # only jpegs have _getexif
     exif_or_none = image._getexif()
     if exif_or_none is not None:
         exif = exif_or_none

 return exif


def _get_orientation_from_exif(exif):
 ORIENTATION_TAG = 'Orientation'
 orientation_iterator = (
     exif.get(tag_key) for tag_key, tag_value in ExifTags.TAGS.items()
     if tag_value == ORIENTATION_TAG
 )
 orientation = next(orientation_iterator, None)
 return orientation
