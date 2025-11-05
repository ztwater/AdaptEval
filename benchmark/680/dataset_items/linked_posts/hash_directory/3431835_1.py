[(fname, hashlib.md5(file_as_bytes(open(fname, 'rb'))).digest()) for fname in fnamelst]
