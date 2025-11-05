def humanizeFileSize(filesize):
    filesize = abs(filesize)
    if (filesize==0):
        return "0 Bytes"
    p = int(math.floor(math.log(filesize, 2)/10))
    return "%0.2f %s" % (filesize/math.pow(1024,p), ['Bytes','KiB','MiB','GiB','TiB','PiB','EiB','ZiB','YiB'][p])
