import Image, ExifTags

try:
    image=Image.open(os.path.join(path, fileName))
    if hasattr(image, '_getexif'): # only present in JPEGs
        for orientation in ExifTags.TAGS.keys(): 
            if ExifTags.TAGS[orientation]=='Orientation':
                break 
        e = image._getexif()       # returns None if no EXIF data
        if e is not None:
            exif=dict(e.items())
            orientation = exif[orientation] 

            if orientation == 3:   image = image.transpose(Image.ROTATE_180)
            elif orientation == 6: image = image.transpose(Image.ROTATE_270)
            elif orientation == 8: image = image.transpose(Image.ROTATE_90)

    image.thumbnail((THUMB_WIDTH , THUMB_HIGHT), Image.ANTIALIAS)
    image.save(os.path.join(path,fileName))

except:
    traceback.print_exc()
