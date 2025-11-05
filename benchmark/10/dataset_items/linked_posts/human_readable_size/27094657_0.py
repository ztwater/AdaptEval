def humanizeFileSize(filesize):
    p = int(math.floor(math.log(filesize, 2)/10))
    return "%.3f%s" % (filesize/math.pow(1024,p), ['B','KiB','MiB','GiB','TiB','PiB','EiB','ZiB','YiB'][p])
