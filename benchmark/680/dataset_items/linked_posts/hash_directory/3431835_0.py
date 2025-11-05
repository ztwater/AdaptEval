import hashlib
def file_as_bytes(file):
    with file:
        return file.read()

print hashlib.md5(file_as_bytes(open(full_path, 'rb'))).hexdigest()
