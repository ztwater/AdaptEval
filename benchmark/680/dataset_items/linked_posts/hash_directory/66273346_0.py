import hashlib
def getMd5(file_path):
    m = hashlib.md5()
    with open(file_path,'rb') as f:
        lines = f.read()
        m.update(lines)
    md5code = m.hexdigest()
    return md5code
