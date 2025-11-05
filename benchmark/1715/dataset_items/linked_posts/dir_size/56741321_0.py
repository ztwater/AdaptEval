import os

def size(path, *, follow_symlinks=False):
    try:
        with os.scandir(path) as it:
            return sum(size(entry, follow_symlinks=follow_symlinks) for entry in it)
    except NotADirectoryError:
        return os.stat(path, follow_symlinks=follow_symlinks).st_size
