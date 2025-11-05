    import Image, ExifTags

    try :
        image=Image.open(os.path.join(path, fileName))
        for orientation in ExifTags.TAGS.keys() : 
            if ExifTags.TAGS[orientation]=='Orientation' : break 
        exif=dict(image._getexif().items())

        if   exif[orientation] == 3 : 
            image=image.rotate(180, expand=True)
        elif exif[orientation] == 6 : 
            image=image.rotate(270, expand=True)
        elif exif[orientation] == 8 : 
            image=image.rotate(90, expand=True)

        image.thumbnail((THUMB_WIDTH , THUMB_HIGHT), Image.ANTIALIAS)
        image.save(os.path.join(path,fileName))

    except:
        traceback.print_exc()
