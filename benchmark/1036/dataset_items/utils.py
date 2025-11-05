import errno
import pathlib
import tempfile


def is_directory_writable(path: pathlib.Path) -> bool:
    # We do not check for permission bits but just try
    # since that is the most reliable solution
    # See: https://stackoverflow.com/a/25868839/1625689

    try:
        testfile = tempfile.TemporaryFile(dir=path)
        testfile.close()
    except OSError as error:
        if error.errno == errno.EACCES:  # 13
            return False
        error.filename = path
        raise

    return True

