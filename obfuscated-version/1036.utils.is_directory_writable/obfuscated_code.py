import tempfile
import errno

def isWritable(var_0):
    try:
        var_1 = tempfile.TemporaryFile(dir = var_0)
        var_1.close()
    except OSError as e:
        if e.errno == errno.EACCES:  # 13
            return False
        e.filename = var_0
        raise
    return True
