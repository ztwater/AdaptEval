def split(path):
    (drive, head) = os.path.splitdrive(path)
    while (head != os.sep):
        (head, tail) = os.path.split(head)
        yield tail
